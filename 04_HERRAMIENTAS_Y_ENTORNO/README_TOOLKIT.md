# 🛠️ Paquete de Detección de Fraude PRO (Forensic Toolkit)

Este directorio contiene las herramientas necesarias para automatizar la extracción de evidencia binaria, cazar **inyecciones algorítmicas**, detectar **anomalías estadísticas** y renderizar **gráficas de varianza (Benford / Gauss)**. Está diseñado específicamente para desensamblar estructuras de **Deepfake Documental** (alteración XREF), revertir operaciones sintéticas de ocultamiento como el **Blind Masking** (máscaras de 1bpc), desempaquetar flujos ocultos por **FlateDecode** usando **mutool**, auditar inconsistencias en códigos **QR** (vía **zbarimg**) y sellar criptográficamente la evidencia mediante **Hashes (SHA-256)** en cientos de miles de actas electorales.

> [!IMPORTANT]
> **Vinculación Académica:** Este paquete de herramientas y su metodología analítica forman parte integral del portafolio académico de la Universidad de Phoenix (UOPX) bajo el marco de **Prior Learning Assessment (PLA)**. El rigor aquí aplicado cumple con estándares de auditoría forense industrial.

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
