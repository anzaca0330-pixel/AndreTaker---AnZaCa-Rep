# ==============================================================================
# FORENSIC DOCKER CAPSULE (Nivel: Senior / Security Researcher)
# Proyecto: Auditoría Forense E-14 (Colombia 2026)
# Vinculación Académica: UOPX Prior Learning Assessment (PLA)
# ==============================================================================
# Esta cápsula dockerizada aísla el entorno de pruebas, garantizando que el 
# código de ingeniería inversa corra de manera idéntica en cualquier OS.
# Cumple con estándares de ciberseguridad industrial y auditoría de pares.

# Imagen base liviana y estable
FROM ubuntu:22.04

# Variables de entorno para evitar interacciones durante apt-get
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Configuración del directorio de trabajo
WORKDIR /forensics_audit

# 1. Instalación del stack forense base
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    qpdf \
    poppler-utils \
    libimage-exiftool-perl \
    tesseract-ocr \
    zbar-tools \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 2. Copiar los requirements y configurar Python
# Nota: Asume que el contexto del build es la raíz del repositorio
COPY 03_DOCUMENTACION/CARITA_FELIZ_DELIVERABLE/requirements.txt /tmp/
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt

# 3. Importar toda la bóveda de evidencia y scripts al contenedor
COPY . /forensics_audit/

# 4. Dar permisos de ejecución a los scripts
RUN chmod +x /forensics_audit/02_ANALISIS/SESION_03_DEEPFAKE_ESTRUCTURAL/SCRIPTS_PYTHON_FORENSES/*.sh

# ENTRYPOINT por defecto: Una shell interactiva para auditar
CMD ["/bin/bash"]
