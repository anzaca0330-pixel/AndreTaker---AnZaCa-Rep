# Muestras de Control (Clonaje Vectorial y Plantilla B)

Este documento registra los Hashes SHA-256 exactos de las actas E-14 utilizadas como muestra de control para demostrar la técnica de "BlindMasking" y la discrepancia de exportación estructural (Paradoja de los Píxeles) en el municipio de Acacias, Meta. 

Se invita a los ingenieros y peritos independientes a descargar estos archivos desde los repositorios originales (Web y USB) y correr los scripts criptográficos (`prueba_criptografica_clonaje.py`) junto con herramientas estándar como `qpdf --check` y `pdfimages -list` para replicar y corroborar los hallazgos.

## Muestra 1: Acacias (Meta) - Mesa 1, Zona 01

### Archivo Web (Delegados)
- **Ruta Típica:** Archivos ofuscados publicados en la web de la Registraduría (Escala de Grises, 72 PPI).
- **Nombre Físico:** `07e0c2e1d97eee344370d712808ebb47935c8b447e57960eab06f4b8f8f7334a.pdf`
- **Hash SHA-256:** `5dc59f0bc7dd6b50ae37089364b63597e49b3a29f5204a13080d44d5050167ea`

### Archivo USB Oficial (Claveros)
- **Ruta Típica:** `META/ACACIAS/ZONA 01/COL MPAL LUIS CARLOS GALAN SARMIENTO/E14_PRE_52_005_001_00_03_001_6924_Mesa_1.pdf` (Color RGB, 300 PPI).
- **Hash SHA-256:** `839bb7f9aeda78d53e53708162dc48bcc39f52e2920b5c2e9318dc9d1439f374`

---

## Muestra 2: Acacias (Meta) - Mesa 6, Zona 99

### Archivo Web (Delegados)
- **Ruta Típica:** Archivos ofuscados publicados en la web de la Registraduría (Escala de Grises, 72 PPI).
- **Nombre Físico:** `0d6323726bba3cb89fd2ea216fd2dddfe3949c5690faeec3e2ae86c9d472862e.pdf`
- **Hash SHA-256:** `c3380695ed64b780ebfaf0e2ccbe4397b1ca8c3f49abe1b817913e9ddb9880d1`

### Archivo USB Oficial (Claveros)
- **Ruta Típica:** `META/ACACIAS/ZONA 99/SAN ISIDRO DE CHICHIMENE/E14_PRE_52_005_099_00_60_006_6925_Mesa_6.pdf` (Color RGB, 300 PPI).
- **Hash SHA-256:** `37b8f171f551031d1e478b6c18a48f68d68e0d086ddb2acc49142020753900db`

---

**Nota Técnica para Peritos:** 
A pesar de que los hashes SHA-256 externos difieren (debido al cambio de calidad de imagen por exportación y metadatos inyectados), ambos pares de archivos comparten matemáticamente la misma ubicación interna de objetos (`Object ID 6 y 11`) y el mismo daño estructural en la tabla vectorial (`WARNING: reported number of objects (15) is not one plus the highest object number (13)`), comprobando la inyección sintética a través de un mismo generador de software.
