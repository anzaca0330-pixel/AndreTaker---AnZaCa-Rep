import os
import subprocess
import glob

def analizar_pdf(pdf_path):
    print(f"Analizando: {os.path.basename(pdf_path)}")
    try:
        # Extraer lista de imágenes usando pdfimages -list
        result = subprocess.run(['pdfimages', '-list', pdf_path], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        
        if len(lines) < 3:
            return 0, 0
            
        # Parsear las líneas para agrupar imágenes por página
        paginas = {}
        for line in lines[2:]:
            parts = line.split()
            if len(parts) >= 1:
                try:
                    page_num = int(parts[0])
                    paginas[page_num] = paginas.get(page_num, 0) + 1
                except ValueError:
                    continue
        
        # Detectar inyección: si alguna página individual tiene > 1 imagen
        inyecciones = sum(1 for p, num_imgs in paginas.items() if num_imgs > 1)
        total_paginas = len(paginas)
        return inyecciones, total_paginas
        
    except FileNotFoundError:
        print("ERROR: Comando 'pdfimages' no encontrado. Instala poppler-utils.")
        return -1, -1
    except subprocess.CalledProcessError as e:
        print(f"Error procesando {pdf_path}: {e}")
        return -1, -1

def procesar_carpeta(carpeta, tipo):
    print(f"\n--- INICIANDO ANÁLISIS DE {tipo.upper()} ---")
    archivos = glob.glob(os.path.join(carpeta, "*.pdf"))
    if not archivos:
        print(f"No se encontraron PDFs en la carpeta {carpeta}")
        return
        
    for pdf in archivos:
        inyecciones, _ = analizar_pdf(pdf)
        if inyecciones > 0:
            print(f"🚨 FRAUDE DIGITAL DETECTADO (Multicapa/Inyección) en {os.path.basename(pdf)}")
        elif inyecciones == 0:
            print(f"✅ LIMPIO ESTRUCTURALMENTE (1 capa plana) en {os.path.basename(pdf)}")

if __name__ == "__main__":
    base_dir = "/home/andrea-zabala-c/Desktop/MUESTRA_LINEA_FRAUDE"
    dir_delegados = os.path.join(base_dir, "DELEGADOS")
    dir_claveros = os.path.join(base_dir, "CLAVEROS")
    
    procesar_carpeta(dir_delegados, "DELEGADOS (Transmisión / Preconteo)")
    procesar_carpeta(dir_claveros, "CLAVEROS (Escrutinio Oficial)")
