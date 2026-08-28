#!/usr/bin/env python3
# =========================================================
# babayaga_core.py — AndreTaker / BabaYaga Core Engine v1.1
# =========================================================
# Soporta análisis de un solo archivo PDF o procesamiento en LOTE (Batch)
# Uso: 
#   python3 babayaga_core.py --ruta /ruta/al/archivo.pdf
#   python3 babayaga_core.py --ruta /ruta/a/la/carpeta/
# =========================================================

import os
import sys
import glob
import csv
import argparse
import subprocess
import json
from datetime import datetime

print("⚡ BabaYaga despierta... [Fuerza e Integridad Forense - Modo Lote / Batch]")
print("🔥 La verdad binaria se abre paso sin filtro. Los archivos son interrogados.")

def verificar_herramientas():
    """Comprueba que el sistema tenga las herramientas necesarias."""
    herramientas = ['qpdf', 'exiftool', 'pdfimages', 'identify', 'zbarimg']
    faltan = []
    for h in herramientas:
        if subprocess.run(['which', h], capture_output=True).returncode != 0:
            faltan.append(h)
    return faltan

def analizar_estructura(pdf_path):
    """Busca la cicatriz estructural (XREF)."""
    try:
        resultado = subprocess.run(
            ['qpdf', '--check', pdf_path],
            capture_output=True,
            text=True
        )
        if 'reported number of objects' in resultado.stderr:
            return {'XREF_corrupta': True, 'detalle': resultado.stderr.strip()}
        else:
            return {'XREF_corrupta': False, 'detalle': 'El archivo mantiene su estructura íntegra'}
    except Exception as e:
        return {'error': str(e)}

def analizar_metadatos(pdf_path):
    """Inspecciona las marcas de tiempo y autoría."""
    try:
        resultado = subprocess.run(
            ['exiftool', '-Creator', '-Producer', '-CreateDate', pdf_path],
            capture_output=True,
            text=True
        )
        meta = resultado.stdout.strip() if resultado.stdout else 'Sin metadatos (Purga de huella)'
        tiene_creator = 'Creator' in meta
        return {'metadatos': meta, 'tiene_autoría': tiene_creator}
    except Exception as e:
        return {'error': str(e)}

def analizar_imagenes(pdf_path):
    """Extrae las imágenes y analiza su espacio de color."""
    try:
        base = pdf_path.replace('.pdf', '_img')
        subprocess.run(['pdfimages', '-png', pdf_path, base], capture_output=True)
        imagenes = []
        for archivo in os.listdir('.'):
            if archivo.startswith(os.path.basename(base)) and archivo.endswith('.png'):
                resultado = subprocess.run(
                    ['identify', '-format', '%[colorspace], media: %[mean]', archivo],
                    capture_output=True,
                    text=True
                )
                imagenes.append({archivo: resultado.stdout.strip()})
                try:
                    os.remove(archivo)
                except Exception:
                    pass
        return {'imagenes': imagenes}
    except Exception as e:
        return {'error': str(e)}

def generar_informe_individual(resultados, pdf_path):
    """Escribe el veredicto individual."""
    informe = f"""# 📜 INFORME BABAYAGA — VEREDICTO DE PURA VERDAD

**Archivo analizado:** {pdf_path}  
**Fecha del peritaje:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## ⚡ LO QUE EL ANÁLISIS FORENSE REVELÓ

### Estructura (XREF)
- **Corrupta:** {resultados.get('estructura', {}).get('XREF_corrupta', 'N/A')}
- **Detalle:** {resultados.get('estructura', {}).get('detalle', 'N/A')}

### Metadatos
{resultados.get('metadatos', {}).get('metadatos', 'Sin huella de origen')}

### Imágenes
- **Cantidad extraída:** {len(resultados.get('imagenes', {}).get('imagenes', []))}
- **Detalle:** {resultados.get('imagenes', {}).get('imagenes', [])}

---

## 🧠 EL VEREDICTO

{ '⚠️ CICATRIZ ESTRUCTURAL DETECTADA: Este archivo fue alterado sintéticamente. BabaYaga rompe el camuflaje.' if resultados.get('estructura', {}).get('XREF_corrupta') else '✅ Estructura sin anomalías directas. La auditoría continúa.' }

---
*Informe generado por BabaYaga Core v1.1 — AndreTaker AnZaCa (Pura verdad y fuerza imparable).*
"""
    with open('informe_babayaga.md', 'w', encoding='utf-8') as f:
        f.write(informe)
    print("✅ El veredicto de la verdad está listo: informe_babayaga.md")

def procesar_lote(carpeta_path):
    """Procesa un lote de archivos PDF en una carpeta y genera matriz CSV e informe consolidado."""
    print(f"📦 Escaneando lote en carpeta: {carpeta_path}...")
    archivos_pdf = []
    for root, _, files in os.walk(carpeta_path):
        for f in files:
            if f.lower().endswith('.pdf'):
                archivos_pdf.append(os.path.join(root, f))
    
    archivos_pdf.sort()
    total = len(archivos_pdf)
    print(f"📊 Total de archivos PDF encontrados: {total}\n")
    
    if total == 0:
        print("⚠️ No se encontraron archivos PDF en la carpeta especificada.")
        return

    csv_path = 'matriz_lote_babayaga.csv'
    informe_lote_path = 'informe_lote_babayaga.md'
    
    corruptos = 0
    limpios = 0
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nombre_Archivo', 'Ruta_Absoluta', 'XREF_Corrupta', 'Detalle_XREF', 'Tiene_Metadatos', 'Cant_Imagenes'])
        
        for idx, pdf in enumerate(archivos_pdf, 1):
            nom = os.path.basename(pdf)
            print(f"[{idx}/{total}] Procesando: {nom}...")
            est = analizar_estructura(pdf)
            meta = analizar_metadatos(pdf)
            img = analizar_imagenes(pdf)
            
            is_corrupt = est.get('XREF_corrupta', False)
            if is_corrupt:
                corruptos += 1
            else:
                limpios += 1
                
            det_est = est.get('detalle', '').replace('\n', ' ')
            has_meta = meta.get('tiene_autoría', False)
            cant_img = len(img.get('imagenes', []))
            
            writer.writerow([nom, pdf, is_corrupt, det_est, has_meta, cant_img])

    porcentaje_corrupcion = (corruptos / total) * 100.0 if total > 0 else 0.0

    md_lote = f"""# 📜 INFORME DE LOTE BABAYAGA — VEREDICTO DE MASA

**Carpeta analizada:** `{carpeta_path}`  
**Fecha del ritual de masa:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total de archivos evaluados:** {total}

---

## 📊 LO QUE EL ESCANEO DE MASA REVELÓ

| Métrica | Valor | Porcentaje |
| :--- | :--- | :--- |
| **Total Archivos Evaluados** | {total} | 100.0% |
| **⚠️ Archivos con Cicatriz XREF (Corruptos)** | {corruptos} | **{porcentaje_corrupcion:.2f}%** |
| **✅ Archivos con Estructura Normal** | {limpios} | **{100.0 - porcentaje_corrupcion:.2f}%** |

---

## 🧠 EL VEREDICTO DE LOTE

{f'⚠️ ALERTA DE ALTERACIÓN MASIVA: Se confirmó la cicatriz XREF en {corruptos} de {total} archivos ({porcentaje_corrupcion:.2f}%). BabaYaga expone la anomalía sistémica.' if corruptos > 0 else '✅ No se detectó la cicatriz XREF en el lote evaluado.'}

---

### 📂 Archivos generados:
- **Matriz CSV Completa:** `matriz_lote_babayaga.csv`
- **Informe Consolidado:** `informe_lote_babayaga.md`

---
*Informe generado por BabaYaga Core v1.1 — AndreTaker AnZaCa (Pura verdad y fuerza imparable).*
"""

    with open(informe_lote_path, 'w', encoding='utf-8') as f:
        f.write(md_lote)
        
    print(f"\n✅ Proceso de Lote Finalizado con Éxito!")
    print(f"   ├─ Corruptos (Cicatriz XREF): {corruptos} ({porcentaje_corrupcion:.2f}%)")
    print(f"   ├─ Matriz CSV: {csv_path}")
    print(f"   └─ Informe Markdown: {informe_lote_path}")

def main():
    parser = argparse.ArgumentParser(description='BabaYaga Core — Análisis forense de PDFs (Individual y Lote)')
    parser.add_argument('--ruta', required=True, help='Ruta al archivo PDF o carpeta')
    args = parser.parse_args()

    # Verificar herramientas
    faltan = verificar_herramientas()
    if faltan:
        print(f"⚠️ Faltan herramientas: {', '.join(faltan)}")
        print("Instala con: sudo apt install qpdf exiftool poppler-utils imagemagick zbar-tools")
        sys.exit(1)

    ruta = args.ruta
    if not os.path.exists(ruta):
        print(f"❌ La ruta especificada no existe en el sistema: {ruta}")
        sys.exit(1)

    if os.path.isdir(ruta):
        procesar_lote(ruta)
    else:
        resultados = {
            'estructura': analizar_estructura(ruta),
            'metadatos': analizar_metadatos(ruta),
            'imagenes': analizar_imagenes(ruta)
        }
        generar_informe_individual(resultados, ruta)

if __name__ == "__main__":
    main()
