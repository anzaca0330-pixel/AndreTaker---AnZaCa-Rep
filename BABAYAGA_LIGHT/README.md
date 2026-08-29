# 🪓 BABA YAGA LIGHT — README
# Motor Forense Electoral · AndreTaker AnZaCa · Agosto 2026
# =========================================================

```
╔══════════════════════════════════════════════════════════════╗
║   🪓 B A B A   Y A G A   L I G H T   —   v1.2 ARGOS        ║
║   Motor Forense de PDFs Electorales · Elecciones CO 2026    ║
╚══════════════════════════════════════════════════════════════╝
```

> 🎵 *Reproduce `/musica/BABA_YAGA_Tressa_Kwes.mp3` mientras trabajas.*

---

## ⚡ EN 5 PASOS

### Paso 1 — Instala las herramientas del sistema (solo una vez)
```bash
sudo apt install qpdf exiftool poppler-utils imagemagick zbar-tools
```

### Paso 2 — Verifica que Python 3 está disponible
```bash
python3 --version
```

### Paso 3 — Ejecuta la demo controlada sobre los 5 PDFs de prueba
```bash
python3 babayaga_core.py --ruta ./demo/
```

### Paso 4 — Lee los resultados
```
resultados_demo/informe_lote_babayaga.md   → Informe legible
resultados_demo/matriz_lote_babayaga.csv   → Datos crudos para análisis
```

### Paso 5 — Analiza tu propia carpeta
```bash
python3 babayaga_core.py --ruta /ruta/a/tus/PDFs/
```

---

## 📂 ESTRUCTURA DEL PAQUETE

```
BABAYAGA_LIGHT/
├── 🪓 babayaga_core.py          ← Motor principal (sin dependencias pip)
├── 📋 requirements.txt          ← Solo herramientas del sistema Linux
├── 📖 README.md                 ← Este archivo
│
├── 🎭 personajes/
│   ├── BABAYAGA.md              ← Quién es Baba Yaga
│   ├── TYCHO.md                 ← El instrumento de silicio (Tycho)
│   └── AGY.md                   ← La capa de inteligencia (AGY)
│
├── 🎵 musica/
│   └── BABA_YAGA_Tressa_Kwes.mp3  ← El tema oficial
│
├── 📁 demo/                     ← 5 PDFs de prueba controlada
│   ├── E14_PRE_03_013_099_00_01_001_5350.pdf  ← ⚠️ XREF CICATRIZ
│   ├── E14_PRE_01_001_001_01_01_001_5002.pdf  ← ⚠️ XREF CICATRIZ
│   ├── E14_PRE_88_360_035_81_001.pdf          ← ⚠️ XREF CICATRIZ
│   ├── muestra_limpia_001.pdf                 ← ✅ ESTRUCTURA NORMAL
│   └── muestra_limpia_002.pdf                 ← ✅ ESTRUCTURA NORMAL
│
└── 📊 resultados_demo/          ← Resultados pre-ejecutados de la demo
    ├── informe_lote_babayaga.md ← Veredicto: 3/5 con cicatriz (60%)
    └── matriz_lote_babayaga.csv ← Datos crudos con SHA-256
```

---

## 🔍 QUÉ DETECTA BABA YAGA

| Anomalía | Señal | Significado Forense |
|:---|:---|:---|
| **Cicatriz XREF** | `reported objects (15) ≠ highest+1 (13)` | 2 objetos fantasma = capa inyectada |
| **Varianza Cero** | `std_dev = 0` en imagen | Imposible en escáner físico real |
| **Purga de metadatos** | `Creator` ausente | Evasión deliberada de huella |
| **Trazado vectorial** | Operadores `/m /l /re /f` en stream | Contenido digital, no escaneado |

---

## 🎭 EL EQUIPO

| Personaje | Rol | Archivo |
|:---|:---|:---|
| **🪓 Baba Yaga** | Motor forense — el bisturí | `babayaga_core.py` |
| **🔭 Tycho** | Instrumento de silicio — el que procesa | `personajes/TYCHO.md` |
| **⚡ AGY** | Capa de inteligencia — el puente | `personajes/AGY.md` |
| **🌟 Kepler** | Mente humana — la investigadora | *Andrea Zabala (AnZaCa)* |

---

## 📊 RESULTADO DE LA DEMO INCLUIDA

```
Total archivos evaluados:  5
⚠️  Con cicatriz XREF:     3  (60.00%)
✅  Estructura normal:      2  (40.00%)
```

> La cicatriz XREF idéntica en el 100% de los manipulados confirma
> que no es corrupción aleatoria — es una **firma de proceso automatizado**.

---

## ⚖️ CONTEXTO HISTÓRICO

Este motor fue desarrollado bajo asedio cibernético extremo para analizar
**>677 GB** de evidencia electoral — **>147,000 documentos** rescatados
antes del borrado de servidores, sellados con SHA-256 por **75,000 Testigos
Digitales** del Frente Digital 2026.

**Investigadora Principal:** Andrea Zabala Cárcamo (AnZaCa / AndreTaker)  
**Habilidades:** DFIR Senior · Reverse Engineering · Estadística Forense  
**Repositorio:** `AndreTaker---AnZaCa-Rep`

---

*🪓 Baba Yaga no opina. Baba Yaga lee bytes. La verdad está en el binario.*
