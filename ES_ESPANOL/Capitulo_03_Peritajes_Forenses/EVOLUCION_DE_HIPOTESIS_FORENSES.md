# EVOLUCIÓN DE HIPÓTESIS FORENSES: DE LA OBSERVACIÓN PRIMARIA AL DICTAMEN CONSOLIDADO

**Autoría / Veeduría Ciudadana:** Andrea Zabala Cárcamo (Especialista Independiente)  
**Objeto:** Comparativa metodológica y científica entre las Hipótesis Primarias (Junio de 2026) y las Hipótesis Consolidadas de Auditoría Masiva (Agosto de 2026), con desglose cuantitativo de mesas, archivos y versiones analizadas por hallazgo.

---

## 1. MATRIZ DE POBLACIÓN Y ARCHIVOS ANALIZADOS POR FASE Y HALLAZGO

| Fase de Investigación | Hallazgo / Vector Auditado | Mesas / Universo ($N$) | Archivos Totales (Versiones y Páginas) |
| :--- | :--- | :--- | :--- |
| **Fase 1: Detección Primaria (Junio 1-6)** | Hallazgo 0: Lienzo Blanco (`#FFFFFF` DeviceGray) en Los Ángeles (1ª Vuelta) | $N = 19$ mesas (Mesas 001 a 019) | **19 mesas físicas, pero múltiples descargas de versión por mesa (Junio 1, 2, 3 y 4) sumando 76+ archivos PDF (228 páginas totales).** |
| **Fase 1: Detección Primaria (Junio 1-6)** | Quiebre de Participación (Mesa 013 a 014: $t(17)=8.2, p<0.00001$) | $N = 19$ mesas de Los Ángeles | **19 mesas físicas auditadas en sus distintas versiones temporales.** |
| **Fase 1: Muestreo de Control (Junio 6)** | Duplicación de Hashes SHA-256 y Falla de QR (0/30 en Bloque 82-86) | $N = 32$ actas de control | **32 PDFs descompresos, 96 páginas, 30 imágenes QR extraídas.** |
| **Fase 2: Expansión Consular (Junio-Julio)**| Auditoría de Voto en el Exterior y Días de la Semana (Lunes 58.5%) | $N = 5.982$ mesas en 88 consulados | **5.982 actas E-14 consulares escaneadas.** |
| **Fase 3: Auditoría Masiva (Julio-Agosto)**| Transgresión Sintáctica XREF (`reported 15 objects != highest 13`) | $N = 117.993$ mesas (32 Departamentos) | **117.993 archivos PDF (235.986 páginas totales).** |
| **Fase 3: Análisis Ley del segundo dígito de Mebane (Agosto)**  | Distorsión del 2do Dígito ($\chi^2 = 1.755,91, p < 0.001$) | $N = 233.448$ mesas a nivel nacional | **233.448 registros electorales procesados.** |
| **Fase 3: Cross-Auditoría (Agosto)**       | Cruce de Preconteo vs. E-14 Escrutinio | $N = 244.034$ registros de preconteo | **244.034 filas de datos consolidados.** |

---

## 2. CUADRO COMPARATIVO DE EVOLUCIÓN METODOLÓGICA

```
+-----------------------------------------------------------------------------------+
| PRIMER HALLAZGO PRIMARIO (Junio 2026)  ──>  HIPÓTESIS CONSOLIDADAS (Agosto 2026)  |
| Inyección de Páginas Blancas #FFFFFF        Auditoría Masiva 117.993 Mesas + Benford |
+-----------------------------------------------------------------------------------+
```

| Eje de Análisis | **Hallazgo Primario Inicial (1–6 Junio 2026)** | **Hipótesis Consolidada (Agosto 2026)** | Refinamiento y Alcance Probatorio |
| :--- | :--- | :--- | :--- |
| **Hallazgo Inicial del Lienzo Blanco** | **Detección Directa de Páginas Blancas (`#FFFFFF` DeviceGray):** En las 19 mesas de Los Ángeles (con múltiples descargas de versión por mesa: Junio 1, 2, 3 y 4), el primer descubrimiento fue el lienzo blanco sintético. | **Confirmación Metrológica ($\sigma = 0$):** Prueba en las 117.993 actas de que las páginas blancas son objetos digitales inyectados con varianza óptica cero. | Se confirmó que el lienzo blanco no fue un artefacto óptico, sino un objeto vectorial sintético inyectado por software. |
| **Origen del Error PDF** | Sospecha inicial de falla en el escáner local (Kodak Alaris) o firmware del consulado de Los Ángeles ($N=19$ mesas, 76+ PDFs de versión). | **Pasarela de Re-empaquetado Centralizado:** Alteración estructural XREF idéntica (*`reported 15 objects != highest 13`*) en las 117.993 actas de los 32 departamentos. | Se descartó el fallo de hardware local y se probó la existencia de un script centralizado de re-empaquetado informático. |
| **Comportamiento Estadístico** | Detección del desplome de participación (-53%) de la Mesa 013 a la 014 ($t(17) = 8.2, p < 0.00001$). | **Desviación Nacional Ley del segundo dígito de Mebane (2BL):** Varianza nula inter-mesa y distorsión del segundo dígito en 233.448 mesas ($\chi^2 = 1.755,91, p < 0.001$). | De una anomalía local ($N=19$ mesas) en Los Ángeles se pasó a la demostración cuantitativa masiva ($N=233.448$). |
| **Relación Delegados vs. Claveros** | Presunción inicial de que Claveros provenía del escaneo de papel físico guardado en el arca tricolor. | **Demostración de Clonación Digital:** El archivo de Claveros comparte la misma cicatriz XREF de 15 objetos que Delegados en las 117.993 actas. | Se probó que Claveros no es un escaneo físico independiente, sino un **clon cibernético**, demostrando la ruptura total de la cadena de custodia. |
| **Sabotaje de Red** | Interrupciones de red no atribuidas. | **Ciberataque APT, Evasión DPI (`#BLINDMASKING`) y Geobloqueo WAF:** Certificación de 1.650 intentos de rastreo en 5 min, borrado de Drive, rescate en `markdownlive` y geobloqueo Cloudflare. | Evidencia de represalia técnica y ocultamiento activo de infraestructura tras hacer pública la evidencia. |

---

## 3. PUNTOS CLAVE A RESALTAR

1. **El Hallazgo Cero Fueron las Páginas Blancas:**  
   La investigación no nació de especulaciones de formato (las 3 páginas eran el estándar regulatorio de 1ª Vuelta), sino del **hallazgo material directo de las páginas blancas sintéticas (`#FFFFFF`)** en la muestra inicial de 19 mesas de Los Ángeles (con sus descargas de versión diaria del 1 al 4 de junio).
2. **Escalamiento Cuantitativo Transparente:**  
   De las 19 mesas físicas iniciales (76+ PDFs de versiones entre el 1 y 4 de junio), la investigación escaló rigurosamente a **5.982 actas consulares**, luego a **117.993 PDFs de Claveros** y finalmente al escrutinio nacional de **233.448 mesas**.
3. **Inviolabilidad de la Prueba de Clonación:**  
   La demostración en los 117.993 archivos de que Claveros no es un escaneo físico sino un derivado sintético de Delegados constituye el pilar jurídico maestro para impugnaciones internacionales.
