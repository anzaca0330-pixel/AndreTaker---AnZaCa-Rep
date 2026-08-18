import csv
import math
import sys

archivo_preconteo = "/home/andrea-zabala-c/Desktop/reporte_preconteo (4).csv"
archivo_salida = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/anomalias_benford_2BL_nacional_abelardo.csv"

def expected_2BL():
    """Calcula la probabilidad teórica del SEGUNDO dígito en la Ley de Benford (2BL)"""
    probs = {}
    for d in range(10):  # El segundo dígito va de 0 a 9
        prob = sum(math.log10(1 + 1 / (10 * k + d)) for k in range(1, 10))
        probs[str(d)] = prob * 100
    return probs

def auditoria_benford_2BL_nacional():
    # Ley de Benford teórica para el SEGUNDO dígito
    benford_teorico = expected_2BL()
    mesas_finales = {}
    
    print("Iniciando Auditoría Masiva Nacional (2BL - SEGUNDO DÍGITO Ley de Benford)...")
    print("Objetivo: Abelardo de la Espriella (Inmune al límite de 300 votantes por mesa)")
    
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
                    
    conteo_digitos = {str(d): 0 for d in range(10)}
    total_votos_analizados = 0
    total_anomalas = 0
    
    print("Calculando desviación matemática nacional (2BL)...")
    
    # 2. Generar reporte de mesas anómalas y calcular 2BL
    with open(archivo_salida, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cod_departamento', 'cod_municipio', 'zona', 'puesto', 'num_mesa', 'votos_espriella', 'segundo_digito', 'alerta'])
        
        for mesa_key, data in mesas_finales.items():
            votos_str = data['votos_espriella']
            # Para el segundo dígito, el número debe tener al menos 2 caracteres
            if votos_str and len(votos_str) >= 2 and votos_str[1] in conteo_digitos:
                segundo_digito = votos_str[1]
                conteo_digitos[segundo_digito] += 1
                total_votos_analizados += 1
                
                # Aislar mesas anómalas (Ajustaremos esto si hay un pico en el segundo dígito, ej: 0 o 9)
                # Por ahora solo exportamos las de segundo dígito '0' o '9' para revisarlas
                if segundo_digito in ['0', '9']:
                    writer.writerow([
                        data['cod_departamento'],
                        data['cod_municipio'], 
                        data['zona'], 
                        data['puesto'], 
                        data['num_mesa'], 
                        data['votos_espriella'],
                        segundo_digito,
                        'PICO_ANOMALO_2BL'
                    ])
                    total_anomalas += 1
                    
    if total_votos_analizados == 0:
        print("No se encontraron mesas para analizar a nivel nacional.")
        return
        
    print(f"\nTotal de mesas únicas procesadas (Solo números >= 10): {total_votos_analizados:,}")
    print("\n--- DESVIACIÓN NACIONAL SEGUNDO DÍGITO BENFORD (2BL) ---")
    print("Dígito | Observado (%) | Esperado (%) | Desviación")
    print("-" * 55)
    
    for d in range(10):
        digito = str(d)
        observado = (conteo_digitos[digito] / total_votos_analizados) * 100
        esperado = benford_teorico[digito]
        desviacion = observado - esperado 
        
        marcador = ""
        if abs(desviacion) > 2.0: 
            marcador = " <--- ANOMALÍA SEVERA"
            
        print(f"   {digito}   |    {observado:05.2f}%    |   {esperado:05.2f}%   |   {desviacion:+05.2f}%{marcador}")

if __name__ == "__main__":
    auditoria_benford_2BL_nacional()
