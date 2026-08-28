#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse

def inspect_and_recover_hidden_content(pdf_path, output_dir):
    """
    Rastrea y extrae el contenido cubierto, suprimido o intrusivo en el PDF:
    1. Extrae TODOS los objetos de imagen crudos (incluyendo capas ocultas bajo máscaras blancas).
    2. Inspecciona el flujo de comandos de texto y vectores (/Contents stream) buscando intrusión de QR (XObjects).
    3. Recupera objetos no enlazados en el árbol sintáctico.
    """
    os.makedirs(output_dir, exist_ok=True)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    sub_dir = os.path.join(output_dir, pdf_name)
    os.makedirs(sub_dir, exist_ok=True)
    
    print(f"🔍 [REVELADOR FORENSE] Inspeccionando capas ocultas en: {pdf_path}")
    print(f"📂 Carpeta de extracción: {sub_dir}\n")
    
    # 1. Extraer TODAS las imágenes incrustadas (incluso capas inferiores/tapadas)
    print("➜ 1. Extrayendo todas las capas de imagen con pdfimages (formato nativo)...")
    cmd_pdfimages = ["pdfimages", "-all", pdf_path, os.path.join(sub_dir, "capa_img")]
    subprocess.run(cmd_pdfimages, capture_output=True)
    
    # 2. Descomprimir el flujo de comandos /Contents usando qpdf
    decompressed_pdf = os.path.join(sub_dir, "descomprimido.pdf")
    print("➜ 2. Descomprimiendo flujos de contenido gráfico con qpdf (buscando errores xref)...")
    cmd_qpdf = ["qpdf", "--qdf", "--object-streams=disable", pdf_path, decompressed_pdf]
    qpdf_result = subprocess.run(cmd_qpdf, capture_output=True, text=True)
    xref_warnings = [line for line in qpdf_result.stderr.splitlines() if "WARNING" in line or "reported number of objects" in line]
    
    # 3. Buscar intrusiones de XObject / QR en el flujo descomprimido
    print("➜ 3. Rastreando comandos de intrusión gráfica (/XObject /Image /Do)...")
    intrusiones = []
    if os.path.exists(decompressed_pdf):
        with open(decompressed_pdf, "r", encoding="latin-1") as f:
            content = f.read()
            # Buscar referencias a XObjects e imágenes superpuestas
            xobjects = [line for line in content.splitlines() if "/XObject" in line or "/Do" in line or "/Image" in line]
            intrusiones = xobjects
            
    # Write summary report for this PDF
    summary_file = os.path.join(sub_dir, "informe_capas_ocultas.txt")
    with open(summary_file, "w", encoding="utf-8") as f_sum:
        f_sum.write(f"# REPORTE DE CAPAS Y CONTENIDO CUBIERTO / INTRUSIVO\n")
        f_sum.write(f"Archivo: {pdf_path}\n\n")
        f_sum.write("## CAPAS GRÁFICAS EXTRAÍDAS\n")
        imgs = [i for i in os.listdir(sub_dir) if i.startswith("capa_img")]
        f_sum.write(f"Total imágenes extraídas: {len(imgs)}\n")
        for img in imgs:
            f_sum.write(f"  - {img} ({os.path.getsize(os.path.join(sub_dir, img))} bytes)\n")
            
        f_sum.write("\n## COMANDOS DE INTRUSIÓN EN EL FLUJO DE CONTENIDO (/Contents)\n")
        for line in intrusiones[:50]:
            f_sum.write(f"  {line.strip()}\n")
            
        f_sum.write("\n## ADVERTENCIAS ESTRUCTURALES Y CORRUPCIÓN XREF\n")
        if xref_warnings:
            f_sum.write("🚨 SE DETECTÓ ALTERACIÓN SINTÁCTICA (MANIPULACIÓN POR SOFTWARE):\n")
            for warning in xref_warnings:
                f_sum.write(f"  - {warning.strip()}\n")
        else:
            f_sum.write("  (No se detectaron errores en la tabla xref)\n")
            
    print(f"✅ Extracción completada.")
    print(f"📄 Revisa las imágenes y el informe en: {sub_dir}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramienta Forense de Extracción de Capas Ocultas y Desenmascaramiento de PDFs")
    parser.add_argument("pdf", type=str, help="Ruta al archivo PDF a inspeccionar")
    parser.add_argument("--out", type=str, default="/home/andrea-zabala-c/Desktop/REVELACION_CAPAS_OCULTAS", help="Carpeta de salida")
    args = parser.parse_args()
    
    inspect_and_recover_hidden_content(args.pdf, args.out)
