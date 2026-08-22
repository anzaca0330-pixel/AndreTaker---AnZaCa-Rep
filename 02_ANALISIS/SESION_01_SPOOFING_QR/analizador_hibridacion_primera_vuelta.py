#!/usr/bin/env python3
"""
Analizador Forense de Foliación Híbrida (Primera Vuelta)
Objetivo: Detectar la mezcla sintética de folios provenientes de 
distintas cadenas de custodia (Delegados, Claveros, CNE) dentro de un mismo PDF.
"""
import os
import sys
import subprocess
import tempfile
from collections import defaultdict

def analyze_hybridization(pdf_path):
    found_types = set()
    page_details = []
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Convertir páginas a JPEG
        subprocess.run(["pdftoppm", "-jpeg", "-r", "150", pdf_path, os.path.join(tmpdir, "page")], capture_output=True)
        
        # Listar imágenes generadas (ordenadas por página)
        images = sorted([f for f in os.listdir(tmpdir) if f.endswith('.jpg')])
        
        if not images:
            return f"Error leyendo PDF o sin páginas: {pdf_path}"
            
        for page_num, img in enumerate(images, 1):
            img_path = os.path.join(tmpdir, img)
            try:
                # Ejecutar OCR con tesseract
                result = subprocess.run(["tesseract", img_path, "-", "-l", "eng", "--psm", "3"], capture_output=True, text=True)
                text = result.stdout.upper()
            except:
                text = ""
                
            page_type = "DESCONOCIDO"
            if "CLAVERO" in text:
                page_type = "CLAVEROS"
            elif "DELEGADO" in text:
                page_type = "DELEGADOS"
            elif "CNE" in text:
                page_type = "CNE"
                
            found_types.add(page_type)
            page_details.append(f"Página {page_num}: {page_type}")
        
    # Si hay más de un tipo conocido, es una foliación híbrida!
    is_hybrid = len(found_types - {"DESCONOCIDO"}) > 1
    
    return {
        "is_hybrid": is_hybrid,
        "types": list(found_types),
        "details": page_details
    }

def main(root_dir):
    print(f"[*] Iniciando Auditoría Forense de Hibridación en: {root_dir}")
    print("[*] Buscando PDFs de Los Ángeles...\n")
    
    hybrid_count = 0
    total_pdfs = 0
    report_lines = ["# REPORTE DE FOLIACIÓN HÍBRIDA - LOS ÁNGELES (1RA VUELTA)\n"]
    
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.lower().endswith('.pdf'):
                pdf_path = os.path.join(dirpath, f)
                total_pdfs += 1
                
                result = analyze_hybridization(pdf_path)
                if isinstance(result, str):
                    continue # Skip errors
                    
                if result["is_hybrid"]:
                    hybrid_count += 1
                    alert = f"🚨 **ANOMALÍA DETECTADA**: Mezcla de cadenas de custodia en `{f}`"
                    print(alert)
                    for detail in result["details"]:
                        print(f"    - {detail}")
                    print("-" * 40)
                    
                    report_lines.append(f"### Mesa Afectada: `{f}`")
                    report_lines.append(f"**Tipos encontrados:** {', '.join(result['types'])}")
                    report_lines.append("**Desglose de Folios:**")
                    for detail in result["details"]:
                        report_lines.append(f"- {detail}")
                    report_lines.append("\n---\n")

    print(f"\n[*] Auditoría Completada.")
    print(f"[*] Total de actas auditadas: {total_pdfs}")
    print(f"[*] Total de actas con foliación híbrida: {hybrid_count}")
    
    # Guardar reporte
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "REPORTE_HIBRIDACION_LOS_ANGELES.md")
    with open(report_path, "w", encoding="utf-8") as out:
        out.write("\n".join(report_lines))
    print(f"[*] Reporte guardado en: {report_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analizador_hibridacion_primera_vuelta.py <ruta_al_directorio_pdfs>")
        sys.exit(1)
    
    main(sys.argv[1])
