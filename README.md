# ENTREGABLES FORENSES E-14 (CASO CIDH)

## Acerca de este Repositorio / About
**[ES]** Este repositorio es una bitácora técnica de código abierto y preservación de evidencia digital. Contiene las herramientas analíticas, scripts de auditoría matemática e informática, y dictámenes periciales independientes generados durante el análisis técnico de los comicios presidenciales (1ra y 2da Vuelta) de 2026 en Colombia. Toda la evidencia y metodología fue documentada bajo estrictos estándares forenses para soportar el caso presentado ante la Comisión Interamericana de Derechos Humanos (CIDH) y la comunidad internacional.

**[EN]** This repository serves as an open-source technical log and digital evidence preservation vault. It contains the analytical tools, mathematical and computer auditing scripts, and independent forensic reports generated during the technical analysis of the 2026 presidential elections in Colombia. All evidence and methodology have been documented under strict forensic standards to support the case presented before the Inter-American Commission on Human Rights (IACHR) and the international community.

---

## 1. Cadena de Custodia (Principio de Solo Lectura)
Todas las herramientas contenidas en este repositorio operan bajo el estándar de cadena de custodia forense (RFC 3227 / ISO 27037). El análisis criptográfico y la metrología se realizaron sobre copias exactas en un entorno "Cold Case" aislado, preservando inmaculada la evidencia original obtenida de los servidores públicos.

**IMPORTANTE (Evidencia Pesada / Git LFS):** 
Debido a los límites de tamaño de GitHub, los terabytes de archivos PDF originales no están subidos a este repositorio directamente. La arquitectura del repositorio está configurada con **Git LFS** (`.gitattributes`) para manejar futuros archivos pesados. Sin embargo, la evidencia en bruto está disponible en repositorios de almacenamiento externo (Ej. Mega / Google Drive) proporcionados por la Veeduría. 
Para validar las muestras, los peritos pueden referirse al documento `MUESTRAS_CONTROL_HASHES.md` que contiene las firmas criptográficas para corroborar los archivos externos.

---

## 2. Metodología Forense y Herramientas

El análisis se centra en dos vectores de anomalía estructural comprobados matemáticamente y documentados en los informes `INFORME_TECNICO_DE_HALLAZGOS.md` y `TECHNICAL_REPORT_OF_FINDINGS.md`:

### A. La Técnica "BlindMasking" y Clonación Algorítmica
Se usó software generador de PDFs sintéticos para inyectar vectores gráficos (Plantilla B) usando máscaras `DeviceGray` para sobreescribir los votos. Se utilizaron las siguientes herramientas para desarmar el ataque:
- **`qpdf`**: Manipulación y detección de daños en la tabla de referencias cruzadas (XREF). Descubrió la cicatriz inyectada de 15 vs 13 objetos.
- **`pdfimages` / `ImageMagick`**: Utilizadas para metrología de píxeles, revelando cómo las matrices diferían visualmente (B/N vs Color) mientras que la arquitectura interna del contenedor se mantenía idéntica (La Paradoja de los Píxeles).
- **`sha256sum` (Hashes)**: Para análisis criptográfico interno y externo.

### B. "Planchado Matemático" (Desviación Estadística)
Inyección de resultados fijos en bloques de votación, detectado a través de herramientas estadísticas y scripts desarrollados a medida en Python:
- **Ley de Benford (Segundo Dígito - 2BL)**: Para exponer el sesgo humano y la alteración de la varianza natural en favor del candidato Abelardo De la Espriella.

### C. Arquitectura Forense de Doble Capa
Síntesis técnica que explica cómo y por qué coexisten las anomalías estructurales y ópticas en la misma base de datos.
- **[HIPOTESIS_FORENSE_ARQUITECTURA_DOBLE.md](file:///home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/HIPOTESIS_FORENSE_ARQUITECTURA_DOBLE.md)**: Documento pericial que modela el "embudo" centralizado de re-empaquetado e inyección sintética.

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

## 🇨🇴 Autoría Colectiva y Dedicatoria (Frente Digital 2026)

**Este repositorio no me pertenece a mí, le pertenece a Colombia.**

Aunque mi nombre (Andrea Zabala Cárcamo) figura como coordinadora de la estructura técnica y pericial, este esfuerzo monumental fue impulsado por la fuerza de más de **70,000 "Testigos Digitales"** (Frente Digital 2026). Ciudadanos comunes que descargaron, verificaron y protegieron la evidencia digital cuando los servidores oficiales fallaron.

**Dedicamos este peritaje científico y forense:**
- A la **gente** que salió a votar masivamente, impulsada por la esperanza y el deber cívico.
- Por sus **tierras y territorios**, pilares de la soberanía de nuestras comunidades.
- Por **nuestra selva y nuestras aguas**, que requieren protección y voces que las defiendan.
- Por **nuestros animales**, que son sagrados y dependen del futuro que construimos hoy.
- Por mi **mamá y mi hermana**, que siguen allá resistiendo.
- Por **mis amigos y por los hijos de mis amigos**, a quienes les debemos un país donde la verdad no sea borrada.

Nuestra labor (incluyendo el hiperenfoque neurodivergente que detectó las primeras anomalías microscópicas en los PDF) fue solo el catalizador técnico al servicio de este colectivo. La alteración estructural de votos que hemos demostrado aquí (inyección sintética y desviación de la Ley de Benford) intentó silenciar el clamor por esos territorios y ecosistemas. 

**Este repositorio es la prueba inmutable y matemática de que la voz de los colombianos existió, fue registrada y no será borrada.**

*Advertencia de Seguridad:* Debido a los continuos ciberataques y hostigamientos documentados, este entorno actúa como bóveda de preservación "Cold Case" descentralizada para garantizar que la verdad llegue intacta a la CIDH.
