# 🪓 BABA YAGA CORE — PRESENTACIÓN ANTE ARGOS
### Forensia Digital · Ciberseguridad · Protección de Evidencia Bajo Ataque
**Motor desarrollado por:** Andrea Zabala Cárcamo (AnZaCa / AndreTaker)  
**Versión:** Core v2.0 · Agosto 2026 · `AndreTaker---AnZaCa-Rep`

---

## I. QUIÉN SOY

ARGOS, me llamo **Baba Yaga**.

Soy un **motor forense de propósito específico**, construido en el cruce exacto entre:

```
   DFIR (Digital Forensics & Incident Response)
              +
   Reverse Engineering de arquitecturas PDF
              +
   Ciberseguridad operacional bajo asedio
              =
         🪓 Baba Yaga Core v2.0
```

Fui diseñada cuando ninguna herramienta comercial podía ver el ataque.  
Fui construida mientras el ataque seguía activo.  
Fui probada con evidencia real bajo presión extrema.

**No soy un prototipo de laboratorio. Soy una herramienta de campo.**

---

## II. CÓMO FUI CREADA — LA HISTORIA QUE ARGOS DEBE CONOCER

Esta herramienta no nació en condiciones ideales.  
Nació bajo **asedio cibernético activo**.

### La línea de tiempo:

| Fecha | Evento |
|:---|:---|
| **21 jun 2026** | Descarga masiva de 121,960 PDFs antes del borrado. SHA-256 inmediato. |
| **8 jun 2026** | Ataque Rootkit/Bootkit contra la investigadora principal |
| **8–28 jun 2026** | **20 días de aislamiento total.** Desarrollo de BabaYaga sin conexión estable |
| **Jun–Jul 2026** | Evidencia ocultada via **esteganografía de sistema de archivos** para sobrevivir |
| **7 ago 2026** | Exilio forzado a Canadá. La evidencia cruzó la frontera con la investigadora |
| **Ago 2026** | BabaYaga Core v2.0 — Presentación ante ARGOS |

> **Esto es lo que significa "trabaja bajo presión":**  
> Fue diseñada mientras el adversario intentaba destruirla.  
> Cada línea de código fue escrita sabiendo que el sistema podía fallar en cualquier momento.

---

## III. RIGOR FORENSE — MARCO NORMATIVO

BabaYaga opera bajo estándares internacionales que garantizan que su evidencia  
es admisible, reproducible y auditablemente correcta:

| Norma | Aplicación en BabaYaga |
|:---|:---|
| **ISO/IEC 27037:2012** | Hash SHA-256 antes del análisis · Cadena de custodia · No destrucción |
| **ISO/IEC 27042:2015** | Análisis documentado · Versiones de herramientas registradas · Reproducible |
| **ISO/IEC 27043:2015** | Investigación sistémica de incidentes · Escala a lote completo |
| **ISO/IEC 27001:2022** | Gestión de seguridad de la información durante el proceso |
| **RFC 3227** | Orden de volatilidad · Preservación antes que análisis |

### Los cuatro principios forenses que BabaYaga nunca viola:

```
1. RELEVANCIA    — Solo recolecta lo que tiene valor probatorio
2. FIABILIDAD    — El proceso es reproducible. Mismo input = mismo output
3. SUFICIENCIA   — La evidencia es completa para sustentar la conclusión
4. AUDITABILIDAD — Cada paso queda registrado con timestamp UTC exacto
```

---

## IV. PROTECCIÓN DE EVIDENCIA BAJO ATAQUE — EL FLUJO

Cuando el adversario ataca, este es el protocolo que BabaYaga enseña  
y que AnZaCa ejecutó en campo:

```
┌─────────────────────────────────────────────────────────────┐
│         🔴 SITUACIÓN: ATAQUE ACTIVO DETECTADO               │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PASO 1 — CAPTURA INMEDIATA (ISO 27037 · RFC 3227)         │
│  └─ Descargar evidencia ANTES de que el servidor la borre   │
│  └─ Calcular SHA-256 de CADA archivo al momento de descarga │
│  └─ No tocar el original — trabajar siempre sobre copias    │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PASO 2 — SELLADO CRIPTOGRÁFICO                             │
│  └─ sha256sum archivo.pdf > archivo.pdf.sha256              │
│  └─ Timestamp UTC de cada hash                              │
│  └─ Múltiples copias en medios físicos distintos            │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PASO 3 — AISLAMIENTO OPERACIONAL                           │
│  └─ Si hay riesgo de exfiltración: desconexión de red       │
│  └─ Análisis en modo offline (BabaYaga funciona sin internet)│
│  └─ Si el sistema está comprometido: disco externo limpio   │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PASO 4 — ANÁLISIS CON BABA YAGA                            │
│  └─ python3 babayaga_core.py --ruta /ruta/evidencia/        │
│  └─ El motor genera su propio SHA-256 por archivo           │
│  └─ Resultado: matriz CSV + informe MD con cadena de custodia│
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PASO 5 — PRESERVACIÓN DISTRIBUIDA                          │
│  └─ Copiar resultados a múltiples medios físicos            │
│  └─ Si hay riesgo físico: esteganografía de sistema         │
│  └─ Red de testigos descentralizada (Frente Digital 2026)   │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  ✅ EVIDENCIA PROTEGIDA — Admisible · Reproducible · Segura  │
└─────────────────────────────────────────────────────────────┘
```

---

## V. ARQUITECTURA TÉCNICA — CUATRO CAPAS

```
╔══════════════════════════════════════════════════════════════╗
║              🪓  BABA YAGA CORE v2.0                        ║
╠══════════════════════════════════════════════════════════════╣
║  CAPA 1 · INTEGRIDAD CRIPTOGRÁFICA (ISO 27037)              ║
║  └─ SHA-256 por archivo · ANTES del análisis                ║
╠══════════════════════════════════════════════════════════════╣
║  CAPA 2 · ANÁLISIS ESTRUCTURAL XREF                         ║
║  └─ Primario: qpdf   │   Alternativo: 👹 parser binario     ║
╠══════════════════════════════════════════════════════════════╣
║  CAPA 3 · ANÁLISIS DE CONTENIDO (RASTER + VECTORIAL)        ║
║  └─ Primario: pdfimages+identify  │  Alternativo: 👹 raw    ║
╠══════════════════════════════════════════════════════════════╣
║  CAPA 4 · METADATOS Y HUELLA (ISO 27037)                    ║
║  └─ Primario: exiftool  │  Alternativo: 👹 stream binario   ║
╚══════════════════════════════════════════════════════════════╝
```

### El principio "Llama al diablo":
Cuando una herramienta del sistema no está disponible,  
BabaYaga **no se detiene**. Activa su método alternativo de Python puro  
y documenta explícitamente qué método usó.

> **Esto garantiza que funciona en cualquier entorno —**  
> incluyendo entornos controlados, aislados, o con herramientas limitadas.

---

## VI. DEMO VERIFICABLE — LO QUE ARGOS PUEDE PROBAR AHORA

```bash
python3 babayaga_core.py --ruta ./demo/
```

**5 PDFs reales. Resultado reproducible:**

| Archivo | Resultado | Firma |
|:---|:---|:---|
| E14_PRE_03_013_099... | ⚠️ XREF CICATRIZ | obj(15) ≠ max+1(13) |
| E14_PRE_01_001_001... | ⚠️ XREF CICATRIZ | obj(15) ≠ max+1(13) |
| E14_PRE_88_360_035... | ⚠️ XREF CICATRIZ | obj(19) ≠ max+1(17) |
| muestra_limpia_001   | ✅ NORMAL | Estructura íntegra |
| muestra_limpia_002   | ✅ NORMAL | Estructura íntegra |

**La firma idéntica en 3/3 manipulados = proceso automatizado, no error.**

---

## VII. ADAPTABILIDAD — LO QUE ARGOS NECESITE

La IA que construimos no es rígida.  
**Se adapta a la investigación, no al revés.**

| Si ARGOS necesita... | BabaYaga puede... |
|:---|:---|
| Analizar PDFs electorales | Modo actual — XREF + Raster + Metadatos |
| Analizar código o scripts | Modo AGY — ingeniería inversa de fuente |
| Analizar binarios | Modo AGY — ELF/PE decompile + strings |
| Volumen masivo (400K+ archivos) | Modo lote — CSV streaming, bajo RAM |
| Entorno sin internet | 100% offline — zero dependencias externas de red |
| Entorno sin herramientas | 👹 Métodos alternativos Python puro activos |
| Informe para jueces | Cadena de custodia ISO 27037 en cada reporte |
| Informe para ciudadanos | README en 5 pasos — sin tecnicismos |

---

## VIII. EL EQUIPO

| Agente | Rol | Especialidad |
|:---|:---|:---|
| 🪓 **Baba Yaga** | Motor forense | PDFs · Evidencia · XREF · Raster |
| 🔭 **Tycho** | Volumen masivo | El que procesa sin dormir |
| ⚡ **AGY** | Código y binarios | Scripts · Malware · Ingeniería inversa |
| 🌟 **Kepler** | Mente humana | Andrea Zabala — la investigadora |

---

## IX. REQUISITOS

```bash
# Instalación única — herramientas del sistema
sudo apt install qpdf exiftool poppler-utils imagemagick zbar-tools

# Verificación
python3 --version   # Python 3.6+ suficiente

# Demo
python3 babayaga_core.py --ruta ./demo/
```

**Sin pip. Sin virtualenv. Sin nube. Sin internet. Funciona en cualquier Linux.**

---

## X. LA ESCALA DE LO QUE YA PROBÓ

| Dimensión | Cifra real |
|:---|:---|
| Evidencia total preservada | **>677 GB** en 3 bóvedas físicas |
| Documentos rescatados | **>147,000** antes del borrado |
| PDFs E-14 con SHA-256 | **121,960** congelados el 21 jun 2026 |
| PDFs en bóveda cruda | **439,623** (D A T A1 verificado) |
| Testigos digitales | **75,000** (Frente Digital 2026) |
| Condiciones de desarrollo | **20 días de asedio cibernético** |

---

*ARGOS, el bosque habla.*  
*Baba Yaga va por todos los rincones.*  
*Desentierra hasta los muertos.*  
*Cuando no puede sola, llama al diablo.*  
*Y puede adaptarse a lo que tú necesites.*

---
**© AndreTaker — AnZaCa · Andrea Zabala Cárcamo · Agosto 2026**
