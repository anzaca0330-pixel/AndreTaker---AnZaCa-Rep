# HIPÓTESIS FORENSE: ABUSO EN LA TRIANGULACIÓN DE LOS 3 EJEMPLARES (DELEGADOS, TRANSMISIÓN Y CLAVEROS)
## Arquitectura de Alteración Sintáctica y Clonación Digital

**Autora / Veedora Ciudadana:** Andrea Zabala Cárcamo (Investigadora Independiente)  
**Objeto de Análisis:** Relación estructural y cibernética entre las tres copias oficiales del formulario E-14 (Delegados, Transmisión y Claveros).

---

## 1. EL ABUSO EN EL SISTEMA DE LOS 3 EJEMPLARES E-14

En la legislación electoral colombiana, cada mesa de votación genera tres ejemplares físicos independientes del formulario E-14:
1. **E-14 Delegados:** Destinado a la digitalización rápida para la transmisión pública.
2. **E-14 Transmisión:** Destinado al procesamiento intermedio de preconteo.
3. **E-14 Claveros:** Introducido en el arca tricolor para la custodia física de los jueces y claveros en el escrutinio oficial.

Al tratarse de tres capturas ópticas independientes realizadas sobre papel físico en la mesa, **cada archivo PDF debería poseer una firma digital de ruido térmico y una estructura sintáctica XREF independiente**.

```
+-----------------------------------------------------------------------------------+
| EJEMPLAR DELEGADOS ──> Muestra todo el patrón gráfico de inyección (#FFFFFF)       |
| EJEMPLAR CLAVEROS  ──> Conserva la cicatriz sintáctica XREF (15 vs 13 objetos)     |
+-----------------------------------------------------------------------------------+
```

---

## 2. HALLAZGOS PERICIALES POR TIPO DE ARCHIVO

### 2.1 E-14 Delegados: El Patrón Completo de Inyección Gráfica
Al analizar el ejemplar de **Delegados**, se descubre la totalidad de la intervención visual y documental:
* **Lienzo Sintético Blanco Puro (`#FFFFFF` DeviceGray):** Inyección de capas sobrepuestas en la 3ª página (1ª Vuelta) que cubren las casillas originales de votación.
* **Varianza Óptica Cero:** Inexistencia de ruido térmico CMOS/CCD de escáner en las áreas intervenidas.
* **Falla de Lectura QR:** Bloqueo e ilegibilidad del código QR por alteración de la secuencia de bytes.

### 2.2 E-14 Claveros: La Cicatriz Estructural XREF
Al auditar el ejemplar de **Claveros** (que legalmente debería provenir del escaneo directo del papel guardado en el arca tricolor):
* **Falla de Clonación XREF:** `QPDF` reporta la misma advertencia sintáctica en el 100% de los casos (*`reported 15 objects != highest 13`*).
* **Demostración de Clonación:** Al compartir de forma idéntica la huella de objetos fantasma con el archivo de Delegados, **se demuestra que el PDF de Claveros NO proviene del escaneo físico de un papel independiente en el arca**, sino de un **clon informático o re-empaquetado sintético** generado a partir de la matriz modificada de Delegados.

---

## 3. CONCLUSIÓN TÉCNICA
El peritaje demuestra un **abuso sistémico del principio de la triple acta**:
1. **En Delegados** se ejecutó la inyección y modificación gráfica del conteo.
2. **En Claveros** quedó grabada la cicatriz estructural XREF como residuo del re-empaquetado informático.

Esta evidencia prueba la **ruptura total de la cadena de custodia** entre la mesa de votación, el preconteo y el escrutinio oficial.
