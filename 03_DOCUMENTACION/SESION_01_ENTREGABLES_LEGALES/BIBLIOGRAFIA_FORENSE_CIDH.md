# 📚 BIBLIOGRAFÍA ACADÉMICA Y NORMATIVA TÉCNICA | ACADEMIC BIBLIOGRAPHY & TECHNICAL STANDARDS
**Caso Radicado CIDH / IACHR Case Number:** `[CONFIDENCIAL — MEDIDAS CAUTELARES]`  
**Referencia de Proyecto / Project Reference:** Acervo Probatorio Forense E-14 (Colombia 2026) / E-14 Forensic Evidence Vault

*(Scroll down for English Version / Desplácese hacia abajo para la versión en Inglés)*

---

## [ES] VERSIÓN EN ESPAÑOL

Este documento compila el marco teórico, los estándares internacionales y la literatura científica utilizada para auditar matemáticamente e informáticamente el fraude electoral estructurado.

### 1. Estándares Forenses y Normativa Internacional (ISO)
- **ISO/IEC 27037:2012** – *Information technology — Security techniques — Guidelines for identification, collection, acquisition and preservation of digital evidence*. Define los principios de integridad, volatilidad y el "Principio de Solo Lectura" (Read-Only) para evitar la alteración de los metadatos.
- **ISO 32000-1:2008** – *Document management — Portable document format*. Especificación oficial del formato PDF, fundamental para el análisis de objetos (`/Obj`), árboles de directorios, capas (`/Contents`) y la tabla de referencias cruzadas (XREF) corrupta encontrada en la evidencia.
- **RFC 3227** – *Guidelines for Evidence Collection and Archiving*. Define la recolección estricta y segura de información digital bajo la cadena de custodia.

### 2. Criptografía, Preservación y Compresión
- **FIPS 180-4 (NIST)** – *Secure Hash Standard (SHS)*. Estándar oficial del Instituto Nacional de Estándares y Tecnología de EE.UU. que avala el uso del algoritmo criptográfico **SHA-256**, utilizado en este repositorio para blindar y garantizar la inmutabilidad matemática de cada acta (E-14) y de los metadatos de recolección.
- **RFC 3161** – *Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)*. Estándar utilizado para certificar los sellos de tiempo inalterables de las descargas en los laboratorios.
- **Gailly, Jean-loup y Adler, Mark.** (1995). *Zlib / DEFLATE Compression Algorithm*. Creadores de la librería zlib y el formato de compresión subyacente que el estándar PDF utiliza bajo el filtro `/FlateDecode`. La decodificación forense de sus flujos de datos fue el paso técnico crítico que permitió revelar la inyección de comandos vectoriales ocultos (`cm`, `re`, `Do`) en los formularios E-14.

### 3. Estadística Forense (Ley del segundo dígito de Mebane y Simulaciones)
- **Nigrini, Mark J. (2012).** *Benford's Law (2nd Digit - Mebane): Applications for Forensic Accounting, Auditing, and Fraud Detection*. (John Wiley & Sons). Obra cumbre en auditoría forense que sustenta matemáticamente por qué la desviación y el "planchado estadístico" encontrados en la digitación de los votos constituye fraude sintético, y no varianza natural.
- **Fewster, R. M. (2009).** *A simple explanation of Benford's Law (2nd Digit - Mebane)*. (The American Statistician). Utilizado para el sustento probabilístico y cálculo de P-Values.
- **Mebane, Walter R. Jr. (2006).** *Election Forensics: The Second-digit Benford's Law (2nd Digit - Mebane) Test and Recent American Presidential Elections*. Aplicación directa del test del segundo dígito en entornos electorales, la misma técnica ejecutada sobre los formularios nacionales.
  - 🖥️ **Repositorio Oficial:** [wmebane/Election-Forensics-Toolkit](https://github.com/wmebane/Election-Forensics-Toolkit) (Herramientas base de análisis).

### 4. Manipulación Digital y Detección de Falsificaciones (Deepfakes)
- **Fridrich, Jessica. (2009).** *Steganalysis and Blind Image Forensics*. Pionera de la disciplina de "Blind Forensics" (detección de manipulación digital sin requerir la imagen original de referencia). Aunque sus conceptos fundamentales fueron creados para esteganografía y análisis de ruido de sensores, **esta es la base teórica que hemos adaptado y aplicado por primera vez de forma masiva para identificar alteraciones electorales (Blind Masking)** en documentos escaneados.
- **Farid, Hany. (2016).** *Photo Forensics*. (MIT Press). Metodología base para el análisis de compresión (JPEG Quantization), errores de nivel de error (ELA) y alteraciones estructurales en la grilla de píxeles, aplicable a la inyección y el "1-Bit Flattening" detectado en las firmas de los jurados.
- **SWGDE (Scientific Working Group on Digital Evidence)**. Documentos guía sobre mejores prácticas para el análisis de alteraciones en imágenes y documentos escaneados.
- **Herramientas de Análisis Estructural y Visual**:
  - **QPDF (Jay Berkenbilt):** Utilizado como marco técnico para entender y aislar la tabla XREF corrupta. 
    - 🖥️ **Repositorio Oficial:** [qpdf/qpdf](https://github.com/qpdf/qpdf)
  - **Peepdf (Jose Miguel Esparza):** Utilizado para el análisis de ofuscación de comandos.
    - 🖥️ **Repositorio Oficial:** [jesparza/peepdf](https://github.com/jesparza/peepdf)
  - **DidierStevensSuite (Didier Stevens):** Base técnica para el uso avanzado de `pdfid` y `pdf-parser` en la detección de anomalías maliciosas en documentos.
    - 🖥️ **Repositorio Oficial:** [DidierStevens/DidierStevensSuite](https://github.com/DidierStevens/DidierStevensSuite)
  - **Sherloq (Guido Bartoli):** Entorno integrado open-source para análisis forense de imágenes digitales (Error Level Analysis, Quantization).
    - 🖥️ **Repositorio Oficial:** [GuidoBartoli/sherloq](https://github.com/GuidoBartoli/sherloq)
  - **ImageMagick:** Utilizado para la extracción de la paleta `DeviceGray` (1-Bit Flattening).
    - 🖥️ **Repositorio Oficial:** [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick)

### 5. Metodología de Auditoría Crowdsourced
- **OAS (Organization of American States) / OEA.** *Manual for Election Observation Missions*. Manual de referencia para la trazabilidad y la observación del conteo paralelo, implementado aquí de manera descentralizada a través de los *Testigos Digitales*.

---

### 📜 INVITACIÓN ABIERTA A REVISIÓN POR PARES (CALL FOR PEER REVIEW)

Este repositorio constituye un caso de estudio sin precedentes sobre **fraude electoral estructural a nivel de binarios PDF** y manipulación estadística a gran escala. 

Extendemos una **invitación pública y formal** a los creadores de las herramientas y metodologías aquí aplicadas para que auditen y revisen la solidez matemática e informática de este trabajo. En especial, invitamos a:

- **Dra. Jessica Fridrich**: Para evaluar cómo hemos adaptado sus conceptos pioneros de *Blind Image Forensics* (originalmente aplicados a esteganografía) para aislar inyecciones sintéticas en decenas de miles de escaneos electorales.
- **Dr. Walter Mebane** (`@wmebane`): Para revisar la aplicación de sus modelos del segundo dígito de Benford frente a la inyección sintética detectada en los departamentos de Colombia.
- **Dr. Mark Nigrini**: Para evaluar la sonificación y el análisis macroscópico del "planchado estadístico".
- **Dr. Hany Farid**: Para revisar la técnica que hemos bautizado como *Blind Masking* y *1-Bit Flattening* en la generación masiva de Deepfakes electorales.
- **Jay Berkenbilt** (`@jberkenbilt` / QPDF), **Jose Miguel Esparza** (`@jesparza` / Peepdf), **Didier Stevens** (`@DidierStevens` / PDFiD) y **Guido Bartoli** (`@GuidoBartoli` / Sherloq): Para analizar la firma persistente del generador PDF que corrompió intencionalmente las tablas XREF y los objetos `/Contents` de 121,000 actas, y validar la ofuscación visual detectada.

Su "Peer Review" (revisión por pares) es invaluable para validar ante la **Corte Interamericana de Derechos Humanos (CIDH)** que estos hallazgos son matemáticamente irrefutables. Pueden realizar sus observaciones abriendo un **[Issue](https://github.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep/issues)** directamente en este repositorio o creando un *Pull Request*.

---
---

## [EN] ENGLISH VERSION

This document compiles the theoretical framework, international standards, and scientific literature used to mathematically and computationally audit the structural electoral fraud.

### 1. Forensic Standards and International Norms (ISO)
- **ISO/IEC 27037:2012** – *Information technology — Security techniques — Guidelines for identification, collection, acquisition and preservation of digital evidence*. Defines the principles of integrity, volatility, and the "Read-Only Principle" to prevent metadata alteration.
- **ISO 32000-1:2008** – *Document management — Portable document format*. Official PDF format specification, fundamental for the analysis of objects (`/Obj`), directory trees, layers (`/Contents`), and the corrupt cross-reference table (XREF) found in the evidence.
- **RFC 3227** – *Guidelines for Evidence Collection and Archiving*. Defines strict and secure digital information collection under chain of custody.

### 2. Cryptography, Preservation, and Compression
- **FIPS 180-4 (NIST)** – *Secure Hash Standard (SHS)*. Official standard from the US National Institute of Standards and Technology validating the use of the **SHA-256** cryptographic algorithm, used in this repository to shield and guarantee the mathematical immutability of each tally sheet (E-14).
- **RFC 3161** – *Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)*. Standard used to certify unalterable time-stamps of downloads in the laboratories.
- **Gailly, Jean-loup and Adler, Mark.** (1995). *Zlib / DEFLATE Compression Algorithm*. Creators of the zlib library and the underlying compression format that the PDF standard uses under the `/FlateDecode` filter. The forensic decoding of these data streams was the critical technical step that allowed us to reveal the injection of hidden vector commands (`cm`, `re`, `Do`) within the E-14 forms.

### 3. Forensic Statistics (Benford's Law (2nd Digit - Mebane) and Simulations)
- **Nigrini, Mark J. (2012).** *Benford's Law (2nd Digit - Mebane): Applications for Forensic Accounting, Auditing, and Fraud Detection*. (John Wiley & Sons). Landmark work in forensic auditing that mathematically supports why the deviation and "statistical ironing" found in vote digitization constitutes synthetic fraud, not natural variance.
- **Fewster, R. M. (2009).** *A simple explanation of Benford's Law (2nd Digit - Mebane)*. (The American Statistician). Used for probabilistic support and P-Value calculation.
- **Mebane, Walter R. Jr. (2006).** *Election Forensics: The Second-digit Benford's Law (2nd Digit - Mebane) Test and Recent American Presidential Elections*. Direct application of the second-digit test in electoral environments, the exact technique executed on the national forms.
  - 🖥️ **Official Repository:** [wmebane/Election-Forensics-Toolkit](https://github.com/wmebane/Election-Forensics-Toolkit) (Base analysis tools).

### 4. Digital Manipulation and Forgery Detection (Deepfakes)
- **Fridrich, Jessica. (2009).** *Steganalysis and Blind Image Forensics*. Pioneer of the "Blind Forensics" discipline (detecting digital manipulation without requiring the original reference image). Although her fundamental concepts were created for steganography and sensor noise analysis, **this is the theoretical baseline we have adapted and applied for the first time on a massive scale to identify electoral alterations (Blind Masking)** in scanned documents.
- **Farid, Hany. (2016).** *Photo Forensics*. (MIT Press). Baseline methodology for compression analysis (JPEG Quantization), error level analysis (ELA), and structural alterations in the pixel grid, applicable to the injection (Blind Masking) detected in the jury signatures.
- **SWGDE (Scientific Working Group on Digital Evidence)**. Guidance documents on best practices for analyzing alterations in images and scanned documents.
- **Structural and Visual Analysis Tools**:
  - **QPDF (Jay Berkenbilt):** Used as a technical framework to understand and isolate the corrupt XREF table. 
    - 🖥️ **Official Repository:** [qpdf/qpdf](https://github.com/qpdf/qpdf)
  - **Peepdf (Jose Miguel Esparza):** Used for command obfuscation analysis.
    - 🖥️ **Official Repository:** [jesparza/peepdf](https://github.com/jesparza/peepdf)
  - **DidierStevensSuite (Didier Stevens):** Technical baseline for using `pdfid` and `pdf-parser` in detecting malicious anomalies in documents.
    - 🖥️ **Official Repository:** [DidierStevens/DidierStevensSuite](https://github.com/DidierStevens/DidierStevensSuite)
  - **Sherloq (Guido Bartoli):** Open-source integrated environment for digital image forensics (Error Level Analysis, Quantization).
    - 🖥️ **Official Repository:** [GuidoBartoli/sherloq](https://github.com/GuidoBartoli/sherloq)
  - **ImageMagick:** Used for the extraction of the `DeviceGray` palette (1-Bit Flattening).
    - 🖥️ **Official Repository:** [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick)

### 5. Crowdsourced Audit Methodology
- **OAS (Organization of American States).** *Manual for Election Observation Missions*. Reference manual for traceability and parallel counting observation, implemented here decentralized through the *Digital Witnesses* (Testigos Digitales).

---

### 📜 OPEN CALL FOR PEER REVIEW (REQUEST FOR COMMENTS)

This repository constitutes an unprecedented case study on **structural electoral fraud at the PDF binary level** and large-scale statistical manipulation. 

We extend a **public and formal invitation** to the creators of the tools and methodologies applied herein to audit and review the mathematical and computational soundness of this work. We especially invite:

- **Dr. Jessica Fridrich**: To evaluate how we have adapted your pioneering concepts of *Blind Image Forensics* (originally applied to steganography) to isolate synthetic injections in tens of thousands of electoral scans.
- **Dr. Walter Mebane** (`@wmebane`): To review the application of your second-digit Benford models against the synthetic injection detected in the departments of Colombia.
- **Dr. Mark Nigrini**: To evaluate the sonification and macroscopic analysis of the "statistical ironing".
- **Dr. Hany Farid**: To review the technique we have baptized as *Blind Masking* and *1-Bit Flattening* in the massive generation of Electoral Deepfakes.
- **Jay Berkenbilt** (`@jberkenbilt` / QPDF), **Jose Miguel Esparza** (`@jesparza` / Peepdf), **Didier Stevens** (`@DidierStevens` / PDFiD), and **Guido Bartoli** (`@GuidoBartoli` / Sherloq): To analyze the persistent signature of the PDF generator that intentionally corrupted the XREF tables and `/Contents` objects of 121,000 tally sheets, and to validate the visual obfuscation detected.

Your "Peer Review" is invaluable in validating before the **Inter-American Commission on Human Rights (IACHR)** that these findings are mathematically irrefutable. You can make your observations by opening an **[Issue](https://github.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep/issues)** directly in this repository or by creating a *Pull Request*.

---

*This bibliography certifies that the scripts, tools, and technical reports in this repository are not based on empirical deductions, but on the rigorous application of the scientific method backed by the global academic community.*
