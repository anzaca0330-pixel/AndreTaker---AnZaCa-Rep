# NOTA EXPLICATIVA PERICIAL: ORIGEN DE LOS DATOS Y BASE DE DATOS DE CONSULADOS (DEPTO 88)

**Dirigido a:** Representación Jurídica (Abogado Jose), Auditores, Jueces y Organismos Internacionales (CIDH/OEA).  
**Veeduría Principal:** Andrea Zabala Cárcamo (C.C. 43.925.102)  
**Fecha:** 31 de Julio de 2026  

---

## 📌 ¿POR QUÉ LOS CONSULADOS NO ESTÁN EN LA CARPETA DE CLAVEROS Y DÓNDE ESTÁ EL SOPORTE PROBATORIO?

### 1. Inexistencia de Claveros Locales en el Exterior
Bajo el Código Electoral Colombiano, en los puestos de votación en el exterior (Consulados) **no existen Comisiones Escrutadoras Locales de Claveros** (como sí existen a nivel municipal y departamental en el territorio colombiano). Al cerrarse la votación en los consulados, la información se transmite y consolida de forma directa hacia Bogotá. Por tanto, procedimentalmente no se expiden actas de claveros locales mesa a mesa por consulado.

### 2. Inexistencia Técnica en los Servidores del Estado
En la API perimetral e infraestructura oficial de la Registraduría (`escrutinios2vueltapresidente2026.registraduria.gov.co`), la entidad estatal **NO publica ni aloja la rama de archivos E-14 de Claveros para el Departamento 88 (Consulados)**. Por esta razón, cualquier barrido o descarga masiva de la carpeta de claveros genera únicamente los 32 departamentos territoriales colombianos.

### 3. Fuente Oficial Primaria Incluida en esta Carpeta
Para suplir la ausencia de claveros consulares y realizar el peritaje forense sobre las **2,365 mesas del exterior (455,262 votos efectivos)**, la veeduría utilizó la **Base de Datos Oficial de Preconteo del Departamento 88 emitida por la Registraduría Nacional**:

* 📄 **`reporte_preconteo_oficial_registraduria_depto88.csv`** (Soporte plano con el desglose de las 2,365 mesas consulares en 24 países).
* 📊 **`ESTUDIO_ESTADISTICO_ANOMALIAS_CONSULADOS.md`** (Prueba de hipótesis Z = -56.96, p < 0.0001 y Ley del segundo dígito de Mebane).
* 🌍 **Reportes por País** (`informe_forense_estados_unidos.md`, `informe_forense_espana.md`, etc.).

---

## 🚨 4. REPROCHE JURÍDICO-PERICIAL: OPACIDAD DEL VOTO EXTERIOR Y VULNERACIÓN DE LA AUDITORÍA CIUDADANA

### 4.1. ¿Por qué el Estado NO debería omitir la transparencia del escrutinio en el exterior?
* **Creación de un "Enclave de Opacidad":** Excluir al exterior de la publicación de actas E-14 de claveros digitalizadas y de audiencias de escrutinio local rompe la equidad de garantías procesales entre los votantes en Colombia y la diáspora en el exterior (censo de 827.750 ciudadanos).
* **Riesgo de Inyección Directa en Transmisión:** Al transmitir la votación consular "en paquete cerrado" directamente a los servidores centrales de Bogotá sin la intermediación de actas de claveros verificables públicamente mesa a mesa, se elimina el control social en origen. Esto crea una **ventana de vulnerabilidad óptima** para la inyección informáticamente inducida de vectores (`/XObject`) o permutaciones de votos ($V_1 \leftrightarrow V_2$) sin riesgo de contraste físico local inmediato.

### 4.2. Intentos Sistemáticos de Opacar la Verificabilidad Pública
* **Asimetría Informativa Forzada:** Al no disponer de la rama 88 en la API de escrutinio y simultáneamente activar mecanismos de **Geo-bloqueo (Geofencing via Nexusguard/Cloudflare `cf-mitigated: challenge`)** que bloquean las solicitudes masivas desde IP internacionales (como se demostró en el peritaje de red), el Estado implementó un cerco técnico doble para impedir que la ciudadanía en el exterior audite sus propios votos.
* **Imposibilidad de Cotejo Físico vs. Digital:** Sin actas E-14 de claveros publicadas para el Depto 88, los electores y veedores internacionales quedan imposibilitados para cotejar la copia física recibida por el jurado/testigo consular contra el dato consolidado final, obligando a la veeduría a desenmascarar el anomalía estructural mediante **prueba inferencial matemática ($Z = -56.96, p < 0.0001$)**.

---
*Este documento y sus archivos anexos constituyen prueba pericial inmutable y garantizan la solidez jurídica de la impugnación electoral.*
