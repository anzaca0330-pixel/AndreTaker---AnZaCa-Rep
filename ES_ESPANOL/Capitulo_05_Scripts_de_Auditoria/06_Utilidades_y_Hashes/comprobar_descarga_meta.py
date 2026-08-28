import os
import hashlib

def calcular_hash_sha256(ruta_archivo):
    sha256_hash = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def principal():
    dir_delegados = "/media/andrea-zabala-c/D A T A1/delegados/Delegados_21_06_2026"
    dir_meta_descarga = "/home/andrea-zabala-c/Downloads/Meta. "
    
    # Obtener lista de hashes en Meta.
    hashes_meta_descarga = set()
    for f in os.listdir(dir_meta_descarga):
        if f.endswith(".pdf"):
            hashes_meta_descarga.add(f.replace(".pdf", ""))
            
    print(f"Total PDFs en Meta. (Downloads): {len(hashes_meta_descarga)}")
    
    coincidencias = 0
    total_delegados = 0
    
    for file in os.listdir(dir_delegados):
        if file.startswith("52_") and file.endswith(".pdf"): # Filtrar Meta
            ruta_delegados = os.path.join(dir_delegados, file)
            hash_dele = calcular_hash_sha256(ruta_delegados)
            total_delegados += 1
            if hash_dele in hashes_meta_descarga:
                coincidencias += 1
            
            if total_delegados >= 50: # Muestra de 50 para rapidez
                break
                
    print(f"Total archivos evaluados de Delegados (21 Jun): {total_delegados}")
    print(f"Coincidencias de hash exactas encontradas en Meta. (Downloads): {coincidencias}")

if __name__ == '__main__':
    principal()
