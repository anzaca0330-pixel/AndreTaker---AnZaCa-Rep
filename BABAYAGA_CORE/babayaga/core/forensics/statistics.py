import math
from typing import List

class BenfordAnalyzer:
    @staticmethod
    def obtener_segundo_digito(valor: float) -> int:
        """Extrae el segundo dígito significativo de un número."""
        try:
            val_str = str(abs(valor)).replace('.', '').lstrip('0')
            if len(val_str) >= 2:
                return int(val_str[1])
            return -1
        except Exception:
            return -1

    @staticmethod
    def analizar_mebane_2bl(valores: List[float]) -> dict:
        """
        Aplica la ley del segundo dígito de Mebane (2BL) a un conjunto de números.
        Calcula la distribución empírica frente a la teórica de Benford y devuelve métricas de desviación.
        """
        # Distribución teórica de Benford para el segundo dígito (0-9)
        teorica = {
            0: 0.1197, 1: 0.1139, 2: 0.1088, 3: 0.1043, 4: 0.1003,
            5: 0.0967, 6: 0.0934, 7: 0.0904, 8: 0.0876, 9: 0.0850
        }
        
        digitos = [BenfordAnalyzer.obtener_segundo_digito(v) for v in valores]
        digitos_validos = [d for d in digitos if d >= 0]
        total = len(digitos_validos)
        
        if total < 10:
            return {
                'conteo_total': total,
                'suficiente_data': False,
                'desviacion_chi2': 0.0,
                'anomalo': False
            }
            
        frecuencias = {i: 0 for i in range(10)}
        for d in digitos_validos:
            frecuencias[d] += 1
            
        dist_empirica = {i: frecuencias[i] / total for i in range(10)}
        
        # Cálculo de Chi-Cuadrado de bondad de ajuste
        chi2 = 0.0
        for i in range(10):
            esperado = teorica[i] * total
            observado = frecuencias[i]
            chi2 += ((observado - esperado) ** 2) / esperado
            
        # Umbral crítico aproximado para 9 grados de libertad al 95% de confianza (16.92)
        es_anomalo = chi2 > 16.92
        
        return {
            'conteo_total': total,
            'suficiente_data': True,
            'frecuencias': frecuencias,
            'distribucion_empirica': dist_empirica,
            'distribucion_teorica': teorica,
            'desviacion_chi2': round(chi2, 4),
            'anomalo': es_anomalo
        }
