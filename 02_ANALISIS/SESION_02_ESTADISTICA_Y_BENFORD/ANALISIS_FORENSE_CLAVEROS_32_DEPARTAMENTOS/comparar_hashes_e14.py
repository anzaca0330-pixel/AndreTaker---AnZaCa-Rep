#!/usr/bin/env python3
import os
import sys
import hashlib
import argparse
from concurrent.futures import ThreadPoolExecutor

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(65536), b""):
                sha256_hash.update(byte_block)
        return file_path, sha256_hash.hexdigest()
    except Exception:
        return file_path, None

def scan_pdf_hashes(directory):
    pdf_map = {}
    files_to_process = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.lower().endswith('.pdf'):
                full_path = os.path.join(root, f)
                files_to_process.append((f, full_path))
                
    with ThreadPoolExecutor(max_workers=16) as executor:
        for (filename, full_path), (p, sha) in zip(files_to_process, executor.map(lambda x: calculate_sha256(x[1]), files_to_process)):
            if sha:
                pdf_map[filename] = (full_path, sha)
    return pdf_map

def compare_collections(new_dir, old_dirs, output_report):
    print("🔍 [SEGUNDA VUELTA] Escaneando descarga masiva directa de Segunda Vuelta...")
    new_map = scan_pdf_hashes(new_dir)
    print(f"✅ Segunda Vuelta cargada: {len(new_map)} archivos PDF.")
    
    print("\n🔍 Escaneando y separando colecciones previas (1ra Vuelta vs 2da Vuelta)...")
    old_segunda_map = {}
    old_primera_map = {}
    
    for od in old_dirs:
        if os.path.exists(od):
            print(f"  ➜ Procesando fuente: {od}")
            m = scan_pdf_hashes(od)
            for fn, (fp, sha) in m.items():
                if "segundavuelta" in fp.lower() or "2v" in fp.lower():
                    old_segunda_map[fn] = (fp, sha)
                else:
                    old_primera_map[fn] = (fp, sha)
            
    print(f"✅ Archivos de 2da Vuelta previos identificados: {len(old_segunda_map)}")
    print(f"ℹ️ Archivos de 1ra Vuelta aislados (para no mezclar rondas): {len(old_primera_map)}")
    
    identicos_2v = []
    modificados_2v = []
    solo_nuevos_2v = []
    
    for filename, (new_path, new_sha) in new_map.items():
        if filename in old_segunda_map:
            old_path, old_sha = old_segunda_map[filename]
            if new_sha == old_sha:
                identicos_2v.append((filename, new_sha))
            else:
                modificados_2v.append((filename, old_sha, new_sha, old_path, new_path))
        else:
            solo_nuevos_2v.append((filename, new_sha))
            
    print("\n================ RESULTADOS COMPARATIVOS (SEGUNDA VUELTA) ================")
    print(f"Total Actas de Segunda Vuelta en Nueva Descarga: {len(new_map)}")
    print(f"Actas de 2da Vuelta Comparadas: {len(identicos_2v) + len(modificados_2v)}")
    print(f"🟢 Archivos Idénticos en 2da Vuelta: {len(identicos_2v)}")
    print(f"🚨 Archivos de 2da Vuelta Modificados: {len(modificados_2v)}")
    print(f"🆕 Archivos Nuevos de 2da Vuelta: {len(solo_nuevos_2v)}")
    
    with open(output_report, "w", encoding="utf-8") as out:
        out.write("# REPORTE PERICIAL COMPARATIVO DE HASHES - SEGUNDA VUELTA PRESIDENCIAL 2026\n")
        out.write(f"# Alcance: Evaluación exclusiva de actas correspondientes a la Segunda Vuelta Electoral.\n")
        out.write(f"# Total evaluados (Segunda Vuelta): {len(new_map)}\n")
        out.write(f"# Coincidentes de 2da Vuelta: {len(identicos_2v)} | Modificados: {len(modificados_2v)} | Nuevos: {len(solo_nuevos_2v)}\n")
        out.write(f"# Archivos de 1ra Vuelta Aislados: {len(old_primera_map)}\n\n")
        
        if modificados_2v:
            out.write("## 🚨 ARCHIVOS DE SEGUNDA VUELTA CON HASH ALTERADO / MODIFICADO\n")
            out.write("NOMBRE_ARCHIVO | HASH_ANTERIOR (2da V) | HASH_NUEVO (2da V)\n")
            out.write("-" * 80 + "\n")
            for fn, o_sha, n_sha, o_p, n_p in modificados_2v:
                out.write(f"{fn} | {o_sha} | {n_sha}\n")
            out.write("\n")
        else:
            out.write("## 🛡️ ESTADO DE INTEGRIDAD DE SEGUNDA VUELTA\n")
            out.write("No se detectaron discrepancias entre los registros de Segunda Vuelta evaluados.\n\n")
            
        out.write("## 🟢 MUESTRA DE ARCHIVOS DE SEGUNDA VUELTA VERIFICADOS\n")
        for fn, sha in identicos_2v[:100]:
            out.write(f"{fn} | {sha}\n")
            
    print(f"\n📄 Reporte pericial de Segunda Vuelta guardado en: {output_report}")

if __name__ == "__main__":
    new_directory = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
    previous_directories = [
        "/home/andrea-zabala-c/Desktop/actas",
        "/home/andrea-zabala-c/Documents/Para Revisar/E14",
        "/media/andrea-zabala-c/D A T A1/EVIDENCIA_FORENSE_E14_2026",
        "/media/andrea-zabala-c/BACKUP/EVIDENCIA_FORENSE_E14_2026"
    ]
    report_path = "/home/andrea-zabala-c/Desktop/REPORTE_COMPARATIVO_HASHES_2DA_VUELTA.md"
    compare_collections(new_directory, previous_directories, report_path)
