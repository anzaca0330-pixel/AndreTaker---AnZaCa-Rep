# ENTREGABLES FORENSES E-14 (CASO CIDH)

Este repositorio contiene las herramientas analíticas, scripts de auditoría y reportes generados durante el peritaje técnico forense a los comicios presidenciales (1ra y 2da Vuelta) de 2026. Toda la evidencia y scripts fueron diseñados para soportar el caso presentado ante la CIDH.

---

## 1. Cadena de Custodia (Principio de Solo Lectura)
Todas las herramientas contenidas en este repositorio operan bajo el estándar de cadena de custodia forense (RFC 3227 / ISO 27037). El análisis criptográfico y la metrología se realizaron sobre copias exactas en un entorno "Cold Case" aislado, preservando inmaculada la evidencia original obtenida de los servidores públicos.

**IMPORTANTE (Evidencia Pesada / Git LFS):** 
Debido a los límites de tamaño de GitHub, los terabytes de archivos PDF originales no están subidos a este repositorio directamente. La arquitectura del repositorio está configurada con **Git LFS** (`.gitattributes`) para manejar futuros archivos pesados. Sin embargo, la evidencia en bruto está disponible en repositorios de almacenamiento externo (Ej. Mega / Google Drive) proporcionados por la Veeduría. 
Para validar las muestras, los peritos pueden referirse al documento `MUESTRAS_CONTROL_HASHES.md` que contiene las firmas criptográficas para corroborar los archivos externos.

---

## 2. Metodología Forense y Herramientas

El análisis se centra en dos vectores de fraude comprobados matemáticamente y documentados en los informes `INFORME_TECNICO_DE_HALLAZGOS.md` y `TECHNICAL_REPORT_OF_FINDINGS.md`:

### A. La Técnica "BlindMasking" y Clonación Algorítmica
Se usó software generador de PDFs sintéticos para inyectar vectores gráficos (Plantilla B) usando máscaras `DeviceGray` para sobreescribir los votos. Se utilizaron las siguientes herramientas para desarmar el ataque:
- **`qpdf`**: Manipulación y detección de daños en la tabla de referencias cruzadas (XREF). Descubrió la cicatriz inyectada de 15 vs 13 objetos.
- **`pdfimages` / `ImageMagick`**: Utilizadas para metrología de píxeles, revelando cómo las matrices diferían visualmente (B/N vs Color) mientras que la arquitectura interna del contenedor se mantenía idéntica (La Paradoja de los Píxeles).
- **`sha256sum` (Hashes)**: Para análisis criptográfico interno y externo.

### B. "Planchado Matemático" (Desviación Estadística)
Inyección de resultados fijos en bloques de votación, detectado a través de herramientas estadísticas y scripts desarrollados a medida en Python:
- **Ley de Benford (Segundo Dígito - 2BL)**: Para exponer el sesgo humano y la alteración de la varianza natural en favor del candidato Abelardo De la Espriella.

---

## 3. Scripts de Auditoría (`SCRIPTS_PYTHON_FORENSES`)

### Auditoría PDF y XREF (La "Cicatriz")
- **`auditoria_masiva_xref.sh`**: Script en Bash ultra-rápido (`xargs -P 32`) diseñado para escanear masivamente cientos de miles de PDFs de Claveros y detectar el error de 15 objetos. Cuenta con tolerancia a fallas.
- **`auditoria_claveros_antioquia.sh`**: Versión focalizada del escáner XREF dedicada al departamento de Antioquia.
- **`fusion_nacional_xref_preconteo.py`**: Cruza los archivos "CORRUPTOS" con los resultados de la Registraduría.
- **`prueba_criptografica_clonaje.py`**: El script definitivo de metrología binaria. Extrae objetos rasterizados internos del PDF usando `pdfimages` y computa sus hashes SHA-256 para demostrar clonación vectorial evadiendo los metadatos de superficie.

### Auditoría Estadística (Ley de Benford y Varianza)
- **`auditoria_nacional_benford.py` / `auditoria_nacional_benford_2BL.py`**: Aplican la Ley de Benford a los resultados nacionales.
- **`auditoria_meta_acacias_benford.py`**: Submódulo focalizado en Acacias (Meta).
- **`buscar_planchado_nacional.py`**: Algoritmo de minería de datos que busca mesas contiguas con desviación estándar inusual (cercana a 0).

---

## 4. Ejecución para Peritos Externos (Peer Review)

Todos los scripts están diseñados para ser ejecutados en entornos Linux (Debian/Ubuntu). Recomendamos a la comunidad de ingenieros clonar este repositorio y validar el `INFORME_INTEGRIDAD_SHA256.md` antes de ejecutar.

**Dependencias Requeridas:**
- `python3`
- `qpdf` (`sudo apt install qpdf`) - Vital para la detección de la inyección XREF.
- `poppler-utils` (`sudo apt install poppler-utils`) - Requerido por `pdfimages` para la extracción de capas binarias.
- `exiftool` (`sudo apt install libimage-exiftool-perl`) - Requerido para verificación de eliminación de metadatos de tiempo en actas web.

---
**Documento Confidencial.** Generado por la Veeduría Técnica / Andrea Zabala Cárcamo.
