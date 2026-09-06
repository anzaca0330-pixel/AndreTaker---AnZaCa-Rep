# HALLAZGO CRÍTICO: DOS CÓDIGOS QR EN ACTA DE TRANSMISIÓN

**Investigadora:** Andrea Zabala Cárcamo  
**Fecha:** 23 de agosto de 2026  
**Caso:** Auditoría forense a actas E-14 (Elecciones 2026)

---

## 🔍 Resumen del Hallazgo

Durante el proceso de auditoría forense de las actas E-14, específicamente en la copia correspondiente a **TRANSMISIÓN**, se detectó la presencia de **dos códigos QR** en un mismo documento. Esto representa una anomalía crítica, ya que el estándar oficial establece **un único código QR por acta**.

---

## 📊 Detalles Técnicos

| Elemento | Descripción |
| :--- | :--- |
| **Archivo analizado** | `Acta_Transmision_2026_E14.pdf` |
| **Cantidad de QR detectados** | 2 |
| **Herramienta utilizada** | `zbarimg` + inspección visual (decodificación de capas) |
| **Ubicación** | Ambos QR aparecen superpuestos en la misma zona de la página |

---

## 🧠 Implicaciones

1. **Posible manipulación digital** — La presencia de dos QR sugiere una inserción posterior o una superposición de capas.
2. **Riesgo de suplantación** — Uno de los QR podría redirigir a un sitio no oficial.
3. **Violación del estándar** — El manual técnico de la Registraduría establece claramente un solo QR por acta.

---

## 🔗 Acciones Recomendadas

- Realizar un análisis de metadatos con `exiftool` y `pdfid.py`.
- Comparar el QR oficial con el sospechoso mediante decodificación binaria.
- Reportar a la Fiscalía y al CNE para peritaje oficial.

---

## 📎 Evidencia Asociada

- Archivo original: `01_EVIDENCIA/TRANSMISION/Acta_Transmision_2026_E14.pdf`
- Hash SHA-256: `(por calcular al momento de la verificación)`
- Captura de pantalla: `04_BITACORA/NOTAS_DE_CAMPO/captura_dos_qr.png`
