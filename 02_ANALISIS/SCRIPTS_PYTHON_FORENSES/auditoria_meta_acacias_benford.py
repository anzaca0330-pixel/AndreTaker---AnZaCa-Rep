import csv
import math
import sys

archivo_preconteo = "/media/andrea-zabala-c/D A T A1/segundaVuelta/CONSULADOS_DATASET_Y_FUENTES_ORIGEN/reporte_preconteo (4).csv"

def expected_2BL():
    probs = {}
    for d in range(10):
        prob = sum(math.log10(1 + 1 / (10 * k + d)) for k in range(1, 10))
        probs[str(d)] = prob * 100
    return probs

def auditoria_benford_acacias():
    benford_teorico = expected_2BL()
    mesas_finales = {}
    
    print("Iniciando Auditoría (2BL - SEGUNDO DÍGITO) para META - ACACIAS (Depto 52, Mun 005)...")
    
    try:
        with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                # Filtrar estrictamente por Meta (52) y Acacias (005)
                if row['cod_departamento'] != '52' or row['cod_municipio'] != '005':
                    continue
                    
                mesa_key = f"{row['zona']}-{row['puesto']}-{row['num_mesa']}"
                try:
                    boletin_actual = int(row['num_boletin'])
                except ValueError:
                    continue
                
                if mesa_key not in mesas_finales or boletin_actual > mesas_finales[mesa_key]['boletin']:
                    mesas_finales[mesa_key] = {
                        'boletin': boletin_actual,
                        'votos_espriella': str(row['Abelardo De la espriella']).strip()
                    }
    except Exception as e:
        print(f"Error al leer el archivo de preconteo: {e}")
        sys.exit(1)
                    
    conteo_digitos = {str(d): 0 for d in range(10)}
    total_votos_analizados = 0
    
    for mesa_key, data in mesas_finales.items():
        votos_str = data['votos_espriella']
        if votos_str and len(votos_str) >= 2 and votos_str[1] in conteo_digitos:
            segundo_digito = votos_str[1]
            conteo_digitos[segundo_digito] += 1
            total_votos_analizados += 1
                    
    if total_votos_analizados == 0:
        print("No se encontraron mesas para analizar.")
        return
        
    print(f"\nTotal de mesas únicas procesadas en Acacias (Solo votos >= 10): {total_votos_analizados:,}")
    print("\n--- DESVIACIÓN META ACACIAS (2BL) ---")
    print("Dígito | Observado (%) | Esperado (%) | Desviación")
    print("-" * 55)
    
    for d in range(10):
        digito = str(d)
        observado = (conteo_digitos[digito] / total_votos_analizados) * 100
        esperado = benford_teorico[digito]
        desviacion = observado - esperado 
        
        marcador = ""
        if abs(desviacion) > 2.0: 
            marcador = " <--- ANOMALÍA"
            
        print(f"   {digito}   |    {observado:05.2f}%    |   {esperado:05.2f}%   |   {desviacion:+05.2f}%{marcador}")

if __name__ == "__main__":
    auditoria_benford_acacias()
