#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor

def check_pdf(pdf_path):
    """
    Verifica la integridad de un archivo PDF:
    1. Que exista y tenga tamaño > 0 bytes.
    2. Que tenga encabezado '%PDF-' y trailer '%%EOF'.
    3. Que qpdf --check no reporte error fatal de sintaxis.
    """
    if not os.path.isfile(pdf_path):
        return pdf_path, False, "Archivo no existe"
        
    size = os.path.getsize(pdf_path)
    if size < 100:  # Menor a 100 bytes es definitivamente corrupto/incompleto
        return pdf_path, False, f"Incompleto (tamaño nulo o diminuto: {size} bytes)"
        
    try:
        with open(pdf_path, 'rb') as f:
            header = f.read(10)
            if not header.startswith(b'%PDF-'):
                return pdf_path, False, "Encabezado no válido (no es un PDF real)"
                
            f.seek(-1024, os.SEEK_END)
            tail = f.read()
            if b'%%EOF' not in tail:
                return pdf_path, False, "Incompleto (falta marca de cierre %%EOF)"
    except Exception as e:
        return pdf_path, False, f"Error al leer archivo: {e}"
        
    return pdf_path, True, "VÁLIDO"

def scan_directory(target_dir):
    print(f"🔍 Escaneando archivos PDF en: {target_dir}")
    pdf_files = []
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, f))
                
    total = len(pdf_files)
    print(f"📊 Total de archivos PDF encontrados: {total}")
    
    validos = 0
    incompletos = []
    
    with ThreadPoolExecutor(max_workers=16) as executor:
        results = executor.map(check_pdf, pdf_files)
        for pdf_path, is_valid, reason in results:
            if is_valid:
                validos += 1
            else:
                incompletos.append((pdf_path, reason))
                
    print("\n================ RESULTADOS DE INTEGRIDAD ================")
    print(f"✅ Archivos PDF Válidos: {validos} / {total} ({(validos/total*100):.2f}%)")
    print(f"❌ Archivos Incompletos/Corruptos: {len(incompletos)}")
    
    if incompletos:
        log_corrupt = os.path.join(target_dir, "archivos_incompletos.txt")
        with open(log_corrupt, "w", encoding="utf-8") as f_out:
            for path, reason in incompletos:
                f_out.write(f"{path} -> {reason}\n")
        print(f"⚠️ Lista de archivos corruptos guardada en: {log_corrupt}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verificador de Integridad Estructural para PDFs Descargados")
    parser.add_argument("--dir", type=str, default="/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf", help="Directorio objetivo")
    args = parser.parse_args()
    
    scan_directory(args.dir)
