#!/usr/bin/env python3
"""
Forensic Toolkit - Wald-Wolfowitz Runs Test (Prueba de Rachas)
Detección Matemática de Generación Algorítmica vs Aleatoriedad Humana
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import argparse
import sys
import os

def wald_wolfowitz_test(data):
    """
    Ejecuta el test de rachas de Wald-Wolfowitz.
    Asume que la data es un array numpy de números.
    """
    median = np.median(data)
    
    # Excluir valores que son exactamente iguales a la mediana
    filtered_data = data[data != median]
    
    if len(filtered_data) == 0:
        return None, None, None, None, "Error: Varianza nula en la data."

    # Convertir a secuencia binaria (1 si es > mediana, 0 si es < mediana)
    binary_seq = (filtered_data > median).astype(int)
    
    n1 = np.sum(binary_seq)  # Cantidad de elementos sobre la mediana
    n2 = len(binary_seq) - n1 # Cantidad de elementos bajo la mediana
    n = n1 + n2
    
    if n < 2:
        return None, None, None, None, "Error: Insuficientes datos para la prueba."

    # Contar las rachas (runs)
    runs = 1
    for i in range(1, n):
        if binary_seq[i] != binary_seq[i-1]:
            runs += 1

    # Calcular expected runs y varianza
    expected_runs = ((2 * n1 * n2) / n) + 1
    variance = (2 * n1 * n2 * (2 * n1 * n2 - n)) / ((n ** 2) * (n - 1))
    
    if variance <= 0:
        return runs, expected_runs, 0, 1.0, "Secuencia idéntica."

    # Z-score y P-value
    z_score = (runs - expected_runs) / np.sqrt(variance)
    p_value = 2 * (1 - norm.cdf(abs(z_score))) # Two-tailed test

    return runs, expected_runs, z_score, p_value, binary_seq

def plot_runs(binary_seq, z_score, p_value, output_path):
    """
    Genera un gráfico visual mostrando la secuencia de rachas.
    """
    plt.figure(figsize=(12, 4))
    
    # Trazar puntos y líneas
    plt.step(range(len(binary_seq)), binary_seq, where='mid', color='#d62728', linewidth=2)
    plt.plot(range(len(binary_seq)), binary_seq, 'o', color='black', alpha=0.5)
    
    # Decoración de diseño forense
    plt.title('Wald-Wolfowitz Runs Test - Análisis de Aleatoriedad Documental', fontsize=14, pad=20)
    plt.xlabel('Índice Secuencial de Actas', fontsize=12)
    plt.ylabel('Señal Binaria (>Mediana vs <Mediana)', fontsize=12)
    plt.yticks([0, 1], ['Bajo Mediana (-)', 'Sobre Mediana (+)'])
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Añadir veredicto matemático en texto
    veredicto = "ALTERACIÓN ALGORÍTMICA DETECTADA" if p_value < 0.05 else "Variación Natural Humana"
    color_veredicto = 'red' if p_value < 0.05 else 'green'
    
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1)
    plt.annotate(f"Z-Score: {z_score:.2f}\nP-Value: {p_value:.6f}\nVeredicto: {veredicto}", 
                 xy=(0.02, 0.85), xycoords='axes fraction', 
                 fontsize=10, bbox=bbox_props, color=color_veredicto, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"[+] Gráfico forense de rachas guardado en: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Detector Forense Estadístico: Wald-Wolfowitz Runs Test")
    parser.add_argument('-i', '--input', required=True, help="Archivo CSV de entrada")
    parser.add_argument('-c', '--columna', required=True, help="Nombre de la columna numérica a auditar (ej. 'VOTOS_MESA')")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"[-] Error: No se encuentra el archivo {args.input}")
        sys.exit(1)

    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        print(f"[-] Error leyendo el CSV: {e}")
        sys.exit(1)

    if args.columna not in df.columns:
        print(f"[-] Error: La columna '{args.columna}' no existe. Columnas disponibles: {list(df.columns)}")
        sys.exit(1)

    # Limpieza básica
    data = pd.to_numeric(df[args.columna], errors='coerce').dropna().values
    
    print("\n" + "="*50)
    print("🔎 FORENSIC TOOLKIT: ANÁLISIS DE RACHAS (RUNS TEST)")
    print("="*50)
    print(f"[*] Analizando {len(data)} registros de la columna '{args.columna}'...")
    
    runs, expected, z, p, seq = wald_wolfowitz_test(data)
    
    if runs is None:
        print(f"[-] {seq}") # Mensaje de error
        sys.exit(1)

    print(f"[*] Rachas Observadas (R): {runs}")
    print(f"[*] Rachas Esperadas (E): {expected:.2f}")
    print(f"[*] Z-Score:              {z:.4f}")
    print(f"[*] P-Value:              {p:.8f}")
    
    print("-" * 50)
    if p < 0.05:
        print("[!] VEREDICTO: ANOMALÍA MATEMÁTICA DETECTADA (Rechazo H0)")
        print("[!] La secuencia de datos carece de entropía humana. Evidencia de generación algorítmica/artificial.")
    else:
        print("[+] VEREDICTO: Variación Aleatoria Natural.")
        print("[+] La secuencia se comporta dentro del caos estocástico esperado.")
    print("=" * 50 + "\n")

    # Generar gráfica
    output_png = os.path.splitext(args.input)[0] + "_runs_test_report.png"
    plot_runs(seq, z, p, output_png)

if __name__ == "__main__":
    main()
