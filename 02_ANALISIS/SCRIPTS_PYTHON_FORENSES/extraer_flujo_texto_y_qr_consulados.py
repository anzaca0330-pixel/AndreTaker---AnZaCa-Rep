#!/usr/bin/env python3
import os
import csv
import subprocess
import re
import argparse
import hashlib
from concurrent.futures import ThreadPoolExecutor

def get_file_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

def extract_stream_and_qr_data(pdf_path):
    res = {
        "pdf": pdf_path,
        "filename": os.path.basename(pdf_path),
        "folder": os.path.basename(os.path.dirname(pdf_path)),
        "qr_content": "NO_DECODIFICADO",
        "text_stream_content": "SIN_TEXTO_INTERNO",
        "xobjects_count": 0
    }
    
    # 1. Extraer QR con zbarimg
    try:
        tmp_img = f"/tmp/qr_ext_{os.getpid()}_{hash(pdf_path)&0xffff}.png"
        subprocess.run(["pdftoppm", "-png", "-singlefile", "-r", "150", pdf_path, tmp_img[:-4]], capture_output=True, timeout=15)
        if os.path.exists(tmp_img):
            zproc = subprocess.run(["zbarimg", "--raw", "-q", tmp_img], capture_output=True, text=True, timeout=10)
            qr_raw = zproc.stdout.strip()
            if qr_raw:
                res["qr_content"] = qr_raw.replace("\n", " | ")
            try: os.remove(tmp_img)
            except Exception: pass
    except Exception:
        pass
        
    # 2. Extraer Flujo de Texto Interno (/Contents stream)
    try:
        tproc = subprocess.run(["pdftotext", pdf_path, "-"], capture_output=True, text=True, timeout=10)
        text_out = tproc.stdout.strip()
        if text_out:
            clean_t = " ".join(text_out.split())
            res["text_stream_content"] = clean_t[:200]
        else:
            qproc = subprocess.run(["qpdf", "--qdf", "--object-streams=disable", pdf_path, "-"], capture_output=True, text=True, timeout=15)
            bt_matches = re.findall(r'BT\s+([\s\S]*?)\s+ET', qproc.stdout)
            if bt_matches:
                res["text_stream_content"] = (" | ".join(bt_matches))[:200]
    except Exception:
        pass

    # 3. Contar XObjects
    try:
        proc_img = subprocess.run(["pdfimages", "-list", pdf_path], capture_output=True, text=True, timeout=10)
        lines = [l for l in proc_img.stdout.splitlines() if l.strip()]
        res["xobjects_count"] = max(0, len(lines) - 2)
    except Exception:
        pass

    return res

def run_extraction(input_dir, output_dir, filter_zone):
    print(f"🔬 [EXTRACCIÓN DE FLUJO] Parseando contenido inyectado y QRs...")
    print(f"📁 Directorio Origen: {input_dir}")
    print(f"📁 Directorio Destino: {output_dir}")
    
    pdf_list = []
    seen_hashes = set()
    
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith('.pdf') and '_descomprimido' not in f.lower():
                if filter_zone and filter_zone not in f:
                    continue
                filepath = os.path.join(root, f)
                file_hash = get_file_hash(filepath)
                if file_hash not in seen_hashes:
                    seen_hashes.add(file_hash)
                    pdf_list.append(filepath)
                        
    total = len(pdf_list)
    print(f"📊 Total Actas Únicas a Analizar: {total}")
    
    os.makedirs(output_dir, exist_ok=True)
    
    csv_file = os.path.join(output_dir, "REPORTE_FLUJO_TEXTO_Y_QR.csv")
    md_file = os.path.join(output_dir, "REPORTE_FLUJO_TEXTO_Y_QR.md")
    
    results = []
    processed = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        for r in executor.map(extract_stream_and_qr_data, pdf_list):
            processed += 1
            results.append(r)
            if processed % 10 == 0 or processed == total:
                print(f"  ➜ Extraídos {processed} / {total} flujos ({(processed/total*100):.1f}%)...")

    results.sort(key=lambda x: (x["folder"], x["filename"]))

    # Export CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Archivo_Mesa", "Ubicacion_Origen", "Cadena_Codigo_QR", "Texto_Flujo_Contents", "Capas_XObject"])
        for r in results:
            writer.writerow([r["filename"], r["folder"], r["qr_content"], r["text_stream_content"], r["xobjects_count"]])

    # 3. Export TXT
    txt_file = os.path.join(output_dir, "REPORTE_FLUJO_TEXTO_Y_QR.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("TABLA DE EXTRACCIÓN DE FLUJO DE TEXTO INTERNO Y CÓDIGOS QR\n")
        f.write("="*80 + "\n\n")
        for r in results:
            f.write(f"ARCHIVO: {r['filename']}\n")
            f.write(f"UBICACIÓN: {r['folder']}\n")
            f.write(f"CADENA QR: {r['qr_content']}\n")
            f.write(f"FLUJO TEXTO (/Contents): {r['text_stream_content']}\n")
            f.write(f"CAPAS XOBJECT: {r['xobjects_count']}\n")
            f.write("-" * 60 + "\n")

    print(f"\n✅ Extracción de flujo completada. Resultados en: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Motor Forense AndreTaker - Extracción de Flujos y QR")
    parser.add_argument("--input", required=True, help="Directorio raíz de la evidencia")
    parser.add_argument("--output", required=True, help="Directorio de salida para los reportes CSV/MD")
    parser.add_argument("--zone", required=False, default="", help="Filtro opcional de zona (ej. 88_360_035)")
    args = parser.parse_args()
    
    run_extraction(args.input, args.output, args.zone)
