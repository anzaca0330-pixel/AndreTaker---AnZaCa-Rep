#!/bin/bash
OUTPUT_CSV="/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/resultado_xref_claveros_antioquia.csv"
echo "Departamento,Municipio,Zona,Puesto,Mesa,Estado_XREF" > "$OUTPUT_CSV"

DIR="/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf/ANTIOQUIA"
export DIR

TMP_DIR=$(mktemp -d)

check_pdf() {
    pdf="$1"
    filename=$(basename "$pdf" .pdf)
    IFS='_' read -r dep mun zon pue mes <<< "$filename"
    
    qpdf_output=$(qpdf --check "$pdf" 2>&1)
    if [[ "$qpdf_output" == *"XREF"* ]] || [[ "$qpdf_output" == *"damaged"* ]] || [[ "$qpdf_output" == *"error"* ]] || [[ "$qpdf_output" == *"WARNING"* ]]; then
        estado="CORRUPTO_PLANTILLA_B"
    else
        estado="OK_ORGANICO"
    fi
    echo "$dep,$mun,$zon,$pue,$mes,$estado" > "$2/$filename.tmp"
}
export -f check_pdf

find "$DIR" -type f -name "*.pdf" | xargs -n 1 -P 32 -I {} bash -c 'check_pdf "$@"' _ {} "$TMP_DIR"

# Concatenar resultados
for f in "$TMP_DIR"/*.tmp; do
    [ -f "$f" ] && cat "$f" >> "$OUTPUT_CSV"
done

rm -rf "$TMP_DIR"

total=$(wc -l < "$OUTPUT_CSV")
total=$((total - 1))
corruptos=$(grep -c "CORRUPTO_PLANTILLA_B" "$OUTPUT_CSV" || true)

echo "====================================="
echo "   REPORTE CLAVEROS (GRUPO CONTROL)  "
echo "====================================="
echo "Total PDFs Antioquia Claveros procesados: $total"
echo "Total corruptos (Plantilla B): $corruptos"
echo "====================================="
