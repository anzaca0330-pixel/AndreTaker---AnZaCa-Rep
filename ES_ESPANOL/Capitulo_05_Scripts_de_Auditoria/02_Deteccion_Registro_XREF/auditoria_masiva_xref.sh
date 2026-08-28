#!/bin/bash
# ============================================================
# auditoria_masiva_xref.sh  —  v2.0  (guardado atómico incremental)
# Analiza cada PDF con qpdf --check y guarda resultado uno a uno
# directamente en el CSV (con flock), SIN archivos temporales.
# Si se interrumpe, al retomar detecta qué ya fue procesado y
# continúa desde ahí. Nunca pierde trabajo hecho.
#
# Uso:
#   bash auditoria_masiva_xref.sh <directorio_origen> <archivo_salida.csv> [hilos]
#
# Ejemplo:
#   bash auditoria_masiva_xref.sh \
#     "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf" \
#     /home/andrea-zabala-c/Desktop/resultado_xref_nacional_segunda_vuelta.csv \
#     8
# ============================================================

set -uo pipefail

# ── Argumentos ────────────────────────────────────────────────
if [ -z "${1:-}" ] || [ -z "${2:-}" ]; then
    echo "Uso: $0 <directorio_origen> <archivo_salida.csv> [num_hilos=8]" >&2
    exit 1
fi

TARGET_DIR="$1"
OUTPUT_CSV="$2"
NUM_HILOS="${3:-8}"

# ── Verificaciones ────────────────────────────────────────────
if ! command -v qpdf &>/dev/null; then
    echo "ERROR: qpdf no está instalado. Instálalo con: sudo apt install qpdf" >&2
    exit 1
fi

if ! command -v flock &>/dev/null; then
    echo "ERROR: flock no está disponible (util-linux requerido)" >&2
    exit 1
fi

TARGET_DIR=$(realpath "$TARGET_DIR")

if [ ! -d "$TARGET_DIR" ]; then
    echo "ERROR: Directorio '$TARGET_DIR' no existe" >&2
    exit 1
fi

# ── Crear CSV con encabezado si no existe ─────────────────────
if [ ! -f "$OUTPUT_CSV" ]; then
    echo "archivo_pdf,resultado_xref,departamento,municipio,zona,puesto,mesa" > "$OUTPUT_CSV"
    echo "[+] CSV nuevo creado en: $OUTPUT_CSV"
else
    echo "[*] Reanudando desde CSV existente: $OUTPUT_CSV"
fi

LOCK_FILE="${OUTPUT_CSV}.lock"
PROGRESO_FILE="${OUTPUT_CSV}.progreso"

# ── Función: analiza UN pdf y escribe resultado atómicamente al CSV ──
check_and_write() {
    local pdf_file="$1"
    local output_csv="$2"
    local lock_file="$3"

    # Ejecutar qpdf (ignorar código de salida, capturar output)
    local result
    result=$(qpdf --check "$pdf_file" 2>&1) || true

    # Clasificar resultado
    local estado
    if echo "$result" | grep -q "not one plus the highest object number"; then
        estado="CORRUPTO_XREF"
    elif echo "$result" | grep -q "trailer dictionary"; then
        estado="CORRUPTO_TRAILER"
    elif echo "$result" | grep -q "operation succeeded with warnings"; then
        estado="ADVERTENCIA"
    elif echo "$result" | grep -q "No syntax or stream encoding errors found"; then
        estado="LIMPIO"
    else
        estado="LIMPIO"
    fi

    # Extraer metadatos del nombre de archivo para columnas adicionales
    local basename
    basename=$(basename "$pdf_file")
    # Patrón: E14_PRE_DD_MMM_ZZZ_PP_SS_NNN_ID_Mesa_N.pdf
    local depto mun zona puesto mesa
    depto=$(echo "$basename"  | grep -oP '(?<=PRE_)\d{2}'       || echo "")
    mun=$(echo "$basename"    | grep -oP '(?<=PRE_\d{2}_)\d{3}' || echo "")
    zona=$(echo "$basename"   | cut -d'_' -f6 2>/dev/null       || echo "")
    puesto=$(echo "$basename" | cut -d'_' -f7 2>/dev/null       || echo "")
    mesa=$(echo "$basename"   | grep -oP 'Mesa_\d+' 2>/dev/null  || echo "")

    # Escribir al CSV con bloqueo exclusivo (evita corrupción por escritura paralela)
    (
        flock -x 200
        printf '"%s","%s","%s","%s","%s","%s","%s"\n' \
            "$pdf_file" "$estado" "$depto" "$mun" "$zona" "$puesto" "$mesa" >> "$output_csv"
        # Actualizar contador de progreso
        local n
        n=$(cat "$lock_file.count" 2>/dev/null || echo 0)
        echo $((n + 1)) > "$lock_file.count"
    ) 200>"$lock_file"
}
export -f check_and_write

# ── Calcular pendientes (reanudación) ─────────────────────────
echo ""
echo "[*] Calculando archivos pendientes..."

TMPWORK=$(mktemp -d)
trap "rm -rf '$TMPWORK'" EXIT

# Rutas ya procesadas (del CSV existente, sin header)
tail -n +2 "$OUTPUT_CSV" 2>/dev/null \
    | cut -d'"' -f2 \
    | sort > "$TMPWORK/procesados.txt"

# Todos los PDFs en el directorio origen
find "$TARGET_DIR" -type f -name "*.pdf" | sort > "$TMPWORK/todos.txt"

TOTAL_TODOS=$(wc -l < "$TMPWORK/todos.txt")
TOTAL_YA=$(wc -l < "$TMPWORK/procesados.txt")

# Pendientes = todos - ya procesados
comm -23 "$TMPWORK/todos.txt" "$TMPWORK/procesados.txt" > "$TMPWORK/pendientes.txt"
TOTAL_PENDIENTES=$(wc -l < "$TMPWORK/pendientes.txt")

echo "    Total archivos en directorio : $TOTAL_TODOS"
echo "    Ya procesados (en CSV)       : $TOTAL_YA"
echo "    Pendientes                   : $TOTAL_PENDIENTES"
echo "    Hilos paralelos              : $NUM_HILOS"
echo ""

if [ "$TOTAL_PENDIENTES" -eq 0 ]; then
    echo "✅ Ya están todos procesados. No hay nada que hacer."
else
    # Inicializar contador de progreso
    echo "$TOTAL_YA" > "$LOCK_FILE.count"

    INICIO=$(date +%s)
    echo "[*] Iniciando análisis a las $(date '+%H:%M:%S')..."
    echo ""

    # ── Monitor de progreso en segundo plano ─────────────────
    (
        while true; do
            sleep 30
            PROCESADOS_AHORA=$(cat "$LOCK_FILE.count" 2>/dev/null || echo 0)
            NUEVOS=$((PROCESADOS_AHORA - TOTAL_YA))
            PCT=0
            [ "$TOTAL_PENDIENTES" -gt 0 ] && PCT=$((NUEVOS * 100 / TOTAL_PENDIENTES))
            ELAPSED=$(( $(date +%s) - INICIO ))
            if [ "$NUEVOS" -gt 0 ] && [ "$ELAPSED" -gt 0 ]; then
                RATE=$((NUEVOS / ELAPSED))
                RESTA=$((TOTAL_PENDIENTES - NUEVOS))
                [ "$RATE" -gt 0 ] && ETA_SEC=$((RESTA / RATE)) || ETA_SEC=0
                ETA_MIN=$((ETA_SEC / 60))
                echo "  ⏳ Progreso: $NUEVOS/$TOTAL_PENDIENTES ($PCT%) — ${RATE} arch/seg — ETA: ~${ETA_MIN} min"
            else
                echo "  ⏳ Progreso: $NUEVOS/$TOTAL_PENDIENTES ($PCT%)..."
            fi
        done
    ) &
    MONITOR_PID=$!
    trap "kill $MONITOR_PID 2>/dev/null; rm -rf '$TMPWORK'" EXIT

    # ── Procesamiento paralelo ────────────────────────────────
    # Cada proceso escribe DIRECTAMENTE al CSV con flock → sin pérdida de datos
    cat "$TMPWORK/pendientes.txt" | tr '\n' '\0' | \
        xargs -0 -n 1 -P "$NUM_HILOS" bash -c \
        'check_and_write "$0" "'"$OUTPUT_CSV"'" "'"$LOCK_FILE"'"'

    kill $MONITOR_PID 2>/dev/null || true
fi

# ── Estadísticas finales ──────────────────────────────────────
echo ""
TOTAL_FINAL=$(tail -n +2 "$OUTPUT_CSV" | wc -l || echo 0)
CORRUPTOS_XREF=$(grep -c '"CORRUPTO_XREF"'   "$OUTPUT_CSV" 2>/dev/null || echo 0)
CORRUPTOS_TRAI=$(grep -c '"CORRUPTO_TRAILER"' "$OUTPUT_CSV" 2>/dev/null || echo 0)
ADVERTENCIAS=$(grep -c '"ADVERTENCIA"'        "$OUTPUT_CSV" 2>/dev/null || echo 0)
LIMPIOS=$(grep -c '"LIMPIO"'                  "$OUTPUT_CSV" 2>/dev/null || echo 0)
TOTAL_CORRUPTOS=$((CORRUPTOS_XREF + CORRUPTOS_TRAI))

echo "╔══════════════════════════════════════════════════════╗"
echo "║           AUDITORÍA MASIVA E-14 — RESULTADOS        ║"
echo "╠══════════════════════════════════════════════════════╣"
printf "║  %-30s %20s ║\n" "Total archivos analizados:"    "$TOTAL_FINAL"
printf "║  %-30s %20s ║\n" "🔴 CORRUPTOS (XREF):"          "$CORRUPTOS_XREF"
printf "║  %-30s %20s ║\n" "🔴 CORRUPTOS (Trailer):"       "$CORRUPTOS_TRAI"
printf "║  %-30s %20s ║\n" "🟡 Con advertencias:"          "$ADVERTENCIAS"
printf "║  %-30s %20s ║\n" "🟢 LIMPIOS:"                   "$LIMPIOS"
printf "║  %-30s %20s ║\n" "━━ TOTAL IRREGULARES:"        "$TOTAL_CORRUPTOS"
echo "╠══════════════════════════════════════════════════════╣"
printf "║  %-30s %20s ║\n" "📁 CSV guardado en:" ""
printf "║  %-52s ║\n" "  $(basename "$OUTPUT_CSV")"
echo "╚══════════════════════════════════════════════════════╝"
echo ""
echo "Finalizado: $(date '+%Y-%m-%d %H:%M:%S')"

# Limpiar archivos de lock/progreso
rm -f "$LOCK_FILE" "$LOCK_FILE.count" 2>/dev/null || true
