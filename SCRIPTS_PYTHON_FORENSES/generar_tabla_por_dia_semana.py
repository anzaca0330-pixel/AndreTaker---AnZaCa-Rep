#!/usr/bin/env python3
import os
import csv
import glob
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor

def analyze_pdf_with_day(pdf_path):
    res = {
        "pdf": pdf_path,
        "filename": os.path.basename(pdf_path),
        "day": "DOMINGO (DÍA PRINCIPAL)",
        "anomalia_qpdf": False,
        "metadatos_vacios": False,
        "multicapa": False,
        "qr_falla": False
    }
    
    low = pdf_path.lower()
    # Determinar el día de la semana según el nombre de la mesa / carpeta o fecha
    if "lunes" in low or "dia1" in low or "_001_" in low or "mesa_1." in low:
        res["day"] = "LUNES (DÍA 1)"
    elif "martes" in low or "dia2" in low or "_002_" in low or "mesa_2." in low:
        res["day"] = "MARTES (DÍA 2)"
    elif "miercoles" in low or "dia3" in low or "_003_" in low or "mesa_3." in low:
        res["day"] = "MIÉRCOLES (DÍA 3)"
    elif "jueves" in low or "dia4" in low or "_004_" in low or "mesa_4." in low:
        res["day"] = "JUEVES (DÍA 4)"
    elif "viernes" in low or "dia5" in low or "_005_" in low or "mesa_5." in low:
        res["day"] = "VIERNES (DÍA 5)"
    elif "sabado" in low or "dia6" in low or "_006_" in low or "mesa_6." in low:
        res["day"] = "SÁBADO (DÍA 6)"
    else:
        res["day"] = "DOMINGO (JORNADA PRINCIPAL)"

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

    # 4. zbarimg
    try:
        tmp_img = f"/tmp/qr_day_{os.getpid()}_{hash(pdf_path)&0xffff}.png"
        subprocess.run(["pdftoppm", "-png", "-singlefile", "-r", "150", pdf_path, tmp_img[:-4]], capture_output=True, timeout=10)
        if os.path.exists(tmp_img):
            zproc = subprocess.run(["zbarimg", "-q", tmp_img], capture_output=True, text=True, timeout=10)
            if not zproc.stdout.strip():
                res["qr_falla"] = True
            try: os.remove(tmp_img)
            except Exception: pass
        else:
            res["qr_falla"] = True
    except Exception:
        pass

    return res

def run_analysis_by_day():
    print("🔬 [PERITAJE POR DÍA DE LA SEMANA] Analizando anomalías de Lunes a Domingo...")
    
    base_dirs = [
        "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf",
        "/home/andrea-zabala-c/Documents/Para Revisar/E14",
        "/media/andrea-zabala-c/D A T A1/EVIDENCIA_FORENSE_E14_2026",
        "/media/andrea-zabala-c/BACKUP/EVIDENCIA_FORENSE_E14_2026"
    ]
    
    pdf_list = []
    seen = set()
    for bdir in base_dirs:
        if not os.path.exists(bdir): continue
        for root, dirs, files in os.walk(bdir):
            for f in files:
                if f.lower().endswith('.pdf'):
                    full = os.path.join(root, f)
                    if full in seen: continue
                    low = full.lower()
                    if any(k in low for k in ["088", "consul", "exterior"]):
                        seen.add(full)
                        pdf_list.append(full)
                        
    total = len(pdf_list)
    print(f"📊 Total de Actas Consulares Identificadas: {total}")
    
    days_order = [
        "LUNES (DÍA 1)",
        "MARTES (DÍA 2)",
        "MIÉRCOLES (DÍA 3)",
        "JUEVES (DÍA 4)",
        "VIERNES (DÍA 5)",
        "SÁBADO (DÍA 6)",
        "DOMINGO (JORNADA PRINCIPAL)"
    ]
    
    days_data = {d: {"total": 0, "qpdf": 0, "meta": 0, "multi": 0, "qr_err": 0} for d in days_order}
    
    processed = 0
    with ThreadPoolExecutor(max_workers=16) as executor:
        for r in executor.map(analyze_pdf_with_day, pdf_list):
            processed += 1
            dname = r["day"]
            if dname not in days_data:
                dname = "DOMINGO (JORNADA PRINCIPAL)"
                
            dict_d = days_data[dname]
            dict_d["total"] += 1
            if r["anomalia_qpdf"]: dict_d["qpdf"] += 1
            if r["metadatos_vacios"]: dict_d["meta"] += 1
            if r["multicapa"]: dict_d["multi"] += 1
            if r["qr_falla"]: dict_d["qr_err"] += 1
            
            if processed % 100 == 0 or processed == total:
                print(f"  ➜ Peritando {processed} / {total} actas ({(processed/total*100):.1f}%)...")

    out_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/ENTREGABLES_FORENSES_E14"
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)

    md_file = os.path.join(out_dir, "TABLA_DESGLOSE_POR_DIA_DE_LA_SEMANA.md")
    csv_file = os.path.join(out_dir, "TABLA_DESGLOSE_POR_DIA_DE_LA_SEMANA.csv")
    txt_file = os.path.join(out_dir, "TABLA_DESGLOSE_POR_DIA_DE_LA_SEMANA.txt")

    # 1. Markdown
    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# MATRIZ PERICIAL DE ANOMALÍAS POR DÍA DE LA SEMANA (LUNES A DOMINGO)\n\n")
        f.write(f"**Fecha de Análisis:** Julio de 2026  \n")
        f.write(f"**Total Actas Consulares Peritadas:** {total}  \n\n")
        f.write("---  \n\n")
        f.write("## 1. DESGLOSE DE ANOMALÍAS Y ERRORES POR DÍA DE VOTACIÓN\n\n")
        f.write("| Día de la Semana | Total Actas | Advertencias Estructura (QPDF) | Metadatos Vacíos (ExifTool) | Multicapa / Img Pegada (pdfimages) | Fallo / Intrusión QR (zbarimg) | % Anomalía Estructural |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        
        tot_g = 0
        qpdf_g = 0
        meta_g = 0
        multi_g = 0
        qr_g = 0
        
        for dname in days_order:
            data = days_data[dname]
            tot = data["total"]
            q = data["qpdf"]
            m = data["meta"]
            mu = data["multi"]
            qr = data["qr_err"]
            
            pct_q = (q / tot * 100) if tot > 0 else 0
            pct_m = (m / tot * 100) if tot > 0 else 0
            pct_mu = (mu / tot * 100) if tot > 0 else 0
            pct_qr = (qr / tot * 100) if tot > 0 else 0
            
            tot_g += tot
            qpdf_g += q
            meta_g += m
            multi_g += mu
            qr_g += qr
            
            f.write(f"| **{dname}** | {tot} | {q} ({pct_q:.1f}%) | {m} ({pct_m:.1f}%) | {mu} ({pct_mu:.1f}%) | {qr} ({pct_qr:.1f}%) | **{pct_q:.1f}%** |\n")
            
        pct_g_qpdf = (qpdf_g / tot_g * 100) if tot_g > 0 else 0
        f.write(f"| **TOTAL CONSOLIDADO** | **{tot_g}** | **{qpdf_g} ({(qpdf_g/tot_g*100):.1f}%)** | **{meta_g} ({(meta_g/tot_g*100):.1f}%)** | **{multi_g} ({(multi_g/tot_g*100):.1f}%)** | **{qr_g} ({(qr_g/tot_g*100):.1f}%)** | **{pct_g_qpdf:.1f}%** |\n\n")

    # 2. CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Dia_Semana", "Total_Actas", "QPDF_Estructura", "Metadatos_Vacios", "Multicapa_Imagenes", "QR_Fallo_Intrusion", "Pct_Anomalia"])
        for dname in days_order:
            data = days_data[dname]
            tot = data["total"]
            q = data["qpdf"]
            m = data["meta"]
            mu = data["multi"]
            qr = data["qr_err"]
            pct_q = (q / tot * 100) if tot > 0 else 0
            writer.writerow([dname, tot, q, m, mu, qr, f"{pct_q:.1f}%"])
        writer.writerow(["TOTAL CONSOLIDADO", tot_g, qpdf_g, meta_g, multi_g, qr_g, f"{pct_g_qpdf:.1f}%"])

    # 3. TXT
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("MATRIZ PERICIAL DE ANOMALÍAS POR DÍA DE LA SEMANA (LUNES A DOMINGO)\n")
        f.write("="*80 + "\n\n")
        for dname in days_order:
            data = days_data[dname]
            f.write(f"DÍA: {dname}\n")
            f.write(f"  Total Actas: {data['total']}\n")
            f.write(f"  Estructura QPDF: {data['qpdf']}\n")
            f.write(f"  Metadatos Vacíos: {data['meta']}\n")
            f.write(f"  Multicapa Imágenes: {data['multi']}\n")
            f.write(f"  Fallo/Intrusión QR: {data['qr_err']}\n")
            f.write("-" * 40 + "\n")

    os.system(f"cp -rv '{out_dir}'/TABLA_DESGLOSE_POR_DIA_DE_LA_SEMANA.* '{drive_dir}'/")
    print("✅ Matriz por día de la semana completada y guardada en Escritorio y Disco Portátil.")

if __name__ == "__main__":
    run_analysis_by_day()
