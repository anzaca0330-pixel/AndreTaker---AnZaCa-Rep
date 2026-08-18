import csv
import re

archivo_corruptos = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/reporte_amazonas.csv"
archivo_resultados = "/media/andrea-zabala-c/D A T A1/resultados_municipios_2026_limpio.csv"

def analizar_corrupcion_vs_votos():
    print("Iniciando cruce de datos forenses...")
    
    patron = r"E14_PRE_(\d{2})_(\d{3})_"
    mpios_corruptos = set()
    total_actas_corruptas = 0
    
    # 1. Leer los corruptos
    with open(archivo_corruptos, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_actas_corruptas += 1
            match = re.search(patron, row['archivo_pdf'])
            if match:
                dpto, mpio = match.group(1), match.group(2)
                mpios_corruptos.add(f"{dpto}{mpio}")
                
    print(f"Total actas corruptas en Amazonas: {total_actas_corruptas} (100% del reporte)")
    print(f"Municipios afectados (códigos): {mpios_corruptos}")
    
    # 2. Leer resultados electorales
    votos_cepeda = 0
    votos_espriella = 0
    votos_validos = 0
    nulos = 0
    no_marcados = 0
    
    encontrados = False
    with open(archivo_resultados, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            codigo = str(row['codigo']).zfill(5)
            if codigo in mpios_corruptos:
                encontrados = True
                votos_cepeda += int(row['iván cepeda castro'] or 0)
                votos_espriella += int(row['abelardo de la espriella'] or 0)
                votos_validos += int(row['validos'] or 0)
                nulos += int(row['nulos'] or 0)
                no_marcados += int(row['no_marcados'] or 0)
                
    if not encontrados:
        print("Error: No se encontraron los municipios en el archivo de resultados.")
        return
        
    print("\n--- RESULTADOS ELECTORALES EN MUNICIPIOS 100% CORRUPTOS (XREF) ---")
    print(f"Total Votos Válidos: {votos_validos:,}")
    
    if votos_validos > 0:
        pct_cepeda = (votos_cepeda / votos_validos) * 100
        pct_espriella = (votos_espriella / votos_validos) * 100
    else:
        pct_cepeda = pct_espriella = 0
        
    print(f"Iván Cepeda Castro: {votos_cepeda:,} ({pct_cepeda:.2f}%)")
    print(f"Abelardo de la Espriella: {votos_espriella:,} ({pct_espriella:.2f}%)")
    print(f"Nulos: {nulos:,} | No Marcados: {no_marcados:,}")
    
    if votos_cepeda > votos_espriella:
        print("\n[ALERTA FORENSE]: Ganancia mayoritaria para CEPEDA en los recintos donde el 100% de las actas fueron inyectadas/modificadas (XREF).")
    elif votos_espriella > votos_cepeda:
        print("\n[ALERTA FORENSE]: Ganancia mayoritaria para DE LA ESPRIELLA en los recintos donde el 100% de las actas fueron inyectadas/modificadas (XREF).")

if __name__ == "__main__":
    analizar_corrupcion_vs_votos()
