# Bitácora de Evidencia

## 1. Archivo de hashes añadido
- Archivo: `hashes_takeout_gemini.txt`
- Ruta en repositorio: `01_EVIDENCIA/HASHES/hashes_takeout_gemini.txt`
- Propósito: conservar la cadena de custodia con SHA‑256 de los archivos del Takeout.

## 2. Búsqueda de actividad (junio/julio 2026)
- Se ejecutó `grep -ri "2026-06"` y `grep -ri "2026-07"` dentro de `takeout_contents`.
- **Resultado:** no se encontraron coincidencias en los archivos inspeccionados (JSON, LOG, TXT).

## 3. Dependencias de Playwright
- Se intentó instalar dependencias con `sudo npx playwright install-deps`, pero se requiere elevación de privilegios. Se dejó pendiente para que el usuario lo ejecute.

## 4. Extracción de Indicadores de Compromiso (IoCs) del Google Takeout
- **Archivo Fuente:** `REPORTE_FORENSE_TAKEOUT_IOCS.md` (575 registros de telemetría).
- **Dispositivo Primario Detectado:** `motorola edge plus 2023`.
- **Análisis de IPs / Subredes:** Mapeo de 112 direcciones IP registradas en los logs de acceso de Google, incluyendo rangos de salida VPN (ExpressVPN/Cloudflare) y peticiones anómalas.

## 5. Integración con el Punto de Control
- **Estado:** Sincronizado en `03_DOCUMENTACION/PUNTO_DE_CONTROL.md`.
- **Cadena de Custodia:** Certificada mediante el sello SHA-256 en `01_EVIDENCIA/HASHES/hashes_takeout_gemini.txt`.

## 6. Procesamiento de Takeout de Hoy (Cuenta `azabalabaez`)
- **Directorio Fuente:** `/home/andrea-zabala-c/Desktop/AISLAMIENTO_AZABALABAEZ/Takeout`
- **Contenido Extraído:** Conversaciones de Gemini Workspace sobre la Denuncia Estadística de Los Ángeles (análisis mesa por mesa y día por día).
- **Transcripción Formateada:** `03_DOCUMENTACION/SESION_01_ENTREGABLES_LEGALES/TRANSCRIPCION_GEMINI_AZABALABAEZ.md`
- **Sello Criptográfico SHA-256:** `4fc30014761dfec1601be3f06f83ed217a3194b81f844392403e150e177176f4` (congelado en `hashes_takeout_gemini.txt`).

## 7. Refutación del Argumento de "Comportamiento Normal del Software"
- **Documento Creado:** `03_DOCUMENTACION/SESION_01_ENTREGABLES_LEGALES/REFUTACION_ARGUMENTO_SOFTWARE_NORMAL.md`.
- **Principios Clave:** Violación ISO 32000, presencia de Mesas de Control Limpias, física de captura ($\sigma = 0$), invalidación de QR y mutación criptográfica.
- **Veredicto:** No es un error de fábrica. Es sistemático. Y está documentado.

_Nota: Se mantiene la integridad forense usando datos reales; no se generaron datos ficticios._



