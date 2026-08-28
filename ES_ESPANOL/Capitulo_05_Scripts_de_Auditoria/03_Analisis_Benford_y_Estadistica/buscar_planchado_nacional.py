import csv
import statistics
import sys
from collections import defaultdict

archivo_preconteo = "/home/andrea-zabala-c/Desktop/reporte_preconteo (4).csv"
archivo_salida = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_05_Scripts_de_Auditoria/anomalias_planchado_nacional.csv"

def buscar_planchados_nacionales():
    print("Iniciando cacería de 'Planchados' (Compresión de Varianza) a nivel nacional...")
    
    # Estructura: puestos[departamento-municipio-zona-puesto] = [votos_mesa1, votos_mesa2, ...]
    puestos = defaultdict(list)
    mesas_finales = {}
    
    try:
        with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                dpto = row['cod_departamento']
                if dpto == '60': # Ignorar el cebo de Amazonas
                    continue
                    
                mesa_key = f"{dpto}-{row['cod_municipio']}-{row['zona']}-{row['puesto']}-{row['num_mesa']}"
                puesto_key = f"Dpto:{dpto}-Mun:{row['cod_municipio']}-Zona:{row['zona']}-Puesto:{row['puesto']}"
                
                try:
                    boletin_actual = int(row['num_boletin'])
                    votos = int(row['Abelardo De la espriella'])
                except ValueError:
                    continue
                
                # Solo el boletín final
                if mesa_key not in mesas_finales or boletin_actual > mesas_finales[mesa_key]['boletin']:
                    mesas_finales[mesa_key] = {
                        'boletin': boletin_actual,
                        'puesto_key': puesto_key,
                        'votos': votos
                    }
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Agrupar por puesto
    for data in mesas_finales.values():
        puestos[data['puesto_key']].append(data['votos'])

    puestos_planchados = 0
    mesas_afectadas = 0
    
    with open(archivo_salida, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Puesto', 'Total_Mesas', 'Promedio_Votos', 'Desviacion_Estandar', 'Alerta'])
        
        for puesto, votos_list in puestos.items():
            if len(votos_list) >= 5: # Solo analizar puestos con 5 o más mesas para tener peso estadístico
                promedio = statistics.mean(votos_list)
                if promedio < 20: 
                    continue # Ignorar puestos donde nadie vota, es normal que la varianza sea baja
                    
                desviacion = statistics.stdev(votos_list)
                
                # CRITERIO DE FRAUDE (PLANCHADO): 
                # Si la desviación estándar es menor a 2.5 votos (como en Primera Vuelta)
                # significa que a todas las mesas les inyectaron exactamente el mismo número.
                if desviacion <= 2.5:
                    writer.writerow([puesto, len(votos_list), round(promedio, 2), round(desviacion, 2), 'PLANCHADO_DETECTADO'])
                    puestos_planchados += 1
                    mesas_afectadas += len(votos_list)
                    
                    if puestos_planchados <= 15: # Mostrar los primeros 15 en pantalla
                        print(f"🚨 PLANCHADO EN {puesto} | Mesas: {len(votos_list)} | Promedio: {promedio:.1f} | Desviación: {desviacion:.2f}")

    print(f"\n✅ Análisis completado.")
    print(f"Total de Puestos con patrón de 'Planchado' algorítmico: {puestos_planchados}")
    print(f"Total de Mesas afectadas por este patrón: {mesas_afectadas}")
    print(f"Reporte guardado en: {archivo_salida}")

if __name__ == "__main__":
    buscar_planchados_nacionales()
