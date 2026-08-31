# Híbrido Detector Multicapas: Desensamblaje de Deepfakes Documentales a Escala Institucional

**Investigadora Principal y Descubridora:** Andrea Zabala Carcamo (C.C. 43.925.102 | UOPX ID: [STUDENT-ID-REDACTED])  
**Afiliación:** Universidad de Phoenix (UOPX) - Prior Learning Assessment (PLA)  
**Dominio:** Auditoría Forense, Ciberdefensa, Análisis Estadístico  
**Fecha:** Agosto 2026  

---

## Abstracto Ejecutivo

La digitalización de procesos institucionales y electorales ha introducido una nueva superficie de ataque conocida como **Deepfake Documental Institucional**. Este documento presenta un *Forensic Toolkit* de código abierto diseñado específicamente para el procesamiento por lotes (Batch Processing) de cientos de miles de registros (PDFs) sospechosos de haber sido alterados sistémicamente desde servidores centrales.

Mientras las herramientas OSINT convencionales se limitan a analizar la metadata superficial o a auditar malware de forma individual, este marco forense opera bajo una arquitectura de **Híbrido Detector Multicapas**. La herramienta aborda tácticas avanzadas de evasión, incluyendo:

1.  **Manipulación Estructural XREF:** Detección de tablas de referencias cruzadas reescritas que ocultan la inyección de actas prefabricadas.
2.  **Blind Masking (Máscaras 1bpc):** Reversión de operaciones sintéticas destinadas a anular la visibilidad de códigos QR y firmas, logrando aislar visualmente las capas de sabotaje.
3.  **Flujos FlateDecode Ocultos:** Uso de parsers estructurales (`mutool`, `qpdf`) para desempaquetar y exponer información ofuscada algorítmicamente.
4.  **Evasión de Metadatos (Scrubbing):** Capacidad de auditar anomalías estructurales incluso cuando actores estatales o corporativos han eliminado intencionalmente los datos EXIF (Producer, ModifyDate).

Además de la extracción binaria, el ecosistema automatiza un cruce matemático renderizando la **Ley del segundo dígito de Mebane (2nd Digit)** y distribuciones de Gauss para correlacionar los hallazgos binarios con colapsos estadísticos a macroescala. El análisis enfocado en el segundo dígito anula las tácticas convencionales de camuflaje de datos, exponiendo la inyección sintética con precisión quirúrgica.

### Propiedad Intelectual y Licenciamiento
El descubrimiento primario de la alteración algorítmica, el aislamiento de las operaciones sintéticas (Blind Masking) y el desarrollo de la metodología estadística aquí documentados son producto exclusivo de la investigación independiente de Andrea Zabala Carcamo.
Esta herramienta y su metodología subyacente se liberan bajo **Licencia Apache 2.0**. Se autoriza su uso para peritajes independientes, investigaciones periodísticas y auditorías oficiales, garantizando el blindaje intelectual a través de su arquitectura Open Source, requiriendo citación obligatoria (Ver `CITATION.cff`).

El repositorio está diseñado para ser clonado e implementado por auditores sin necesidad de acceso a servidores internos, funcionando bajo un principio descentralizado de "No confíes, verifica".
