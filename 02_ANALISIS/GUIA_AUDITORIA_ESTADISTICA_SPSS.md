# GUÍA DE IMPORTACIÓN Y ANÁLISIS ESTADÍSTICO EN IBM SPSS STATISTICS
## Protocolo de Reproducibilidad Pericial para Actas E-14

**Autora / Veedora Ciudadana:** Andrea Zabala Cárcamo (Investigadora Independiente)  
**Objeto:** Guía paso a paso para importar las matrices `.csv` del acervo probatorio en **IBM SPSS Statistics** y replicar las pruebas de Chi-cuadrado ($\chi^2$), Prueba t de Student y Ley de Benford (2BL).

---

## 1. PASOS PARA IMPORTAR LOS CSV EN IBM SPSS STATISTICS

Para cargar cualquier matriz de datos del repositorio en SPSS (ejemplo: `REPORTE_XREF_DEEPFAKE.csv`, `anomalias_benford_2BL_nacional_abelardo.csv` o `TABLA_DESGLOSE_POR_DIA_DE_LA_SEMANA.csv`):

1. Abra **IBM SPSS Statistics**.
2. Vaya al menú principal: `Archivo` $\rightarrow$ `Importar datos` $\rightarrow$ `Datos CSV...` (o `File` $\rightarrow$ `Open` $\rightarrow$ `Data...`).
3. Seleccione el archivo `.csv` deseado desde la carpeta `Capitulo_03_Peritajes_Forenses` o `Capitulo_05_Scripts_de_Auditoria`.
4. En la ventana del asistente de importación configure:
   * **¿Los nombres de las variables están en la primera línea?:** Marcar **Sí** (`Yes`).
   * **Codificación de texto:** Seleccionar **UTF-8**.
   * **Delimitador de campos:** Seleccionar **Coma (`,`)** (Para la base de preconteo `reporte_preconteo_oficial_registraduria_depto88.csv`, seleccionar **Punto y coma (`;`)**).
5. Haga clic en **Finalizar**. SPSS creará la vista de variables (`Variable View`) y vista de datos (`Data View`) automáticamente.

---

## 2. REPLICACIÓN DE PRUEBAS ESTADÍSTICAS EN SPSS

### 2.1 Prueba T de Student para Muestras Independientes (Derrumbe Mesa 013 a 014 en Los Ángeles)
* **Objetivo:** Verificar la caída de participación ($t(17) = 8.2, p < 0.00001$).
* **Ruta en SPSS:**  
  `Analizar` $\rightarrow$ `Comparar medias` $\rightarrow$ `Prueba T para muestras independientes...`
* **Variable de prueba:** `Votantes_Totales`
* **Variable de agrupación:** `Bloque_Mesa` (Grupo 1: Mesas 001-013, Grupo 2: Mesas 014-019).

### 2.2 Prueba de Chi-Cuadrado de Bondad de Ajuste ($\chi^2$) — Ley de Benford 2BL
* **Objetivo:** Demostrar la distorsión del segundo dígito a nivel nacional ($\chi^2 = 1.755,91, p < 0.001$).
* **Ruta en SPSS:**  
  `Analizar` $\rightarrow$ `Pruebas no paramétricas` $\rightarrow$ `Cuadros de diálogo heredados` $\rightarrow$ `Chi-cuadrado...`
* **Variable de prueba:** `segundo_digito`
* **Valores esperados:** Ingresar la distribución teórica de Benford 2BL ($d_2 \in \{0, 1, \dots, 9\}$).

### 2.3 Tablas de Contingencia y Análsis por Día de la Semana en Consulados
* **Objetivo:** Verificar la concentración de anomalías los Lunes ($58.5\%$) y Martes ($55.2\%$).
* **Ruta en SPSS:**  
  `Analizar` $\rightarrow$ `Estadísticos descriptivos` $\rightarrow$ `Tablas cruzadas...`
* **Filas:** `Dia_Semana`
* **Columnas:** `QPDF_Estructura` o `Estado_Anomalia`
* **Estadísticos:** Marcar `Chi-cuadrado`, `Phi y V de Cramér`.

---

## 3. COMPATIBILIDAD 100% GARANTIZADA
Todas las matrices `.csv` del repositorio contienen encabezados limpios sin caracteres especiales incompatibles, asegurando que SPSS reconozca los tipos de datos como **Escala** (`Numeric`), **Ordinal** o **Nominal** de forma inmediata.
