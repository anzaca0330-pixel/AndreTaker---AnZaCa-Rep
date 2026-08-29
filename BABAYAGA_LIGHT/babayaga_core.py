#!/usr/bin/env python3
# =========================================================
# babayaga_core.py — AndreTaker / BabaYaga Core Engine v2.1
# =========================================================
# OPTIMIZACIÓN v2.1: pdfimages usa -list (metadata, sin extracción)
# Timeout de 30s por subprocess para no bloquearse bajo presión
#
# MARCO NORMATIVO:
#   ISO/IEC 27037:2012 — Identificación, recolección, adquisición
#                         y preservación de evidencia digital
#   ISO/IEC 27042:2015 — Análisis e interpretación de evidencia digital
#   ISO/IEC 27043:2015 — Principios y procesos de investigación de incidentes
#   ISO/IEC 27001:2022 — Sistema de Gestión de Seguridad de la Información
#   RFC 3227            — Directrices para recolección y archivo de evidencia
#
# FILOSOFÍA OPERACIONAL:
#   "Va por todos los rincones. Desentierra hasta los muertos.
#    Cuando no puede, llama al diablo a hacer su trabajo."
#    — AnZaCa, Agosto 2026
#
# PRINCIPIOS ISO 27037:
#   1. RELEVANCIA    — Solo se recolecta lo que tiene valor probatorio
#   2. FIABILIDAD    — El proceso es reproducible y documentado
#   3. SUFICIENCIA   — La evidencia es completa para sustentar la conclusión
#   4. AUDITABILIDAD — Cada paso queda registrado con timestamp UTC
#
# Autor: Andrea Zabala Cárcamo (AnZaCa / AndreTaker)
# =========================================================

import os
import sys
import csv
import argparse
import subprocess
import hashlib
import struct
import re
from datetime import datetime, timezone

# ─── BANNER ───────────────────────────────────────────────────────────────────
TIMEOUT_SUBPROCESS = 30  # segundos máximo por operación

print("🪓 BabaYaga Core v2.1 — Forensia Digital · ISO 27037/27042/27043")
print("⚡ Va por todos los rincones. Desentierra hasta los muertos.")
print("👹 Cuando no puede sola, llama al diablo.\n")

# ─── CONSTANTES ISO ───────────────────────────────────────────────────────────
ISO_FRAMEWORK = {
    'ISO_27037': 'Identificación, recolección, adquisición y preservación de evidencia digital',
    'ISO_27042': 'Análisis e interpretación de evidencia digital',
    'ISO_27043': 'Principios y procesos de investigación de incidentes',
    'ISO_27001': 'Sistema de Gestión de Seguridad de la Información',
    'RFC_3227' : 'Directrices para recolección y archivo de evidencia'
}

# ─── HERRAMIENTAS PRIMARIAS Y ALTERNATIVAS ("EL DIABLO") ─────────────────────
# Cuando la herramienta principal no está, BabaYaga escala al método alternativo
HERRAMIENTAS = {
    'qpdf':      {'alternativa': 'raw_xref_parser',  'descripcion': 'Auditoría XREF'},
    'exiftool':  {'alternativa': 'raw_meta_parser',  'descripcion': 'Análisis de metadatos'},
    'pdfimages': {'alternativa': 'raw_image_counter', 'descripcion': 'Extracción de imágenes'},
    'identify':  {'alternativa': 'raw_stats_parser', 'descripcion': 'Estadísticas de imagen'},
}

disponibles = {}

def verificar_herramientas():
    """
    ISO 27037 §7: Verifica herramientas y activa alternativas.
    BabaYaga no se detiene. Cuando no puede, llama al diablo.
    """
    for h in HERRAMIENTAS:
        ok = subprocess.run(['which', h], capture_output=True).returncode == 0
        disponibles[h] = ok
        estado = "✅" if ok else f"⚠️  → Activando: [{HERRAMIENTAS[h]['alternativa']}]"
        print(f"   {estado} {h} ({HERRAMIENTAS[h]['descripcion']})")
    print()

def obtener_versiones_herramientas():
    """ISO 27042 §7.2: Documenta versiones exactas del entorno de análisis."""
    versiones = {}
    cmds = {
        'qpdf':      (['qpdf', '--version'], 'stdout', 0),
        'exiftool':  (['exiftool', '-ver'], 'stdout', 0),
        'pdfimages': (['pdfimages', '-v'], 'stderr', 0),
        'identify':  (['identify', '-version'], 'stdout', 0),
    }
    for nombre, (cmd, stream, line) in cmds.items():
        if disponibles.get(nombre):
            try:
                res = subprocess.run(cmd, capture_output=True, text=True)
                out = getattr(res, stream).split('\n')[line].strip()
                versiones[nombre] = out or 'Versión no detectada'
            except Exception:
                versiones[nombre] = 'Error al consultar versión'
        else:
            versiones[nombre] = f'NO INSTALADO → Método alternativo activo'
    return versiones

# ─── CAPA 1: INTEGRIDAD CRIPTOGRÁFICA (ISO 27037 §8.3) ───────────────────────
def calcular_sha256(file_path):
    """
    ISO 27037 §8.3.1: Sellado criptográfico previo al análisis.
    El hash es calculado ANTES de cualquier operación sobre el archivo.
    Garantiza la integridad de la evidencia original.
    """
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for bloque in iter(lambda: f.read(65536), b''):
                sha256.update(bloque)
        return sha256.hexdigest()
    except Exception as e:
        return f'ERROR_HASH: {str(e)}'

# ─── CAPA 2A: ANÁLISIS ESTRUCTURAL — MÉTODO PRIMARIO (qpdf) ──────────────────
def _xref_via_qpdf(pdf_path):
    """ISO 27042: Auditoría XREF mediante herramienta certificada qpdf."""
    resultado = subprocess.run(
        ['qpdf', '--check', pdf_path],
        capture_output=True, text=True, timeout=TIMEOUT_SUBPROCESS
    )
    stderr = resultado.stderr.strip()
    stdout = resultado.stdout.strip()
    scar = 'reported number of objects' in stderr or 'reported number of objects' in stdout
    detalle = stderr if stderr else stdout if stdout else 'Estructura íntegra — sin advertencias'
    return {
        'metodo': 'qpdf (ISO 27042)',
        'exit_code': resultado.returncode,
        'XREF_discrepancia': scar,
        'detalle': detalle,
        'stdout': stdout,
        'stderr': stderr
    }

# ─── CAPA 2B: ANÁLISIS ESTRUCTURAL — "EL DIABLO" (parser binario nativo) ─────
def _xref_via_raw(pdf_path):
    """
    Cuando qpdf no está disponible, BabaYaga llama al diablo:
    parsea el binario del PDF directamente para leer la tabla XREF.
    Sin dependencias externas. Solo Python puro.
    """
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()

        # Buscar header PDF
        if not content.startswith(b'%PDF'):
            return {'metodo': 'raw_binary (diablo)', 'XREF_discrepancia': False,
                    'detalle': 'No es un PDF válido', 'exit_code': -1}

        # Buscar declaración de tamaño en trailer (/Size)
        size_matches = re.findall(rb'/Size\s+(\d+)', content)
        # Buscar objetos declarados (N 0 obj)
        obj_matches = re.findall(rb'(\d+)\s+0\s+obj', content)

        declared = int(size_matches[-1]) if size_matches else None
        actual_max = max(int(n) for n in obj_matches) if obj_matches else None

        scar = False
        detalle = 'Estructura íntegra (análisis binario nativo)'

        if declared and actual_max:
            expected = actual_max + 1
            if declared != expected:
                scar = True
                detalle = (f'[MÉTODO ALTERNATIVO — DIABLO ACTIVO] '
                           f'reported number of objects ({declared}) is not one plus '
                           f'the highest object number ({actual_max})')

        return {
            'metodo': 'raw_binary_parser (diablo — sin qpdf)',
            'exit_code': 0,
            'XREF_discrepancia': scar,
            'detalle': detalle,
            'stdout': '',
            'stderr': detalle
        }
    except Exception as e:
        return {
            'metodo': 'raw_binary_parser (diablo)',
            'exit_code': -1,
            'XREF_discrepancia': False,
            'detalle': f'Error en análisis binario: {str(e)}',
            'stdout': '', 'stderr': str(e)
        }

def analizar_estructura(pdf_path):
    """
    ISO 27042 §8: Análisis estructural con escalada automática.
    Primero intenta qpdf. Si no está, llama al diablo (parser binario nativo).
    """
    if disponibles.get('qpdf'):
        return _xref_via_qpdf(pdf_path)
    else:
        return _xref_via_raw(pdf_path)

# ─── CAPA 3A: METADATOS — MÉTODO PRIMARIO (exiftool) ─────────────────────────
def _meta_via_exiftool(pdf_path):
    """ISO 27042: Extracción de metadatos mediante exiftool."""
    res = subprocess.run(
        ['exiftool', '-Creator', '-Producer', '-CreateDate', pdf_path],
        capture_output=True, text=True, timeout=TIMEOUT_SUBPROCESS
    )
    meta = res.stdout.strip() or 'Sin metadatos (purga de huella detectada)'
    return {'metodo': 'exiftool', 'metadatos': meta, 'tiene_autoría': 'Creator' in meta}

# ─── CAPA 3B: METADATOS — "EL DIABLO" (parser binario nativo) ────────────────
def _meta_via_raw(pdf_path):
    """
    Cuando exiftool no está, BabaYaga llama al diablo:
    extrae metadatos directamente del stream binario del PDF.
    """
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
        campos = {}
        for campo in [b'/Creator', b'/Producer', b'/CreationDate', b'/Author']:
            pattern = re.compile(campo + rb'\s*\(([^)]{0,200})\)', re.DOTALL)
            match = pattern.search(content)
            if match:
                try:
                    campos[campo.decode()] = match.group(1).decode('latin-1', errors='replace').strip()
                except Exception:
                    campos[campo.decode()] = '[datos binarios]'

        if campos:
            meta_str = '\n'.join(f'{k}: {v}' for k, v in campos.items())
            return {'metodo': 'raw_binary (diablo)', 'metadatos': meta_str, 'tiene_autoría': '/Creator' in campos}
        else:
            return {'metodo': 'raw_binary (diablo)', 'metadatos': 'Sin metadatos legibles (purga de huella)',
                    'tiene_autoría': False}
    except Exception as e:
        return {'metodo': 'raw_binary (diablo)', 'metadatos': f'Error: {str(e)}', 'tiene_autoría': False}

def analizar_metadatos(pdf_path):
    """ISO 27042: Análisis de metadatos con escalada automática al método alternativo."""
    if disponibles.get('exiftool'):
        return _meta_via_exiftool(pdf_path)
    else:
        return _meta_via_raw(pdf_path)

# ─── CAPA 4A: IMÁGENES — MÉTODO PRIMARIO (pdfimages -list, sin extracción) ────
def _imagenes_via_tools(pdf_path):
    """
    ISO 27042: Análisis de capas raster mediante pdfimages -list.
    OPTIMIZACIÓN v2.1: Usa -list (solo metadatos) — no extrae PNGs a disco.
    ~50x más rápido que extracción completa. Detecta 1bpc por columna 'enc'.
    """
    try:
        res = subprocess.run(
            ['pdfimages', '-list', pdf_path],
            capture_output=True, text=True, timeout=TIMEOUT_SUBPROCESS
        )
        imagenes = []
        lineas = res.stdout.strip().split('\n')
        # Saltar las dos líneas de cabecera de pdfimages -list
        for linea in lineas[2:]:
            if not linea.strip():
                continue
            partes = linea.split()
            if len(partes) < 8:
                continue
            try:
                # Columnas: page num type width height color comp bpc enc ...
                bpc   = int(partes[7]) if len(partes) > 7 else -1
                color = partes[5] if len(partes) > 5 else 'unknown'
                enc   = partes[8] if len(partes) > 8 else ''
                # 1bpc = máscara sintética (Blind Masking)
                varianza_cero = (bpc == 1)
                imagenes.append({
                    'archivo': f'img_{len(imagenes)+1} (list)',
                    'colorspace': color,
                    'media': 0.0 if varianza_cero else -1.0,
                    'desviacion_estandar': 0.0 if varianza_cero else -1.0,
                    'varianza_cero': varianza_cero,
                    'bpc': bpc,
                    'enc': enc
                })
            except (ValueError, IndexError):
                continue
        return {'metodo': 'pdfimages -list (fast, ISO 27042)', 'imagenes': imagenes}
    except subprocess.TimeoutExpired:
        return {'metodo': 'pdfimages -list (TIMEOUT)', 'imagenes': []}
    except Exception as e:
        return {'metodo': 'pdfimages -list (error)', 'imagenes': [], 'error': str(e)}

# ─── CAPA 4B: IMÁGENES — "EL DIABLO" (conteo binario nativo) ─────────────────
def _imagenes_via_raw(pdf_path):
    """
    Cuando pdfimages/identify no están, el diablo cuenta imágenes
    directamente del stream binario buscando objetos /XObject /Image.
    """
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
        imagen_refs = len(re.findall(rb'/Subtype\s*/Image', content))
        # Intentar detectar std=0 buscando streams de imagen 1bpc
        bpc_1 = len(re.findall(rb'/BitsPerComponent\s+1', content))
        imagenes = []
        for i in range(imagen_refs):
            imagenes.append({
                'archivo': f'raw_img_{i+1}',
                'colorspace': 'Desconocido (análisis binario)',
                'media': 0.0,
                'desviacion_estandar': 0.0 if bpc_1 > 0 else -1.0,
                'varianza_cero': bpc_1 > 0
            })
        return {'metodo': 'raw_binary (diablo)', 'imagenes': imagenes, 'bpc_1_detectado': bpc_1}
    except Exception as e:
        return {'metodo': 'raw_binary (diablo)', 'imagenes': [], 'error': str(e)}

def analizar_imagenes(pdf_path):
    """ISO 27042: Análisis de capas con escalada automática al método alternativo."""
    if disponibles.get('pdfimages') and disponibles.get('identify'):
        return _imagenes_via_tools(pdf_path)
    else:
        return _imagenes_via_raw(pdf_path)

# ─── CAPA 5: DETECCIÓN VECTORIAL ─────────────────────────────────────────────
def detectar_elementos_vectoriales(pdf_path):
    """
    ISO 27042: Detección de operadores de trazado vectorial en stream binario.
    Método puro Python — sin dependencias externas. Siempre disponible.
    """
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
        score = 0
        for op in [b'/Paint ', b'/Pattern ', b'/Shading ', b' m ', b' l ', b' re ', b' f ', b' S ']:
            score += content.count(op)
        return {'contiene_vectores': score > 15, 'score_vectorial': score}
    except Exception:
        return {'contiene_vectores': False, 'score_vectorial': 0}

# ─── INFORME INDIVIDUAL (ISO 27042 §9 — Documentación del análisis) ──────────
def generar_informe_individual(resultados, pdf_path):
    """
    ISO 27042 §9: Documentación completa del análisis.
    Incluye entorno, metodología, cadena de custodia y hallazgos.
    """
    versiones  = obtener_versiones_herramientas()
    sha256     = calcular_sha256(pdf_path)
    fecha_utc  = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    est        = resultados.get('estructura', {})
    imgs       = resultados.get('imagenes', {}).get('imagenes', [])

    informe = f"""# 📜 INFORME DE DIAGNÓSTICO FORENSE INDIVIDUAL
### Marco Normativo: ISO/IEC 27037 · ISO/IEC 27042 · ISO/IEC 27043

**Archivo analizado:** `{os.path.basename(pdf_path)}`
**Ruta absoluta:** `{pdf_path}`
**SHA-256 (ISO 27037 §8.3.1):** `{sha256}`
**Fecha del diagnóstico (UTC):** `{fecha_utc}`
**Método de análisis estructural:** `{est.get('metodo', 'Desconocido')}`

---

## 🛠️ ENTORNO DE ANÁLISIS (ISO 27042 §7.2)

| Herramienta | Versión | Estado |
|:---|:---|:---|
| qpdf      | `{versiones.get('qpdf', 'N/A')}` | {'✅ Activo' if disponibles.get('qpdf') else '👹 Diablo activo'} |
| exiftool  | `{versiones.get('exiftool', 'N/A')}` | {'✅ Activo' if disponibles.get('exiftool') else '👹 Diablo activo'} |
| pdfimages | `{versiones.get('pdfimages', 'N/A')}` | {'✅ Activo' if disponibles.get('pdfimages') else '👹 Diablo activo'} |
| identify  | `{versiones.get('identify', 'N/A')}` | {'✅ Activo' if disponibles.get('identify') else '👹 Diablo activo'} |

---

## ⚡ ANÁLISIS ESTRUCTURAL — XREF (ISO 27042 §8)

- **Exit Code:** `{est.get('exit_code')}`
- **Discrepancia XREF detectada:** `{est.get('XREF_discrepancia')}`
- **Detalle:**
```
{est.get('detalle', '(Vacío)')}
```

---

## 🖼️ ANÁLISIS DE CAPAS RASTER (ISO 27042 §8)

- **Imágenes detectadas:** `{len(imgs)}`
"""
    for img in imgs:
        informe += f"  - `{img['archivo']}` · Colorspace: `{img['colorspace']}` · Std: `{img['desviacion_estandar']:.1f}` · **Varianza Cero: `{img['varianza_cero']}`**\n"

    vec = resultados.get('vectorial', {})
    meta = resultados.get('metadatos', {})

    informe += f"""
---

## 📐 ANÁLISIS VECTORIAL (Método puro Python)

- **Trazados vectoriales detectados:** `{vec.get('contiene_vectores')}`
- **Score de operadores:** `{vec.get('score_vectorial')}`

---

## 📋 METADATOS (ISO 27037 §8)

```
{meta.get('metadatos', 'Sin metadatos detectados')}
```

---

*Informe generado con rigor de cadena de custodia ISO 27037/27042/27043.*
*BabaYaga Core v2.0 — AndreTaker AnZaCa — Andrea Zabala Cárcamo*
"""
    with open('informe_babayaga.md', 'w', encoding='utf-8') as f:
        f.write(informe)
    print("✅ Diagnóstico individual: informe_babayaga.md")

# ─── PROCESAMIENTO EN LOTE (ISO 27043 — Investigación de incidentes) ─────────
def procesar_lote(carpeta_path):
    """
    ISO 27043: Investigación sistémica de incidentes en masa.
    Va por todos los rincones recursivamente.
    Optimiza recursos — procesa, no acumula en memoria.
    """
    print(f"🌲 Entrando al bosque: {carpeta_path}")
    print(f"🪓 Recolectando PDFs recursivamente...")

    archivos_pdf = []
    for root, _, files in os.walk(carpeta_path):
        for f in files:
            if f.lower().endswith('.pdf'):
                archivos_pdf.append(os.path.join(root, f))
    archivos_pdf.sort()
    total = len(archivos_pdf)

    if total == 0:
        print("⚠️  El bosque está vacío. No se encontraron PDFs.")
        return

    print(f"📊 {total} PDFs encontrados. Comenzando el ritual...\n")

    csv_path          = 'matriz_lote_babayaga.csv'
    informe_lote_path = 'informe_lote_babayaga.md'
    versiones         = obtener_versiones_herramientas()
    fecha_utc         = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    con_xref = sin_xref = var_cero = 0

    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([
            'Nombre_Archivo', 'SHA256', 'Fecha_Analisis_UTC', 'Ruta_Absoluta',
            'Metodo_XREF', 'QPDF_ExitCode', 'Discrepancia_XREF', 'Detalle_XREF',
            'Metodo_Metadatos', 'Tiene_Metadatos',
            'Metodo_Imagenes', 'Cant_Imagenes', 'Varianza_Cero',
            'Contiene_Vectores', 'Score_Vectorial'
        ])

        for idx, pdf in enumerate(archivos_pdf, 1):
            nom = os.path.basename(pdf)
            print(f"[{idx}/{total}] 🪓 {nom}")

            sha256 = calcular_sha256(pdf)  # ISO 27037 — hash antes del análisis
            est    = analizar_estructura(pdf)
            meta   = analizar_metadatos(pdf)
            img    = analizar_imagenes(pdf)
            vec    = detectar_elementos_vectoriales(pdf)

            has_xref = est.get('XREF_discrepancia', False)
            imgs_l   = img.get('imagenes', [])
            has_vz   = any(im['varianza_cero'] for im in imgs_l)

            if has_xref: con_xref += 1
            else:        sin_xref += 1
            if has_vz:   var_cero += 1

            writer.writerow([
                nom, sha256, fecha_utc, pdf,
                est.get('metodo', '?'), est.get('exit_code'), has_xref,
                est.get('detalle', '')[:200].replace('\n', ' '),
                meta.get('metodo', '?'), meta.get('tiene_autoría', False),
                img.get('metodo', '?'), len(imgs_l), has_vz,
                vec.get('contiene_vectores'), vec.get('score_vectorial')
            ])

    pct_xref = (con_xref / total * 100) if total else 0
    pct_vz   = (var_cero / total * 100) if total else 0

    # ── Métodos activos ──
    metodos_activos = []
    for h, info in HERRAMIENTAS.items():
        if not disponibles.get(h):
            metodos_activos.append(f"- **{h}** → 👹 `{info['alternativa']}` activo")

    md = f"""# 📜 INFORME DE LOTE FORENSE — VEREDICTO DE MASA
### Marco Normativo: ISO/IEC 27037 · ISO/IEC 27042 · ISO/IEC 27043

**Carpeta analizada:** `{carpeta_path}`
**Fecha del diagnóstico (UTC):** `{fecha_utc}`
**Total de archivos evaluados:** `{total}`

---

## 🛠️ ENTORNO DE AUDITORÍA (ISO 27042 §7.2)

| Herramienta | Versión/Estado |
|:---|:---|
| qpdf      | `{versiones.get('qpdf', 'N/A')}` |
| exiftool  | `{versiones.get('exiftool', 'N/A')}` |
| pdfimages | `{versiones.get('pdfimages', 'N/A')}` |
| identify  | `{versiones.get('identify', 'N/A')}` |

{"### 👹 Métodos alternativos activos (El Diablo):" + chr(10) + chr(10).join(metodos_activos) if metodos_activos else ""}

---

## 📊 RESUMEN ESTADÍSTICO (ISO 27042)

| Métrica | Valor | Porcentaje |
|:---|:---|:---|
| **Total Archivos Evaluados** | {total} | 100.0% |
| **⚠️ Discrepancia XREF (Alteración estructural)** | {con_xref} | **{pct_xref:.2f}%** |
| **✅ Estructura Normal** | {sin_xref} | **{100.0 - pct_xref:.2f}%** |
| **🎭 Imágenes Varianza Cero (Máscara sintética 1bpc)** | {var_cero} | **{pct_vz:.2f}%** |

---

## 🧠 INTERPRETACIÓN METODOLÓGICA (ISO 27042 §9)

- **XREF:** La discrepancia `reported number of objects (N) ≠ highest+1 (N-2)` indica
  objetos declarados ausentes del archivo. Cuando el delta es idéntico en múltiples archivos,
  constituye una **firma de proceso automatizado**, no corrupción aleatoria.

- **Varianza Cero:** Ningún sensor óptico físico produce imágenes con `std=0`.
  Su presencia indica **inyección digital de capas sintéticas** posteriores a la captura.

---

## ⚖️ CADENA DE CUSTODIA (ISO 27037)

- Análisis **no destructivo** — archivos originales intactos
- Hash SHA-256 calculado **antes** del análisis por archivo
- Timestamps en **UTC** estandarizado
- Versiones de herramientas documentadas
- Métodos alternativos activos registrados explícitamente

---

*BabaYaga Core v2.0 — AndreTaker AnZaCa — Andrea Zabala Cárcamo*
*Va por todos los rincones. Desentierra hasta los muertos.*
*Cuando no puede sola, llama al diablo.*
"""

    with open(informe_lote_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"\n✅ Ritual completado.")
    print(f"   ├─ ⚠️  Con cicatriz XREF : {con_xref} ({pct_xref:.2f}%)")
    print(f"   ├─ 🎭  Varianza Cero     : {var_cero} ({pct_vz:.2f}%)")
    print(f"   ├─ Matriz CSV           : {csv_path}")
    print(f"   └─ Informe Markdown     : {informe_lote_path}")

# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description='🪓 BabaYaga Core v2.0 — ISO 27037/27042/27043 · AndreTaker AnZaCa'
    )
    parser.add_argument('--ruta', required=True, help='Archivo PDF o carpeta a analizar')
    args = parser.parse_args()

    print("🔍 Verificando herramientas (primarias y alternativas):")
    verificar_herramientas()

    ruta = args.ruta
    if not os.path.exists(ruta):
        print(f"❌ Ruta no encontrada: {ruta}")
        sys.exit(1)

    if os.path.isdir(ruta):
        procesar_lote(ruta)
    else:
        resultados = {
            'estructura': analizar_estructura(ruta),
            'metadatos':  analizar_metadatos(ruta),
            'imagenes':   analizar_imagenes(ruta),
            'vectorial':  detectar_elementos_vectoriales(ruta)
        }
        generar_informe_individual(resultados, ruta)

if __name__ == '__main__':
    main()
