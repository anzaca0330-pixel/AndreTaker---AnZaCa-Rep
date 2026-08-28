import os
import subprocess
import hashlib
import glob
import shutil

def get_qr(img_path):
    try:
        out = subprocess.check_output(['zbarimg', '-q', '--raw', img_path], stderr=subprocess.DEVNULL)
        return out.decode('utf-8').strip()
    except:
        return None

def calcular_hash_sha256(ruta_archivo):
    sha256_hash = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def principal():
    dir_pc = "/home/andrea-zabala-c/Downloads/Meta. "
    dir_disco = "/media/andrea-zabala-c/D A T A1/delegados/Delegados_21_06_2026"
    
    print("Mapeando QR codes en PC (Downloads/Meta.)...")
    pc_qr_map = {} 
    
    for img_file in glob.glob(os.path.join(dir_pc, "*_img-000.png")):
        qr = get_qr(img_file)
        if qr:
            pdf_path = img_file.replace("_img-000.png", ".pdf")
            if os.path.exists(pdf_path):
                pc_qr_map[qr] = pdf_path
                
    print(f"Archivos PC mapeados por QR: {len(pc_qr_map)}")
    
    print("\nBuscando coincidencias en Disco (Delegados 21 Jun)...")
    
    tmp_dir = "/tmp/qrs_disco"
    os.makedirs(tmp_dir, exist_ok=True)
    
    coincidencias = 0
    alterados = 0
    
    # Filtrar solo ACACIAS (005) o todos los de Meta
    archivos_disco = [f for f in os.listdir(dir_disco) if f.startswith("52_005_") and f.endswith(".pdf")]
    
    for i, file in enumerate(archivos_disco): 
        ruta_pdf_disco = os.path.join(dir_disco, file)
        
        prefix = os.path.join(tmp_dir, f"ext_{i}")
        subprocess.run(['pdfimages', '-png', '-f', '1', '-l', '1', ruta_pdf_disco, prefix], stderr=subprocess.DEVNULL)
        
        img_extraida = f"{prefix}-000.png"
        if not os.path.exists(img_extraida):
            continue
            
        qr_disco = get_qr(img_extraida)
        
        for f in glob.glob(f"{prefix}*.png"):
            os.remove(f)
            
        if qr_disco and qr_disco in pc_qr_map:
            ruta_pdf_pc = pc_qr_map[qr_disco]
            coincidencias += 1
            
            hash_pc = calcular_hash_sha256(ruta_pdf_pc)
            hash_disco = calcular_hash_sha256(ruta_pdf_disco)
            
            size_pc = os.path.getsize(ruta_pdf_pc)
            size_disco = os.path.getsize(ruta_pdf_disco)
            
            print(f"\n[+] MATCH QR: {qr_disco[:20]}...")
            print(f"    Disco (Delegados 21 Jun): {file} -> Hash: {hash_disco[:8]}, Size: {size_disco}")
            print(f"    PC (Descarga Drive)     : {os.path.basename(ruta_pdf_pc)} -> Hash: {hash_pc[:8]}, Size: {size_pc}")
            
            if hash_pc != hash_disco:
                alterados += 1
                print("    >> ! LOS HASHES SON DIFERENTES A PESAR DE SER LA MISMA ACTA !")
            else:
                print("    >> MATCH EXACTO DE HASH (Sin alteracion)")
                
            if coincidencias >= len(pc_qr_map):
                break

    print(f"\nResumen: {coincidencias} coincidencias encontradas. {alterados} alterados.")

if __name__ == '__main__':
    principal()
