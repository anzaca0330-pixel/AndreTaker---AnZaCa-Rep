#!/usr/bin/env python3
# =========================================================
# demo_babayaga.py — El ritual de apertura
# =========================================================
# Uso: python3 demo_babayaga.py --ruta /ruta/al/archivo.pdf
# =========================================================

import os
import sys
import argparse
import subprocess
import json
from datetime import datetime

# La invocación
print("🧙‍♀️ BabaYaga despierta...")
print("🌲 El bosque se abre. Los archivos esperan.")

def verificar_herramientas():
    """Comprueba que el bosque tenga las herramientas necesarias."""
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
            return {'XREF_corrupta': False, 'detalle': 'El archivo respira normal'}
    except Exception as e:
        return {'error': str(e)}

def analizar_metadatos(pdf_path):
    """Escucha lo que el archivo dice de sí mismo."""
    try:
        resultado = subprocess.run(
            ['exiftool', '-Creator', '-Producer', '-CreateDate', pdf_path],
            capture_output=True,
            text=True
        )
        return {'metadatos': resultado.stdout.strip() if resultado.stdout else 'Silencio. No hay huella.'}
    except Exception as e:
        return {'error': str(e)}

def analizar_imagenes(pdf_path):
    """Extrae las imágenes y las interroga."""
    try:
        base = pdf_path.replace('.pdf', '_img')
        subprocess.run(['pdfimages', '-png', pdf_path, base], capture_output=True)
        imagenes = []
        for archivo in os.listdir('.'):
            if archivo.startswith(os.path.basename(base)) and archivo.endswith('.png'):
                resultado = subprocess.run(
                    ['identify', '-format', '%[colorspace] %[mean]', archivo],
                    capture_output=True,
                    text=True
                )
                imagenes.append({archivo: resultado.stdout.strip()})
                os.remove(archivo)
        return {'imagenes': imagenes}
    except Exception as e:
        return {'error': str(e)}

def generar_informe(resultados, pdf_path):
    """Escribe el veredicto en la lengua de los humanos."""
    informe = f"""# 📜 INFORME BABAYAGA — El veredicto del bosque

**Archivo analizado:** {pdf_path}  
**Fecha del ritual:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 🔍 Lo que la noche reveló

### Estructura (XREF)
- **Corrupta:** {resultados.get('estructura', {}).get('XREF_corrupta', 'N/A')}
- **Detalle:** {resultados.get('estructura', {}).get('detalle', 'N/A')}

### Metadatos
{resultados.get('metadatos', {}).get('metadatos', 'No hay voz en el archivo')}

### Imágenes
- **Cantidad extraída:** {len(resultados.get('imagenes', {}).get('imagenes', []))}
- **Detalle:** {resultados.get('imagenes', {}).get('imagenes', [])}

---

## 🧠 El veredicto

{ '⚠️ Hay una cicatriz en este archivo. Algo fue alterado.' if resultados.get('estructura', {}).get('XREF_corrupta') else '✅ El archivo parece limpio. Pero BabaYaga nunca confía del todo.' }

---
*Informe generado por BabaYaga Core v1.0 — porque la verdad también tiene derecho a ser poética.*
"""
    with open('informe_babayaga.md', 'w') as f:
        f.write(informe)
    print("✅ El veredicto está listo: informe_babayaga.md")

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
