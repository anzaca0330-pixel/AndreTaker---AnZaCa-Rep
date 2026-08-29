#!/usr/bin/env python3
import os
import csv
import glob
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor

def analyze_pdf_national(pdf_path):
    res = {
        "pdf": pdf_path,
        "filename": os.path.basename(pdf_path),
        "depto": "BOGOTA D.C.",
        "anomalia_qpdf": False,
        "metadatos_vacios": False,
        "multicapa": False
    }
    
    # Extraer nombre del departamento desde la ruta
    parts = pdf_path.split(os.sep)
    dept_names = {'ANTIOQUIA', 'ATLANTICO', 'BOGOTA D.C.', 'BOLIVAR', 'BOYACA', 'CALDAS', 'CAUCA', 'CESAR', 'CHOCO', 'CORDOBA', 'CUNDINAMARCA', 'HUILA', 'MAGDALENA', 'NARIÑO', 'NORTE DE SAN', 'QUINDIO', 'RISARALDA', 'SANTANDER', 'SUCRE', 'TOLIMA', 'VALLE', 'ARAUCA', 'CAQUETA', 'CASANARE', 'LA GUAJIRA', 'GUAINIA', 'META', 'GUAVIARE', 'SAN ANDRES', 'AMAZONAS', 'PUTUMAYO', 'VAUPES', 'VICHADA', 'CONSULADOS'}
    
    for p in parts:
        up = p.upper()
        if up in dept_names:
            res["depto"] = up
            break

    # 1. QPDF
    try:
        proc = subprocess.run(["qpdf", "--check", pdf_path], capture_output=True, text=True, timeout=10)
        out = proc.stdout + proc.stderr
        if "operation succeeded with warnings" in out or "warning" in out.lower():
            res["anomalia_qpdf"] = True
    except Exception:
        pass

    # 2. ExifTool
    try:
        proc = subprocess.run(["exiftool", "-Creator", "-Producer", "-CreateDate", pdf_path], capture_output=True, text=True, timeout=10)
        if not proc.stdout.strip():
            res["metadatos_vacios"] = True
    except Exception:
        pass

    # 3. pdfimages
    try:
        proc = subprocess.run(["pdfimages", "-list", pdf_path], capture_output=True, text=True, timeout=10)
        lines = [l for l in proc.stdout.splitlines() if l.strip()]
        if len(lines) > 3:
            res["multicapa"] = True
    except Exception:
        pass

    return res

def run_national_colombia_audit():
    print("🚀 [AUDITORÍA NACIONAL MASIVA] Escaneando las actas de los 32 Departamentos de Colombia...")
    
    base_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
    out_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/ENTREGABLES_FORENSES_E14"
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)
    
    pdf_list = []
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_list.append(os.path.join(root, f))
                
    total_national = len(pdf_list)
    print(f"📊 Total Actas Nacionales E-14 Identificadas: {total_national:,}")
    
    depto_results = {}
    
    processed = 0
    with ThreadPoolExecutor(max_workers=16) as executor:
        for r in executor.map(analyze_pdf_national, pdf_list):
            processed += 1
            dep = r["depto"]
            if dep not in depto_results:
                depto_results[dep] = {"total": 0, "qpdf": 0, "meta": 0, "multi": 0}
                
            dict_d = depto_results[dep]
            dict_d["total"] += 1
            if r["anomalia_qpdf"]: dict_d["qpdf"] += 1
            if r["metadatos_vacios"]: dict_d["meta"] += 1
            if r["multicapa"]: dict_d["multi"] += 1
            
            if processed % 5000 == 0 or processed == total_national:
                print(f"  ➜ Auditando Colombia: {processed:,} / {total_national:,} actas ({(processed/total_national*100):.1f}%)...")

    # Exportar Auditoría Nacional
    md_file = os.path.join(out_dir, "AUDITORIA_NACIONAL_32_DEPARTAMENTOS_COLOMBIA.md")
    csv_file = os.path.join(out_dir, "AUDITORIA_NACIONAL_32_DEPARTAMENTOS_COLOMBIA.csv")
    txt_file = os.path.join(out_dir, "AUDITORIA_NACIONAL_32_DEPARTAMENTOS_COLOMBIA.txt")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# AUDITORÍA FORENSE NACIONAL — 32 DEPARTAMENTOS DE COLOMBIA Y BOGOTÁ D.C.\n\n")
        f.write(f"**Fecha de Auditoría:** Julio de 2026  \n")
        f.write(f"**Total Actas E-14 Auditadas en Colombia:** {total_national:,}  \n\n")
        f.write("---  \n\n")
        f.write("## 1. MATRIZ NACIONAL DE ANOMALÍAS POR DEPARTAMENTO\n\n")
        f.write("| Departamento | Total Actas | Advertencias Estructura (QPDF) | Metadatos Vacíos (ExifTool) | Multicapa / Img Pegada (pdfimages) | % Desviación Estructural |\n")
        f.write("|---|---|---|---|---|---|\n")
        
        tot_g, qpdf_g, meta_g, multi_g = 0, 0, 0, 0
        for dep, data in sorted(depto_results.items()):
            tot = data["total"]
            q = data["qpdf"]
            m = data["meta"]
            mu = data["multi"]
            pct = (q / tot * 100) if tot > 0 else 0
            
            tot_g += tot
            qpdf_g += q
            meta_g += m
            multi_g += mu
            
            f.write(f"| **{dep}** | {tot:,} | {q:,} ({pct:.1f}%) | {m:,} ({(m/tot*100):.1f}%) | {mu:,} ({(mu/tot*100):.1f}%) | **{pct:.1f}%** |\n")
            
        pct_g = (qpdf_g / tot_g * 100) if tot_g > 0 else 0
        f.write(f"| **TOTAL NACIONAL COLOMBIA** | **{tot_g:,}** | **{qpdf_g:,} ({pct_g:.1f}%)** | **{meta_g:,} ({(meta_g/tot_g*100):.1f}%)** | **{multi_g:,} ({(multi_g/tot_g*100):.1f}%)** | **{pct_g:.1f}%** |\n\n")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Departamento", "Total_Actas", "QPDF_Estructura", "Metadatos_Vacios", "Multicapa_Imagenes", "Porcentaje_Anomalia"])
        for dep, data in sorted(depto_results.items()):
            tot = data["total"]
            q = data["qpdf"]
            m = data["meta"]
            mu = data["multi"]
            pct = (q / tot * 100) if tot > 0 else 0
            writer.writerow([dep, tot, q, m, mu, f"{pct:.1f}%"])
        writer.writerow(["TOTAL NACIONAL COLOMBIA", tot_g, qpdf_g, meta_g, multi_g, f"{pct_g:.1f}%"])

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("AUDITORÍA FORENSE NACIONAL - 32 DEPARTAMENTOS DE COLOMBIA\n")
        f.write("="*80 + "\n\n")
        f.write(f"TOTAL ACTAS COLOMBIA: {tot_g:,}\n")
        f.write(f"QPDF ESTRUCTURA: {qpdf_g:,} ({pct_g:.1f}%)\n")
        f.write(f"METADATOS VACÍOS EXIFTOOL: {meta_g:,}\n")
        f.write("="*80 + "\n")

    os.system(f"cp -rv '{out_dir}'/AUDITORIA_NACIONAL_32_DEPARTAMENTOS_COLOMBIA.* '{drive_dir}'/")
    print(f"\n🎉 Auditoría Nacional de Colombia completada exitosamente.")
    print(f"📄 Archivos guardados en Escritorio y Disco Portátil.")

if __name__ == "__main__":
    run_national_colombia_audit()
