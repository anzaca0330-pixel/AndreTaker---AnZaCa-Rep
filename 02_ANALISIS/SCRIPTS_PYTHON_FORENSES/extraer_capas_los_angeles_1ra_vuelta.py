#!/usr/bin/env python3
import os
import glob
import subprocess

import hashlib

def get_file_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

def extract_la_1st_round_layers():
    la_base = "/media/andrea-zabala-c/ANZACA"
    out_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/DESENMASCARAMIENTO_CAPAS_OCULTAS/1RA_VUELTA_LOS_ANGELES"
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"🔬 [DESENMASCARAMIENTO LOS ÁNGELES - 1ª VUELTA] Escaneando TODO el disco ANZACA por la Zona 035...")
    
    la_pdfs = []
    seen_hashes = set()
    for root, dirs, files in os.walk(la_base):
        for f in files:
            if f.lower().endswith('.pdf') and '88_360_035' in f and '_descomprimido' not in f.lower():
                filepath = os.path.join(root, f)
                file_hash = get_file_hash(filepath)
                if file_hash not in seen_hashes:
                    seen_hashes.add(file_hash)
                    la_pdfs.append(filepath)
                
    print(f"📊 Total Actas de Los Ángeles (1ª Vuelta) Encontradas: {len(la_pdfs)}")
    
    for idx, pdf in enumerate(la_pdfs, 1):
        folder_name = os.path.basename(os.path.dirname(pdf))
        fname = os.path.splitext(os.path.basename(pdf))[0]
        sub_dir = os.path.join(out_dir, f"{idx:02d}_{folder_name}_{fname}")
        os.makedirs(sub_dir, exist_ok=True)
        
        # Extracción pura de imágenes
        subprocess.run(["pdfimages", "-all", pdf, os.path.join(sub_dir, "capa_la_v1")], capture_output=True)
        
        # Descomprimir estructura QPDF
        decomp_file = os.path.join(sub_dir, "descomprimido.qdf")
        subprocess.run(["qpdf", "--qdf", "--object-streams=disable", pdf, decomp_file], capture_output=True)
        
        imgs = glob.glob(os.path.join(sub_dir, "capa_la_v1*"))
        print(f"  ➜ [{idx}/{len(la_pdfs)}] `{folder_name}/{fname}`: Extraídas {len(imgs)} capas puras en: {sub_dir}")

    print(f"\n🎉 ¡Extracción completa de capas de 1ª Vuelta de Los Ángeles finalizada!")
    print(f"📁 Revisa las capas desenterradas en: {out_dir}")

if __name__ == "__main__":
    extract_la_1st_round_layers()
