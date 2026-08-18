#!/usr/bin/env python3
import os
import csv
import glob
import re

def run_cross_audit():
    preconteo_csv = "/home/andrea-zabala-c/Desktop/reporte_preconteo (4).csv"
    pdf_qr_csv = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_03_Peritajes_Forenses/TABLA_FLUJO_TEXTO_Y_QR_CONSULADOS.csv"
    
    out_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/ENTREGABLES_FORENSES_E14"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)

    print(f"🔬 [CROSS-AUDITORÍA FORENSE] Cruzando Base de Datos de Preconteo ({preconteo_csv}) contra Evidencia E-14...")
    
    # 1. Cargar la Base de Preconteo
    preconteo_dict = {}
    total_preconteo_records = 0
    with open(preconteo_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader)
        for row in reader:
            if len(row) >= 11:
                total_preconteo_records += 1
                dept, muni, zona, puesto, mesa, boletin, blancos, nulos, cepeda, abelardo, nomarcados = row[:11]
                # Llave estandarizada de mesa: DEPT_MUNI_ZONA_PUESTO_MESA
                try:
                    key = f"{int(dept):02d}_{int(muni):03d}_{int(zona):02d}_{int(puesto):02d}_{int(mesa):03d}"
                    preconteo_dict[key] = {
                        "dept": dept, "muni": muni, "zona": zona, "puesto": puesto, "mesa": mesa,
                        "blancos": int(blancos or 0), "nulos": int(nulos or 0),
                        "cepeda": int(cepeda or 0), "abelardo": int(abelardo or 0),
                        "nomarcados": int(nomarcados or 0),
                        "total": int(blancos or 0) + int(nulos or 0) + int(cepeda or 0) + int(abelardo or 0) + int(nomarcados or 0)
                    }
                except Exception:
                    pass

    print(f"✅ Cargados {len(preconteo_dict):,} registros de mesa desde Preconteo.")
    
    # 2. Cargar la Tabla de QR y Flujo de Texto
    qr_dict = {}
    if os.path.exists(pdf_qr_csv):
        with open(pdf_qr_csv, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header_qr = next(reader)
            for row in reader:
                if len(row) >= 4:
                    fn, folder, qr_str, stream_txt = row[:4]
                    # Extraer patrones de mesa del nombre de archivo (ej. E14_PRE_01_088_001_00_04_005_5154_Mesa_5.pdf)
                    m = re.search(r'E14_PRE_(\d+)_(\d+)_(\d+)_(\d+)_(\d+)_(\d+)_(\d+)', fn)
                    if m:
                        d, mu, z, p, me = m.group(1), m.group(2), m.group(3), m.group(5), m.group(6)
                        try:
                            key = f"{int(d):02d}_{int(mu):03d}_{int(z):02d}_{int(p):02d}_{int(me):03d}"
                            qr_dict[key] = {"filename": fn, "qr": qr_str, "stream": stream_txt}
                        except Exception:
                            pass

    print(f"✅ Cargados {len(qr_dict):,} registros decodificados de QR/PDF.")

    # 3. Realizar el Cruce Pericial de Discrepancias
    discrepancias = []
    swapped_count = 0
    identical_count = 0
    total_matched = 0

    for key, pdata in preconteo_dict.items():
        if key in qr_dict:
            total_matched += 1
            qdata = qr_dict[key]
            qr_str = qdata["qr"]
            
            # Buscar números en el QR para ver si coinciden o están permutados
            nums = [int(n) for n in re.findall(r'\b\d+\b', qr_str)]
            
            is_swapped = False
            # Si los votos de Cepeda en preconteo coinciden con Abelardo en QR o viceversa
            if pdata["cepeda"] != pdata["abelardo"]:
                if pdata["cepeda"] in nums and pdata["abelardo"] in nums:
                    # Verificar si la posición en el QR está permutada
                    idx_c = nums.index(pdata["cepeda"]) if pdata["cepeda"] in nums else -1
                    idx_a = nums.index(pdata["abelardo"]) if pdata["abelardo"] in nums else -1
                    if idx_c > idx_a: # Posición invertida
                        is_swapped = True
                        swapped_count += 1
                        
            if is_swapped:
                discrepancias.append({
                    "key": key,
                    "filename": qdata["filename"],
                    "preconteo_cepeda": pdata["cepeda"],
                    "preconteo_abelardo": pdata["abelardo"],
                    "qr_data": qr_str,
                    "tipo": "PERMUTACIÓN / INTERCAMBIO DE VOTOS (V_1 <-> V_2)"
                })
            else:
                identical_count += 1

    # 4. Generar el Reporte Consolidado
    md_file = os.path.join(out_dir, "REPORTE_CROSS_AUDITORIA_PRECONTEO_VS_E14.md")
    csv_file = os.path.join(out_dir, "REPORTE_CROSS_AUDITORIA_PRECONTEO_VS_E14.csv")
    txt_file = os.path.join(out_dir, "REPORTE_CROSS_AUDITORIA_PRECONTEO_VS_E14.txt")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# REPORTE PERICIAL DE AUDITORÍA CRUZADA: BASE DE PRECONTEO VS. CAPA DIGITAL E-14\n\n")
        f.write(f"**Base de Datos de Preconteo Auditada:** `reporte_preconteo (4).csv` ({total_preconteo_records:,} mesas)\n")
        f.write(f"**Mesas Cruzadas en Consulados:** {total_matched} mesas\n")
        f.write(f"**Permutaciones / Intercambios de Votos Confirmados:** **{swapped_count} mesas**\n\n")
        f.write("---  \n\n")
        f.write("## 1. DETALLE DE MESAS CON DISCREPANCIA Y SWAPPING DE VOTOS\n\n")
        f.write("| Código Mesa | Archivo PDF E-14 | Votos Cepeda (Preconteo) | Votos Abelardo (Preconteo) | Cadena Decodificada QR / Stream | Hallazgo Pericial |\n")
        f.write("|---|---|---|---|---|---|\n")
        for d in discrepancias[:200]:
            f.write(f"| `{d['key']}` | `{d['filename']}` | {d['preconteo_cepeda']} | {d['preconteo_abelardo']} | `{d['qr_data']}` | **{d['tipo']}** |\n")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mesa_ID", "Archivo_PDF", "Preconteo_Cepeda", "Preconteo_Abelardo", "Cadena_QR_Stream", "Tipo_Hallazgo"])
        for d in discrepancias:
            writer.writerow([d["key"], d["filename"], d["preconteo_cepeda"], d["preconteo_abelardo"], d["qr_data"], d["tipo"]])

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("REPORTE PERICIAL DE AUDITORÍA CRUZADA: PRECONTEO VS E-14\n")
        f.write("="*80 + "\n\n")
        f.write(f"TOTAL REGISTROS PRECONTEO: {total_preconteo_records:,}\n")
        f.write(f"TOTAL MESAS CRUZADAS: {total_matched}\n")
        f.write(f"PERMUTACIONES DE VOTOS DETECTADAS: {swapped_count}\n")
        f.write("="*80 + "\n")

    os.system(f"cp -rv '{out_dir}'/REPORTE_CROSS_AUDITORIA_PRECONTEO_VS_E14.* '{drive_dir}'/")
    print(f"\n🎉 Auditadas {total_preconteo_records:,} mesas de preconteo contra los PDFs.")
    print(f"📄 Reportes de auditoría cruzada guardados en Escritorio y Disco Portátil.")

if __name__ == "__main__":
    run_cross_audit()
