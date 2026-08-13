#!/usr/bin/env python3
import os
import sys
import glob
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor

def analyze_pdf(pdf_path):
    """
    Ejecuta el peritaje completo sobre un PDF individual:
    1. QPDF Check (Estructura interna / advertencias xref)
    2. ExifTool (Metadatos Creator, Producer, CreationDate)
    3. pdfimages -list (Conteo de capas de imágenes incrustadas)
    4. mutool + zbarimg (Decodificación de código QR)
    """
    res = {
        "pdf": pdf_path,
        "anomalia_estructura": False,
        "metadatos_vacios": False,
        "num_imagenes": 0,
        "multicapa_sospechosa": False,
        "qr_extraido": False,
        "qr_contenido": ""
    }
    
    # 1. QPDF Check
    try:
        proc = subprocess.run(["qpdf", "--check", pdf_path], capture_output=True, text=True, timeout=10)
        if "operation succeeded with warnings" in proc.stdout or "operation succeeded with warnings" in proc.stderr:
            res["anomalia_estructura"] = True
    except Exception:
        pass
        
    # 2. ExifTool Metadata Check
    try:
        proc = subprocess.run(["exiftool", "-Creator", "-Producer", "-CreateDate", pdf_path], capture_output=True, text=True, timeout=10)
        out = proc.stdout.strip()
        if not out or ("Creator" not in out and "Producer" not in out and "CreateDate" not in out):
            res["metadatos_vacios"] = True
    except Exception:
        pass

    # 3. pdfimages -list (Capas de Imagen)
    try:
        proc = subprocess.run(["pdfimages", "-list", pdf_path], capture_output=True, text=True, timeout=10)
        lines = [l for l in proc.stdout.splitlines() if l.strip()]
        # Quitar las dos líneas de cabecera si existen
        img_count = max(0, len(lines) - 2)
        res["num_imagenes"] = img_count
        if img_count > 2:
            res["multicapa_sospechosa"] = True
    except Exception:
        pass

    # 4. QR Extraction (mutool + zbarimg)
    try:
        tmp_prefix = f"/tmp/qr_check_{os.getpid()}_{hash(pdf_path) & 0xffff}"
        subprocess.run(["mutool", "extract", pdf_path], cwd="/tmp", capture_output=True, timeout=10)
        # Buscar imágenes extraídas en /tmp
        extracted_imgs = sorted(glob.glob("/tmp/image-*.png") + glob.glob("/tmp/image-*.jpg"), key=os.path.getmtime, reverse=True)
        if extracted_imgs:
            img = extracted_imgs[0]
            zproc = subprocess.run(["zbarimg", "--raw", "-q", img], capture_output=True, text=True, timeout=10)
            qr_val = zproc.stdout.strip()
            if qr_val:
                res["qr_extraido"] = True
                res["qr_contenido"] = qr_val
        # Limpiar imágenes temporales
        for img in extracted_imgs:
            try: os.remove(img)
            except Exception: pass
    except Exception:
        pass
        
    return res

def run_forensic_analysis(target_dirs, output_markdown):
    print(f"🔬 Iniciando Peritaje Forense Automatizado sobre TODOS los Consulados del Mundo...")
    
    colombian_deptos = {'ANTIOQUIA', 'ATLANTICO', 'BOGOTA D.C.', 'BOLIVAR', 'BOYACA', 'CALDAS', 'CAUCA', 'CESAR', 'CHOCO', 'CORDOBA', 'CUNDINAMARCA', 'HUILA', 'MAGDALENA', 'NARIÑO', 'NORTE DE SAN', 'QUINDIO', 'RISARALDA', 'SANTANDER', 'SUCRE', 'TOLIMA', 'VALLE', 'ARAUCA', 'CAQUETA', 'CASANARE', 'LA GUAJIRA', 'GUAINIA', 'META', 'GUAVIARE', 'SAN ANDRES', 'AMAZONAS', 'PUTUMAYO', 'VAUPES', 'VICHADA'}
    
    pdf_list = []
    seen = set()
    
    for tdir in target_dirs:
        if not os.path.exists(tdir):
            continue
        print(f"  ➜ Escaneando ruta de evidencia: {tdir}")
        for root, dirs, files in os.walk(tdir):
            for f in files:
                if f.lower().endswith('.pdf'):
                    full_path = os.path.join(root, f)
                    if full_path in seen:
                        continue
                    
                    # Criterio de inclusión: Cualquier acta de Consulado / Exterior (Código 88 o fuera de los 33 departamentos nacionales)
                    parts = full_path.split(os.sep)
                    is_consulate = False
                    for part in parts:
                        up = part.upper()
                        if '088' in up or 'CONSUL' in up or 'EXTERIOR' in up or any(k in up for k in ['ESTADOS', 'ESPAÑA', 'ESPANA', 'ALEMANIA', 'ARGENTINA', 'AUSTRALIA', 'BELGICA', 'BOLIVIA', 'BRASIL', 'CANADA', 'CHILE', 'CHINA', 'COSTA RICA', 'CUBA', 'ECUADOR', 'FRANCIA', 'INGLATERRA', 'ITALIA', 'JAPON', 'MEXICO', 'PANAMA', 'PERU', 'SUIZA', 'VENEZUELA', 'URUGUAY', 'PARAGUAY']):
                            is_consulate = True
                            break
                    
                    if is_consulate:
                        seen.add(full_path)
                        pdf_list.append(full_path)
                    
    total_pdfs = len(pdf_list)
    print(f"📊 Total de Actas de Consulados (TODOS LOS PAÍSES) Identificadas: {total_pdfs}")
    
    # Map de Paises Conocidos / Consulares
    country_keywords = {
        'ESTADOS UNIDOS': ['ESTADOS UNIDOS', 'ATLANTA', 'BOSTON', 'CHICAGO', 'HOUSTON', 'LOS ANGELES', 'LOS_ANGELES', 'MIAMI', 'NEW YORK', 'NEW_YORK', 'NEWARK', 'ORLANDO', 'SAN FRANCISCO', 'SAN_FRANCISCO', 'WASHINGTON'],
        'ESPAÑA': ['ESPAÑA', 'ESPANA', 'MADRID', 'BARCELONA', 'VALENCIA', 'SEVILLA', 'BILBAO'],
        'CANADÁ': ['CANADA', 'TORONTO', 'MONTREAL', 'VANCOUVER', 'OTTAWA'],
        'MÉXICO': ['MEXICO', 'GUADALAJARA', 'MONTERREY'],
        'VENEZUELA': ['VENEZUELA', 'CARACAS', 'MARACAIBO', 'SAN CRISTOBAL'],
        'ALEMANIA': ['ALEMANIA', 'BERLIN', 'FRANKFURT'],
        'FRANCIA': ['FRANCIA', 'PARIS'],
        'INGLATERRA / REINO UNIDO': ['INGLATERRA', 'LONDRES', 'REINO UNIDO'],
        'ITALIA': ['ITALIA', 'ROMA', 'MILAN'],
        'SUIZA': ['SUIZA', 'GINEBRA', 'BERNA'],
        'ARGENTINA': ['ARGENTINA', 'BUENOS AIRES'],
        'CHILE': ['CHILE', 'SANTIAGO'],
        'BRASIL': ['BRASIL', 'BRASILIA', 'SAO PAULO'],
        'ECUADOR': ['ECUADOR', 'QUITO', 'GUAYAQUIL'],
        'PERÚ': ['PERU', 'LIMA'],
        'PANAMÁ': ['PANAMA'],
        'COSTA RICA': ['COSTA RICA', 'SAN JOSE'],
        'CUBA': ['CUBA', 'LA HABANA'],
        'BOLIVIA': ['BOLIVIA', 'LA PAZ'],
        'URUGUAY': ['URUGUAY', 'MONTEVIDEO'],
        'PARAGUAY': ['PARAGUAY', 'ASUNCION'],
        'JAPÓN': ['JAPON', 'TOKIO'],
        'AUSTRALIA': ['AUSTRALIA', 'SYDNEY', 'CANBERRA'],
        'CHINA': ['CHINA', 'PEKIN', 'SHANGHAI']
    }
    
    results_by_country = {}
    
    processed = 0
    with ThreadPoolExecutor(max_workers=16) as executor:
        for r in executor.map(analyze_pdf, pdf_list):
            processed += 1
            full_p = r["pdf"].upper()
            
            # Detectar país
            matched_country = "OTROS CONSULADOS / VOTO EXTERIOR"
            for country_name, keywords in country_keywords.items():
                if any(kw in full_p for kw in keywords):
                    matched_country = country_name
                    break
                    
            if matched_country not in results_by_country:
                results_by_country[matched_country] = {
                    "total": 0,
                    "anomalias": 0
                }
                
            cdict = results_by_country[matched_country]
            cdict["total"] += 1
            # Se considera anómalo si tiene advertencia de estructura QPDF, metadatos vacíos o multicapa
            if r["anomalia_estructura"] or r["metadatos_vacios"] or r["multicapa_sospechosa"]:
                cdict["anomalias"] += 1
                
            if processed % 100 == 0 or processed == total_pdfs:
                print(f"  ➜ Peritando {processed} / {total_pdfs} actas ({(processed/total_pdfs*100):.1f}%)...")
                
    # Generar Tabla Markdown de 4 Columnas
    with open(output_markdown, "w", encoding="utf-8") as out:
        out.write("# TABLA CONSOLIDADA DE ANÁLISIS FORENSE — CONSULADOS EN TODOS LOS PAÍSES\n")
        out.write(f"**Fecha de Análisis:** Julio de 2026  \n")
        out.write(f"**Total Actas Peritadas en Consulados:** {total_pdfs}  \n\n")
        out.write("---  \n\n")
        out.write("## 1. TABLA DE ANOMALÍAS FORENSES POR PAÍS\n\n")
        out.write("| País | Actas Totales | Con Anomalías | Porcentaje de Anomalías |\n")
        out.write("|---|---|---|---|\n")
        
        tot_global = 0
        tot_anomalias = 0
        
        for country_name, data in sorted(results_by_country.items()):
            tot = data["total"]
            anom = data["anomalias"]
            pct = (anom / tot * 100) if tot > 0 else 0
            
            tot_global += tot
            tot_anomalias += anom
            
            out.write(f"| **{country_name}** | {tot} | {anom} | **{pct:.1f}%** |\n")
            
        pct_global = (tot_anomalias / tot_global * 100) if tot_global > 0 else 0
        out.write(f"| **TOTAL CONSOLIDADO** | **{tot_global}** | **{tot_anomalias}** | **{pct_global:.1f}%** |\n\n")
        
        out.write("---  \n\n")
        out.write("## 2. HALLAZGOS Y CONCLUSIONES PERICIALES\n\n")
        out.write(f"- **Universo Total Analizado:** {tot_global} actas consulares en el exterior.\n")
        out.write(f"- **Tasa Global de Desviación:** El **{pct_global:.1f}%** del total de actas consulares presenta patrones anómalos de depuración de metadatos o inconsistencias sintácticas en la tabla `xref`.\n")

    print(f"\n✅ Análisis forense de 4 columnas completado con éxito.")
    print(f"📊 Tabla Markdown guardada en: {output_markdown}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análisis Forense Multihilo para Actas E14 de Consulados")
    parser.add_argument("--out", type=str, default="/home/andrea-zabala-c/Desktop/TABLA_ANALISIS_FORENSE_CONSULADOS.md", help="Ruta de la tabla Markdown de salida")
    args = parser.parse_args()
    
    target_paths = [
        "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf",
        "/home/andrea-zabala-c/Documents/Para Revisar/E14",
        "/media/andrea-zabala-c/D A T A1/EVIDENCIA_FORENSE_E14_2026",
        "/media/andrea-zabala-c/BACKUP/EVIDENCIA_FORENSE_E14_2026",
        "/home/andrea-zabala-c/Desktop"
    ]
    
    run_forensic_analysis(target_paths, args.out)
