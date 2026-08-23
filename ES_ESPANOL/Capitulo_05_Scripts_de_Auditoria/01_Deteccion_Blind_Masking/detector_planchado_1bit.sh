#!/bin/bash
# ==============================================================================
# Script de Extracción Forense: Detección de "1-Bit Flattening" (Planchado Raster)
# Autor: Andrea Zabala Carcamo
# Fecha de Descubrimiento Original: 4 de Junio de 2026 (Recuperado vía Opera/DeepSeek)
# Descripción: Analiza los metadatos de color de imágenes extraídas de PDF 
# (Actas E-14) utilizando ImageMagick para clasificar automáticamente aquellas 
# que fueron aplanadas a 1 bit (Máscaras de Spoofing) vs Escaneos Originales (Color).
# ==============================================================================

echo "Iniciando análisis forense de imágenes (1-Bit Flattening Detection)..."

for img in *_img-*.png; do
    # Verifica que existan archivos para no arrojar errores en carpetas vacías
    if [ ! -e "$img" ]; then
        echo "No se encontraron imágenes *_img-*.png en el directorio actual."
        exit 1
    fi

    # Extrae el espacio de color (RGB, Gray, CMYK, etc.)
    colorspace=$(identify -format "%[colorspace]" "$img" 2>/dev/null)
    
    # Extrae el conteo de colores únicos
    colores=$(identify -format "%[colors]" "$img" 2>/dev/null)
    
    # Condición Forense: 
    # Si el espacio es explícitamente Gris o los colores totales son <= 2
    # se marca como "Blanco y Negro" (Evidencia de alteración estructural o Planchado 1-bit)
    if echo "$colorspace" | grep -qi "gray" || [ "$colores" -le 2 ] 2>/dev/null; then
        echo "BN (ALTERACIÓN/1-BIT): $img"
    else
        echo "COLOR (GENUINO/MULTI-CAPA): $img"
    fi
done

echo "Análisis completado."
