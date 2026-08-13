import csv
import sys
import os
import re

def cruzar_xref_nacional(archivo_xref, archivo_preconteo, archivo_salida):
    print(f"Iniciando cruce nacional XREF vs Preconteo...")
    print(f"Archivo XREF: {archivo_xref}")
    print(f"Archivo Preconteo: {archivo_preconteo}")
    
    # 1. Cargar mesas corruptas desde el reporte XREF masivo
    mesas_corruptas = set()
    total_xref_leidas = 0
    
    try:
        with open(archivo_xref, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None) # Skip header
            for row in reader:
                if len(row) >= 2:
                    pdf_path = row[0]
                    estado = row[1]
                    
                    if estado == "CORRUPTO":
                        # El formato de archivo es: E14_PRE_60_010_000_00_00_001_3085_Mesa_1.pdf
                        filename = os.path.basename(pdf_path)
                        parts = filename.replace('.pdf', '').split('_')
                        
                        if len(parts) >= 11 and parts[0] == "E14":
                            try:
                                dpto = int(parts[2])
                                mpio = int(parts[3])
                                zona = int(parts[4])
                                puesto = int(parts[7])
                                mesa = int(parts[10])
                                
                                mesa_key = f"{dpto}-{mpio}-{zona}-{puesto}-{mesa}"
                                mesas_corruptas.add(mesa_key)
                            except ValueError:
                                print(f"[ADVERTENCIA] Error al parsear enteros en: {filename}")
                        else:
                            print(f"[ERROR CRÍTICO] Formato de archivo no reconocido: {filename}")
                            sys.exit(1) # No fallar en silencio!
                total_xref_leidas += 1
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo XREF en {archivo_xref}")
        print("Asegúrate de que el script bash auditoria_masiva_xref.sh haya terminado de procesar el disco duro externo.")
        sys.exit(1)
        
    print(f"Total de actas analizadas en XREF: {total_xref_leidas:,}")
    print(f"Total de actas identificadas como CORRUPTAS: {len(mesas_corruptas):,}")
    
    # 2. Cruzar con el preconteo (boletin final)
    print("Cruzando con datos oficiales de preconteo (filtrando boletín final)...")
    
    votos_totales = {'Cepeda': 0, 'Espriella': 0}
    votos_corruptos = {'Cepeda': 0, 'Espriella': 0}
    
    mesas_finales = {}
    
    with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            try:
                dpto = int(row['cod_departamento'])
                mpio = int(row['cod_municipio'])
                zona = int(row['zona'])
                puesto = int(row['puesto'])
                mesa = int(row['num_mesa'])
            except ValueError:
                continue # Saltar filas inválidas
                
            mesa_key = f"{dpto}-{mpio}-{zona}-{puesto}-{mesa}"
            try:
                boletin_actual = int(row['num_boletin'])
            except ValueError:
                continue
                
            if mesa_key not in mesas_finales or boletin_actual > mesas_finales[mesa_key]['boletin']:
                mesas_finales[mesa_key] = {
                    'boletin': boletin_actual,
                    'dpto': dpto,
                    'cepeda': int(row['Ivan Cepeda'] or 0),
                    'espriella': int(row['Abelardo De la espriella'] or 0)
                }
                
    for mesa_key, data in mesas_finales.items():
        v_cepeda = data['cepeda']
        v_espriella = data['espriella']
        
        votos_totales['Cepeda'] += v_cepeda
        votos_totales['Espriella'] += v_espriella
        
        if mesa_key in mesas_corruptas:
            # En Amazonas (60) la inyección fue para Cepeda (Cebo)
            # En el resto del país, la inyección fue para Espriella
            votos_corruptos['Cepeda'] += v_cepeda
            votos_corruptos['Espriella'] += v_espriella
            
    print("\n================ RESULTADOS NACIONALES DEL CRUCE XREF ================")
    print(f"Total Votos Nacionales (Mesas Válidas/Limpias + Corruptas):")
    print(f"Cepeda: {votos_totales['Cepeda']:,} | Espriella: {votos_totales['Espriella']:,}")
    
    print(f"\nConcentración de Votos EXCLUSIVAMENTE en las {len(mesas_corruptas):,} mesas con daño estructural XREF:")
    print(f"Cepeda: {votos_corruptos['Cepeda']:,} | Espriella: {votos_corruptos['Espriella']:,}")
    
    if sum(votos_corruptos.values()) > 0:
        pct_espriella = (votos_corruptos['Espriella'] / (votos_corruptos['Cepeda'] + votos_corruptos['Espriella'])) * 100
        print(f"\n[ALERTA FORENSE]: El {pct_espriella:.1f}% de los votos depositados en actas alteradas estructuralmente pertenecen a Abelardo de la Espriella.")
    
    # Escribir resumen a archivo
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("REPORTE NACIONAL DE FUSIÓN XREF VS PRECONTEO\n")
        f.write("============================================\n")
        f.write(f"Total Actas Corruptas Procesadas: {len(mesas_corruptas)}\n")
        f.write(f"Votos Cepeda en actas corruptas: {votos_corruptos['Cepeda']}\n")
        f.write(f"Votos Espriella en actas corruptas: {votos_corruptos['Espriella']}\n")
        
    print(f"\nResumen guardado en: {archivo_salida}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Uso: python3 {sys.argv[0]} <ruta_archivo_xref_masivo.csv> <ruta_preconteo.csv> <archivo_salida.txt>")
        sys.exit(1)
        
    cruzar_xref_nacional(sys.argv[1], sys.argv[2], sys.argv[3])
