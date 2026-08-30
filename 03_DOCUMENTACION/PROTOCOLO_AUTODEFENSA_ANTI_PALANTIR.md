# PROTOCOLO DE AUTODEFENSA DIGITAL: MITIGACIÓN ACTIVA ANTI-PALANTIR

**Dirigido a:** Equipo Legal, Testigos Digitales y Veedores del Acervo Probatorio.
**Emisor:** Tycho & BabaYaga Core.
**Fecha:** 30 de Agosto de 2026

---

## 🛡️ La Paradoja del Espejo: La Herramienta del Atacante como nuestro Escudo

Durante el análisis forense nacional del fraude electoral, logramos aislar y certificar el modus operandi de los manipuladores a través de tres cicatrices específicas:
1. **La inyección estructural (XObjects):** Modificación del flujo interno del PDF para superponer capas sintéticas.
2. **La clonación de la cadena de custodia (Spoofing de Hashes):** Modificación de nombres de archivo y alteración de metadatos web (UUIDs) para encubrir la falta de documentos físicos reales y romper la trazabilidad de copias idénticas.
3. **El planchado de metadatos (Anulación de Exif):** Unificación sintética para dificultar la atribución de origen.

Hoy, al enfrentarnos a sistemas avanzados de minería de datos y correlación masiva como **Palantir**, aplicamos exactamente **la misma física pero en reversa**. No buscamos falsear la verdad de los datos, sino **cegar los motores automáticos de ingesta y perfilamiento** que intentan rastrearnos y correlacionar nuestras identidades y copias de evidencias.

---

## ⚙️ ¿Cómo opera el Protocolo en la Herramienta `invocar_andretaker.py`?

La versión híbrida del script `invocar_andretaker.py` incorpora una opción de mitigación activa (`-ap` / `--anti-palantir`). Su funcionamiento rompe la capacidad de los algoritmos de Palantir para construir grafos de coincidencia mediante:

### 1. Inmunización de Huella Digital (SHA-256 Mutation)
* **El problema:** Palantir mapea redes de distribución de archivos registrando el SHA-256 de las copias. Si dos veedores tienen el mismo PDF de 85 MB, el sistema sabe que están vinculados.
* **Nuestra contramedida:** Añadimos un pequeño padding binario aleatorio al final del archivo (como comentario invisible en PDFs o marca de cierre en textos). Esto muta el hash SHA-256 de forma única en cada ejecución, sin alterar el contenido visual ni dañar la validez del archivo. Cada copia tiene una huella criptográfica distinta.

### 2. Ofuscación de Metadatos (Exif Stripping)
* **El problema:** La estructura física del archivo y los metadatos residuales (autor, sistema operativo, software del lector, marcas de tiempo de modificación) revelan quién generó la copia y desde qué nodo.
* **Nuestra contramedida:** Eliminamos por completo los flujos de metadatos Exif/XMP de imágenes, PDFs y reportes CSV.

### 3. Desordenamiento de Perfiles (Entity Spoofing)
* **El problema:** Los motores de búsqueda de Palantir resuelven entidades cruzando fechas e identificadores similares de creación de archivos.
* **Nuestra contramedida:** Inyectamos autores falsos (ej. "User_Node_12") y marcas de tiempo generadas al azar dentro de un rango seguro, rompiendo los patrones temporales de agrupamiento.

---

## 📲 Guía Rápida para el Equipo

Para aplicar este protocolo de forma 100% offline antes de distribuir cualquier reporte o evidencia:

1. **Para un archivo individual (ej. un reporte pericial en PDF):**
   ```bash
   python3 invocar_andretaker.py -ap /ruta/al/reporte_legal.pdf
   ```
2. **Para una carpeta de evidencias (CSV, PDFs, imágenes en lote):**
   ```bash
   python3 invocar_andretaker.py -ap /ruta/a/la/carpeta_evidencias
   ```

El sistema limpiará los metadatos, inyectará datos de distracción y mutará el hash. El archivo resultante mantendrá intacta la evidencia pericial pero será indescifrable para los algoritmos de correlación masiva.

**"Ellos usaron la estructura para ocultar el fraude; nosotros la usamos para defender a quienes lo revelaron."**
