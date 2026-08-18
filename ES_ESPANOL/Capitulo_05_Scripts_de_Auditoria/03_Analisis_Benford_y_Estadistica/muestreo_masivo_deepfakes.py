import os
import random
import subprocess
import csv
from concurrent.futures import ProcessPoolExecutor, as_completed
try:
    from PIL import Image
except ImportError:
    print("PIL no está instalado.")
    exit(1)

def analyze_clipping(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        pixels = img.load()
        width, height = img.size
        
        pure_white_count = 0
        total_pixels = width * height
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if r == 255 and g == 255 and b == 255:
                    pure_white_count += 1
                    
        return (pure_white_count / total_pixels) * 100
    except Exception as e:
        return 0.0

def process_pdf(task_data):
    pdf_path = task_data['pdf_path']
    dept_name = task_data['dept_name']
    filename = os.path.basename(pdf_path)
    
    # Extraer metadatos de la nomenclatura
    # Ej: E14_PRE_60_001_002_00_03_005_6948_Mesa_5.pdf
    dept_code = "N/A"
    mun_code = "N/A"
    mesa = "N/A"
    
    try:
        if "_Mesa_" in filename:
            parts = filename.split("_Mesa_")
            mesa = parts[1].replace(".pdf", "")
            
            prefix_parts = parts[0].split("_")
            if len(prefix_parts) >= 4:
                dept_code = prefix_parts[2]
                mun_code = prefix_parts[3]
    except Exception:
        pass

    # Archivo temporal único
    tmp_prefix = f"/tmp/mass_sample_{random.randint(100000,999999)}"
    
    # Extraer 1era página a baja resolución para rapidez (72 DPI)
    subprocess.run(["pdftoppm", "-jpeg", "-f", "1", "-l", "1", "-r", "72", pdf_path, tmp_prefix], capture_output=True)
    
    jpg_path = f"{tmp_prefix}-1.jpg"
    white_percent = 0.0
    status = "ERROR"
    
    if os.path.exists(jpg_path):
        white_percent = analyze_clipping(jpg_path)
        status = "🔴 DEEPFAKE SINTÉTICO" if white_percent > 1.0 else "🟢 ESCANEO REAL"
        os.remove(jpg_path)
    
    return {
        'Departamento': dept_name,
        'Cod_Dep': dept_code,
        'Cod_Mun': mun_code,
        'Mesa': mesa,
        'Archivo': filename,
        'Blanco_Puro_Pct': round(white_percent, 2),
        'Diagnostico': status
    }

def main():
    base_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
    
    if not os.path.exists(base_dir):
        print(f"Error: No se encontró el directorio {base_dir}")
        return
        
    departments = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    tasks = []
    print(f"[*] Escaneando directorios para seleccionar la muestra...")
    
    for dept in sorted(departments):
        dept_path = os.path.join(base_dir, dept)
        
        all_pdfs = []
        for root, _, files in os.walk(dept_path):
            for f in files:
                if f.lower().endswith('.pdf'):
                    all_pdfs.append(os.path.join(root, f))
                    
        if not all_pdfs:
            continue
            
        sample_size = min(100, len(all_pdfs))
        selected = random.sample(all_pdfs, sample_size)
        
        for pdf in selected:
            tasks.append({'pdf_path': pdf, 'dept_name': dept})
            
    print(f"[+] Total de archivos a analizar: {len(tasks)}. Iniciando procesamiento en paralelo...")
    
    results = []
    deepfakes_count = 0
    
    # Procesar en paralelo para reducir el tiempo drásticamente
    with ProcessPoolExecutor(max_workers=8) as executor:
        future_to_pdf = {executor.submit(process_pdf, task): task for task in tasks}
        
        completed = 0
        for future in as_completed(future_to_pdf):
            try:
                res = future.result()
                results.append(res)
                if res['Blanco_Puro_Pct'] > 1.0:
                    deepfakes_count += 1
                    
                completed += 1
                if completed % 100 == 0:
                    print(f"  -> Progreso: {completed}/{len(tasks)} procesados...")
            except Exception as exc:
                print(f"Error en un worker: {exc}")

    # Guardar en CSV
    csv_path = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/REPORTE_MASIVO_DEEPFAKES.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Departamento', 'Cod_Dep', 'Cod_Mun', 'Mesa', 'Archivo', 'Blanco_Puro_Pct', 'Diagnostico'])
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print(f"\n[+] Análisis finalizado. Total analizados: {len(results)}. Deepfakes: {deepfakes_count}")
    print(f"[+] Base de datos exportada a: {csv_path}")

if __name__ == "__main__":
    main()
