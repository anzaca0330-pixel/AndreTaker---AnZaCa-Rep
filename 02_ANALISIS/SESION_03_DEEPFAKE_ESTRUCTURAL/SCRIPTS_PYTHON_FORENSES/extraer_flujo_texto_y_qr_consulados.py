#!/usr/bin/env python3
import os
import csv
import glob
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor

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
        subprocess.run(["pdftoppm", "-png", "-singlefile", "-r", "150", pdf_path, tmp_img[:-4]], capture_output=True, timeout=10)
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
            res["text_stream_content"] = clean_t[:150] # Primeros 150 caracteres
        else:
            # Si no hay texto renderizado, buscar flujos descompresados QPDF
            qproc = subprocess.run(["qpdf", "--qdf", "--object-streams=disable", pdf_path, "-"], capture_output=True, text=True, timeout=10)
            bt_matches = re.findall(r'BT\s+([\s\S]*?)\s+ET', qproc.stdout)
            if bt_matches:
                res["text_stream_content"] = (" | ".join(bt_matches))[:150]
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

def run_extraction_matrix():
    print("🔬 [EXTRACCIÓN DE FLUJO] Parseando contenido inyectado en /Contents y códigos QR...")
    
    base_dirs = [
        "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf",
        "/home/andrea-zabala-c/Documents/Para Revisar/E14",
        "/media/andrea-zabala-c/D A T A1/EVIDENCIA_FORENSE_E14_2026",
        "/media/andrea-zabala-c/BACKUP/EVIDENCIA_FORENSE_E14_2026"
    ]
    
    pdf_list = []
    seen = set()
    for bdir in base_dirs:
        if not os.path.exists(bdir): continue
        for root, dirs, files in os.walk(bdir):
            for f in files:
                if f.lower().endswith('.pdf'):
                    full = os.path.join(root, f)
                    if full in seen: continue
                    low = full.lower()
                    if any(k in low for k in ["088", "consul", "exterior", "estados", "espana", "españa", "miami", "madrid", "orlando", "los angeles", "boston"]):
                        seen.add(full)
                        pdf_list.append(full)
                        
    total = len(pdf_list)
    print(f"📊 Total Actas Consulares a Extraer Flujo de Texto/QR: {total}")
    
    out_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/ENTREGABLES_FORENSES_E14"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)
    
    md_file = os.path.join(out_dir, "TABLA_FLUJO_TEXTO_Y_QR_CONSULADOS.md")
    csv_file = os.path.join(out_dir, "TABLA_FLUJO_TEXTO_Y_QR_CONSULADOS.csv")
    txt_file = os.path.join(out_dir, "TABLA_FLUJO_TEXTO_Y_QR_CONSULADOS.txt")
    
    results = []
    processed = 0
    with ThreadPoolExecutor(max_workers=16) as executor:
        for r in executor.map(extract_stream_and_qr_data, pdf_list):
            processed += 1
            results.append(r)
            if processed % 100 == 0 or processed == total:
                print(f"  ➜ Extraídos {processed} / {total} flujos ({(processed/total*100):.1f}%)...")

    # Order by folder/filename
    results.sort(key=lambda x: (x["folder"], x["filename"]))

    # 1. Export Markdown
    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# TABLA DE EXTRACCIÓN DE FLUJO DE TEXTO INTERNO Y CÓDIGOS QR — CONSULADOS\n\n")
        f.write(f"**Total Actas Extraídas:** {total}  \n\n")
        f.write("---  \n\n")
        f.write("| Archivo / Mesa | Ubicación / Consulado | Cadena Decodificada Código QR | Texto / Datos Inyectados en Flujo (`/Contents`) | Capas Img (`/XObject`) |\n")
        f.write("|---|---|---|---|---|\n")
        for r in results[:300]: # Primeros 300 para el reporte Markdown
            f.write(f"| `{r['filename']}` | {r['folder']} | `{r['qr_content']}` | `{r['text_stream_content']}` | {r['xobjects_count']} |\n")

    # 2. Export CSV (COMPLETO TODOS LOS REGISTROS)
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Archivo_Mesa", "Ubicacion_Consulado", "Cadena_Codigo_QR", "Texto_Flujo_Contents", "Capas_XObject"])
        for r in results:
            writer.writerow([r["filename"], r["folder"], r["qr_content"], r["text_stream_content"], r["xobjects_count"]])

    # 3. Export TXT
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

    os.system(f"cp -rv '{out_dir}'/TABLA_FLUJO_TEXTO_Y_QR_CONSULADOS.* '{drive_dir}'/")
    print(f"\n✅ Extracción de flujo de texto y QR completada exitosamente.")
    print(f"📄 Archivos guardados en Escritorio y Disco Portátil.")

if __name__ == "__main__":
    run_extraction_matrix()
