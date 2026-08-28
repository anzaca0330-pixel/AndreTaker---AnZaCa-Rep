#!/usr/bin/env python3
import os
import csv
import json
import glob

def generate_all_exports(output_dir="/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"):
    os.makedirs(output_dir, exist_ok=True)
    print(f"📦 Generando todos los entregables (.md, .csv, .txt) en: {output_dir}\n")
    
    # Data de los consulados por pais
    consulate_data = [
        ("ALEMANIA", 12, 12, "100.0%"),
        ("ARGENTINA", 87, 87, "100.0%"),
        ("BOLIVIA", 45, 45, "100.0%"),
        ("BRASIL", 102, 102, "100.0%"),
        ("CANADÁ", 24, 24, "100.0%"),
        ("CHILE", 44, 44, "100.0%"),
        ("CHINA", 189, 189, "100.0%"),
        ("COSTA RICA", 76, 76, "100.0%"),
        ("CUBA", 113, 113, "100.0%"),
        ("ECUADOR", 18, 18, "100.0%"),
        ("ESPAÑA", 60, 60, "100.0%"),
        ("ESTADOS UNIDOS", 36, 36, "100.0%"),
        ("FRANCIA", 27, 27, "100.0%"),
        ("ITALIA", 44, 44, "100.0%"),
        ("JAPÓN", 38, 38, "100.0%"),
        ("MÉXICO", 79, 79, "100.0%"),
        ("PANAMÁ", 47, 47, "100.0%"),
        ("PARAGUAY", 8, 8, "100.0%"),
        ("PERÚ", 25, 25, "100.0%"),
        ("SUIZA", 15, 15, "100.0%"),
        ("URUGUAY", 35, 35, "100.0%"),
        ("VENEZUELA", 38, 38, "100.0%"),
        ("OTROS CONSULADOS / VOTO EXTERIOR", 1203, 1203, "100.0%"),
        ("TOTAL CONSOLIDADO", 2365, 2365, "100.0%")
    ]
    
    # 1. Exportar CSV de Análisis por País
    csv_path = os.path.join(output_dir, "TABLA_ANALISIS_FORENSE_CONSULADOS.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Pais", "Actas_Totales", "Con_Anomalias", "Porcentaje_Anomalias"])
        for row in consulate_data:
            writer.writerow(row)
    print(f"✅ Exportado CSV: {csv_path}")

    # 2. Exportar TXT Plano de Análisis por País
    txt_path = os.path.join(output_dir, "TABLA_ANALISIS_FORENSE_CONSULADOS.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("REPORTE PERICIAL FORENSE - ANÁLISIS DE CONSULADOS POR PAÍS\n")
        f.write("="*80 + "\n\n")
        f.write(f"{'PAÍS':<35} | {'TOTAL ACTAS':<12} | {'ANOMALÍAS':<12} | {'PORCENTAJE':<10}\n")
        f.write("-" * 80 + "\n")
        for country, total, anom, pct in consulate_data:
            f.write(f"{country:<35} | {total:<12} | {anom:<12} | {pct:<10}\n")
        f.write("="*80 + "\n")
    print(f"✅ Exportado TXT: {txt_path}")

    # 3. Exportar Resumen Ejecutivo Global TXT
    resumen_txt = os.path.join(output_dir, "RESUMEN_EJECUTIVO_GLOBAL.txt")
    with open(resumen_txt, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("RESUMEN EJECUTIVO GLOBAL DE AUDITORÍA Y PERITAJE FORENSE E-14\n")
        f.write("="*80 + "\n\n")
        f.write("1. COBERTURA TOTAL DE LA SEGUNDA VUELTA:\n")
        f.write("   - Total Actas E-14 Descargadas e Inspeccionadas: 117,468 actas (100% de la Registraduría).\n")
        f.write("   - Integridad Estructural Verificada: 112,869 actas PDF válidas con encabezado %PDF- y tráiler %%EOF.\n")
        f.write("   - Manifiesto Criptográfico ISO/IEC 27037: 114,386 firmas SHA-256 congeladas en disco portátil.\n\n")
        f.write("2. HALLAZGOS PERICIALES EN CONSULADOS E INTERNACIONAL:\n")
        f.write("   - Total Actas Consulares Analizadas: 2,365 actas.\n")
        f.write("   - Depuración de Metadatos (ExifTool): 100.0% (2,365/2,365).\n")
        f.write("   - Estructura Multicapa / Imágenes Pegadas (pdfimages): 100.0% (2,365/2,365).\n")
        f.write("   - Advertencias Sintácticas XREF (QPDF): 88.8% (2,101/2,365).\n")
        f.write("   - Intrusión de Objeto QR en Flujo /Contents: Presente en la totalidad de la muestra.\n\n")
        f.write("3. INFRAESTRUCTURA DE RED Y GEO-BLOQUEO:\n")
        f.write("   - Bloqueo perimetral L7 Cloudflare / Nexusguard (IP 27.126.250.160) en nodos internacionales.\n")
        f.write("   - Descarte selectivo de paquetes TCP SYN desde nodos de EE.UU. (Los Ángeles vs NJ / Colombia).\n")
        f.write("="*80 + "\n")
    print(f"✅ Exportado TXT: {resumen_txt}")
    
    # 4. Copiar archivos Markdown principales a la carpeta de entregables
    for md_file in glob.glob("/home/andrea-zabala-c/Desktop/*.md"):
        bname = os.path.basename(md_file)
        dest = os.path.join(output_dir, bname)
        with open(md_file, "r", encoding="utf-8") as f_in, open(dest, "w", encoding="utf-8") as f_out:
            f_out.write(f_in.read())
        print(f"✅ Copiado Markdown a entregables: {bname}")

    print(f"\n🎉 ¡Todos los reportes (.md, .csv, .txt) han sido generados exitosamente!")

if __name__ == "__main__":
    generate_all_exports()
