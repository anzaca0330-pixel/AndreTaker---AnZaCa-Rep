# Hipótesis Forense: Arquitectura de Alteración de Doble Capa

El presente documento técnico establece la hipótesis forense que explica la coexistencia de dos anomalías informáticas de distinta naturaleza dentro del corpus documental electoral oficial. El análisis de la evidencia indica la existencia de un "embudo" o pasarela de procesamiento centralizada por la cual transitaron todos los documentos publicados.

## 1. Anomalía Estructural: Capa de Re-empaquetado (100% de Afectación)
La primera capa de intervención consistió en un proceso automatizado de re-empaquetado informático.
La evidencia criptográfica y estructural (tabla `XREF` corrupta y discrepancia de objetos internos `15 vs 13`) está presente en el **100% de las actas analizadas** a nivel nacional y en el exterior. 

**Hipótesis Forense:** Este proceso fue diseñado para actuar como una herramienta de "lavado" o sanitización de metadatos. Al forzar a que todos los documentos originales (provenientes de escáneres heterogéneos) pasaran por este script centralizado, se destruyó deliberadamente la cadena de custodia digital (hardware de origen, timestamps, autoría). El resultado es una estandarización artificial que oculta el origen real de cada archivo.

## 2. Anomalía Óptica: Capa de Inyección Sintética (18% de Afectación)
Una vez establecida la pasarela de re-empaquetado (Capa 1), la infraestructura fue utilizada para introducir documentos que nunca existieron físicamente.
El análisis de varianza óptica mediante extracción RGB demuestra que en regiones específicas (ej. 100% de la muestra en Putumayo y 83% en Norte de Santander), los documentos presentan un fondo de "Blanco Puro" matemático (`#FFFFFF`, RGB 255,255,255) sin ruido térmico ni artefactos de compresión óptica.

**Hipótesis Forense:** Estas actas son lienzos generados directamente en una computadora mediante diseño informático (documentos sintéticos). Al ser introducidos en la misma pasarela de procesamiento (Capa 1) que los documentos escaneados reales, estos documentos sintéticos "heredaron" la misma anomalía estructural XREF, mezclándose de manera estandarizada en la base de datos oficial.

## 3. Conclusión Técnica
Las anomalías no son producto de la casualidad, ni de errores de hardware aislados en las zonas de escaneo, sino de un **diseño arquitectónico de dos pasos**:
1.  **Destrucción de trazabilidad** (afectando a los documentos físicos reales).
2.  **Inyección selectiva** (sustituyendo la realidad en zonas específicas con archivos sintéticos).

La presencia concurrente de estas anomalías demuestra una alteración estructural sistémica que impide auditar y validar la integridad de la información publicada en la base de datos de consolidación.
