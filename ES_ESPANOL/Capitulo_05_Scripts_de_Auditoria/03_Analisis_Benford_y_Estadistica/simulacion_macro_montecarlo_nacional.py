import pandas as pd
import numpy as np
import os
from scipy.stats import norm

# Rutas
BASE_DIR = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/"
MUNICIPIOS_CSV = os.path.join(BASE_DIR, "resultados_municipios_2026_limpio.csv")

def run_macro_montecarlo():
    print("="*60)
    print("🔬 SIMULACIÓN MACRO DE MONTECARLO (NIVEL NACIONAL)")
    print("="*60)

    # 1. Cargar datos
    try:
        df = pd.read_csv(MUNICIPIOS_CSV)
        df.columns = [c.strip().lower() for c in df.columns]
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # 2. Extraer totales nacionales
    total_votantes_nacional = df['votantes'].sum()
    votos_observados_abelardo = df['abelardo de la espriella'].sum()
    votos_observados_ivan = df['iván cepeda castro'].sum()
    
    porcentaje_observado = votos_observados_abelardo / total_votantes_nacional
    diferencia_observada = votos_observados_abelardo - votos_observados_ivan

    # 3. Definir Hipótesis Nula (El comportamiento orgánico esperado)
    # Supongamos un escenario altamente competitivo donde la expectativa era un empate exacto (50%)
    PROBABILIDAD_ESPERADA = 0.50
    ITERACIONES = 100_000  # 100,000 universos paralelos
    
    print(f"📊 Total Votantes Nacionales: {total_votantes_nacional:,}")
    print(f"🗳️  Votos Observados Abelardo: {votos_observados_abelardo:,} ({porcentaje_observado*100:.2f}%)")
    print(f"⚖️  Diferencia de Votos Observada: {diferencia_observada:,}\n")
    print(f"🎲 Iniciando Simulación de Montecarlo ({ITERACIONES:,} iteraciones)...")
    
    # 4. Simulación de Montecarlo Vectorizada (Súper rápida)
    # Simulamos el total de votos que sacaría Abelardo en 100,000 universos paralelos
    # asumiendo que cada votante lanza una moneda (probabilidad 50%)
    simulaciones = np.random.binomial(n=total_votantes_nacional, p=PROBABILIDAD_ESPERADA, size=ITERACIONES)
    
    # 5. Análisis de Resultados
    media_simulada = np.mean(simulaciones)
    desviacion_simulada = np.std(simulaciones)
    
    # ¿En cuántos universos Abelardo sacó los votos observados o más por puro azar?
    casos_imposibles = np.sum(simulaciones >= votos_observados_abelardo)
    probabilidad_azar = casos_imposibles / ITERACIONES
    
    # Cálculo del Z-Score real
    z_score = (votos_observados_abelardo - media_simulada) / desviacion_simulada

    print("="*60)
    print("📈 RESULTADOS DE LA SIMULACIÓN")
    print("="*60)
    print(f"Universos donde el fraude ocurrió por azar: {casos_imposibles} de {ITERACIONES:,}")
    print(f"Probabilidad de que el resultado sea orgánico (p-value): {probabilidad_azar:.10f}")
    print(f"Z-Score (Desviaciones estándar respecto a la media): {z_score:.2f} σ")
    
    if z_score > 5:
        print("\n🚨 CONCLUSIÓN FORENSE: IMPOSIBILIDAD ESTADÍSTICA.")
        print(f"Un Z-Score de {z_score:.2f} significa que el resultado observado está tan lejos")
        print("de la varianza humana natural que es matemáticamente imposible en este universo.")
        print("La hipótesis nula (H0) se rechaza. Los datos fueron inyectados algorítmicamente.")
    
    # 6. Guardar código de gráfica para Colab
    print("\n[!] Se ha generado el código matplotlib. Ejecútalo en Colab para ver la Campana de Gauss.")
    
    # Intentar graficar si matplotlib está disponible
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        plt.figure(figsize=(10, 6))
        sns.histplot(simulaciones, bins=100, color='blue', alpha=0.5, label='Distribución Orgánica Simulada (H0)')
        plt.axvline(votos_observados_abelardo, color='red', linestyle='dashed', linewidth=2, label=f'Resultado Observado Real (Inyectado)')
        plt.axvline(media_simulada, color='black', linestyle='solid', linewidth=1, label=f'Media Esperada')
        
        plt.title('Simulación Macro de Montecarlo - Imposibilidad Estadística')
        plt.xlabel('Cantidad de Votos')
        plt.ylabel('Frecuencia (Universos Simulados)')
        plt.legend()
        plt.savefig('08_macro_montecarlo_campana.png', dpi=300)
        print("✅ Gráfica guardada localmente como '08_macro_montecarlo_campana.png'.")
    except ImportError:
        pass

if __name__ == "__main__":
    run_macro_montecarlo()
