#!/usr/bin/env python3
import os
import sys
import subprocess
import csv
import re
from pathlib import Path

def analyze_department(dept_name, base_path="/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"):
    dept_path = os.path.join(base_path, dept_name)
    if not os.path.exists(dept_path):
        print(f"[!] Error: El departamento '{dept_name}' no existe en {base_path}")
        sys.exit(1)

    print(f"[*] Iniciando cacería de firmas XREF corruptas en Claveros: {dept_name}")
    
    corrupted_files = []
    total_scanned = 0

    # Escaneo recursivo
    for root, dirs, files in os.walk(dept_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                total_scanned += 1
                
                # Extraer número de mesa del nombre de archivo (e.g. Mesa_1.pdf o Mesa 1)
                mesa_match = re.search(r'Mesa_(\d+)', file, re.IGNORECASE)
                mesa_num = mesa_match.group(1) if mesa_match else "DESCONOCIDA"
                
                # Correr qpdf --check para buscar la firma del inyector (XREF corrupta)
                # Usamos --check que es rápido para verificar integridad
                cmd = ["qpdf", "--check", pdf_path]
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                # La firma criptográfica del inyector que descubrimos en Delegados:
                if "reported number of objects" in result.stderr or "WARNING" in result.stderr:
                    corrupted_files.append({
                        "archivo": file,
                        "ruta": pdf_path,
                        "mesa": mesa_num
                    })
                    print(f"  [🚨 DEEPFAKE DETECTADO] Mesa {mesa_num} | Archivo: {file}")

    print("\n" + "="*50)
    print(f"RESUMEN DEPARTAMENTO {dept_name}")
    print(f"Total PDFs escaneados: {total_scanned}")
    print(f"Total clones corruptos encontrados: {len(corrupted_files)}")
    
    if corrupted_files:
        print("\nPatrón de Mesas Corruptas en Claveros:")
        # Agrupar por mesa para comparar con la matriz
        mesa_counts = {}
        for f in corrupted_files:
            m = f['mesa']
            mesa_counts[m] = mesa_counts.get(m, 0) + 1
            
        # Ordenar numéricamente si es posible
        def sort_key(k):
            try:
                return int(k)
            except:
                return float('inf')
                
        sorted_mesas = sorted(mesa_counts.keys(), key=sort_key)
        secuencia = ", ".join([f"{m} (x{mesa_counts[m]})" for m in sorted_mesas])
        print(secuencia)
        
        # Guardar a CSV
        out_csv = f"/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_03_Peritajes_Forenses/CLAVEROS_CORRUPTOS_{dept_name}.csv"
        with open(out_csv, 'w', encoding='utf-8') as f_out:
            writer = csv.DictWriter(f_out, fieldnames=["mesa", "archivo", "ruta"])
            writer.writeheader()
            for row in corrupted_files:
                writer.writerow(row)
        print(f"\n✅ Reporte guardado en {out_csv}")
    else:
        print("✅ No se detectaron firmas corruptas en este departamento.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analizar_claveros_masivo.py <NOMBRE_DEPARTAMENTO>")
        print("Ejemplo: python3 analizar_claveros_masivo.py ANTIOQUIA")
        sys.exit(1)
    
    analyze_department(sys.argv[1])
