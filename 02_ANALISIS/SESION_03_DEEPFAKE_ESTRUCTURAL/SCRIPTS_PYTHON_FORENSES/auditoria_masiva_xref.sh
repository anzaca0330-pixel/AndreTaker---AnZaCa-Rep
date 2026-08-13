#!/bin/bash
set -euo pipefail # Detener en errores, variables no definidas

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Uso: $0 <directorio_origen> <archivo_salida_csv>" >&2
    exit 1
fi

if ! command -v qpdf &> /dev/null; then
    echo "ERROR: qpdf no está instalado" >&2
    exit 1
fi

TARGET_DIR=$(realpath "$1")
OUTPUT_CSV=$(realpath "$2")

if [ ! -d "$TARGET_DIR" ]; then
    echo "ERROR: Directorio '$TARGET_DIR' no existe" >&2
    exit 1
fi

if [ ! -f "$OUTPUT_CSV" ]; then
    echo "archivo_pdf,resultado_xref" > "$OUTPUT_CSV"
fi

check_pdf() {
    pdf_file="$1"
    output=$(qpdf --check "$pdf_file" 2>&1) || true
    if echo "$output" | grep -q "not one plus the highest object number"; then
        echo "\"$pdf_file\",CORRUPTO"
    elif echo "$output" | grep -q "operation succeeded with warnings"; then
        echo "\"$pdf_file\",ADVERTENCIA_OTRA"
    else
        echo "\"$pdf_file\",LIMPIO"
    fi
}
export -f check_pdf

# Usar archivo temporal por proceso (evita condición de carrera)
export TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

echo "Calculando archivos restantes..."
# Extraer rutas ya procesadas
tail -n +2 "$OUTPUT_CSV" | cut -d',' -f1 | sed 's/^"//;s/"$//' | sort > "$TMPDIR/procesados.txt"
# Buscar todos los PDFs
find "$TARGET_DIR" -type f -name "*.pdf" | sort > "$TMPDIR/todos.txt"
# Filtrar los que faltan
comm -23 "$TMPDIR/todos.txt" "$TMPDIR/procesados.txt" > "$TMPDIR/pendientes.txt"

total_pendientes=$(wc -l < "$TMPDIR/pendientes.txt")
echo "Archivos pendientes por procesar: $total_pendientes"

if [ "$total_pendientes" -gt 0 ]; then
    # Correr xargs solo sobre los pendientes (-n 1 en lugar de -I para evitar el warning)
    cat "$TMPDIR/pendientes.txt" | tr '\n' '\0' | xargs -0 -n 1 -P 8 bash -c 'check_pdf "$0" >> "$TMPDIR/salida_$$.tmp"'
    # Consolidar todos los temporales nuevos
    cat "$TMPDIR"/salida_*.tmp >> "$OUTPUT_CSV" 2>/dev/null || true
fi

# Estadísticas
total=$(tail -n +2 "$OUTPUT_CSV" | wc -l || true)
corruptos=$(grep -c ",CORRUPTO" "$OUTPUT_CSV" || true)
limpios=$(grep -c ",LIMPIO" "$OUTPUT_CSV" || true)

echo "========================================"
echo "✅ ANÁLISIS COMPLETADO"
echo "Total Analizados: $total"
echo "Corruptos (XREF alterado): $corruptos"
echo "Limpios: $limpios"
echo "========================================"
