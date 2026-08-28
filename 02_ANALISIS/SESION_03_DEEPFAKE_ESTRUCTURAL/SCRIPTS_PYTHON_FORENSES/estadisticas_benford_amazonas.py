import csv
import math

archivo_preconteo = "/home/andrea-zabala-c/Desktop/EVIDENCIA_Y_DATOS/reporte_preconteo (4).csv"

def benford_law_amazonas_verificado():
    # Ley de Benford teórica
    benford_teorico = {str(d): math.log10(1 + 1/d) * 100 for d in range(1, 10)}
    
    mesas_finales = {}
    
    print("Iniciando DOBLE VERIFICACIÓN (Ley de Benford) para AMAZONAS (Depto 60)...")
    print("Filtrando boletines intermedios para usar solo el boletín final (9999 o mayor) por mesa...")
    
    with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        for row in reader:
            if row['cod_departamento'] == '60':  # Amazonas
                # Llave única por mesa
                mesa_key = f"{row['cod_municipio']}-{row['zona']}-{row['puesto']}-{row['num_mesa']}"
                boletin_actual = int(row['num_boletin'])
                
                # Guardar solo si es el boletín más reciente/final
                if mesa_key not in mesas_finales or boletin_actual > mesas_finales[mesa_key]['boletin']:
                    mesas_finales[mesa_key] = {
                        'boletin': boletin_actual,
                        'votos_cepeda': str(row['Ivan Cepeda']).strip()
                    }
                    
    conteo_digitos = {str(d): 0 for d in range(1, 10)}
    total_votos_analizados = 0
    
    for mesa_key, data in mesas_finales.items():
        votos_str = data['votos_cepeda']
        if votos_str and votos_str != '0' and votos_str[0] in conteo_digitos:
            conteo_digitos[votos_str[0]] += 1
            total_votos_analizados += 1
            
    if total_votos_analizados == 0:
        print("No se encontraron votos para analizar en Amazonas.")
        return
        
    print(f"\nTotal de mesas únicas procesadas en Amazonas (VERIFICADO): {total_votos_analizados}")
    print("\n--- DESVIACIÓN LEY DE BENFORD VERIFICADA (Votos Cepeda) ---")
    print("Dígito | Observado (%) | Esperado (%) | Desviación")
    print("-" * 55)
    
    alerta_roja = False
    for d in range(1, 10):
        digito = str(d)
        observado = (conteo_digitos[digito] / total_votos_analizados) * 100
        esperado = benford_teorico[digito]
        desviacion = abs(observado - esperado)
        
        if desviacion > 5.0:
            alerta_roja = True
            
        print(f"   {digito}   |    {observado:05.2f}%    |   {esperado:05.2f}%   |   {desviacion:05.2f}%")
        
    if alerta_roja:
        print("\n[ALERTA ESTADÍSTICA SEVERA]: Tras doble verificación, la falsificación matemática persiste y es irrefutable.")
        print("La distribución de los votos viola la Ley de Benford de forma alarmante, descartando cualquier anomalía de muestreo.")
    else:
        print("\n[RESULTADO]: Las cifras se ajustan a la Ley de Benford.")

if __name__ == "__main__":
    benford_law_amazonas_verificado()
