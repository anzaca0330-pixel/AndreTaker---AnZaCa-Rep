#!/usr/bin/env python3
"""
Script para comprimir y subir secuencialmente los Departamentos de 1RA VUELTA, 2DA VUELTA y MAPEO DE VERSIONES (Junio 1-4) a Internet Archive.
"""

import os
import sys
import subprocess
from upload_to_internet_archive import upload_file_to_ia

def upload_all_rounds_and_departments(access_key, secret_key, item_identifier="colombia-e14-forensic-acervo-2026"):
    tmp_zip_dir = "/home/andrea-zabala-c/Desktop/ZIPS_DEPARTAMENTALES"
    os.makedirs(tmp_zip_dir, exist_ok=True)

    # 1. Procesar 1RA VUELTA - Muestras y Los Ángeles
    v1_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/DESENMASCARAMIENTO_CAPAS_OCULTAS"
    if os.path.exists(v1_dir):
        print("\n🔹 [1RA VUELTA] Procesando muestras de 1ª Vuelta...")
        zip_v1_name = "E14_RAW_PDFS_1RA_VUELTA_MUESTRAS_LOS_ANGELES.zip"
        zip_v1_path = os.path.join(tmp_zip_dir, zip_v1_name)
        try:
            subprocess.run(["zip", "-r", "-q", zip_v1_path, "."], cwd=v1_dir, check=True)
            print(f"✅ Comprimido 1ª Vuelta Muestras: {zip_v1_name} ({os.path.getsize(zip_v1_path)/(1024*1024):.2f} MB)")
            if upload_file_to_ia(zip_v1_path, item_identifier, access_key, secret_key, zip_v1_name):
                os.remove(zip_v1_path)
        except Exception as e:
            print(f"❌ Error procesando 1ª Vuelta Muestras: {e}")

    # 2. Procesar 1RA VUELTA - MAPEO DE VERSIONES (Junio 1, Junio 2, Junio 3, Junio 4)
    v1_versions_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_06_Archivos_Crudos_y_Respaldos/CARPETAS_VERSIONES_1RA_VUELTA"
    if os.path.exists(v1_versions_dir):
        print("\n🔹 [1RA VUELTA - MAPEO DE VERSIONES] Procesando historial de versiones (Junio 1, 2, 3 y 4)...")
        zip_ver_name = "E14_RAW_PDFS_1RA_VUELTA_MAPEO_VERSIONES_JUNIO_1_A_4.zip"
        zip_ver_path = os.path.join(tmp_zip_dir, zip_ver_name)
        try:
            subprocess.run(["zip", "-r", "-q", zip_ver_path, "."], cwd=v1_versions_dir, check=True)
            print(f"✅ Comprimido Mapeo de Versiones (Junio 1-4): {zip_ver_name} ({os.path.getsize(zip_ver_path)/(1024*1024):.2f} MB)")
            if upload_file_to_ia(zip_ver_path, item_identifier, access_key, secret_key, zip_ver_name):
                os.remove(zip_ver_path)
        except Exception as e:
            print(f"❌ Error procesando Mapeo de Versiones Junio 1-4: {e}")

    # 3. Procesar 2DA VUELTA (135 GB por Departamentos)
    v2_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf"
    if os.path.exists(v2_dir):
        dept_folders = [f for f in os.listdir(v2_dir) if os.path.isdir(os.path.join(v2_dir, f))]
        dept_folders.sort()
        print(f"\n🔹 [2DA VUELTA] Se encontraron {len(dept_folders)} departamentos de 2ª Vuelta.")

        for i, dept in enumerate(dept_folders, 1):
            dept_path = os.path.join(v2_dir, dept)
            zip_name = f"E14_RAW_PDFS_2DA_VUELTA_{dept.replace(' ', '_').upper()}.zip"
            zip_path = os.path.join(tmp_zip_dir, zip_name)

            print(f"\n📦 [{i}/{len(dept_folders)}] Comprimiendo 2ª Vuelta - Departamento: {dept}...")
            try:
                subprocess.run(["zip", "-r", "-q", zip_path, "."], cwd=dept_path, check=True)
                size_mb = os.path.getsize(zip_path)/(1024*1024)
                print(f"✅ Comprimido: {zip_name} ({size_mb:.2f} MB)")
                
                if upload_file_to_ia(zip_path, item_identifier, access_key, secret_key, zip_name):
                    os.remove(zip_path)
                    print(f"🗑️ Eliminado zip temporal local: {zip_name}")
            except Exception as e:
                print(f"❌ Error procesando {dept}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 upload_department_zips_to_ia.py <ia_access_key> <ia_secret_key>")
        sys.exit(1)
        
    acc = sys.argv[1]
    sec = sys.argv[2]
    
    upload_all_rounds_and_departments(acc, sec)
