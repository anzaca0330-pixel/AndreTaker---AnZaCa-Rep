import os
import glob
import subprocess
import multiprocessing
import csv
from datetime import datetime

def check_pdf(pdf_path):
    result = {
        "file": os.path.basename(pdf_path),
        "is_1bpc": False,
        "is_rgb": False,
        "xref_corrupt": False,
        "error": ""
    }
    
    # 1. QPDF Check para corrupcion estructural
    try:
        qproc = subprocess.run(["qpdf", "--check", pdf_path], capture_output=True, text=True)
        if "reported number of objects (15) is not one plus the highest object number (13)" in qproc.stderr or "reported number of objects (15) is not one plus the highest object number (13)" in qproc.stdout:
            result["xref_corrupt"] = True
    except Exception as e:
        result["error"] = "qpdf_error"
        
    # 2. Mutool Info para capas / formato
    try:
        mproc = subprocess.run(["mutool", "info", pdf_path], capture_output=True, text=True)
        out = mproc.stdout.lower()
        if "1bpc devgray" in out:
            result["is_1bpc"] = True
        if "8bpc devrgb" in out:
            result["is_rgb"] = True
    except Exception as e:
        if not result["error"]:
            result["error"] = "mutool_error"
            
    return result

def main():
    target_dir = "/media/andrea-zabala-c/D A T A1/delegados/Delegados_21_06_2026"
    out_csv = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ESTADISTICA_DELEGADOS_MASIVA.csv"
    
    print(f"[{datetime.now()}] Escaneando directorio...")
    pdfs = glob.glob(os.path.join(target_dir, "*.pdf"))
    
    print(f"[{datetime.now()}] Encontrados {len(pdfs)} PDFs para auditar.")
    print("Iniciando pool de multiprocesamiento...")
    
    results = []
    
    # Usar multiprocesamiento para agilizar (usar cpu_count)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    
    for res in pool.imap_unordered(check_pdf, pdfs):
        results.append(res)
        
    pool.close()
    pool.join()
    
    print(f"\n[{datetime.now()}] Analisis terminado. Guardando resultados...")
    
    with open(out_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "is_1bpc", "is_rgb", "xref_corrupt", "error"])
        writer.writeheader()
        writer.writerows(results)
        
    print(f"✅ Reporte masivo exportado a: {out_csv}")
    
    # Imprimir estadistica rapida
    total = len(results)
    c_1bpc = sum(1 for r in results if r["is_1bpc"])
    c_rgb = sum(1 for r in results if r["is_rgb"])
    c_xref = sum(1 for r in results if r["xref_corrupt"])
    
    print("\n--- ESTADÍSTICAS RÁPIDAS ---")
    print(f"Total Auditados: {total}")
    print(f"Deepfake (1bpc DevGray): {c_1bpc} ({(c_1bpc/total)*100 if total else 0:.2f}%)")
    print(f"RGB Encontrado: {c_rgb} ({(c_rgb/total)*100 if total else 0:.2f}%)")
    print(f"XREF Corrupto (Herramienta Fraude): {c_xref} ({(c_xref/total)*100 if total else 0:.2f}%)")

if __name__ == "__main__":
    main()
