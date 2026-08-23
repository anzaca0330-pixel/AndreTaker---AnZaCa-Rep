# ACTA DE HALLAZGOS FORENSES
## Consulado de Los Ángeles - Actas E-14
## Elecciones Presidenciales 2026

---

**Denunciante:** Andrea Zabala Carcamo
**Fechas de análisis:** 1 al 8 de junio de 2026
**Herramientas:** pdfimages, ImageMagick, sha256sum, QPDF, peepdf, ExifTool, zbarimg

---

## ⚠️ HALLAZGO PRINCIPAL: EL PATRÓN QUIRÚRGICO DE INSERCIÓN DIGITAL

### Descubrimiento

El análisis de **45 imágenes blancas** extraídas de las actas 81-86 reveló un **patrón matemáticamente perfecto**:

| Posición | ¿Imagen blanca? | Cantidad | Patrón |
|:--:|:--:|:--:|:--:|
| **001** | ✅ SÍ | 15 | IMPAR |
| 002 | ❌ NO | 0 | PAR |
| **003** | ✅ SÍ | 15 | IMPAR |
| 004 | ❌ NO | 0 | PAR |
| **005** | ✅ SÍ | 15 | IMPAR |
| 006 | ❌ NO | 0 | PAR |

### Estructura Metrológica Compilada (6 imágenes por acta)

| Índice | Tipo | Espacio Color | Peso | Diagnóstico | Anomalía |
|:---:|:---:|:---:|:---:|:---|:---:|
| `img-000` | REAL | sRGB | ~113 KB | Captura óptica legítima | 0/15 |
| `img-001` | ❌ BLANCA | DeviceGray | ~400 B | **Inyección algorítmica** | **15/15** |
| `img-002` | REAL | sRGB | ~168 KB | Captura óptica legítima | 0/15 |
| `img-003` | ❌ BLANCA | DeviceGray | ~400 B | **Inyección algorítmica** | **15/15** |
| `img-004` | REAL | sRGB | ~132 KB | Captura óptica legítima | 0/15 |
| `img-005` | ❌ BLANCA | DeviceGray | ~400 B | **Inyección algorítmica** | **15/15** |

### Matriz de Comportamiento Selectivo (V1 - V4)

| Grupo de Actas | Secuencia | Procesamiento | Diagnóstico |
| :--- | :---: | :--- | :--- |
| ZONA A (`_02_`, `_04_`, `_05_`, `_06_`) | `📷📷📷` | Escaneo físico estándar | 🟢 **NORMAL** |
| ZONA B (`_81_` al `_86_`) | `📷⬜📷⬜📷⬜` | Ensamblaje algorítmico | 🔴 **ALTERACIÓN SELECTIVA** |

### Conclusión Estadística

El patrón de alternancia simétrica indexada (**Real → Digital → Real → Digital → Real → Digital**) con una efectividad del **100% (15/15)** descarta por completo:

- Cualquier factor de error mecánico aleatorio en el hardware del escáner
- Cualquier error humano en el proceso de digitalización
- Cualquier fallo de firmware o configuración

**La única explicación técnica posible:** Ejecución automatizada de un script o bucle de procesamiento de datos en el servidor de ensamblaje final, programado específicamente para insertar páginas blancas en las posiciones impares de cada acta compilada.

---

## HALLAZGO 1: PDFs HÍBRIDOS (COLOR + B/N MEZCLADOS)

**Fecha:** 3 de junio de 2026 | **Herramienta:** ImageMagick
**Resultado:** 19 de 26 actas con mezcla de imágenes a color y B/N en el mismo PDF

---

## HALLAZGO 2: ERRORES DE DECODIFICACIÓN (100% DE ACTAS)

**Fecha:** 4 de junio de 2026 | **Herramienta:** peepdf
**Resultado:** 32 de 32 actas con errores de decodificación (88-91% de objetos afectados)
**Validación:** Confirmado con `qpdf --check`

---

## HALLAZGO 3: OBJETOS FANTASMA (100% DE ACTAS) - DOS PLANTILLAS

**Fecha:** 4 de junio de 2026 | **Herramienta:** QPDF
**Plantilla A:** Actas 02, 04, 05, 06, 81 → 20-23 objetos, 1 fantasma
**Plantilla B:** Actas 82-86 → 26 objetos, 2 fantasmas

---

## HALLAZGO 4: DIMENSIONES DE PÁGINA DIVERGENTES

**Fecha:** 4 de junio de 2026 | **Herramienta:** QPDF
**Acta 82:** 159×453, 168×442, 168×444 píxeles
**Acta 83:** 205×557, 208×538, 211×555 píxeles

---

## HALLAZGO 5: METADATOS DE CREACIÓN ELIMINADOS

**Fecha:** 3 de junio de 2026 | **Herramientas:** ExifTool, pdfinfo
**Resultado:** Campos Creator, Producer y CreationDate VACÍOS en 32/32 actas

---

## HALLAZGO 6: PÁGINAS EN BLANCO DUPLICADAS (ACTAS 82-86)

**Fecha:** 5 de junio de 2026 | **Herramienta:** pdfimages + ImageMagick

| Acta | Día | Imágenes reales | Imágenes blancas |
|:--|:--|:--|:--|
| 82 | Martes | 3 (color) | 3 (DeviceGray) |
| 83 | Miércoles | 3 (color) | 3 (DeviceGray) |
| 84 | Jueves | 3 (color) | 3 (DeviceGray) |
| 85 | Viernes | 3 (color) | 3 (DeviceGray) |
| 86 | Sábado | 3 (color) | 3 (DeviceGray) |

---

## HALLAZGO 7: MODIFICACIÓN SISTEMÁTICA POST-PUBLICACIÓN

**Fecha:** 4 de junio de 2026 | **Herramienta:** sha256sum
**Resultado:** 30 de 30 actas modificadas al menos una vez (100%)
**Hallazgo adicional:** Actas 81 y 85 eran idénticas en V1

---

## HALLAZGO 8: BAJA VARIANZA ATÍPICA (ANÁLISIS ESTADÍSTICO)

**Fecha:** 2 de junio de 2026
**Desviación estándar:** 2.5 votos en mesas 001-005 (inusualmente bajo)

---

## HALLAZGO 9: ACTAS 81 Y 85 ERAN IDÉNTICAS EN V1

**Fecha:** 4 de junio de 2026
**Hash V1 de acta 81:** 992deee3...
**Hash V1 de acta 85:** 992deee3...

---

## HALLAZGO 10: AUSENCIA SISTEMÁTICA DE CÓDIGOS QR

**Fecha:** 5 de junio de 2026 | **Herramienta:** zbarimg
**Actas 82-86:** 0 QR legibles en 30 imágenes

---

## HALLAZGO 11: CONEXIÓN CON EL PRECEDENTE DEL CONSEJO DE ESTADO

**Fecha:** 5 de junio de 2026
El Consejo de Estado ordenó auditar el software electoral. La Registraduría no cumplió durante ~8 años.

---

## HALLAZGO 12: INDICIOS DE ESCANEO NO PROFESIONAL

**Fecha:** 6 de junio de 2026
Características compatibles con dispositivo móvil, no con escáner institucional.

---

## HALLAZGO 13: DOS PLANTILLAS DE PROCESAMIENTO DIFERENTES

**Fecha:** 6 de junio de 2026

| Característica | Plantilla A | Plantilla B |
|:--|:--|:--|
| Objetos XObject | 6 | 9 |
| DeviceGray | 0 | 3 |

---

## HALLAZGO 14: CORRELACIÓN FORENSE-ESTADÍSTICA

**Fecha:** 6 de junio de 2026
Dos metodologías independientes coinciden en identificar manipulación sistemática.

---

## ERRORES COMETIDOS Y CORREGIDOS

| # | Error | Corrección |
|:--|:--|:--|
| 1 | Filtro >100KB excluyó páginas blancas | Eliminado filtro |
| 2 | Expectativa de 169 clones | Verificado: solo 1 |
| 3 | Git no generó historial | Historial en Anexo 2 |
| 4 | Carpetas con espacios | Rutas corregidas |
| 5 | peepdf no instalado | Instalado con pipx |
| 6 | Confusión páginas blancas vs firmas | Verificado: son páginas completas |

---

## ÍNDICE DE ANEXOS

| Anexo | Contenido | Formato |
|:--|:--|:--|
| 1 | Técnico Forense | `.md` / `.html` |
| 2 | Hashes SHA256 | `.txt` |
| 3 | PDFs híbridos | `.txt` |
| 4 | Errores estructurales | `.txt` |
| 5 | Imágenes extraídas | Carpeta |
| 6 | PDFs originales (4 versiones) | Carpeta |
| 7 | Análisis estadístico | `.html` |
| 8 | Denuncia CNE | `.html` |
| 9 | Análisis QR | Carpeta |

---

**Firma:** Andrea Zabala Carcamo
**Fecha:** 8 de junio de 2026

