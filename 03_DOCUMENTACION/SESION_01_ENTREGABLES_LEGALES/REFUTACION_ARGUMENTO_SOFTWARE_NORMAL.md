# REFUTACIÓN TÉCNICA Y LEGAL AL ARGUMENTO DE "COMPORTAMIENTO NORMAL DEL SOFTWARE"

**Autora / Investigadora:** Andrea Zabala Cárcamo (AndreTaker AnZaCa)  
**Fecha:** 27 de agosto de 2026  
**Destino:** Equipo Legal, Tribunales e Investigadores Internacionales

---

## 🛑 EL ARGUMENTO DE LA DEFENSA INSTITUCIONAL
> *"La inconsistencia XREF (15 objetos declarados vs 13 presentes) y la presencia de imágenes grises/blancas son solo comportamientos normales del software de compilación, conversión o visualización del portal oficial."*

---

## 🛡️ REFUTACIÓN FORENSE EN 5 PUNTOS IRREFUTABLES

### 1. Violación del Estándar Internacional ISO 32000-1 (Especificación PDF)
* La especificación universal ISO 32000-1 prohíbe que la tabla de referencias cruzadas (`XREF`) declare direcciones a objetos inexistentes en el flujo (`reported 15 objects != highest 13`).
* Ningún software de digitalización comercial certificado (Kodak Alaris, Fujitsu PaperStream, Kofax Capture) produce archivos que violen la especificación ISO en su compilación nativa. Argumentar que "el software es así" equivale a admitir que el software oficial opera bajo código defectuoso y fuera de norma internacional.

### 2. La Prueba del Grupo de Control (Mesas Limpias)
* Si la cicatriz XREF fuera una característica intrínseca y "normal" del software de la Registraduría, **el 100% de las 117.993 actas E-14 de Colombia presentarían la misma falla**.
* **Resultado de la auditoría:** En el repositorio se preservan los lotes de **Mesas de Control Limpias** (`LISTADO_MESAS_LIMPIAS.md`). Existen miles de actas E-14 descargadas del mismo portal que son **PDF/A estándar 100% válidas (13 objetos declarados = 13 presentes, 0 advertencias `qpdf`, 0 máscaras sintéticas)**.
* **Inferencia Lógica:** Si el software fuera el origen general, afectaría al 100% del censo por igual. El hecho de que la cicatriz aparezca **exclusivamente de forma selectiva** en mesas de votación anticipada (mesas 81-86) y consulados clave demuestra una inyección focalizada, no un rasgo del sistema.

### 3. Física de Captura Óptica vs. Lienzos Sintéticos ($\sigma = 0$)
* Un escáner físico captura luz reflejada en papel. El ruido térmico del sensor óptico (CCD/CMOS) garantiza que un fondo blanco físico tenga variaciones de luminancia con desviación estándar $\sigma > 3.5$.
* Las imágenes extraídas por BabaYaga Core (`img-001`, `img-003`, `img-005`) registran **luminancia media 65.535 y desviación estándar $\sigma = 0$ (blanco sintético puro 1-bit)**.
* Ningún software de digitalización convierte áreas aleatorias de un documento en rectángulos de blanco sintético perfecto ($\sigma = 0$) superpuestos con precisión sobre las casillas de votación. Esto es una inyección de capas digitales en formato raster (`/DeviceGray`).

### 4. Invalidación Deliberada del Código QR
* El propósito primario del software de la Registraduría es leer el código QR impreso en el acta física para la clasificación automatizada de datos en el escrutinio.
* En las actas alteradas, el QR es suprimido o invisibilizado en el stream `/Contents`, arrojando `0 QR decoded` en los escáneres automáticos. Ningún software legítimo anula su propia herramienta de lectura y clasificación.

### 5. Mutación Criptográfica entre Versiones (SHA-256)
* Las descargas de la misma mesa entre el 1, 2, 3 y 4 de Junio demuestran que las actas sufrieron alteraciones criptográficas (cambios de firmas SHA-256) en el servidor post-publicación. Un software de visualización estático no altera los hashes de archivos ya cerrados en mesa.

---

## 🧠 CONCLUSIÓN PARA JUECES Y PERITOS
El argumento de "comportamiento normal del software" queda completamente desmontado. La presencia selectiva de la cicatriz XREF, la perfección sintética ($\sigma = 0$) de las máscaras y la existencia de actas limpias demuestran metrológicamente un **ensamblaje digital malicioso focalizado**.
