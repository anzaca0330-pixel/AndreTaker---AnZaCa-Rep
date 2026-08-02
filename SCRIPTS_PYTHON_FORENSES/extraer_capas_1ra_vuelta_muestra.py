#!/usr/bin/env python3
import os
import glob
import subprocess

def extract_1st_round_sample_layers():
    v1_dir = "/home/andrea-zabala-c/Documents/Para Revisar/E14"
    out_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/DESENMASCARAMIENTO_CAPAS_OCULTAS/1RA_VUELTA_MUESTRA"
    os.makedirs(out_dir, exist_ok=True)
    
    print("🔬 [DESENMASCARAMIENTO 1RA VUELTA] Extrayendo capas puras de la 1ª Vuelta...")
    
    pdf_list = []
    for root, dirs, files in os.walk(v1_dir):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_list.append(os.path.join(root, f))
                if len(pdf_list) >= 10: break
        if len(pdf_list) >= 10: break
        
    for idx, pdf in enumerate(pdf_list, 1):
        fname = os.path.splitext(os.path.basename(pdf))[0]
        sub_dir = os.path.join(out_dir, f"v1_mesa_{idx:02d}_{fname}")
        os.makedirs(sub_dir, exist_ok=True)
        
        # pdfimages -all
        subprocess.run(["pdfimages", "-all", pdf, os.path.join(sub_dir, "capa_v1")], capture_output=True)
        imgs = glob.glob(os.path.join(sub_dir, "capa_v1*"))
        print(f"  ➜ [1ª Vuelta Mesa {idx}] `{fname}`: Extraídas {len(imgs)} capas puras en: {sub_dir}")

    print(f"\n🎉 Extracción de capas de 1ª Vuelta completada en: {out_dir}")

if __name__ == "__main__":
    extract_1st_round_sample_layers()
