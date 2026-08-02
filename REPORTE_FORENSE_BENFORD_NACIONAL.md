# REPORTE PERICIAL FORENSE: ANOMALÍA ESTADÍSTICA LEY DE BENFORD (SEGUNDA VUELTA)

**Fecha del Hallazgo:** 1 de Agosto de 2026
**Perito Investigador:** Ing. Andrea Zabala
**Expediente Referencia CIDH:** IACHR - 0000113728
**Alcance:** Elecciones Presidenciales Colombia 2026 (Segunda Vuelta)

---

## 1. INTRODUCCIÓN Y METODOLOGÍA
El presente documento constituye el reporte técnico pericial sobre el análisis de distribución de dígitos de primer orden (Ley de Benford) aplicado a los resultados del preconteo nacional de la Segunda Vuelta Presidencial (Boletín final 9999). 

La metodología empleada consiste en extraer el primer dígito significativo de los votos obtenidos por el candidato Abelardo de la Espriella en las 121,147 mesas a nivel nacional (excluyendo el Departamento del Amazonas, catalogado previamente como "cebo estadístico" o *Honeypot* de inyección contraria).

## 2. HERRAMIENTAS Y SCRIPTS UTILIZADOS
- **Lenguaje:** Python 3.10+
- **Librerías Nativas:** `csv`, `math`
- **Script Original:** `auditoria_nacional_benford.py`
- **Hash SHA-256 del Script:** (Se anexará en el repositorio de custodia)
- **Ruta de Ejecución Local:** `/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/`

## 3. RESULTADOS DEL ANÁLISIS

La Ley de Benford establece que en sistemas no intervenidos, el dígito 1 debe aparecer como primer dígito en aproximadamente el 30.1% de los casos. Los hallazgos para el candidato De la Espriella son matemáticamente anómalos:

| Dígito | Observado (%) | Esperado (%) | Desviación Absoluta | Estado Pericial |
| :---: | :---: | :---: | :---: | :--- |
| **1** | **42.90%** | **30.10%** | **+12.80%** | 🔴 **ANOMALÍA SEVERA (Inflación artificial)** |
| 2 | 13.18% | 17.61% | -4.43% | 🟡 Supresión secundaria |
| 3 | 05.34% | 12.49% | -7.16% | 🟡 Supresión secundaria |
| 4 | 06.13% | 09.69% | -3.56% | 🟡 Supresión secundaria |
| 5 | 06.58% | 07.92% | -1.34% | Normal |
| 6 | 06.63% | 06.69% | -0.07% | Normal |
| 7 | 06.69% | 05.80% | +0.89% | Normal |
| **8** | 06.37% | 05.12% | **+1.26%** | 🔴 **Pico Artificial Secundario** |
| **9** | 06.18% | 04.58% | **+1.61%** | 🔴 **Pico Artificial Secundario** |

**Total de Mesas Aisladas como "Relleno Artificial Flagrante" (Dígitos 8 y 9):** 15,211 mesas.
**Mecanismo de Fraude:** Elevación artificial de mesas de baja votación natural (rango 20-40) al umbral de los 100+ votos, causando la hiper-densidad del dígito 1 y la desaparición consecuente de los dígitos 2, 3 y 4.

## 4. CONCLUSIÓN JURÍDICO-FORENSE
Se certifica la alteración sistémica de la integridad de los resultados, tipificando una intervención volumétrica en la matriz de preconteo ajena a la voluntad del sufragante natural.

## 5. BIBLIOGRAFÍA FORENSE APLICADA
1. **Nigrini, M. J. (2012).** *Benford's Law: Applications for Forensic Accounting, Auditing, and Fraud Detection*. John Wiley & Sons. (Aplicación al fraude aritmético).
2. **Mebane, W. R. (2006).** *Election Forensics: The Second-digit Benford's Law Test and Recent American Presidential Elections*. En "Election Fraud: Detecting and Deterring Electoral Manipulation" (pp. 162-181).
3. **Roukema, H. F. (2014).** *A first-digit anomaly in the 2009 Iranian presidential election*. Journal of Applied Statistics.
4. **Código Penal Colombiano, Ley 599 de 2000.** *Artículo 286 (Falsedad ideológica en documento público)* y *Artículo 388 (Fraude Electoral)*.
