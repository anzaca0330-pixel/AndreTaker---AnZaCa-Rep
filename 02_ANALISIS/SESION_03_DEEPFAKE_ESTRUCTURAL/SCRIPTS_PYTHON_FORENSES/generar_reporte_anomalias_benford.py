import csv

archivo_preconteo = "/home/andrea-zabala-c/Desktop/reporte_preconteo (4).csv"
archivo_salida = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/anomalias_benford_amazonas.csv"

def aislar_anomalias_benford():
    mesas_finales = {}
    
    print("Aislando mesas con inyección matemática (Dígitos 8 y 9)...")
    
    # 1. Leer y filtrar el boletín final
    with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        for row in reader:
            if row['cod_departamento'] == '60':  # Amazonas
                mesa_key = f"{row['cod_municipio']}-{row['zona']}-{row['puesto']}-{row['num_mesa']}"
                boletin_actual = int(row['num_boletin'])
                
                if mesa_key not in mesas_finales or boletin_actual > mesas_finales[mesa_key]['boletin']:
                    mesas_finales[mesa_key] = {
                        'boletin': boletin_actual,
                        'cod_municipio': row['cod_municipio'],
                        'zona': row['zona'],
                        'puesto': row['puesto'],
                        'num_mesa': row['num_mesa'],
                        'votos_cepeda': str(row['Ivan Cepeda']).strip(),
                        'votos_espriella': str(row['Abelardo De la espriella']).strip()
                    }
                    
    # 2. Generar reporte de mesas anómalas
    total_anomalas = 0
    with open(archivo_salida, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cod_municipio', 'zona', 'puesto', 'num_mesa', 'votos_cepeda', 'votos_espriella', 'digito_inicial', 'tipo_anomalia'])
        
        for mesa_key, data in mesas_finales.items():
            votos_str = data['votos_cepeda']
            if votos_str and votos_str != '0':
                digito_inicial = votos_str[0]
                # Aislar las mesas que causan la desviación masiva en Benford (8 y 9)
                if digito_inicial in ['8', '9']:
                    writer.writerow([
                        data['cod_municipio'], 
                        data['zona'], 
                        data['puesto'], 
                        data['num_mesa'], 
                        data['votos_cepeda'],
                        data['votos_espriella'],
                        digito_inicial,
                        'RELLENO_ARTIFICIAL_BENFORD'
                    ])
                    total_anomalas += 1
                    
    print(f"Reporte generado con éxito en: {archivo_salida}")
    print(f"Total de mesas con evidencia de relleno artificial en Amazonas: {total_anomalas}")

if __name__ == "__main__":
    aislar_anomalias_benford()
