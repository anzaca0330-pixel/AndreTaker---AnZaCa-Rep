import os
import zipfile
import re
import csv
from io import TextIOWrapper

TAKEOUT_DIR = "/media/andrea-zabala-c/ANZACA/TAKEOUT/"
REPORT_PATH = "/home/andrea-zabala-c/Desktop/REPORTE_FORENSE_TAKEOUT_IOCS.md"

def analyze_takeout():
    print("Iniciando análisis forense de archivos ZIP en Google Takeout...")
    
    suspicious_ips = set()
    devices = set()
    
    zip_files = [f for f in os.listdir(TAKEOUT_DIR) if f.endswith('.zip')]
    
    for zip_name in zip_files:
        zip_path = os.path.join(TAKEOUT_DIR, zip_name)
        try:
            with zipfile.ZipFile(zip_path, 'r') as z:
                # Look for Access Log Activity csvs or device config htmls
                for file_info in z.infolist():
                    if "Access Log Activity" in file_info.filename and file_info.filename.endswith(".csv"):
                        print(f"Analizando {file_info.filename} en {zip_name}...")
                        with z.open(file_info) as f:
                            # Read CSV
                            reader = csv.reader(TextIOWrapper(f, 'utf-8'))
                            for row in reader:
                                # IPs are usually in one of the columns, let's just use regex on the whole row string
                                row_str = ",".join(row)
                                ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', row_str)
                                for ip in ips:
                                    suspicious_ips.add(ip)
                    
                    if "Android Device Configuration Service" in file_info.filename and file_info.filename.endswith(".html"):
                        print(f"Analizando {file_info.filename} en {zip_name}...")
                        with z.open(file_info) as f:
                            content = TextIOWrapper(f, 'utf-8').read()
                            # Extract device models
                            models = re.findall(r'Model:\s*([^<]+)<br/>', content)
                            for m in models:
                                devices.add(m)
        except zipfile.BadZipFile:
            print(f"Error: No se pudo leer {zip_name} (BadZipFile)")
        except Exception as e:
            print(f"Error procesando {zip_name}: {e}")

    # Write report
    with open(REPORT_PATH, "w") as f:
        f.write("# REPORTE FORENSE DE GOOGLE TAKEOUT (IoCs)\n\n")
        f.write("## 1. Dispositivos Android Detectados\n")
        if not devices:
            f.write("- No se encontraron configuraciones de dispositivo en los zips analizados.\n")
        else:
            for dev in devices:
                f.write(f"- {dev}\n")
                
        f.write("\n## 2. Direcciones IP Extraídas (Access Logs)\n")
        if not suspicious_ips:
            f.write("- No se encontraron IPs en los Access Logs de los zips analizados.\n")
        else:
            for ip in suspicious_ips:
                f.write(f"- {ip}\n")
                
    print(f"\nAnálisis completado. Reporte guardado en: {REPORT_PATH}")

if __name__ == "__main__":
    analyze_takeout()
