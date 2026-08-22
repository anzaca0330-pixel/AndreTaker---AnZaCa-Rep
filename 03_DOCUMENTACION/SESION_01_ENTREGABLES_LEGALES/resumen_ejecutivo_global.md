# RESUMEN EJECUTIVO GLOBAL: ANÁLISIS TÉCNICO DE ACTAS E-14 (EXTRANJERO)
## CONSOLIDADO GENERAL — ELECCIONES PRESIDENCIALES 2026

**Denunciante:** Andrea Zabala Carcamo  
**Fecha:** Julio de 2026  

---

## 1. CONTEXTO Y ALCANCE DEL ANÁLISIS

El presente documento constituye un resumen ejecutivo global derivado del análisis forense automatizado sobre el material electoral (actas E-14) digitalizado en el exterior. Este informe sintetiza los hallazgos de tres muestras independientes evaluadas mediante el mismo pipeline técnico y metodológico (`QPDF`, `ExifTool`, `mutool`, `zbarimg`).

Las tres poblaciones de datos analizadas y mantenidas de forma independiente en sus respectivos informes son:
1. **Consulados de Estados Unidos:** 987 actas.
2.- **Comparativa de Hashes SHA-256 (Versión 1 vs. Versión 2):**
  - **Versión 1 (Dataset 'Para Revisar'):** 25,061 actas E-14 iniciales.
  - **Versión 2 (Dataset Descargado Ayer en Disco Portátil):** 117,993 actas descargadas ayer de Segunda Vuelta.

### 1.1 Origen Metodológico y Trazabilidad de la Investigación

El desarrollo de este peritaje internacional tuvo su origen en la observación de campo y la veeduría ciudadana iniciada el **2 de junio de 2026** sobre las 19 mesas del Puesto 02 del **Consulado de Los Ángeles, California (EE.UU.)**. En dicha inspección primaria, la especialista documentó tres anomalías empíricas fundamentales:
1. **Supresión e Ilegibilidad de Códigos QR:** Inoperatividad total de lectura automatizada sobre los códigos impresos en las actas de dicho puesto.
2. **Foliación Híbrida en Actas E-14:** Mezcla irregular de páginas a color originales y páginas fotocopiadas/reimpresas en blanco y negro dentro de los mismos paquetes electorales oficiales (ej. Mesas 011, 012 y 015 en color frente a Mesas 013, 014 y 018 en B/N).
3. **Comportamiento Estadístico Atípico:** Clonación de patrones numéricos en mesas contiguas (ej. Mesas 001 a 003) y un desplome abrupto de la participación en las mesas finales del puesto (Mesas 015 a 019 con apenas 12, 7 y 9 votantes).

Estos hallazgos iniciales motivaron la radicación formal de denuncias ante el **Consejo Nacional Electoral (CNE)**, la **Procuraduría General de la Nación**, **URIEL** y la **Misión de Observación Electoral (MOE)**, acompañadas de notas jurídicas sobre el precedente del Consejo de Estado respecto a la auditoría obligatoria del software electoral. 

A partir de este caso testigo en Los Ángeles, la metodología se sistematizó y automatizó mediante un pipeline de código abierto (`QPDF`, `ExifTool`, `mutool`, `zbarimg`), escalando el barrido forense a la totalidad de las actas de **Estados Unidos (987 actas)**, **España (696 actas)** y la construcción de un **Grupo de Control masivo (25.061 actas)** para validar objetivamente los resultados.

---

## 2. EL GRUPO DE CONTROL: LÍNEA BASE DE INTEGRIDAD DOCUMENTAL

Se procesó un volumen masivo de **25.061 archivos PDF** provenientes de diversas regiones para establecer una línea base técnica respecto al comportamiento estándar del hardware y software de digitalización.

> [!NOTE]
> **Importancia de la Muestra de Control**
> De los 25.061 archivos evaluados, el filtro automatizado confirmó que **más de 25.050 archivos (99.96%) eran estructuralmente limpios y conservaban sus metadatos de fábrica**, aislando únicamente 10 documentos (0.04%) con problemas mecánicos o de digitalización física (alteración estructural, páginas faltantes o ilegibilidad). 
> 
> Este análisis evidencia que es plenamente viable que las actas se digitalicen y transmitan preservando la trazabilidad de metadatos y la integridad sintáctica de los archivos PDF.

---

## 3. HALLAZGOS Y COMPARACIÓN ESTADÍSTICA FORMAL

En marcado contraste con el grupo de control, el escrutinio de las actas provenientes de las circunscripciones de Estados Unidos y España reveló una desviación estadística altamente significativa respecto a la línea base:

| Indicador Forense | Grupo de Control (n=25.061) | España (n=696) | EE.UU. (n=987) | Riesgo Relativo (RR) | Odds Ratio (OR) | Significancia ($p$-value) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Metadatos Vacíos (`Creator`/`Producer`)** | 0.00% (0) | 100.0% (696) | 100.0% (987) | $> 25.000$ | $\infty$ | $p < 0.0001$* |
| **Advertencias Estructurales QPDF (`xref`)** | 0.00% (0) | 100.0% (696) | 100.0% (987) | $> 25.000$ | $\infty$ | $p < 0.0001$* |
| **Código QR Ausente o Ilegible** | 0.008% (2) | 21.7% (151) | 23.3% (230) | $> 2.700$ | $> 3.200$ | $p < 0.0001$* |
| **Errores Lógicos Aislados (Incompletos/Vacíos)** | 0.04% (10) | 0.00% (0) | 0.00% (0) | N/A | N/A | N/A |

*\* Calculado mediante prueba exacta de Fisher y prueba de Chi-cuadrado ($\chi^2$).*

### 3.1 Síntesis de Observaciones Técnicas e Inferencias
- **Metadatos Purgados y Advertencias Estructurales (100% de afectación en EE.UU. y España):** La totalidad de los 1.683 archivos de estas dos zonas geográficas presenta vaciado completo de atributos de trazabilidad y advertencias de la tabla `xref` en `QPDF`. Esto es consistente con la existencia de un flujo de procesamiento documental secundario común.
- **Comportamiento del Código QR e Imágenes de 1 bit:** En ambas muestras se detectó una tasa de ilegibilidad de QR (21.7% en España y 23.3% en EE.UU.) e imágenes codificadas en `DeviceGray` a 1 bit. Esto indica que ocurrió una binarización u optimización de imagen en el flujo documental, lo que dificulta la auditoría automatizada inmediata.

---

## 4. CONCLUSIONES INTEGRADAS

1. **Diferenciación Estadística Estadísticamente Probada:** La comparación objetiva demuestra diferencias estadísticamente significativas ($p < 0.0001$) entre los datos de España y EE.UU. frente al grupo de control.
2. **Consistencia de la Hipótesis de Procesamiento:** Los hallazgos son consistentes con la existencia de un flujo de procesamiento documental distinto al observado en la muestra de control.
3. **Necesidad de Auditoría de Sistemas Fuente:** La evidencia forense no permite determinar por sí sola la causa ni intencionalidad de las anomalías; se requiere un examen adicional de los sistemas de adquisición originales, logs de los servidores de recepción y archivos PDF nativos.

---

## 5. PRÓXIMOS PASOS EN LA AUDITORÍA

> [!TIP]
> **Ampliación del Escaneo Forense Global**
> Se continúa con el análisis automatizado sobre el resto de las circunscripciones en el exterior empleando el mismo pipeline pericial (`QPDF`, `ExifTool`, `mutool`, `zbarimg`) para determinar el alcance geográfico de estas desviaciones técnicas respecto al grupo de control.
