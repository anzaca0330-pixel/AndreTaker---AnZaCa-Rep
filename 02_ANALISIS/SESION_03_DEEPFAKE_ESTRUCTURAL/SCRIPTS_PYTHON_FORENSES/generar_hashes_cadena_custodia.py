#!/usr/bin/env python3
import os
import sys
import hashlib
import argparse
from concurrent.futures import ThreadPoolExecutor

def calculate_sha256(file_path):
    """Calcula el hash SHA-256 de un archivo en bloques para optimizar memoria."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(65536), b""):
                sha256_hash.update(byte_block)
        return file_path, sha256_hash.hexdigest(), None
    except Exception as e:
        return file_path, None, str(e)

def generate_hashes(target_dir, output_file):
    print(f"🔒 Iniciando Generación Criptográfica de Hashes SHA-256 (Cadena de Custodia)")
    print(f"📁 Directorio objetivo: {target_dir}")
    
    pdf_files = []
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, f))
                
    total = len(pdf_files)
    print(f"📊 Total de archivos a firmar: {total}")
    
    processed = 0
    with open(output_file, "w", encoding="utf-8") as out_f, ThreadPoolExecutor(max_workers=16) as executor:
        out_f.write("# REGISTRO CRIPTOGRÁFICO SHA-256 - CADENA DE CUSTODIA FORENSE\n")
        out_f.write(f"# Total de Archivos: {total}\n")
        out_f.write("# Formato: HASH_SHA256  RUTA_RELATIVA\n\n")
        
        for file_path, sha256, err in executor.map(calculate_sha256, pdf_files):
            processed += 1
            if sha256:
                rel_path = os.path.relpath(file_path, target_dir)
                out_f.write(f"{sha256}  {rel_path}\n")
            if processed % 5000 == 0 or processed == total:
                print(f"  ➜ Procesados {processed} / {total} archivos ({(processed/total*100):.1f}%)...")
                
    print(f"✅ Hashes SHA-256 generados exitosamente.")
    print(f"📄 Manifiesto de Cadena de Custodia guardado en: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador Criptográfico de Hashes SHA-256 para Cadena de Custodia")
    parser.add_argument("--dir", type=str, default="/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf", help="Directorio objetivo")
    parser.add_argument("--out", type=str, default="/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf/firmas_criptograficas_sha256.txt", help="Archivo de manifiesto de salida")
    args = parser.parse_args()
    
    generate_hashes(args.dir, args.out)
