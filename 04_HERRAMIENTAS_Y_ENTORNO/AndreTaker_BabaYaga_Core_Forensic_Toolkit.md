# 🧙‍♀️ AndreTaker — BabaYaga Core Forensic Toolkit
### 🔍 Híbrido Detector Multicapas para Auditoría Documental y Forense Digital

Este ecosistema está diseñado para procesar **paquetes de archivos en lotes (Batch Processing)**. No solo analiza los archivos, sino que automatiza todo el ciclo pericial: ingiere la evidencia bruta, desensambla la **metadatos** (y extrae huellas estructurales incluso cuando el archivo carece de metadatos por intento de evasión), genera el informe forense final y produce las tablas analíticas listas para tribunales.

Aunque fue diseñado para desensamblar estructuras de **Deepfake Documental** y revertir operaciones de **Blind Masking** en documentos electorales, su arquitectura es **agnóstica (multipropósito)**: sirve para detectar **inyecciones algorítmicas**, alteraciones estructurales (XREF), flujos **FlateDecode** ocultos (vía **mutool**), inyecciones en **QR** (vía **zbarimg**) y sellos **Hashes** en **cualquier campo que requiera auditoría documental rigurosa** (fraudes financieros, alteración de historias clínicas, contratos legales o licitaciones públicas). Incluye el **generador de gráficas de varianza (Benford 2nd Digit / Gauss)** para respaldar los hallazgos.

> [!IMPORTANT]
> **Estándares de Calidad Forense:** Este paquete de herramientas y su metodología analítica han sido desarrollados bajo estrictos estándares de auditoría forense industrial, siguiendo las directrices de **ISO/IEC 27037:2012** (identificación, recolección, adquisición y preservación de evidencia digital) y el proceso forense de 4 pasos documentado en **NIST Special Publication 800-86** (Collection, Examination, Analysis, Reporting). Esto garantiza la integridad, reproducibilidad y validez legal de los análisis realizados.

---

## 🎯 ¿Qué nivel de Auditor eres? (Elige tu instalación)

Hemos preparado dos rutas de despliegue para el *Peer Review*, dependiendo de tu nivel de experiencia técnica:

---

### 1️⃣ Nivel Semi-Senior (Instalador Nativo)
Si utilizas **Ubuntu, Debian o Kali Linux** y quieres configurar tu computadora rápidamente, usa nuestro instalador automatizado. Este script descargará `qpdf`, `exiftool`, creará un entorno virtual y configurará todas las dependencias de Python (`pandas`, `PyPDF2`, etc.).

**Ejecución:**
```bash
chmod +x install_forensic_toolkit.sh
./install_forensic_toolkit.sh
```
Una vez termine, activa tu entorno con: `source .forensic_venv/bin/activate` y estarás listo para ejecutar los scripts de auditoría.

---

### 2️⃣ Nivel Industrial / Security Researcher (Cápsula Docker)
Si usas **Windows, macOS**, o simplemente quieres el máximo nivel de seguridad (Aislamiento de Entorno), utiliza nuestra cápsula forense. Construye un ecosistema virtual sellado idéntico al que usamos en laboratorio, garantizando 100% de reproducibilidad.

**Ejecución:**
Debes ejecutar esto desde la **raíz del repositorio** (para que Docker pueda absorber la evidencia):
```bash
# Vuelve a la raíz del repo
cd ..

# Construye la cápsula forense (solo la primera vez)
docker build -t forensic_toolkit_e14 -f 04_HERRAMIENTAS_Y_ENTORNO/Dockerfile .

# Entra a la bóveda forense sellada
docker run -it --rm forensic_toolkit_e14
```
Una vez dentro de la terminal aislada, podrás correr cualquier comando forense sin ensuciar tu computadora.

---

## 🧠 Filosofía del Toolkit

> *"BabaYaga no sigue caminos rectos. Ella ve en la oscuridad, habita en los bordes, y desmonta lo que otros esconden. Eso es lo que hace AndreTaker con los documentos."*

---

**Versión:** 1.0  
**Autora:** Andrea Zabala Cárcamo (AnZaCa)  
**Licencia:** Apache 2.0  
**Inspiración:** Un sueño, un bosque, y la certeza de que la verdad siempre encuentra un camino.
