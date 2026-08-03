#!/usr/bin/env python3
import subprocess
import sys
import re
import os

def check_qpdf_errors(pdf_path):
    print(f"\n[*] Ejecutando análisis estructural (qpdf --check)...")
    result = subprocess.run(['qpdf', '--check', pdf_path], capture_output=True, text=True)
    if result.returncode != 0 or "reported number of objects" in result.stderr:
        print("    [!] ALERTA: Corrupción en la tabla XREF detectada (Cicatriz Estructural).")
        return True
    else:
        print("    [+] Estructura XREF intacta.")
        return False

def get_image_metadata(pdf_path):
    print(f"\n[*] Extrayendo metadatos de imágenes incrustadas (pdfimages)...")
    result = subprocess.run(['pdfimages', '-list', pdf_path], capture_output=True, text=True)
    
    pages = {}
    lines = result.stdout.split('\n')
    
    for line in lines:
        parts = line.split()
        if len(parts) > 10 and parts[0].isdigit():
            page_num = int(parts[0])
            if page_num not in pages:
                # Nos quedamos con la imagen principal de cada página
                pages[page_num] = {
                    'width': parts[3],
                    'height': parts[4],
                    'color': parts[5],
                    'enc': parts[8],
                    'ppi_x': parts[12],
                    'ppi_y': parts[13]
                }
    return pages

def compare_pages(pages):
    print("\n[*] Comparando Página 1 (Votos) vs Página 2 (Firmas)...")
    if 1 not in pages or 2 not in pages:
        print("    [!] No se encontraron imágenes válidas en ambas páginas.")
        return

    p1 = pages[1]
    p2 = pages[2]
    
    print(f"    Página 1 -> Resolución: {p1['ppi_x']}x{p1['ppi_y']} ppi | Color: {p1['color']} | Codificación: {p1['enc']}")
    print(f"    Página 2 -> Resolución: {p2['ppi_x']}x{p2['ppi_y']} ppi | Color: {p2['color']} | Codificación: {p2['enc']}")
    
    anomalies = []
    if p1['color'] != p2['color']:
        anomalies.append(f"Discrepancia en el espacio de color ({p1['color']} vs {p2['color']}).")
    if p1['ppi_x'] != p2['ppi_x'] or p1['ppi_y'] != p2['ppi_y']:
        anomalies.append(f"Discrepancia en la resolución (DPI/PPI).")
    if p1['enc'] != p2['enc']:
        anomalies.append(f"Diferencia en el formato de compresión interna.")
        
    if anomalies:
        print("    [!] ALERTA: Las páginas no coinciden. Es físicamente IMPOSIBLE que un mismo escáner")
        print("                produzca dos páginas del mismo documento con diferentes propiedades.")
        for a in anomalies:
            print(f"        - {a}")
        print("    [!] Conclusión: La Página 1 fue reemplazada o superpuesta artificialmente.")
    else:
        print("    [+] Las propiedades físicas de ambas páginas coinciden perfectamente.")

def check_devicegray(pdf_path):
    print(f"\n[*] Buscando inyecciones vectoriales (Plantilla B - DeviceGray)...")
    temp_qdf = "/tmp/temp_analysis.qdf"
    subprocess.run(['qpdf', '--qdf', pdf_path, temp_qdf], capture_output=True)
    
    with open(temp_qdf, 'r', encoding='latin-1') as f:
        content = f.read()
        
    if "DeviceGray" in content:
        print("    [!] ALERTA: Capa vectorial intrusa 'DeviceGray' encontrada en el código fuente.")
        return True
    else:
        print("    [+] No se detectaron vectores intrusos.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analisis_comparativo_paginas.py <ruta_al_pdf>")
        sys.exit(1)
        
    target_pdf = sys.argv[1]
    if not os.path.exists(target_pdf):
        print(f"Error: No se encuentra el archivo {target_pdf}")
        sys.exit(1)
        
    print(f"=== ANÁLISIS FORENSE COMPARATIVO INTRA-DOCUMENTO ===")
    print(f"Archivo: {target_pdf}")
    
    check_qpdf_errors(target_pdf)
    pages_meta = get_image_metadata(target_pdf)
    compare_pages(pages_meta)
    check_devicegray(target_pdf)
    
    print("\n=====================================================")
    print("Análisis finalizado.")
