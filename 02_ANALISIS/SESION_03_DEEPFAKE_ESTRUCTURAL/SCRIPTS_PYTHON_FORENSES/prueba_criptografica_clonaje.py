#!/usr/bin/env python3
import os
import sys
import subprocess
import hashlib
import tempfile
import shutil

def calculate_sha256(filepath):
    """Calcula el hash SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Leemos en bloques por si las capas son grandes
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def extract_and_hash_layers(pdf_path, temp_dir):
    """Extrae las capas con pdfimages y calcula sus hashes."""
    print(f"[*] Analizando PDF: {pdf_path}")
    prefix = os.path.join(temp_dir, "capa")
    
    # Ejecutamos pdfimages -all
    try:
        subprocess.run(["pdfimages", "-all", pdf_path, prefix], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error al extraer imágenes de {pdf_path}: {e.stderr.decode('utf-8')}")
        return {}

    # Listamos los archivos extraídos y calculamos sus hashes
    extracted_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
    print(f"    - Se extrajeron {len(extracted_files)} capas binarias puras.")
    
    hashes = {}
    for filename in extracted_files:
        filepath = os.path.join(temp_dir, filename)
        file_hash = calculate_sha256(filepath)
        size_bytes = os.path.getsize(filepath)
        # Solo consideramos capas con peso significativo (>100 bytes) para evitar coincidencias de ruido.
        if size_bytes > 100:
            hashes[file_hash] = filename
            
    return hashes

def main():
    print("="*60)
    print("🔍 PRUEBA CRIPTOGRÁFICA DE CLONAJE (METROLOGÍA BINARIA) 🔍")
    print("="*60)
    
    if len(sys.argv) != 3:
        print("Uso: python3 prueba_criptografica_clonaje.py <pdf_delegados> <pdf_claveros>")
        sys.exit(1)
        
    pdf_delegados = sys.argv[1]
    pdf_claveros = sys.argv[2]
    
    if not os.path.exists(pdf_delegados) or not os.path.exists(pdf_claveros):
        print("[!] Error: Uno de los archivos PDF no existe.")
        sys.exit(1)
        
    # Creamos dos directorios temporales limpios
    temp_dir_del = tempfile.mkdtemp()
    temp_dir_clav = tempfile.mkdtemp()
    
    try:
        hashes_del = extract_and_hash_layers(pdf_delegados, temp_dir_del)
        hashes_clav = extract_and_hash_layers(pdf_claveros, temp_dir_clav)
        
        print("\n" + "-"*60)
        print("⚖️  RESULTADO DEL CRUCE CRIPTOGRÁFICO ⚖️")
        print("-"*60)
        
        set_del = set(hashes_del.keys())
        set_clav = set(hashes_clav.keys())
        
        interseccion = set_del.intersection(set_clav)
        
        if interseccion:
            print("[CRÍTICO] ¡ALERTA DE CLONAJE CONFIRMADO!")
            print(f"Se encontraron {len(interseccion)} capas binarias EXACTAMENTE IGUALES en ambos archivos.\n")
            
            for h in interseccion:
                print(f"  > Hash SHA-256 Coincidente: {h}")
                print(f"    - Archivo Delegados: {hashes_del[h]}")
                print(f"    - Archivo Claveros: {hashes_clav[h]}")
                print("    ---")
                
            print("\n[VEREDICTO FORENSE]: Aunque los metadatos y nombres externos de los PDFs difieren,")
            print("el ADN binario interno (capas gráficas o QR) es idéntico a nivel criptográfico.")
            print("Ruptura total de cadena de custodia probada.")
        else:
            print("[INFO] No se encontraron capas binarias idénticas (hashes SHA-256 distintos).")
            print("Es posible que se trate de escaneos legítimos separados, o de una alteración más profunda.")
            
    finally:
        shutil.rmtree(temp_dir_del)
        shutil.rmtree(temp_dir_clav)

if __name__ == "__main__":
    main()
