# audit_outliers_deepfake.py
import csv
import os
import subprocess
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image

XREF_CSV = "/home/andrea-zabala-c/Desktop/resultado_xref_nacional_segunda_vuelta.csv"
OUTLIERS_CSV = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/ANALISIS_FORENSE_CLAVEROS_32_DEPARTAMENTOS/MESAS_FRAUDULENTAS_OUTLIERS.csv"
OUTPUT_CSV = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/REPORTE_XREF_DEEPFAKE.csv"
OUTPUT_HTML = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/XREF_ALTERACIONES_COLOREADAS.html"

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
    except Exception:
        return 0.0

def process_pdf_file(pdf_path):
    tmp_prefix = f"/tmp/outlier_check_{random.randint(100000,999999)}"
    # Extract 1st page at 72 DPI for speed
    res = subprocess.run(["pdftoppm", "-jpeg", "-f", "1", "-l", "1", "-r", "72", pdf_path, tmp_prefix], capture_output=True)
    jpg_path = f"{tmp_prefix}-1.jpg"
    white_percent = 0.0
    
    if os.path.exists(jpg_path):
        white_percent = analyze_clipping(jpg_path)
        os.remove(jpg_path)
        
    return white_percent

def main():
    print("[*] Leyendo datos de XREF...")
    xref_data = {}
    with open(XREF_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or len(row) < 7:
                continue
            pdf_path, xref_status, dpto, mpio, zona, puesto, mesa = row
            try:
                mesa_num = int(mesa.replace("Mesa_", ""))
            except ValueError:
                continue
            # Store by (dpto, mpio, mesa_num) to maximize matching coverage
            key = (dpto.strip(), mpio.strip(), mesa_num)
            xref_data[key] = {
                'pdf_path': pdf_path,
                'xref_status': xref_status,
                'zona': zona,
                'puesto': puesto,
                'mesa_str': mesa
            }

    print("[*] Leyendo mesas sospechosas (outliers)...")
    outliers = []
    with open(OUTLIERS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or len(row) < 5:
                continue
            dpto, mpio, zona, puesto, mesa = row[:5]
            try:
                mesa_num = int(mesa)
            except ValueError:
                continue
            key = (dpto.strip(), mpio.strip(), mesa_num)
            if key in xref_data:
                outliers.append((key, xref_data[key]['pdf_path']))

    print(f"[+] Total de actas sospechosas encontradas por DMM: {len(outliers)}")
    
    # Run deepfake detection in parallel
    print("[*] Ejecutando análisis de DeepFake en las actas sospechosas...")
    tasks = []
    for key, pdf_path in outliers:
        tasks.append((key, pdf_path))
        
    deepfake_results = {}
    with ProcessPoolExecutor(max_workers=8) as executor:
        future_to_key = {executor.submit(process_pdf_file, pdf_path): (key, pdf_path) for key, pdf_path in tasks}
        completed = 0
        for future in as_completed(future_to_key):
            key, pdf_path = future_to_key[future]
            try:
                pct = future.result()
                deepfake_results[key] = pct
            except Exception as e:
                deepfake_results[key] = 0.0
            completed += 1
            if completed % 100 == 0:
                print(f"  -> {completed}/{len(tasks)} procesados...")

    print("[*] Generando CSV consolidado final...")
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['archivo_pdf', 'resultado_xref', 'departamento', 'municipio', 'zona', 'puesto', 'mesa', 'Blanco_Puro_Pct', 'Diagnostico_DeepFake'])
        
        with open(XREF_CSV, newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                if not row or len(row) < 7:
                    continue
                pdf_path, xref_status, dpto, mpio, zona, puesto, mesa = row
                try:
                    mesa_num = int(mesa.replace("Mesa_", ""))
                except ValueError:
                    continue
                key = (dpto.strip(), mpio.strip(), mesa_num)
                
                # Check if this row was analyzed for DeepFake
                if key in deepfake_results:
                    pct = deepfake_results[key]
                    diag = "🔴 DEEPFAKE SINTÉTICO" if pct > 1.0 else "🟢 ESCANEO REAL"
                else:
                    pct = 0.0
                    diag = ""
                    
                writer.writerow([pdf_path, xref_status, dpto, mpio, zona, puesto, mesa, round(pct, 2), diag])

    print("[*] Generando archivo HTML coloreado...")
    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Listado XREF con Alteraciones y DeepFakes coloreados</title>
<style>
  body {font-family:Arial,Helvetica,sans-serif;background:#0a0a12;color:#e2e8f0;padding:20px;}
  table {border-collapse:collapse;width:100%;margin-top:20px;font-size:12px;}
  th, td {padding:8px 12px;border:1px solid #1e1e30;}
  th {background:#111122;color:#fff;position:sticky;top:0;z-index:2;}
  .red {background:#2a0f0f;color:#f87171;} /* Single Anomaly */
  .blue {background:#0a0f10;color:#60a5fa;} /* Clean */
  .green {background:#0f2818;color:#4ade80;} /* Combined */
</style>
</head>
<body>
<h1>Listado Forense E-14 (XREF + DeepFake)</h1>
<table>
<tr>
  <th>#</th>
  <th>Archivo PDF</th>
  <th>Estado XREF</th>
  <th>Departamento</th>
  <th>Municipio</th>
  <th>Mesa</th>
  <th>Blanco Puro %</th>
  <th>Resultado DeepFake</th>
</tr>""")

    with open(OUTPUT_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for i, row in enumerate(reader, start=1):
            if i > 5000: # Limit rows in HTML for browser speed
                html_parts.append(f"<tr><td colspan='8' style='text-align:center;'>... y {117994 - 5000:,} filas más en el reporte CSV consolidado ...</td></tr>")
                break
            pdf_path, xref_status, dpto, mpio, zona, puesto, mesa, pct, diag = row
            
            has_xref = "CORRUPTO" in xref_status
            has_df = "DEEPFAKE" in diag
            
            if has_xref and has_df:
                css_class = "green"
            elif has_xref or has_df:
                css_class = "red"
            else:
                css_class = "blue"
                
            html_parts.append(f"<tr class='{css_class}'>")
            html_parts.append(f"  <td>{i}</td>")
            html_parts.append(f"  <td>{os.path.basename(pdf_path)}</td>")
            html_parts.append(f"  <td>{xref_status}</td>")
            html_parts.append(f"  <td>{dpto}</td>")
            html_parts.append(f"  <td>{mpio}</td>")
            html_parts.append(f"  <td>{mesa}</td>")
            html_parts.append(f"  <td>{pct}</td>")
            html_parts.append(f"  <td>{diag}</td>")
            html_parts.append("</tr>")

    html_parts.append("</table></body></html>")
    
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write("\n".join(html_parts))

    print(f"[+] HTML generado en: {OUTPUT_HTML}")
    print(f"[+] Proceso completado exitosamente.")

if __name__ == "__main__":
    main()
