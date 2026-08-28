import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurar estilo
sns.set_theme(style="whitegrid")

def plot_benford():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/anomalias_benford_2BL_nacional_abelardo.csv"
    df = pd.read_csv(csv_file)
    
    # Probabilidades teóricas para el 2do dígito (0 a 9)
    benford_probs = [0.11968, 0.11389, 0.10882, 0.10433, 0.10031, 0.09668, 0.09337, 0.09035, 0.08757, 0.08500]
    
    # Calcular frecuencias reales
    counts = df['segundo_digito'].value_counts().sort_index()
    total = counts.sum()
    freqs = (counts / total).reindex(range(10), fill_value=0).values
    
    plt.figure(figsize=(10, 6))
    x = np.arange(10)
    
    plt.bar(x - 0.2, freqs * 100, width=0.4, label='Frecuencia Observada (Anómala)', color='salmon', edgecolor='black')
    plt.bar(x + 0.2, np.array(benford_probs) * 100, width=0.4, label='Distribución Benford (Teórica)', color='lightblue', edgecolor='black')
    
    plt.title("Análisis 2BL: Anomalía Extrema en Segundo Dígito", fontsize=14, fontweight='bold')
    plt.xlabel("Segundo Dígito (0-9)", fontsize=12)
    plt.ylabel("Frecuencia Relativa (%)", fontsize=12)
    plt.xticks(x)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig("/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/real_benford_histogram.png", dpi=300)
    plt.close()

def plot_variance():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/ESTUDIO_ESTADISTICO_NACIONAL.csv"
    df = pd.read_csv(csv_file)
    
    # Filtramos para quitar NaNs o varianzas negativas por error
    df = df[df['var_espriella'].notna() & (df['var_espriella'] >= 0)]
    
    plt.figure(figsize=(10, 6))
    
    # Graficamos cantidad de mesas vs Varianza
    # Coloreamos los puntos sospechosos (varianza colapsada)
    anomalous = df['var_espriella'] < 100
    
    plt.scatter(df.loc[~anomalous, 'mesas'], df.loc[~anomalous, 'var_espriella'], 
                alpha=0.6, label='Varianza Natural', color='blue', edgecolor='white')
    
    plt.scatter(df.loc[anomalous, 'mesas'], df.loc[anomalous, 'var_espriella'], 
                alpha=0.9, label='Varianza Colapsada (Planchado)', color='red', edgecolor='black', s=80)
    
    plt.title("ANOVA / Dispersión: Colapso de Varianza Nacional", fontsize=14, fontweight='bold')
    plt.xlabel("Cantidad de Mesas por Clúster Departamental", fontsize=12)
    plt.ylabel("Varianza de Votos Asignados", fontsize=12)
    
    plt.axhline(y=6.25, color='darkred', linestyle='--', linewidth=2, label='Umbral Fijo Anómalo (Std=2.5)')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig("/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/real_variance_scatter.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_benford()
    plot_variance()
    print("Gráficas reales generadas exitosamente.")
