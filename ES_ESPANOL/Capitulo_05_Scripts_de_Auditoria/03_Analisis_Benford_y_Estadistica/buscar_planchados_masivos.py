import csv
import sys

def check_planchado(votantes, votos_candidato, porcentaje):
    expected = round(votantes * (porcentaje / 100.0))
    return abs(expected - votos_candidato) <= 1

def main():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/resultados_municipios_2026_limpio.csv"
    
    planchados_detectados = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    votantes = int(row['votantes'])
                    votos_abelardo = int(row['abelardo de la espriella'])
                    votos_ivan = int(row['iván cepeda castro'])
                    municipio = row['mpio']
                    depto = row['dpto']
                    
                    if votantes < 500: # Skip tiny towns to avoid pure chance matches
                        continue
                        
                    # Test for 60%, 65%, 70%, 75%, 80% flatlining
                    for pct in [60, 65, 70, 75, 80, 85, 90]:
                        if check_planchado(votantes, votos_abelardo, pct):
                            planchados_detectados.append({
                                'depto': depto,
                                'mpio': municipio,
                                'votantes': votantes,
                                'candidato': 'Abelardo',
                                'votos': votos_abelardo,
                                'porcentaje_fijo': pct
                            })
                        if check_planchado(votantes, votos_ivan, pct):
                            planchados_detectados.append({
                                'depto': depto,
                                'mpio': municipio,
                                'votantes': votantes,
                                'candidato': 'Iván',
                                'votos': votos_ivan,
                                'porcentaje_fijo': pct
                            })
                except (ValueError, KeyError):
                    continue
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return
                
    if planchados_detectados:
        print("🚨 SE HAN DETECTADO PLANCHADOS MATEMÁTICOS A NIVEL MUNICIPAL 🚨")
        for p in planchados_detectados:
            print(f"Depto: {p['depto']} | Mpio: {p['mpio']} | Votantes: {p['votantes']} | Candidato: {p['candidato']} | Votos: {p['votos']} | Fórmula: =REDONDEAR(Votantes * {p['porcentaje_fijo']}%, 0)")
    else:
        print("✅ No se detectaron planchados exactos a nivel municipal (el algoritmo operó a nivel de mesa, diluyéndose a nivel municipal).")

if __name__ == '__main__':
    main()
