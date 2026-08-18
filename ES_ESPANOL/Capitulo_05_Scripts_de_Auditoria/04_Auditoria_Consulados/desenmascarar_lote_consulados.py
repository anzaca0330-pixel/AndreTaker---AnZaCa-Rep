#!/usr/bin/env python3
import os
import glob
import subprocess

def unmask_consulate_sample():
    out_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/DESENMASCARAMIENTO_CAPAS_OCULTAS"
    os.makedirs(out_dir, exist_ok=True)
    
    print("🔬 [DESENMASCARAMIENTO] Buscando capas ocultas bajo las máscaras blancas...")
    
    # Buscar PDFs de consulados claves (Los Ángeles, Miami, Orlando, Madrid, Boston)
    sample_pdfs = []
    base_search = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
    
    for root, dirs, files in os.walk(base_search):
        for f in files:
            if f.lower().endswith('.pdf'):
                full = os.path.join(root, f)
                low = full.lower()
                if any(k in low for k in ["088", "consul", "exterior", "los_angeles", "los angeles", "miami", "orlando", "madrid", "boston"]):
                    sample_pdfs.append(full)
                    if len(sample_pdfs) >= 30: # Tomar una muestra de 30 actas clave
                        break
        if len(sample_pdfs) >= 30:
            break
            
    print(f"📊 Procesando muestra de {len(sample_pdfs)} actas consulares clave...")
    
    for idx, pdf in enumerate(sample_pdfs, 1):
        fname = os.path.splitext(os.path.basename(pdf))[0]
        pdf_out = os.path.join(out_dir, f"{idx:02d}_{fname}")
        os.makedirs(pdf_out, exist_ok=True)
        
        # 1. Extraer TODAS las capas de imagen puras (incluyendo las tapadas)
        subprocess.run(["pdfimages", "-all", pdf, os.path.join(pdf_out, "capa_raw")], capture_output=True)
        
        # 2. Descomprimir estructura de objetos con qpdf
        decomp_pdf = os.path.join(pdf_out, "descomprimido.qdf")
        subprocess.run(["qpdf", "--qdf", "--object-streams=disable", pdf, decomp_pdf], capture_output=True)
        
        # 3. Contar imágenes extraídas
        extracted_imgs = glob.glob(os.path.join(pdf_out, "capa_raw*"))
        print(f"  ➜ [{idx}/{len(sample_pdfs)}] `{fname}`: Extraídas {len(extracted_imgs)} capas de imagen puras en: {pdf_out}")

    print(f"\n🎉 ¡Desenmascaramiento completado!")
    print(f"📁 Revisa todas las capas desenterradas en: {out_dir}")

if __name__ == "__main__":
    unmask_consulate_sample()
