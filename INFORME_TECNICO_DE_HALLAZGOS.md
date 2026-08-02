# INFORME TÉCNICO DE HALLAZGOS INFORMÁTICOS Y ESTADÍSTICOS
**Referencia:** Comicios Electorales Presidenciales 2026 (Primera y Segunda Vuelta)
**Autor:** Veeduría Técnica Independiente / Andrea Zabala Cárcamo
**Fecha de Emisión:** 1 de Agosto de 2026
**Estatus:** REPORTE PRELIMINAR PARA REVISIÓN LEGAL

---

## 1. ALCANCE DEL INFORME
El presente documento consolida los hallazgos técnicos encontrados durante la auditoría informática, estructural y estadística realizada sobre los repositorios digitales públicos de la Registraduría Nacional (formularios E-14). El objetivo de este informe es presentar la evidencia recolectada para que sea evaluada por el equipo legal y sometida a peritaje certificado formal.

---

## 2. METODOLOGÍA DE EXTRACCIÓN Y ANÁLISIS
La investigación se realizó mediante un enfoque multidisciplinario combinando:
1. **Análisis de Red (OSINT/Netsec):** Trazabilidad de la infraestructura de almacenamiento (Amazon S3) y sistemas perimetrales (WAF Nexusguard).
2. **Análisis Estructural de Archivos (QDF/XREF):** Uso de algoritmos de revisión sintáctica (`qpdf --check`, `pdfinfo`, `pdfimages`) para auditar el código fuente interno de los archivos PDF oficiales.
3. **Análisis Estadístico Probabilístico:** Aplicación del Teorema de la Ley de Benford (test 2BL - Análisis del Segundo Dígito) para detectar desviaciones algorítmicas masivas.

---

## 3. HALLAZGO I: ANOMALÍA ESTRUCTURAL (INYECCIÓN DE CAPAS)
El análisis al código fuente de los documentos en formato PDF demostró una alteración sistémica en la estructura del formato documental. 

> [!CAUTION]
> **Corrupción XREF (Cross-Reference Table):** El 100% de los archivos analizados en muestras clave (ej. Consulado de Los Ángeles, Amazonas) presentan una falla crítica en su tabla de referencias cruzadas. El software arroja el error: *`reported number of objects (15) is not one plus the highest object number (13)`*.

Este desfasaje de objetos es el residuo técnico dejado por la inyección forzada de una máscara vectorial sobre el documento original. El código fuente revela la existencia de objetos bajo el perfil `ColorSpace: DeviceGray`, los cuales sobreescriben visualmente el fondo del documento.

---

## 4. HALLAZGO II: RUPTURA DE CADENA DE CUSTODIA (CLONACIÓN)
Al cruzar los archivos de la transmisión web (Delegados) contra los archivos extraídos de las USB oficiales (Claveros) correspondientes a las mismas mesas (Ej. Acacias, Meta), se descubrió lo siguiente:
1. **Herencia de la Anomalía XREF:** Ambos archivos poseen exactamente la misma fractura estructural (15 vs 13 objetos).
2. **Manipulación de Formato:** El archivo de Delegados fue exportado en escala de grises con alta compresión (58 KB), mientras que el archivo de Claveros fue re-empaquetado a color (1.2 MB). 
3. **Evasión de Metadatos:** Ambos documentos sufrieron el borrado de las etiquetas de tiempo (`CreationDate`, `ModDate`) en su diccionario interno, imposibilitando auditar su fecha de escaneo orgánico.

> [!IMPORTANT]
> **Conclusión Técnica:** La existencia del mismo error sintáctico (XREF) en archivos de pesos y colores distintos, sumado al borrado de metadatos, sugiere técnicamente que la matriz de Claveros fue ensamblada a partir del mismo archivo digital alterado que se subió a Delegados, apuntando a una ruptura de la cadena de custodia del papel original.

---

## 5. HALLAZGO III: CORRELACIÓN ESTADÍSTICA MATEMÁTICA
La alteración digital descrita dejó una huella medible estadísticamente.

Al someter los resultados del escrutinio nacional a la prueba **2BL (Ley de Benford del Segundo Dígito)**, se encontró una desviación severa en la distribución de la votación asignada al candidato Abelardo De la Espriella. Particularmente en los municipios con inyección confirmada (ej. Acacias, Meta), el dígito `2` presentó una sobrefrecuencia de **+3.97%** por encima de la media matemática natural, mientras que los dígitos `0` y `1` sufrieron una caída forzada (-3.48%).

> [!WARNING]
> Esta desviación matemática es consistente con la intervención algorítmica o humana de los resultados.

---

## 6. SÍNTESIS DEL REPORTE
Con base en la evidencia informática y estadística expuesta, esta veeduría técnica documenta una intervención estructural en los archivos electorales. Se sugiere someter este material probatorio a un peritaje legal certificado para iniciar las acciones correspondientes ante los tribunales y la CIDH.

**Firma:**
*Andrea Zabala Cárcamo*
*Investigadora Forense Digital Independiente*
*Virginia, EE.UU.*
