# ENTREGABLES FORENSES E-14 (CASO CIDH)

Este repositorio contiene las herramientas analíticas, scripts de auditoría y reportes generados durante el peritaje técnico forense a los comicios presidenciales (1ra y 2da Vuelta) de 2026. Toda la evidencia y scripts fueron diseñados para soportar el caso presentado ante la CIDH.

## Arquitectura de Auditoría

El repositorio está compuesto por herramientas diseñadas para detectar dos tipos de fraude principales:
1. **El "Planchado Matemático" (Primera Vuelta):** Modificación algorítmica de la varianza estadística para asignar resultados fijos en bloques de votación (Ej. Consulado Los Ángeles).
2. **La "Plantilla B" y Clonación de Claveros (Segunda Vuelta):** Inyección de vectores gráficos (`DeviceGray`) para sobreescribir actas escaneadas, rompiendo la estructura XREF del PDF.

## Scripts y Herramientas (SCRIPTS_PYTHON_FORENSES)

### 1. Auditoría PDF y XREF (La "Cicatriz")
- **`auditoria_masiva_xref.sh`**: Script en Bash ultra-rápido (`xargs -P 32`) diseñado para escanear masivamente cientos de miles de PDFs de Claveros y detectar el error `reported number of objects (15) is not one plus the highest object number (13)`. Cuenta con un mecanismo de reanudación automática para tolerar fallas de hardware.
- **`auditoria_claveros_antioquia.sh`**: Versión focalizada del escáner XREF dedicada exclusivamente al departamento de Antioquia.
- **`fusion_nacional_xref_preconteo.py`**: Cruza los archivos marcados como "CORRUPTOS" por el escáner Bash con los resultados oficiales de la Registraduría para encontrar correlaciones.

### 2. Auditoría Estadística (Ley de Benford y Varianza)
- **`auditoria_nacional_benford.py` / `auditoria_nacional_benford_2BL.py`**: Scripts que aplican la Ley de Benford (Específicamente el análisis del Segundo Dígito o 2BL) a los resultados nacionales para detectar anomalías de generación humana/algorítmica en la asignación de votos a Abelardo De la Espriella.
- **`auditoria_meta_acacias_benford.py`**: Submódulo focalizado en Acacias (Meta) para validar matemáticamente la alteración subyacente de las actas clonadas con la Plantilla B.
- **`buscar_planchado_nacional.py`**: Algoritmo de minería de datos que busca mesas contiguas con desviación estándar cercana a 0, probando el "planchado".

## Ejecución para Peritos Externos

Todos los scripts están diseñados para ser ejecutados en entornos Linux (Debian/Ubuntu).
**Dependencias Requeridas:**
- `python3`
- Paquete `qpdf` (`sudo apt install qpdf`) - Vital para la detección del daño estructural de la Plantilla B.
- Paquete `poppler-utils` (`sudo apt install poppler-utils`) - Requerido para la extracción de imágenes rasterizadas si se desea ampliar la investigación visual.

---
**Documento Confidencial.** Generado por la Veeduría Técnica / Andrea Zabala Cárcamo.
