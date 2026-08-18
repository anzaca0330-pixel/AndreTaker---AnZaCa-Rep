# ACTA DE HALLAZGOS FORENSES: MATRIZ TÉCNICA DE 14 PUNTOS DE INMUTABILIDAD Y PRECONTEO VS. ESCRUTINIO

**Autoría / Veeduría Ciudadana:** Andrea Zabala Cárcamo (Especialista Independiente)  
**Origen:** Informe de Hallazgos Forenses (Rescatado de la memoria caché de `markdownlive` post-intrusión)  
**Objeto:** Consolidación de 14 anomalías estructurales e inmutables identificadas en los formularios E-14 de la Registraduría Nacional.

---

## 1. MATRIZ DE LOS 14 HALLAZGOS TÉCNICOS FUNDAMENTALES

```
+-----------------------------------------------------------------------------------+
| 1. Metrología Óptica (#FFFFFF, σ=0) ──> 2. Arquitectura Híbrida (sRGB/DeviceGray) |
| 3. Mutación SHA-256 (4 días cont.) ──> 4. Errores XREF (15 vs 13 Objetos)        |
+-----------------------------------------------------------------------------------+
```

1. **Metrología Óptica de Píxeles ($\sigma = 0$):**  
   Los escaneos ópticos reales contienen varianza de píxeles, microrruido CMOS y textura de papel. El análisis prueba la inyección quirúrgica de objetos digitales blanco puro, matemáticamente estériles (`DeviceGray`), con desviación estándar cero ($\sigma = 0$) y luminancia máxima unificada de 65535.
2. **Arquitectura PDF Híbrida:**  
   19 de 26 archivos de la muestra primaria mezclan de forma atípica escaneos ópticos a color (sRGB) con objetos inyectados en escala de grises/negro (`DeviceGray`).
3. **Mutación Post-Publicación de Hashes SHA-256:**  
   El $100\%$ de la muestra presentó modificación de firmas criptográficas durante cuatro días consecutivos tras su primera publicación en el portal web oficial, violando la cadena de custodia.
4. **Declaración de Objetos Fantasma XREF:**  
   La totalidad de las 32 actas peritadas contiene errores de sintaxis al declarar 15 objetos internos reportados frente a sólo 13 objetos reales existentes (`reported 15 objects != highest 13`).
5. **Supresión Dirigida de Códigos QR:**  
   Tasa del $0\%$ de lectura legible en los códigos QR dentro del clúster de actas alteradas (archivos 82-86).
6. **Varianza Estadística Artificial:**  
   Desviación estándar atípicamente baja de apenas $2.5$ votos, concordante con una fórmula de redondeo algorítmico inyectada y no con la distribución humana.
7. **Incompatibilidad de Hardware Escáner:**  
   Dimensiones de página divergentes y metadatos de creación destruidos (`ExifTool`), lo que descarta el uso de escáneres institucionales homologados Kodak Alaris.
8. **Intervención en Capa Frontal Anverso:**  
   Al ser documentos de una sola cara (anverso sin reverso), la inyección de la máscara blanca actúa cancelando la captura óptica original del conteo.
9. **Desfasaje en Timestamps Cronométricos:**  
   Incoherencia entre la fecha de creación del archivo y la fecha de publicación web en la base de datos de la Registraduría.
10. **Ruptura de Firma de Contenedor PDF:**  
    Alteración del flujo `/Contents` que restructura el código fuente vectorial.
11. **Ausencia de Granulometría Térmica:**  
    Las áreas intervenidas no exhiben la degradación óptica por compresión JPEG propia del escaneo físico.
12. **Inyección de Parámetros de Redondeo:**  
    Presencia de constantes numéricas fijas que forzaban la distribución proporcional.
13. **Clonación Sintáctica entre Delegados y Claveros:**  
    Firma sintáctica XREF idéntica entre la versión web y la versión física de custodia.
14. **Metodología de Solo Lectura (`Read-Only`):**  
    Verificación mediante descriptores de archivos sin permisos de escritura usando `pdfimages`, `ImageMagick`, `qpdf` y `sha256sum`.

---

## 2. DIFERENCIACIÓN TÁCTICA: PRECONTEO VS. ESCRUTINIO

El expediente rescata una distinción legal y técnica crucial para entender el mecanismo del fraude:

### A. El Preconteo (La Narrativa Mediática)
* **Mecanismo:** Transmisión rápida por voz/teléfono desde las mesas a centros de cómputo (call centers).
* **Naturaleza:** Es un proceso **exclusivamente informativo y sin valor jurídico**. No se extrae del código PDF.
* **Función Táctica:** Se utilizó para instalar en los medios y la opinión pública la narrativa de una "victoria por margen mínimo" (menos del 1%).

### B. El Escrutinio Oficial (La Prueba Legal Alterada)
* **Mecanismo:** Procesamiento de las actas físicas E-14 ante los jueces y comisiones escrutadoras.
* **Naturaleza:** Es el **único conteo con valor legal vinculante**.
* **La Inyección del Software:** Al subir a los portales web los archivos PDF inyectados con máscaras blancas (`DeviceGray`) e ilegibilidad declarada, el sistema destruyó la herramienta jurídica que hubiese permitido a los abogados impugnar los números dictados por teléfono durante el preconteo.

---

## 3. CONCLUSIÓN
La estrategia combinó la transmisión telefónica rápida para fijar el resultado informativo con la inyección digital en los PDFs para inutilizar la verificación judicial durante el escrutinio oficial.
