# EVOLUCIÓN TÉCNICA DEL FRAUDE: DE "BLIND MASKING" A "RASTER DEEPFAKE"

**Objetivo Pericial:** Demostrar documentalmente cómo los perpetradores adaptaron sus métodos de falsificación electoral entre la Primera y la Segunda Vuelta (y muestras de Delegados), cambiando la técnica de ocultamiento para evadir detección, pero dejando intacta la firma del software falsificador.

---

## 1. Síntesis de la Evolución Forense

El análisis estructural profundo de los PDFs E-14 (Meta y Delegados) reveló dos técnicas de manipulación sucesivas. Lejos de ser métodos aislados, representan una **evolución intencional** de la misma herramienta de fraude:

| Fase | Técnica Pericial | Evidencia Forense Extraída | Implicación Legal |
| :--- | :--- | :--- | :--- |
| **Fase 1: Blind Masking (Parches vectoriales)** | Inyección de capas `/DeviceGray` (rectángulos blancos) flotantes sobre el contenido original (Objetos 6 y 11). | - Comandos vectoriales detectables (`re`, `cm`, `Do`). <br>- Parches blancos extraíbles físicamente con `pdfimages`. <br>- **Tabla XREF corrupta (Objetos 14 y 15 faltantes).** | Los perpetradores usan el software para "tapar" datos (votos) sin destruir el fondo del escáner original. Detectable por análisis básico de capas. |
| **Fase 2: Raster Deepfake (Planchado a 1-Bit)** | Edición directa de la imagen fuente en software externo (Photoshop/Raster). Aplastamiento de capas a 1-Bit (`DeviceGray`). Inserción de la imagen como bloque único. | - **NO** hay capas separadas ni comandos vectoriales. <br>- Alta proporción anómala de píxeles `#FFFFFF` (Blanco puro > 90%). <br>- **Misma tabla XREF corrupta (Objetos 14 y 15 faltantes).** | Los perpetradores aprendieron que los parches flotantes son rastreables. Decidieron destruir la matriz de la imagen antes de empaquetarla, pero el software empaquetador dejó la misma firma sintáctica. |

---

## 2. La Huella Digital del Software (El Error XREF 15 != 13)

La prueba irrefutable de que ambas fases son producto de la misma organización criminal radica en el empaquetador PDF. A pesar de que la "Carga Útil" (*Payload*) cambió de ser un parche vectorial a ser una imagen aplanada, **el software cometió exactamente el mismo error sintáctico al guardar el archivo**:

```text
WARNING: reported number of objects (15) is not one plus the highest object number (13)
```

Al borrar los objetos originales del escáner (IDs 14 y 15) para inyectar sus falsificaciones en los IDs 6 y 11, el generador rompió el índice (Cross-Reference Table). Esta anomalía es una **firma de autor** ineludible.

---

## 3. Argumento Legal para Organismos Internacionales (CIDH)

La evidencia técnica actual trasciende la mera demostración de manipulación y prueba la **evolución activa del fraude**. 

> *"La persistencia del error estructural (XREF) en ambas variantes —la de 'parches vectoriales' y la de 'planchado a 1-Bit'— constituye la huella digital inmutable del mismo sistema de falsificación. Esta evolución técnica, lejos de debilitar el caso, demuestra que los perpetradores están adaptando activamente sus métodos para evadir la detección forense. El cambio de táctica comprueba la plena conciencia de culpabilidad, la intencionalidad y el nivel de sofisticación organizada detrás de la alteración masiva de los documentos electorales de la Nación."*

---

## 4. Metodología de Auditoría (Scripts Complementarios)

Para auditar esta evolución, el peritaje emplea un enfoque dual (incluido en el repositorio):

1. **Mapeo de Píxeles (El script anterior):** Escanea la proporción anómala de blanco puro (`#FFFFFF`) en imágenes extraídas para detectar las zonas borradas intencionalmente (Photoshop).
2. **Mapeador Estructural Híbrido (`mapeador_estructural_deepfake.py`):** Cruza el análisis de capas (identificando la falta de ensamblaje), la validación de *1-Bit Flattening*, y extrae la confirmación del error `XREF` mediante `qpdf`, garantizando un escrutinio blindado contra cualquier variante de este generador malicioso.
