# 📜 INFORME DE LOTE FORENSE — VEREDICTO DE MASA

**Carpeta analizada:** `/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/00_MUESTRAS_EVIDENCIA`  
**Fecha del diagnóstico:** 2026-08-30 19:12:36 UTC  
**Total de archivos evaluados:** 4

---

## 🛠️ VERSIONES DEL ENTORNO DE AUDITORÍA
*   **qpdf:** `qpdf version 11.9.0`
*   **exiftool:** `ExifTool v12.76`
*   **pdfimages:** `pdfimages version 24.02.0`
*   **identify:** `Version: ImageMagick 6.9.12-98 Q16 x86_64 18038 https://legacy.imagemagick.org`

---

## 📊 RESUMEN ESTADÍSTICO DE ANOMALÍAS

| Métrica / Hallazgo | Valor | Porcentaje |
| :--- | :--- | :--- |
| **Total Archivos Evaluados** | 4 | 100.0% |
| **⚠️ Discrepancia XREF Detectada (Irregularidad/Alteración)** | 4 | **100.00%** |
| **✅ Estructura Normal de Objetos** | 0 | **0.00%** |
| **🖼️ Archivos con Imágenes de Varianza Cero (Std = 0)** | 1 | **25.00%** |

---

## 🧠 VEREDICTO E INTERPRETACIÓN METODOLÓGICA (ARGOS)

*   **Advertencias XREF:** El 100.00% de las muestras presentan discrepancias en el conteo de objetos (`reported number of objects`). Si este comportamiento es idéntico al de los controles del mismo período y plataforma, debe catalogarse como una **irregularidad de generación** propia de la plataforma de la Registraduría, no necesariamente como una modificación deliberada de un atacante.
*   **Varianza Cero ($Std = 0$):** Se confirmaron 1 archivos que contienen imágenes raster con desviación estándar cero. Dado que los sensores ópticos físicos siempre introducen ruido térmico, la presencia de imágenes con $Std = 0$ indica de forma inequívoca la **inyección digital de capas de fondo sintéticas** posteriores a la captura física.

---

### 📂 Archivos generados:
*   **Matriz CSV de Datos Crudos:** `matriz_lote_babayaga.csv`
*   **Informe de Lote Consolidado:** `informe_lote_babayaga.md`

---
*Informe generado con rigor metodológico forense e integridad de datos.*
