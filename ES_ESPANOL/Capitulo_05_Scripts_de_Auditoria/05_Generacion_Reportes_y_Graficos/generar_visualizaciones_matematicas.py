import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def main():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_03_Peritajes_Forenses/REPORTE_XREF_DEEPFAKE.csv"
    output_dir = "/home/andrea-zabala-c/.gemini/antigravity-ide/brain/36ea2a85-f6fa-4890-a8f6-95edd5166126"
    
    depts = []
    mesas = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                diag = row.get('Diagnostico_DeepFake', '')
                if 'DEEPFAKE SINTÉTICO' in diag:
                    try:
                        d = int(row['departamento'])
                        m = int(row['mesa'].replace('Mesa_', ''))
                        depts.append(d)
                        mesas.append(m)
                    except ValueError:
                        continue
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if not mesas:
        print("No se encontraron datos.")
        sys.exit(1)

    # 1. SCATTER PLOT (Estructura de Bloques / Líneas Rectas)
    plt.figure(figsize=(12, 8))
    plt.style.use('dark_background')
    plt.scatter(depts, mesas, alpha=0.5, c='cyan', s=30, edgecolors='none')
    plt.title('Distribución Geométrica de la Botnet (Departamento vs Mesa)', fontsize=16, color='white')
    plt.xlabel('Código de Departamento', fontsize=12)
    plt.ylabel('Número de Mesa Inyectada', fontsize=12)
    plt.grid(True, alpha=0.2, color='gray')
    plt.savefig(f"{output_dir}/matriz_dispersion_deepfakes.png", dpi=300, bbox_inches='tight')
    plt.close()

    # 2. POLAR PLOT (Espiral de Módulo Matemático)
    plt.figure(figsize=(10, 10))
    plt.style.use('dark_background')
    ax = plt.subplot(111, projection='polar')
    
    # Convertimos el número de mesa en un ángulo y el departamento en radio
    angles = [m * (2 * np.pi / max(mesas)) for m in mesas]
    radii = depts
    
    ax.scatter(angles, radii, c='magenta', s=20, alpha=0.6, edgecolors='none')
    ax.set_title("Firma Radial del Algoritmo (Espiral de Inyección)", va='bottom', fontsize=16, color='white')
    ax.set_rticks([10, 20, 30, 40, 50, 60, 70])  # Departamentos
    ax.set_rlabel_position(-22.5)  
    ax.grid(True, alpha=0.3, color='gray')
    
    plt.savefig(f"{output_dir}/espiral_polar_deepfakes.png", dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✅ Gráficos geométricos renderizados y guardados en el directorio de artefactos.")

if __name__ == '__main__':
    main()
