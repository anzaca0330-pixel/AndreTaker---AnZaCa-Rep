import csv
import sys
from collections import Counter, defaultdict

def main():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_03_Peritajes_Forenses/REPORTE_XREF_DEEPFAKE.csv"
    
    # Trackers
    total_deepfakes = 0
    dept_counter = Counter()
    mun_counter = Counter()
    zona_counter = Counter()
    puesto_counter = Counter()
    
    # Estructura: dpto -> mun -> list of mesas
    dpto_mun_mesas = defaultdict(lambda: defaultdict(list))

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                diag = row.get('Diagnostico_DeepFake', '')
                if 'DEEPFAKE SINTÉTICO' in diag:
                    total_deepfakes += 1
                    dpto = row['departamento']
                    mun = row['municipio']
                    zona = row['zona']
                    puesto = row['puesto']
                    mesa = row['mesa'].replace('Mesa_', '')
                    
                    dept_counter[dpto] += 1
                    mun_counter[f"Dpt:{dpto}-Mun:{mun}"] += 1
                    zona_counter[f"Dpt:{dpto}-Mun:{mun}-Zona:{zona}"] += 1
                    puesto_counter[f"Dpt:{dpto}-Mun:{mun}-Zona:{zona}-Puesto:{puesto}"] += 1
                    
                    dpto_mun_mesas[dpto][mun].append(mesa)
                    
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    print(f"=========================================================")
    print(f"🔍 ANÁLISIS FORENSE PROFUNDO: PATRONES DE DEEPFAKE (XREF)")
    print(f"=========================================================\n")
    print(f"Total de Actas XREF Corruptas Encontradas: {total_deepfakes}\n")

    print("--- 1. TOP 5 DEPARTAMENTOS MÁS ATACADOS ---")
    for d, c in dept_counter.most_common(5):
        print(f"  Departamento {d}: {c} inyecciones ({(c/total_deepfakes)*100:.1f}%)")

    print("\n--- 2. TOP 10 MUNICIPIOS (EPICENTROS DEL FRAUDE) ---")
    for m, c in mun_counter.most_common(10):
        print(f"  {m}: {c} inyecciones")

    print("\n--- 3. TOP 5 PUESTOS DE VOTACIÓN MÁS SATURADOS ---")
    for p, c in puesto_counter.most_common(5):
        print(f"  Puesto {p}: {c} inyecciones")

    print("\n--- 4. CLUSTERS DE BOTNET POR MUNICIPIO (Secuencias Numéricas) ---")
    # Only show a few to avoid terminal overload
    top_muns = [x[0] for x in mun_counter.most_common(10)]
    for dpto in dpto_mun_mesas:
        for mun in dpto_mun_mesas[dpto]:
            full_mun = f"Dpt:{dpto}-Mun:{mun}"
            if full_mun in top_muns:
                mesas = dpto_mun_mesas[dpto][mun]
                
                # Sort numerically
                def sort_k(k):
                    try: return int(k)
                    except: return 999
                
                mesas_sorted = sorted(set(mesas), key=sort_k)
                # Count frequencies
                c = Counter(mesas)
                seq = ", ".join([f"{m}(x{c[m]})" for m in mesas_sorted])
                print(f"  > {full_mun}: {seq}")

if __name__ == '__main__':
    main()
