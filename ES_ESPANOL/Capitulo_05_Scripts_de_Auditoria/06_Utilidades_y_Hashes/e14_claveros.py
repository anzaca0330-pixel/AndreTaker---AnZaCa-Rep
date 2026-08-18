import os
import sys
import re
import json
import logging
import argparse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

# Setup Logging
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, "segundaVuelta")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "downloader_claveros.log")

# Clear/create the log file on startup
with open(log_file, "w", encoding="utf-8") as f:
    f.write("--- Claveros HTTP Downloader Log Started ---\n")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s')

# File Handler (stores all details)
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Console Handler (only warnings & errors to keep stdout small)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class E14ClaverosDownloader:
    def __init__(self, depto_filter=None, muni_filter=None, zona_filter=None, puesto_filter=None, output_dir=None):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        if output_dir:
            self.output_dir = output_dir
        else:
            portable_drive = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
            if os.path.exists("/media/andrea-zabala-c/D A T A1"):
                self.output_dir = portable_drive
            else:
                self.output_dir = os.path.join(self.base_dir, "segundaVuelta", "claveros_pdf")
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.base_url = "https://escrutinios2vueltapresidente2026.registraduria.gov.co"
        
        self.depto_filter = depto_filter
        self.muni_filter = muni_filter
        self.zona_filter = zona_filter
        self.puesto_filter = puesto_filter
        
        self.index_data = {}

    def sanitize(self, name: str) -> str:
        return re.sub(r'[\\/*?:"<>|]', '_', name).strip()

    def fetch_json(self, url):
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))

    def load_index(self):
        index_url = f"{self.base_url}/data/index.json"
        logger.warning(f"Fetching index file from {index_url}...")
        self.index_data = self.fetch_json(index_url)

    def get_divipole(self):
        divipole_path = self.index_data.get("data/esc/v1/divipole/")
        if not divipole_path:
            # Fallback to known path if not in index keys
            divipole_path = "divipole_20260609_095453_471.json"
            divipole_url = f"{self.base_url}/data/esc/v1/divipole/{divipole_path}"
        else:
            divipole_url = f"{self.base_url}/data/esc/v1/divipole/{divipole_path}"
            
        logger.warning(f"Fetching divipole hierarchy from {divipole_url}...")
        return self.fetch_json(divipole_url)

    def process_puesto(self, p):
        depto_code = p["depto_code"]
        depto_name = p["depto_name"]
        muni_code = p["muni_code"]
        muni_name = p["muni_name"]
        zona_code = p["zona_code"]
        zona_name = p["zona_name"]
        puesto_code = p["puesto_code"]
        puesto_name = p["puesto_name"]
        
        key = f"data/esc/v1/actas-documentos/001/{depto_code}/{muni_code}/{zona_code}/{puesto_code}/mesas/"
        filename = self.index_data.get(key)
        if not filename:
            logger.info(f"No E14 index entry found for puesto: {puesto_name} ({depto_name})")
            return
            
        mesas_url = f"{self.base_url}/{key}{filename}"
        try:
            mesas = self.fetch_json(mesas_url)
        except Exception as e:
            logger.error(f"Error fetching mesas metadata for puesto {puesto_name}: {e}")
            return
            
        # Sanitize paths
        depto_san = self.sanitize(depto_name)
        muni_san = self.sanitize(muni_name)
        
        zona_label = zona_name
        if not zona_label.upper().startswith("ZONA"):
            zona_label = f"ZONA {zona_label}"
        zona_san = self.sanitize(zona_label)
        puesto_san = self.sanitize(puesto_name)
        
        full_dir = os.path.join(self.output_dir, depto_san, muni_san, zona_san, puesto_san)
        os.makedirs(full_dir, exist_ok=True)
        
        for mesa in mesas:
            if mesa.get("digitalizado") == 1 and mesa.get("nombre_archivo"):
                numero = mesa.get("numero")
                mesa_suffix = f"Mesa_{numero}"
                
                # Resumption check
                existing_files = [f for f in os.listdir(full_dir) if f.endswith(f"_{mesa_suffix}.pdf")]
                if existing_files:
                    logger.info(f"Mesa {numero} already downloaded as {existing_files[0]}. Skipping.")
                    continue
                    
                pdf_path = mesa.get("nombre_archivo")
                pdf_url = f"{self.base_url}{pdf_path}"
                
                filename_base = os.path.basename(pdf_path)
                name_part, ext_part = os.path.splitext(filename_base)
                filename_with_suffix = f"{name_part}_{mesa_suffix}{ext_part}"
                target_path = os.path.join(full_dir, filename_with_suffix)
                
                logger.info(f"Downloading Claveros E14: {depto_name} -> {muni_name} -> {mesa_suffix}")
                try:
                    req_pdf = urllib.request.Request(
                        pdf_url, 
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
                    )
                    with urllib.request.urlopen(req_pdf, timeout=45) as resp, open(target_path, "wb") as f_out:
                        f_out.write(resp.read())
                    
                    # Verificación de Integridad Inmediata
                    size = os.path.getsize(target_path) if os.path.exists(target_path) else 0
                    if size < 500:
                        logger.error(f"Incomplete download for {depto_name} {muni_name} Mesa {numero} (size: {size} bytes). Removing.")
                        os.remove(target_path)
                    else:
                        with open(target_path, 'rb') as f_chk:
                            header = f_chk.read(10)
                            f_chk.seek(-1024, os.SEEK_END)
                            tail = f_chk.read()
                            if not header.startswith(b'%PDF-') or b'%%EOF' not in tail:
                                logger.error(f"Corrupt/truncated PDF trailer for {depto_name} {muni_name} Mesa {numero}. Removing.")
                                os.remove(target_path)
                            else:
                                logger.info(f"Saved & Verified Integrity: {target_path}")
                except Exception as download_err:
                    logger.error(f"Error downloading PDF for {depto_name} {muni_name} Mesa {numero}: {download_err}")

    def process_department(self, depto_info):
        depto_code = depto_info["code"]
        depto_name = depto_info["nombre"]
        depto_data = depto_info["data"]
        
        logger.warning(f"====== Thread Worker started for Claveros Department: {depto_name} ======")
        
        puestos = []
        munis = depto_data.get("municipios", {})
        for muni_code, muni in munis.items():
            muni_name = muni.get("nombre", "").strip()
            if self.muni_filter and self.muni_filter.upper() not in muni_name.upper():
                continue
                
            zonas = muni.get("zonas", {})
            for zona_code, zona in zonas.items():
                zona_name = zona.get("nombre", "").strip()
                if self.zona_filter and self.zona_filter.upper() not in zona_name.upper():
                    continue
                    
                puestos_dict = zona.get("puestos", {})
                for puesto_code, puesto in puestos_dict.items():
                    puesto_name = puesto.get("nombre", "").strip()
                    if self.puesto_filter and self.puesto_filter.upper() not in puesto_name.upper():
                        continue
                        
                    puestos.append({
                        "depto_code": depto_code,
                        "depto_name": depto_name,
                        "muni_code": muni_code,
                        "muni_name": muni_name,
                        "zona_code": zona_code,
                        "zona_name": zona_name,
                        "puesto_code": puesto_code,
                        "puesto_name": puesto_name
                    })
                    
        total_puestos = len(puestos)
        for idx, p in enumerate(puestos):
            self.process_puesto(p)
            
        logger.warning(f"====== Thread Worker finished successfully for Claveros Department: {depto_name} ======")

    def run(self):
        logger.warning("Starting High-Speed Claveros API Downloader (Department Parallelization)...")
        self.load_index()
        
        divipole_data = self.get_divipole()
        deptos_dict = divipole_data.get("departamentos", {})
        
        departments_to_run = []
        for depto_code, depto_data in deptos_dict.items():
            depto_name = depto_data.get("nombre", "").strip()
            if self.depto_filter and self.depto_filter.upper() not in depto_name.upper():
                continue
            departments_to_run.append({
                "code": depto_code,
                "nombre": depto_name,
                "data": depto_data
            })
            
        total_depts = len(departments_to_run)
        logger.warning(f"Discovered {total_depts} matching departments in Divipole.")
        
        max_workers = 8
        logger.warning(f"Launching {max_workers} concurrent HTTP worker hilos (Queue-based)...")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(self.process_department, departments_to_run)
            
        logger.warning("====== Claveros Downloader Finished Successfully! ======")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descargador Masivo de Formularios E14 de Claveros vía API HTTP.")
    parser.add_argument("--depto", type=str, default=None, help="Nombre del departamento a filtrar.")
    parser.add_argument("--muni", type=str, default=None, help="Nombre del municipio a filtrar.")
    parser.add_argument("--zona", type=str, default=None, help="Nombre de la zona a filtrar.")
    parser.add_argument("--puesto", type=str, default=None, help="Nombre del puesto a filtrar.")
    parser.add_argument("--output", type=str, default=None, help="Ruta de destino (ej. en el disco portátil).")
    args = parser.parse_args()
    
    downloader = E14ClaverosDownloader(
        depto_filter=args.depto,
        muni_filter=args.muni,
        zona_filter=args.zona,
        puesto_filter=args.puesto,
        output_dir=args.output
    )
    downloader.run()
