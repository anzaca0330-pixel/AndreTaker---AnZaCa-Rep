import os
import hashlib
import re

def calcular_hash_sha256(ruta_archivo):
    sha256_hash = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def principal():
    dir_claveros = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf/META/VILLAVICENCIO"
    dir_delegados = "/media/andrea-zabala-c/D A T A1/delegados/Delegados_21_06_2026"
    
    # E14_PRE_52_001_001_01_01_001_6900_Mesa_1.pdf -> 52_001_01_01_001.pdf
    patron = re.compile(r'E14_PRE_(\d+)_(\d+)_001_(\d+)_(\d+)_(\d+)_.*\.pdf')
    
    total_comparados = 0
    alterados = 0
    
    print("Iniciando comparación criptográfica: Meta/Villavicencio (2da Vuelta)")
    print("=" * 70)
    
    for root, dirs, files in os.walk(dir_claveros):
        for file in files:
            if not file.endswith(".pdf"):
                continue
            
            match = patron.match(file)
            if match:
                # Construir el nombre en el formato de Delegados
                # ej: 52_001_01_01_001.pdf
                nombre_delegados = f"{match.group(1)}_{match.group(2)}_{match.group(3)}_{match.group(4)}_{match.group(5)}.pdf"
                
                ruta_claveros = os.path.join(root, file)
                ruta_delegados = os.path.join(dir_delegados, nombre_delegados)
                
                if os.path.exists(ruta_delegados):
                    hash_clav = calcular_hash_sha256(ruta_claveros)
                    hash_dele = calcular_hash_sha256(ruta_delegados)
                    
                    size_clav = os.path.getsize(ruta_claveros)
                    size_dele = os.path.getsize(ruta_delegados)
                    
                    total_comparados += 1
                    
                    if hash_clav != hash_dele:
                        alterados += 1
                        print(f"[-] ALTERADO: {nombre_delegados}")
                        print(f"    Delegados (21-Jun): Hash: {hash_dele[:8]}... Size: {size_dele} bytes")
                        print(f"    Claveros (Julio)  : Hash: {hash_clav[:8]}... Size: {size_clav} bytes ({(size_clav/size_dele):.2f}x de inflado)")
                    else:
                        print(f"[+] INTACTO : {nombre_delegados}")
                        
            if total_comparados >= 20: # Limitar a 20 para la prueba inicial
                break
        if total_comparados >= 20:
            break

    print("=" * 70)
    print(f"Total comparados: {total_comparados}")
    print(f"Total alterados: {alterados} ({(alterados/total_comparados)*100 if total_comparados > 0 else 0:.1f}%)")

if __name__ == '__main__':
    principal()
