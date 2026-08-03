#!/usr/bin/env python3
import os
import glob
import subprocess
import re

def compare_advance_vs_sunday_2nd_round():
    print("🔬 [VERIFICACIÓN 2DA VUELTA] Comparando Votación Adelantada (Semana Previa) vs. Domingo...")
    
    base_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
    
    advance_pdfs = []
    sunday_pdfs = []
    
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.lower().endswith('.pdf'):
                full = os.path.join(root, f)
                low = full.lower()
                if any(k in low for k in ["088", "consul", "exterior"]):
                    if any(k in low for k in ["semana", "anticipada", "previa", "adelantada"]):
                        advance_pdfs.append(full)
                    else:
                        sunday_pdfs.append(full)
                        
    print(f"📊 Total Actas Votación Adelantada Identificadas (2ª Vuelta): {len(advance_pdfs)}")
    print(f"📊 Total Actas Domingo Identificadas (2ª Vuelta): {len(sunday_pdfs)}")
    
    # Inspeccionar muestra de ambas categorías
    def check_sample(pdf_list, label):
        meta_purged = 0
        xref_warns = 0
        multi_img = 0
        
        sample = pdf_list[:50]
        for pdf in sample:
            # 1. ExifTool
            proc_meta = subprocess.run(["exiftool", "-Creator", "-Producer", "-CreateDate", pdf], capture_output=True, text=True)
            if not proc_meta.stdout.strip():
                meta_purged += 1
            # 2. QPDF
            proc_qpdf = subprocess.run(["qpdf", "--check", pdf], capture_output=True, text=True)
            if "operation succeeded with warnings" in proc_qpdf.stdout or "warning" in proc_qpdf.stderr.lower():
                xref_warns += 1
            # 3. pdfimages
            proc_img = subprocess.run(["pdfimages", "-list", pdf], capture_output=True, text=True)
            lines = [l for l in proc_img.stdout.splitlines() if l.strip()]
            if len(lines) > 4: # más de 2 imágenes incrustadas
                multi_img += 1
                
        tot = len(sample)
        print(f"\n--- RESULTADOS MUESTRA 2DA VUELTA: {label} (N={tot}) ---")
        print(f"  ➜ Metadatos Depurados (ExifTool): {meta_purged}/{tot} ({(meta_purged/tot*100):.1f}%)")
        print(f"  ➜ Advertencias XREF (QPDF): {xref_warns}/{tot} ({(xref_warns/tot*100):.1f}%)")
        print(f"  ➜ Capas de Imagen Multicapa (pdfimages): {multi_img}/{tot} ({(multi_img/tot*100):.1f}%)")
        
    if advance_pdfs:
        check_sample(advance_pdfs, "VOTACIÓN ADELANTADA / SEMANA PREVIA")
    check_sample(sunday_pdfs, "JORNADA DOMINGO ELECCIÓN")

if __name__ == "__main__":
    compare_advance_vs_sunday_2nd_round()
