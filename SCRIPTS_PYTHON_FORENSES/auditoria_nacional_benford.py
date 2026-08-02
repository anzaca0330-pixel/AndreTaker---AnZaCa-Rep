import csv
import math
import sys

archivo_preconteo = "/home/andrea-zabala-c/Desktop/reporte_preconteo (4).csv"
archivo_salida = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/anomalias_benford_nacional_abelardo.csv"

def auditoria_benford_nacional():
    # Ley de Benford teórica
    benford_teorico = {str(d): math.log10(1 + 1/d) * 100 for d in range(1, 10)}
    mesas_finales = {}
    
    print("Iniciando Auditoría Masiva Nacional (Ley de Benford)...")
    print("Objetivo: Abelardo de la Espriella (Ignorando Honeypot Amazonas Depto 60)")
    
    # 1. Leer y filtrar el boletín final
    try:
        with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            
            for row in reader:
                cod_dpto = row['cod_departamento']
                # IGNORAR AMAZONAS (EL CEBO)
                if cod_dpto == '60':
                    continue
                    
                mesa_key = f"{cod_dpto}-{row['cod_municipio']}-{row['zona']}-{row['puesto']}-{row['num_mesa']}"
                try:
                    boletin_actual = int(row['num_boletin'])
                except ValueError:
                    continue
                
                # Filtrar solo boletín final (el más reciente)
                if mesa_key not in mesas_finales or boletin_actual > mesas_finales[mesa_key]['boletin']:
                    mesas_finales[mesa_key] = {
                        'boletin': boletin_actual,
                        'cod_departamento': cod_dpto,
                        'cod_municipio': row['cod_municipio'],
                        'zona': row['zona'],
                        'puesto': row['puesto'],
                        'num_mesa': row['num_mesa'],
                        'votos_espriella': str(row['Abelardo De la espriella']).strip()
                    }
    except Exception as e:
        print(f"Error al leer el archivo de preconteo: {e}")
        sys.exit(1)
                    
    conteo_digitos = {str(d): 0 for d in range(1, 10)}
    total_votos_analizados = 0
    total_anomalas = 0
    
    print("Calculando desviación matemática nacional...")
    
    # 2. Generar reporte de mesas anómalas y calcular Benford
    with open(archivo_salida, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cod_departamento', 'cod_municipio', 'zona', 'puesto', 'num_mesa', 'votos_espriella', 'digito_inicial', 'alerta'])
        
        for mesa_key, data in mesas_finales.items():
            votos_str = data['votos_espriella']
            if votos_str and votos_str != '0' and votos_str[0] in conteo_digitos:
                digito_inicial = votos_str[0]
                conteo_digitos[digito_inicial] += 1
                total_votos_analizados += 1
                
                # Aislar mesas con inyección masiva (8 y 9)
                if digito_inicial in ['8', '9']:
                    writer.writerow([
                        data['cod_departamento'],
                        data['cod_municipio'], 
                        data['zona'], 
                        data['puesto'], 
                        data['num_mesa'], 
                        data['votos_espriella'],
                        digito_inicial,
                        'RELLENO_NACIONAL_BENFORD'
                    ])
                    total_anomalas += 1
                    
    if total_votos_analizados == 0:
        print("No se encontraron mesas para analizar a nivel nacional.")
        return
        
    print(f"\nTotal de mesas únicas procesadas (Excluyendo Amazonas): {total_votos_analizados:,}")
    print("\n--- DESVIACIÓN NACIONAL LEY DE BENFORD (Abelardo de la Espriella) ---")
    print("Dígito | Observado (%) | Esperado (%) | Desviación")
    print("-" * 55)
    
    alerta_roja = False
    for d in range(1, 10):
        digito = str(d)
        observado = (conteo_digitos[digito] / total_votos_analizados) * 100
        esperado = benford_teorico[digito]
        desviacion = observado - esperado # Mantener signo para ver si es inflación o supresión
        
        marcador = ""
        if abs(desviacion) > 2.0: # Umbral de alerta severa a nivel nacional
            alerta_roja = True
            marcador = " <--- ANOMALÍA"
            
        print(f"   {digito}   |    {observado:05.2f}%    |   {esperado:05.2f}%   |   {desviacion:+05.2f}%{marcador}")
        
    if alerta_roja:
        print(f"\n[ALERTA ESTADÍSTICA SEVERA]: Se aisló un volumen de {total_anomalas:,} mesas a nivel nacional con relleno artificial.")
        print(f"Las actas anómalas han sido guardadas en: {archivo_salida}")

if __name__ == "__main__":
    auditoria_benford_nacional()
