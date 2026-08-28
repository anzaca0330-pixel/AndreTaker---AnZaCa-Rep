import csv
import sys
from collections import defaultdict

def main():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_03_Peritajes_Forenses/REPORTE_XREF_DEEPFAKE.csv"
    
    # department -> dict of mesa -> count
    dept_mesa_counts = defaultdict(lambda: defaultdict(int))
    total_deepfakes = 0

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                diag = row.get('Diagnostico_DeepFake', '')
                if 'DEEPFAKE SINTÉTICO' in diag:
                    dpto = row['departamento']
                    mesa = row['mesa'].replace('Mesa_', '')
                    dept_mesa_counts[dpto][mesa] += 1
                    total_deepfakes += 1
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    print(f"Total Deepfakes Detectados: {total_deepfakes}")
    print("-" * 50)
    
    for dpto in sorted(dept_mesa_counts.keys()):
        print(f"\nDEPARTAMENTO: {dpto}")
        
        # Sort mesas by integer value if possible, else string
        mesa_counts = dept_mesa_counts[dpto]
        
        def sort_key(k):
            try:
                return int(k)
            except ValueError:
                return float('inf')
                
        sorted_mesas = sorted(mesa_counts.keys(), key=sort_key)
        
        # Extract the pattern sequence
        sequence = []
        for mesa in sorted_mesas:
            count = mesa_counts[mesa]
            sequence.append(f"{mesa} (x{count})")
            
        print("  Patrón de Mesas Inyectadas: " + ", ".join(sequence))

if __name__ == '__main__':
    main()
