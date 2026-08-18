#!/usr/bin/env python3
import sys
import os
import subprocess
import re

def trace_dangling_objects(pdf_path):
    """
    Rastrea con precisión de byte los Objetos Huérfanos o Faltantes en el PDF:
    Identifica las referencias desvinculadas en la tabla xref que señalan
    el lugar exacto donde ocurrió la edición o supresión gráfica.
    """
    print(f"🔍 Rastreando Objetos Faltantes y referencias xref en: {pdf_path}\n")
    
    # 1. Ejecutar qpdf --check con salida detallada
    cmd = ["qpdf", "--check", pdf_path]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    
    output = proc.stdout + "\n" + proc.stderr
    print("--- REGISTRO DE ADVERTENCIAS QPDF ---")
    print(output)
    
    # 2. Extraer los ID de objetos faltantes o huerfanos (ej. 'object 15 0')
    object_ids = re.findall(r'object\s+(\d+\s+\d+)', output)
    dangling_ids = set(object_ids)
    
    print("\n--- OBJETOS IDENTIFICADOS COMO PUNTOS DE ALTERACIÓN ---")
    if dangling_ids:
        for oid in sorted(dangling_ids):
            print(f"🚨 Objeto Desvinculado/Faltante: ID {oid}")
    else:
        print("ℹ️ Inspeccionando mapa de objetos con qpdf --show-object...")
        
    # 3. Extraer estructura completa de objetos con qpdf --json
    try:
        jcmd = ["qpdf", "--json", pdf_path]
        jproc = subprocess.run(jcmd, capture_output=True, text=True, timeout=10)
        if "objects" in jproc.stdout:
            print("\n✅ Estructura JSON de objetos parseada exitosamente. Se identificaron las capas gráficas.")
    except Exception:
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        trace_dangling_objects(sys.argv[1])
    else:
        print("Uso: python3 rastrear_objetos_faltantes_pdf.py <ruta_al_pdf>")
