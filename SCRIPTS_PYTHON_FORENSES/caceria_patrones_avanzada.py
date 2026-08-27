import csv
import sys
from collections import defaultdict, Counter

archivo_preconteo = "/home/andrea-zabala-c/Desktop/EVIDENCIA_Y_DATOS/reporte_preconteo (4).csv"

def caceria_patrones():
    print("Iniciando cacería avanzada de patrones forenses...")
    
    mesas_finales = {}
    
    try:
        with open(archivo_preconteo, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                dpto = row['cod_departamento']
                if dpto == '60': # Ignorar Amazonas
                    continue
                
                mesa_key = f"{dpto}-{row['cod_municipio']}-{row['zona']}-{row['puesto']}-{row['num_mesa']}"
                try:
                    boletin = int(row['num_boletin'])
                except:
                    continue
                    
                if mesa_key not in mesas_finales or boletin > mesas_finales[mesa_key]['boletin']:
                    mesas_finales[mesa_key] = {
                        'boletin': boletin,
                        'dpto': dpto,
                        'mun': row['cod_municipio'],
                        'zona': row['zona'],
                        'puesto': row['puesto'],
                        'mesa': row['num_mesa'],
                        'blancos': int(row['Blancos']),
                        'nulos': int(row['Nulos']),
                        'cepeda': int(row['Ivan Cepeda']),
                        'abelardo': int(row['Abelardo De la espriella']),
                        'no_marcados': int(row['No Marcados'])
                    }
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # 1. BÚSQUEDA DE MESAS CLÓNICAS (Copy-Paste)
    # Agrupamos por los 5 valores exactos de votación dentro del mismo departamento
    firmas_votacion = defaultdict(list)
    
    # 2. PREFERENCIA DE ÚLTIMO DÍGITO (Sesgo humano al inventar números)
    ultimo_digito_abelardo = Counter()
    
    # 3. ZAPATEROS (Cepeda = 0)
    mesas_cepeda_cero = 0

    total_mesas = len(mesas_finales)

    for key, data in mesas_finales.items():
        # Firma para clones
        firma = f"{data['blancos']}-{data['nulos']}-{data['cepeda']}-{data['abelardo']}-{data['no_marcados']}"
        firmas_votacion[(data['dpto'], data['mun'], firma)].append(key)
        
        # Último dígito
        votos_abelardo = str(data['abelardo'])
        if len(votos_abelardo) > 0:
            ultimo_digito_abelardo[votos_abelardo[-1]] += 1
            
        # Zapateros
        if data['cepeda'] == 0 and data['abelardo'] > 0:
            mesas_cepeda_cero += 1

    print(f"Total de mesas procesadas: {total_mesas}")
    print("\n--- 1. BÚSQUEDA DE MESAS CLÓNICAS (Copy-Paste) ---")
    clones_encontrados = 0
    for (dpto, mun, firma), mesas in firmas_votacion.items():
        if len(mesas) >= 3: # Si 3 o más mesas tienen exactamente los mismos 5 números
            clones_encontrados += 1
    print(f"Patrones de clonación exacta detectados (>= 3 mesas idénticas): {clones_encontrados}")

    print("\n--- 2. SESGO HUMANO (Último Dígito) ---")
    print("Si el fraude fue manual/inventado, los humanos prefieren números terminados en 0 o 5 (Debería ser ~20%)")
    total_digitos = sum(ultimo_digito_abelardo.values())
    cero_y_cinco = ultimo_digito_abelardo['0'] + ultimo_digito_abelardo['5']
    if total_digitos > 0:
        pct = (cero_y_cinco / total_digitos) * 100
        print(f"Votos terminados en 0 o 5: {pct:.2f}% (Esperado: 20%)")
        if pct > 25:
            print("🚨 ALERTA: Fuerte sesgo humano detectado.")
        elif pct < 15:
            print("🚨 ALERTA: Evasión intencional de 0 y 5 detectada.")
        else:
            print("✅ Distribución orgánica (Sin sesgo humano evidente).")

    print("\n--- 3. MESAS 'ZAPATERO' (Oponente en Cero) ---")
    pct_zapateros = (mesas_cepeda_cero / total_mesas) * 100
    print(f"Mesas donde Iván Cepeda tiene 0 votos y Abelardo > 0: {mesas_cepeda_cero} ({pct_zapateros:.2f}%)")

if __name__ == "__main__":
    caceria_patrones()
