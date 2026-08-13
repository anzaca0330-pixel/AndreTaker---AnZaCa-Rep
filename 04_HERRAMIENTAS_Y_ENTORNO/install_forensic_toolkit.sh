#!/bin/bash

# ==============================================================================
# FORENSIC TOOLKIT INSTALLER (Nivel: Junior / Semi-Senior)
# Proyecto: Auditoría Forense E-14 (Colombia 2026)
# ==============================================================================
# Este script automatiza la instalación de todas las dependencias del sistema y
# librerías de Python necesarias para ejecutar la auditoría de forma nativa.
# Garantiza que no tengas que buscar ni compilar librerías una por una.

set -e

echo -e "\n[+] Iniciando despliegue automático del Forensic Toolkit...\n"

# 1. Verificar si estamos en un entorno basado en Debian/Ubuntu
if ! command -v apt-get &> /dev/null; then
    echo -e "⚠️ [ERROR] Este script está diseñado para Ubuntu/Debian/Kali Linux."
    echo -e "Si usas macOS (Brew) o Windows, por favor usa la versión de Docker."
    exit 1
fi

# 2. Instalación de binarios forenses (Stack de PDF y Metadata)
echo -e "📦 Instalando binarios estructurales (qpdf, poppler, exiftool)..."
sudo apt-get update -y
sudo apt-get install -y \
    qpdf \
    poppler-utils \
    libimage-exiftool-perl \
    python3 \
    python3-pip \
    python3-venv \
    tesseract-ocr \
    zbar-tools

# 3. Configuración del entorno de Python
echo -e "\n🐍 Configurando entorno virtual de Python..."
VENV_DIR=".forensic_venv"

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

# 4. Instalación de librerías criptográficas y analíticas
echo -e "\n📊 Instalando dependencias de Python (pandas, opencv, pypdf2, etc.)..."
# Usamos el requirements.txt del repositorio principal
pip install --upgrade pip
if [ -f "../03_DOCUMENTACION/CARITA_FELIZ_DELIVERABLE/requirements.txt" ]; then
    pip install -r ../03_DOCUMENTACION/CARITA_FELIZ_DELIVERABLE/requirements.txt
else
    # Fallback en caso de que lo corran fuera de ruta
    pip install pandas numpy opencv-python PyPDF2 matplotlib seaborn scipy
fi

echo -e "\n=============================================================================="
echo -e "✅ ¡ENTORNO LISTO!"
echo -e "Para activar tu entorno antes de correr las pruebas, ejecuta:"
echo -e "source 04_HERRAMIENTAS_Y_ENTORNO/.forensic_venv/bin/activate"
echo -e "==============================================================================\n"
