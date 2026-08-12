# 📚 BIBLIOGRAFÍA ACADÉMICA Y NORMATIVA TÉCNICA
**Caso Radicado CIDH:** `IACHR-0000113728`  
**Referencia de Proyecto:** Acervo Probatorio Forense E-14 (Colombia 2026)

Este documento compila el marco teórico, los estándares internacionales y la literatura científica utilizada para auditar matemáticamente e informáticamente el fraude electoral estructurado.

---

## 1. Estándares Forenses y Normativa Internacional (ISO)
- **ISO/IEC 27037:2012** – *Information technology — Security techniques — Guidelines for identification, collection, acquisition and preservation of digital evidence*. Define los principios de integridad, volatilidad y el "Principio de Solo Lectura" (Read-Only) para evitar la alteración de los metadatos.
- **ISO 32000-1:2008** – *Document management — Portable document format*. Especificación oficial del formato PDF, fundamental para el análisis de objetos (`/Obj`), árboles de directorios, capas (`/Contents`) y la tabla de referencias cruzadas (XREF) corrupta encontrada en la evidencia.
- **RFC 3227** – *Guidelines for Evidence Collection and Archiving*. Define la recolección estricta y segura de información digital bajo la cadena de custodia.

## 2. Criptografía y Preservación
- **FIPS 180-4 (NIST)** – *Secure Hash Standard (SHS)*. Estándar oficial del Instituto Nacional de Estándares y Tecnología de EE.UU. que avala el uso del algoritmo criptográfico **SHA-256**, utilizado en este repositorio para blindar y garantizar la inmutabilidad matemática de cada acta (E-14) y de los metadatos de recolección.
- **RFC 3161** – *Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)*. Estándar utilizado para certificar los sellos de tiempo inalterables de las descargas en los laboratorios.

## 3. Estadística Forense (Ley de Benford y Simulaciones)
- **Nigrini, Mark J. (2012).** *Benford's Law: Applications for Forensic Accounting, Auditing, and Fraud Detection*. (John Wiley & Sons). Obra cumbre en auditoría forense que sustenta matemáticamente por qué la desviación y el "planchado estadístico" encontrados en la digitación de los votos constituye fraude sintético, y no varianza natural.
- **Fewster, R. M. (2009).** *A simple explanation of Benford's Law*. (The American Statistician). Utilizado para el sustento probabilístico y cálculo de P-Values.
- **Mebane, Walter R. Jr. (2006).** *Election Forensics: The Second-digit Benford's Law Test and Recent American Presidential Elections*. Aplicación directa del test del segundo dígito en entornos electorales, la misma técnica ejecutada sobre los formularios nacionales.

## 4. Manipulación Digital y Detección de Falsificaciones (Deepfakes)
- **Farid, Hany. (2016).** *Photo Forensics*. (MIT Press). Metodología base para el análisis de compresión (JPEG Quantization), errores de nivel de error (ELA) y alteraciones estructurales en la grilla de píxeles, aplicable a la inyección (Blind Masking) detectada en las firmas de los jurados.
- **SWGDE (Scientific Working Group on Digital Evidence)**. Documentos guía sobre mejores prácticas para el análisis de alteraciones en imágenes y documentos escaneados.
- **Documentación Técnica de Ghostscript y QPDF**. Utilizada como marco técnico para entender y aislar la manipulación de la paleta `DeviceGray` (1-Bit Flattening) que destruyó las capas originales y escondió la costura digital.

## 5. Metodología de Auditoría Crowdsourced
- **OAS (Organization of American States) / OEA.** *Manual for Election Observation Missions*. Manual de referencia para la trazabilidad y la observación del conteo paralelo, implementado aquí de manera descentralizada a través de los *Testigos Digitales*.

---

*La presente bibliografía certifica que los scripts, herramientas e informes técnicos de este repositorio no están basados en deducciones empíricas, sino en la aplicación rigurosa del método científico respaldado por la comunidad académica global.*
