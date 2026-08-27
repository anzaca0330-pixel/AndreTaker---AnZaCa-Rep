# EVOLUCIÓN TÉCNICA: BLIND MASKING Y PLANCHADO 1-BIT

**Investigadora:** Andrea Zabala Cárcamo  
**Fecha:** 25 de agosto de 2026

---

## 🧩 Línea de Tiempo

| Fase | Técnica | Descripción |
| :--- | :--- | :--- |
| **Fase 1** | Parches | Inserción de fragmentos PDF sobre el original. Detectable por diferencias en fuentes y tamaños. |
| **Fase 2** | Blind Masking | Ocultamiento de datos mediante capas blancas semitransparentes. |
| **Fase 3** | Planchado 1-Bit | Conversión forzada a 1-bit (blanco y negro) con pérdida de capas. **Estrategia actual.** |

---

## 🛠️ Método de Detección

1. **Extracción de metadatos:** `exiftool -all <archivo>`
2. **Análisis de profundidad de bits:** `pdfimages -list <archivo>`
3. **Inspección de capas:** Extracción con `qpdf` y comparación de estructuras internas.

---

## ⚠️ Implicaciones Forenses

- El planchado 1-Bit elimina las capas de edición, pero **no elimina los metadatos internos** (XREF, objetos).
- Permite identificar manipulación mediante el análisis de la tabla de objetos del PDF.

---

## 🔬 Hallazgo en Claveros

- **Acta:** Claveros E-14
- **Error detectado:** XREF indica 15 objetos, pero al inspeccionar solo hay 13 válidos.
- **Conclusión:** 2 objetos fueron insertados y luego "planchados" para ocultarlos.

---

## 📎 Referencias

- `qpdf` documentación oficial
- "Forensic Analysis of PDF Files" - Simson Garfinkel
- Norma ISO/IEC 27037 (Preservación de evidencia digital)
