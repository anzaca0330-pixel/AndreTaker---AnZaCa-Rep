#!/usr/bin/env python3
# =========================================================
# babayaga_core.py — AndreTaker / BabaYaga Core Engine
# =========================================================
# Uso: python3 babayaga_core.py --ruta /ruta/al/archivo.pdf
# =========================================================

import os
import sys
import argparse
import subprocess
import json
from datetime import datetime

print("⚡ BabaYaga despierta... [Fuerza e Integridad Forense]")
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
        return {'metadatos': resultado.stdout.strip() if resultado.stdout else 'Sin metadatos (Purga de huella)'}
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
                os.remove(archivo)
        return {'imagenes': imagenes}
    except Exception as e:
        return {'error': str(e)}

def generar_informe(resultados, pdf_path):
    """Escribe el veredicto con la fuerza imparable de la verdad."""
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
*Informe generado por BabaYaga Core v1.0 — AndreTaker AnZaCa (Pura verdad y fuerza imparable).*
"""
    with open('informe_babayaga.md', 'w') as f:
        f.write(informe)
    print("✅ El veredicto de la verdad está listo: informe_babayaga.md")

def main():
    parser = argparse.ArgumentParser(description='BabaYaga Core — Análisis forense de PDFs')
    parser.add_argument('--ruta', required=True, help='Ruta al archivo PDF o carpeta')
    args = parser.parse_args()

    print("🧙‍♀️ BabaYaga Core — El bosque se abre...")
    
    # Verificar herramientas
    faltan = verificar_herramientas()
    if faltan:
        print(f"⚠️ Faltan herramientas: {', '.join(faltan)}")
        print("Instala con: sudo apt install qpdf exiftool poppler-utils imagemagick zbar-tools")
        sys.exit(1)

    pdf_path = args.ruta
    if not os.path.exists(pdf_path):
        print(f"❌ El archivo no está en el bosque: {pdf_path}")
        sys.exit(1)

    resultados = {
        'estructura': analizar_estructura(pdf_path),
        'metadatos': analizar_metadatos(pdf_path),
        'imagenes': analizar_imagenes(pdf_path)
    }

    generar_informe(resultados, pdf_path)

if __name__ == "__main__":
    main()
