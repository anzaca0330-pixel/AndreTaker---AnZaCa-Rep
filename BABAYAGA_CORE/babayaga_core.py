#!/usr/bin/env python3
# =========================================================
# babayaga_core.py — AndreTaker / BabaYaga Core Engine v2.0
# =========================================================
# "She is the reason monsters hide." — Implacable Forensic Engine
# =========================================================

import os
import sys
import csv
import argparse
import subprocess
from datetime import datetime, timezone

# Asegurar importabilidad de babayaga
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from babayaga.core.forensics.xref import XrefAnalyzer
from babayaga.core.forensics.raster import RasterAnalyzer
from babayaga.core.custody import CustodyTracker
from babayaga.api import database
from babayaga.api.cloud import CloudSync

print("🪓 BabaYaga Core v2.0 [Ecosistema Forense de Alta Rigurosidad]")
print("🔥 La verdad binaria se abre paso bajo estándares ISO 27037/27042/27043.\n")

def comando_init():
    database.init_db()
    print("✅ Inicialización completada.")

def comando_scan(ruta, caso_nombre, sync=False, lock=False):
    # Inicializar db si no existe
    database.init_db()
    
    # Obtener el bucket si la sincronización está activa
    bucket_name = None
    if sync:
        bucket_name = os.environ.get("BABAYAGA_BUCKET")
        if not bucket_name:
            print("⚠️ ADVERTENCIA: La bandera --sync está activa, pero no se ha definido la variable de entorno BABAYAGA_BUCKET.")
            print("👉 Sincronización con la nube omitida.")
            sync = False

    # Registrar/obtener caso
    caso_id = database.registrar_caso(caso_nombre, f"Auditoría de actas en: {ruta}")
    if not caso_id:
        print("❌ Error al registrar o recuperar el caso en la base de datos.")
        return

    # Verificar si es un archivo o una carpeta
    if not os.path.exists(ruta):
        print(f"❌ La ruta especificada no existe: {ruta}")
        return

    archivos_pdf = []
    if os.path.isdir(ruta):
        for root, _, files in os.walk(ruta):
            for f in files:
                if f.lower().endswith('.pdf'):
                    archivos_pdf.append(os.path.join(root, f))
    else:
        if ruta.lower().endswith('.pdf'):
            archivos_pdf.append(ruta)

    archivos_pdf.sort()
    total = len(archivos_pdf)
    if total == 0:
        print("⚠️ No se encontraron archivos PDF para analizar.")
        return

    print(f"🔎 Iniciando escaneo de {total} archivo(s) para el caso '{caso_nombre}'...")
    
    for idx, pdf_path in enumerate(archivos_pdf, 1):
        nom = os.path.basename(pdf_path)
        print(f"[{idx}/{total}] Procesando: {nom}...")
        
        # Capa 1: Integridad Criptográfica (SHA-256)
        sha256 = CustodyTracker.calcular_sha256(pdf_path)
        
        # Registrar evidencia en base de datos
        ev_id = database.registrar_evidencia(caso_id, nom, os.path.abspath(pdf_path), sha256)
        if not ev_id:
            continue
            
        # Correr análisis
        xref_res = XrefAnalyzer.analizar_estructura(pdf_path)
        raster_res = RasterAnalyzer.analizar_imagenes(pdf_path)
        vec_res = RasterAnalyzer.detectar_elementos_vectoriales(pdf_path)
        
        discrepancia_xref = xref_res.get('XREF_discrepancia', False)
        xref_detalle = xref_res.get('detalle', '')
        
        imagenes = raster_res.get('imagenes', [])
        cant_imagenes = len(imagenes)
        varianza_cero = any(im.get('varianza_cero', False) for im in imagenes)
        
        contiene_vectores = vec_res.get('contiene_vectores', False)
        score_vectorial = vec_res.get('score_vectorial', 0)
        
        # Registrar veredicto final en la base de datos
        database.registrar_analisis_resultado(
            evidencia_id=ev_id,
            exit_code=xref_res.get('exit_code', -1),
            discrepancia_xref=discrepancia_xref,
            xref_detalle=xref_detalle,
            cant_imagenes=cant_imagenes,
            varianza_cero_detectada=varianza_cero,
            contiene_vectores=contiene_vectores,
            score_vectorial=score_vectorial
        )
        
        # Sincronización GCS opcional
        if sync and bucket_name:
            res_sync = CloudSync.subir_a_nube(pdf_path, bucket_name)
            if res_sync.get("status") == "success":
                print(f"  [Nube] Sincronización exitosa ({res_sync.get('metodo')}) -> {res_sync.get('destination')}")
                database.registrar_custody_log(ev_id, "CLOUD_SYNC", f"Evidencia exfiltrada a: {res_sync.get('destination')}")
            else:
                print(f"  [!] Fallo en sincronización de nube: {res_sync.get('message')}")
                database.registrar_custody_log(ev_id, "CLOUD_FAIL", f"Fallo al subir a la nube: {res_sync.get('message')}")
                
        # Bloqueo físico de inmutabilidad (chattr +i) opcional
        if lock:
            try:
                res_lock = subprocess.run(['sudo', 'chattr', '+i', pdf_path], capture_output=True)
                if res_lock.returncode == 0:
                    print(f"  [Lock] Bóveda inmutable activada para {nom} (chattr +i).")
                    database.registrar_custody_log(ev_id, "LOCK_IMMUTABLE", "Archivo marcado como inmutable en disco (+i).")
                else:
                    err_msg = res_lock.stderr.decode().strip()
                    print(f"  [!] No se pudo aplicar bloqueo de inmutabilidad: {err_msg}")
            except Exception as e:
                print(f"  [!] Fallo al invocar chattr: {str(e)}")
        
    # Sincronizar archivo de base de datos de custodia al final del lote
    if sync and bucket_name:
        print("\n☁️ Sincronizando base de datos de custodia relacional...")
        res_db = CloudSync.sincronizar_caso(database.DB_PATH, bucket_name)
        if res_db.get("status") == "success":
            print(f"  [Nube] Custodia base de datos asegurada -> {res_db.get('destination')}")
        else:
            print(f"  [!] Fallo al sincronizar base de datos: {res_db.get('message')}")

    print(f"\n🎉 Escaneo completado. Evidencias registradas en 'babayaga_custody.db'.")

def comando_status(caso_nombre):
    conn = database.get_connection()
    cursor = conn.cursor()
    
    # Obtener ID del caso
    cursor.execute("SELECT id, fecha_creacion FROM casos WHERE nombre = ?", (caso_nombre,))
    row = cursor.fetchone()
    if not row:
        print(f"❌ El caso '{caso_nombre}' no existe en la base de datos.")
        conn.close()
        return
        
    caso_id = row['id']
    fecha_creacion = row['fecha_creacion']
    
    resumen = database.obtener_resumen_caso(caso_id)
    if not resumen:
        conn.close()
        return
        
    print(f"====================================================")
    print(f"ESTADO DEL CASO: {caso_nombre}")
    print(f"Fecha de Creación: {fecha_creacion}")
    print(f"====================================================")
    print(f"  Total de archivos auditados: {resumen['total_archivos']}")
    print(f"  Total con anomalías detectadas: {resumen['total_anomalos']} ({resumen['anomalias_porcentaje']:.2f}%)")
    
    # Mostrar desglose por anomalía
    cursor.execute("""
        SELECT count(*) as count FROM analisis_resultados ar
        JOIN evidencias e ON ar.evidencia_id = e.id
        WHERE e.caso_id = ? AND ar.discrepancia_xref = 1
    """, (caso_id,))
    xref_count = cursor.fetchone()['count']
    
    cursor.execute("""
        SELECT count(*) as count FROM analisis_resultados ar
        JOIN evidencias e ON ar.evidencia_id = e.id
        WHERE e.caso_id = ? AND ar.varianza_cero_detectada = 1
    """, (caso_id,))
    var_count = cursor.fetchone()['count']
    
    print(f"  ├─ Discrepancias XREF (Estructura): {xref_count}")
    print(f"  └─ Imágenes con Varianza Cero (Std = 0): {var_count}")
    
    conn.close()

def comando_export(caso_nombre, tipo_formato):
    conn = database.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM casos WHERE nombre = ?", (caso_nombre,))
    row = cursor.fetchone()
    if not row:
        print(f"❌ El caso '{caso_nombre}' no existe.")
        conn.close()
        return
    caso_id = row['id']
    
    # Query de todas las evidencias y resultados
    cursor.execute("""
        SELECT e.nombre_archivo, e.sha256_original, e.estado_custodia,
               ar.exit_code, ar.discrepancia_xref, ar.xref_detalle,
               ar.cant_imagenes, ar.varianza_cero_detectada, ar.contiene_vectores, ar.score_vectorial
        FROM evidencias e
        LEFT JOIN analisis_resultados ar ON ar.evidencia_id = e.id
        WHERE e.caso_id = ?
    """, (caso_id,))
    rows = cursor.fetchall()
    
    if not rows:
        print("⚠️ No hay evidencias registradas en este caso.")
        conn.close()
        return
        
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    
    if tipo_formato == 'csv':
        out_file = 'matriz_custodia_babayaga.csv'
        with open(out_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Nombre_Archivo', 'SHA256', 'Estado_Custodia', 'QPDF_Exit', 'Discrepancia_XREF', 'Detalle_XREF', 'Cant_Imgs', 'Varianza_Cero', 'Vectores', 'Score_Vectorial'])
            for r in rows:
                writer.writerow([
                    r['nombre_archivo'], r['sha256_original'], r['estado_custodia'],
                    r['exit_code'], r['discrepancia_xref'], r['xref_detalle'],
                    r['cant_imagenes'], r['varianza_cero_detectada'], r['contiene_vectores'], r['score_vectorial']
                ])
        print(f"✅ Matriz exportada exitosamente a: {out_file}")
        
    elif tipo_formato == 'md':
        out_file = 'informe_custodia_babayaga.md'
        total = len(rows)
        anomalos = sum(1 for r in rows if r['discrepancia_xref'] or r['varianza_cero_detectada'])
        
        report = f"""# 📜 INFORME DE CUSTODIA Y AUDITORÍA DE CASO FORENSE
### Caso: {caso_nombre} | Generado el: {fecha_utc}

---

## 📊 RESUMEN EJECUTIVO
*   **Total de evidencias auditadas:** {total}
*   **Total de evidencias con anomalías:** {anomalos} ({anomalos/total*100:.2f}%)
*   **Estado de la Bóveda:** {"⚠️ RIESGO / ANOMALÍAS DETECTADAS" if anomalos > 0 else "✅ INTEGRIDAD CONFIRMADA"}

---

## 🔍 DETALLE DE EVIDENCIAS EN CUSTODIA
| Archivo | SHA-256 | Custodia | XREF | Varianza 0 | Vectores |
| :--- | :--- | :--- | :---: | :---: | :---: |
"""
        for r in rows:
            report += f"| {r['nombre_archivo']} | `{r['sha256_original'][:16]}...` | {r['estado_custodia']} | {'⚠️' if r['discrepancia_xref'] else '✅'} | {'⚠️' if r['varianza_cero_detectada'] else '✅'} | {'Si' if r['contiene_vectores'] else 'No'} |\n"
            
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ Informe Markdown exportado exitosamente a: {out_file}")
        
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='BabaYaga Core — CLI de Auditoría Forense y Custodia Criptográfica')
    subparsers = parser.add_subparsers(dest='command', required=True, help='Subcomando a ejecutar')
    
    # Subcomando: init
    subparsers.add_parser('init', help='Inicializa la base de datos de custodia SQLite')
    
    # Subcomando: scan
    scan_parser = subparsers.add_parser('scan', help='Analiza archivos PDF y los registra en custodia')
    scan_parser.add_argument('--ruta', required=True, help='Ruta al archivo PDF o directorio de lote')
    scan_parser.add_argument('--caso', default='Caso General E14', help='Nombre del caso de la investigación')
    scan_parser.add_argument('--sync', action='store_true', help='Sincronizar evidencias y base de datos con GCS en la nube')
    scan_parser.add_argument('--lock', action='store_true', help='Hacer que las evidencias locales sean inmutables (chattr +i) contra borrados')
    
    # Subcomando: status
    status_parser = subparsers.add_parser('status', help='Muestra el estado de auditoría de un caso')
    status_parser.add_argument('--caso', default='Caso General E14', help='Nombre del caso')
    
    # Subcomando: export
    export_parser = subparsers.add_parser('export', help='Exporta la matriz de custodia y resultados')
    export_parser.add_argument('--caso', default='Caso General E14', help='Nombre del caso')
    export_parser.add_argument('--tipo', choices=['md', 'csv'], default='md', help='Formato de exportación')
    
    # Subcomando: auto-sync-drive
    drive_parser = subparsers.add_parser('auto-sync-drive', help='Escanea e indexa automáticamente un disco extraíble conectado manteniendo la cronología')
    drive_parser.add_argument('--ruta', required=True, help='Ruta del disco montado (ej: /media/andrea-zabala-c/DISCO_BACKUP)')

    # Subcomando: ai-prompt
    subparsers.add_parser('ai-prompt', help='Muestra el System Prompt y la configuración del modelo de IA local (Ollama / AndreTaker)')
    
    args = parser.parse_args()
    
    if args.command == 'init':
        comando_init()
    elif args.command == 'scan':
        comando_scan(args.ruta, args.caso, args.sync, args.lock)
    elif args.command == 'status':
        comando_status(args.caso)
    elif args.command == 'export':
        comando_export(args.caso, args.tipo)
    elif args.command == 'auto-sync-drive':
        print(f"📡 ESCANEANDO E INDEXANDO DISCO EXTRAÍBLE EN: {args.ruta}")
        print("🔒 Sellando hashes SHA-256 y concatenando al Registro Inmutable de Cronología...")
        comando_scan(args.ruta, 'Respaldo Disco Extraíble', sync=False, lock=True)
    elif args.command == 'ai-prompt':
        from babayaga.core.intelligence import system_prompt
        print(system_prompt.get_system_prompt())

if __name__ == "__main__":
    main()
