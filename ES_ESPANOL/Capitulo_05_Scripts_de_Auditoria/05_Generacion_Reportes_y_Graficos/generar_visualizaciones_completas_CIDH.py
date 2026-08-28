import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configuración de estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Rutas centralizadas
BASE_DIR = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/"
MUNICIPIOS_CSV = os.path.join(BASE_DIR, "resultados_municipios_2026_limpio.csv")
XREF_CSV = os.path.join(BASE_DIR, "REPORTE_XREF_DEEPFAKE.csv")

def generar_graficos():
    print("Iniciando generación de gráficas forenses...")
    
    # 1. Cargar Datos
    try:
        df_muni = pd.read_csv(MUNICIPIOS_CSV)
        df_xref = pd.read_csv(XREF_CSV)
    except FileNotFoundError as e:
        print(f"Error cargando datos: {e}")
        return

    # Limpieza básica
    df_muni.columns = [c.strip().lower() for c in df_muni.columns]
    
    # GRAFICO 1: Distribución de Diferencia
    if 'abelardo de la espriella' in df_muni.columns and 'iván cepeda castro' in df_muni.columns:
        df_muni['diferencia'] = df_muni['abelardo de la espriella'] - df_muni['iván cepeda castro']
        plt.figure()
        sns.histplot(df_muni['diferencia'].dropna(), bins=100, kde=True, color='red', alpha=0.6)
        plt.axvline(0, color='black', linestyle='--', label='Empate')
        plt.axvline(df_muni['diferencia'].mean(), color='blue', linestyle='-', label=f'Media: {df_muni["diferencia"].mean():.0f}')
        plt.xlabel('Diferencia de Votos (Abelardo - Iván)')
        plt.title('Distribución de la Diferencia de Votos (Macro)')
        plt.legend()
        plt.savefig('01_distribucion_diferencia.png', dpi=300)
        plt.close()
        print("✅ Gráfico 1 generado.")

    # GRAFICO 2: Votantes vs Votos Abelardo (Buscando el Planchado)
    if 'votantes' in df_muni.columns and 'abelardo de la espriella' in df_muni.columns:
        plt.figure()
        sns.regplot(x='votantes', y='abelardo de la espriella', data=df_muni, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
        plt.title('Relación Votantes Totales vs Votos Abelardo')
        plt.savefig('02_scatter_planchado.png', dpi=300)
        plt.close()
        print("✅ Gráfico 2 generado.")

    # GRAFICO 3: Benford 2BL (Simulado de los datos limpios si existe columna)
    # Extraemos el segundo dígito de los votos
    df_muni['segundo_digito'] = df_muni['abelardo de la espriella'].astype(str).str.zfill(3).str[1].astype(int)
    observado = df_muni['segundo_digito'].value_counts(normalize=True).sort_index() * 100
    esperado = [10] * 10 # Esperado uniforme para 2BL
    
    plt.figure()
    x = np.arange(10)
    width = 0.35
    plt.bar(x - width/2, esperado, width, label='Esperado (Uniforme)', alpha=0.6, color='gray')
    plt.bar(x + width/2, observado.reindex(x, fill_value=0), width, label='Observado', alpha=0.8, color='red')
    plt.xlabel('Segundo Dígito')
    plt.ylabel('Frecuencia (%)')
    plt.title('Desviación Ley de Benford (2BL) - Votos Abelardo')
    plt.xticks(x)
    plt.legend()
    plt.savefig('03_benford_2bl.png', dpi=300)
    plt.close()
    print("✅ Gráfico 3 generado.")

    # GRAFICO 4: Top 10 Departamentos XREF
    if 'departamento' in df_xref.columns:
        top_deptos = df_xref['departamento'].value_counts().head(10)
        plt.figure()
        top_deptos.plot(kind='barh', color='darkred')
        plt.gca().invert_yaxis()
        plt.xlabel('Cantidad de Mesas con XREF Corrupto')
        plt.title('Focalización Geográfica de la Inyección Sintética')
        plt.savefig('04_top10_xref.png', dpi=300)
        plt.close()
        print("✅ Gráfico 4 generado.")

    # GRAFICO 7: Varianza Artificial Los Ángeles (Hardcoded based on the report)
    mesas_la = ['Mesa 1', 'Mesa 2', 'Mesa 3', 'Mesa 4', 'Mesa 5']
    votos_abelardo_la = [56, 56, 55, 60, 53] 
    
    plt.figure(figsize=(8, 5))
    plt.bar(mesas_la, votos_abelardo_la, color='darkorange')
    plt.axhline(56, color='black', linestyle='--', label='Media (56 votos, std=2.5)')
    plt.title('Anomalía de Varianza Baja: Consulado Los Ángeles (Planchado)')
    plt.ylabel('Votos Asignados a Abelardo')
    plt.legend()
    plt.savefig('07_varianza_los_angeles.png', dpi=300)
    plt.close()
    print("✅ Gráfico 7 generado.")

    print("\n🎉 Todas las gráficas han sido exportadas como .png en el directorio actual.")

if __name__ == "__main__":
    generar_graficos()
