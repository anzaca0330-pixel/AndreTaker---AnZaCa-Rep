# INFORME METODOLÓGICO Y ANÁLISIS ESTADÍSTICO ELECTORAL
## Evaluación de Inconformidades Cuantitativas y Progresión Muestral en los Comicios Presidenciales de 2026

**Autora / Veedora Ciudadana:** Andrea Zabala Cárcamo (Investigadora Independiente)  
**Área de Aplicación:** Estadística Aplicada y Metodología de la Investigación  
**Objeto:** Análisis de Distribuciones de Frecuencia (Ley de Benford 2BL), Pruebas de Hipótesis No Paramétricas ($\chi^2$) y Progresión Muestral (EE.UU. $\rightarrow$ España $\rightarrow$ Colombia Nacional).

---

## 1. INTRODUCCIÓN Y JUSTIFICACIÓN METODOLÓGICA DE LA MUESTRA

La presente investigación adoptó una estrategia de **Muestreo Progresivo por Etapas y Estratificación Geográfica**, diseñada para probar la hipótesis de consistencia en el procesamiento informático de la información electoral.

```
+-----------------------------------------------------------------------------------+
| FASE 1: EE.UU. (N=987)     ──>  FASE 2: ESPAÑA (N=696)    ──>  FASE 3: NACIONAL (N=233.448)|
| (Muestra Primaria Diáspora)     (Replicación Homóloga)         (Línea Base Agregada)  |
+-----------------------------------------------------------------------------------+
```

### 1.1 Origen de la Investigación y Enfoque Cognitivo (Reconocimiento de Patrones TDAH)
Toda la investigación nació el **1 de Junio de 2026** a partir de la observación minuciosa de un primer consulado (Los Ángeles). Gracias a la capacidad cognitiva de **hiperfoco y reconocimiento intensivo de patrones** (asociada al perfil neurodivergente TDAH de la investigadora), se detectó una sutil anomalía gráfica y sintáctica que habría pasado inadvertida en una revisión estándar.

Siguiendo esa primera pista de forma sistemática, la investigación evolucionó desde el análisis manual de 1 acta consular hasta el desarrollo de **scripts automatizados de scraping web y auditoría masiva en Python** (`muestreo_masivo_deepfakes.py`, `auditoria_masiva_xref.sh`), capaces de descargar y procesar los 117.993 archivos PDF a nivel nacional.

### 1.2 ¿Por qué se inició con Estados Unidos ($N = 987$ actas)?
Estados Unidos representa la circunscripción electoral en el exterior con mayor volumen de votantes registrados y mayor número de mesas instaladas ($N = 987$). Metodológicamente, ofrecía tres condiciones idóneas como punto de partida:
1. **Homogeneidad Logística:** Operación bajo el esquema de votación anticipada (Lunes a Domingo) con escaneo y transmisión consular centralizada.
2. **Mayor Tamaño Muestral Inicial:** Permitió establecer una línea base de varianza sin los ruidos dispersos de puestos rurales aislados.
3. **Hallazgo Inicial:** El análisis estructural reveló que el $100\%$ de los archivos PDF presentaban inconsistencias sintácticas en la tabla de referencias cruzadas (`xref`) y depuración de metadatos (`Creator`, `Producer`, `CreationDate`).

### 1.3 Replicación Muestral en España ($N = 696$ actas): Muestras Estadísticamente Homólogas
Para determinar si el fenómeno detectado en EE.UU. respondía a una anomalía local (un escáner o servidor aislado) o a un patrón sistemático, se seleccionó a **España ($N = 696$ actas)** como grupo de replicación.

* **Criterio de Homología Estadística:** España constituye la segunda circunscripción exterior con mayor peso demográfico y comparte características socio-electorales equivalentes con la diáspora en EE.UU. (patrones de votación anticipada, distribución de censos consulares y transmisión remota).
* **Resultado de la Replicación:** La muestra de España presentó exactamente la misma huella estructural que la muestra de EE.UU. ($100\%$ de inconsistencias XREF y omisión de metadatos). Esto permitió validar estadísticamente que el fenómeno respondía a un **flujo de procesamiento centralizado para el voto en el exterior**, descartando la hipótesis de un error técnico accidental en una sede consular específica.

### 1.3 Escalamiento a la Línea Base Nacional ($N = 233.448$ mesas)
Tras confirmar el patrón en las dos muestras más representativas del exterior, la investigación escaló al universo de la consolidación nacional ($N = 233.448$ mesas), permitiendo contrastar el comportamiento de la diáspora (Departamento 88) contra el comportamiento del territorio nacional (32 departamentos).

---

## 2. ANÁLISIS ESTADÍSTICO DE FRECUENCIAS (LEY DE BENFORD DEL SEGUNDO DÍGITO - 2BL)

La Ley del Segundo Dígito de Benford (2BL) establece la frecuencia probabilística esperada para la segunda posición numérica en conjuntos de datos numéricos generados por procesos orgánicos o naturales.

### 2.1 Modelo Matemático Teórico
La probabilidad teórica $P(d)$ de que el segundo dígito sea $d \in \{0, 1, \dots, 9\}$ está dada por:
$$P(d) = \sum_{k=1}^{9} \log_{10} \left( 1 + \frac{1}{10k + d} \right)$$

| Dígito ($d$) | Frecuencia Teórica Esperada (%) |
| :---: | :---: |
| 0 | 11.97% |
| 1 | 11.39% |
| 2 | 10.88% |
| 3 | 10.43% |
| 4 | 10.03% |
| 5 | 9.67% |
| 6 | 9.34% |
| 7 | 9.04% |
| 8 | 8.76% |
| 9 | 8.50% |

---

## 3. RESULTADOS CUANTITATIVOS Y PRUEBAS DE HIPÓTESIS

### 3.1 Planteamiento de Hipótesis
* **Hipótesis Nula ($H_0$):** La distribución observada del segundo dígito se ajusta al modelo probabilístico de Benford 2BL ($p \ge 0.001$).
* **Hipótesis Alternativa ($H_1$):** La distribución observada del segundo dígito se desvía significativamente del modelo probabilístico de Benford 2BL ($p < 0.001$), indicando atipicidad cuantitativa.

### 3.2 Matriz Comparativa por Bloques Territoriales

$$\chi^2 = \sum_{i=0}^{9} \frac{(O_i - E_i)^2}{E_i}$$

| Bloque Territorial | Candidato | Muestra ($N$) | Chi-Cuadrado ($\chi^2$) | Grados de Libertad | $p$-value | Estado Estadístico |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Consulados (Depto 88)** | Abelardo De la Espriella | 6.552 | 19.96 | 9 | $0.0181$ | 🟢 Ajuste aceptable a escala global |
| **Consulados (Depto 88)** | Iván Cepeda | 5.982 | 41.40 | 9 | $4.23 \times 10^{-6}$ | 🔴 **Atipicidad Significativa** ($p < 0.001$) |
| **Nacional (32 Deptos)** | Abelardo De la Espriella | 229.524 | 495.55 | 9 | $5.15 \times 10^{-101}$ | 🔴 **Desviación Severa** ($p < 0.001$) |
| **Nacional (32 Deptos)** | Iván Cepeda | 233.448 | 1.755,91 | 9 | $0.0000$ | 🔴 **Desviación Severa** ($p < 0.001$) |

---

## 4. DISCUSIÓN DE RESULTADOS Y CONTEXTO

1. **Contexto Exterior y Multiculturalidad (Diáspora):** 
   En los consulados de EE.UU. y España, el comportamiento electoral está fuertemente mediado por **factores socioculturales y demográficos heterogéneos** (tiempo de residencia, niveles de integración económica, variaciones regionales de origen en Colombia y dinámicas de movilización en comunidades migrantes). Estas condiciones socio-conductuales introducen variaciones naturales en el volumen de abstención y la concentración del voto. Sin embargo, la prueba 2BL agregada para el Departamento 88 reveló un desvío que excede la varianza sociocultural ($Z = +3.53$ en el dígito `1` y $Z = -3.81$ en el dígito `3`).

2. **Contexto Nacional (Colombia):** 
   A nivel nacional ($N > 229.000$ mesas), las pruebas $\chi^2$ para ambos candidatos superan con creces los valores críticos de la distribución. La presencia de Z-Scores de $-20.98$ y $-27.31$ en los dígitos altos ($8$ y $9$) evidencia una sobrerrepresentación de dígitos bajos ($0, 1, 2$), un fenómeno documentado en la literatura de auditoría de datos como indicador de truncamiento o moldeado cuantitativo.

3. **Limitación Forense:** Conforme a las normas **ISO/IEC 27037** y **NIST SP 800-86**, las pruebas estadísticas constituyen **indicadores de atipicidad para priorización de auditoría**, exigiendo la verificación directa de los registros de log en bases de datos y la confrontación física contra los formularios originales.

---

## 5. REFERENCIAS Y BIBLIOGRAFÍA ACADÉMICA

* **Benford, F. (1938).** *The law of anomalous numbers*. Proceedings of the American Philosophical Society, 78(4), 551-572.
* **Diekmann, A. (2007).** *Not the first digit! Using Benford's law to detect fraudulent data in the scientific literature and the election files*. Journal of Applied Statistics, 34(3), 321-329.
* **ISO/IEC 27037:2012.** *Information technology — Security techniques — Guidelines for identification, collection, acquisition and preservation of digital evidence*.
* **Nigrini, M. J. (2012).** *Benford's Law: Applications for forensic accounting, auditing, and fraud detection*. John Wiley & Sons.
* **NIST SP 800-86 (2006).** *Guide to Integrating Forensic Techniques into Incident Response*. National Institute of Standards and Technology.
