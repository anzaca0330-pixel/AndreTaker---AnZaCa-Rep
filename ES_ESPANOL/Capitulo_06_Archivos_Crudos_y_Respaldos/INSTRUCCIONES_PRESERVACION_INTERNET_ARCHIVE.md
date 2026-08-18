# GUÍA DE PRESERVACIÓN INMUTABLE EN INTERNET ARCHIVE (ARCHIVE.ORG) Y ZENODO
## Protocolo para la Ingesta de la Bóveda Pesada (100 GB - 117.993 PDFs)

**Objetivo:** Garantizar la preservación inalterable, descentralizada e inmutable de la base de datos completa de actas E-14 (100 GB) bajo estándares de ciencia abierta y derecho internacional.

---

## 1. ¿POR QUÉ INTERNET ARCHIVE (ARCHIVE.ORG)?
1. **Inmunidad contra Censura:** Una vez cargados los archivos en Internet Archive, quedan congelados permanentemente. Ninguna entidad gubernamental, CDN ni administrador puede modificar o eliminar la evidencia.
2. **Capacidad Ilimitada y Gratuita:** Soporta la subida de los 100 GB sin costo alguno.
3. **Acceso Público Universal:** Genera enlaces permanentes (`https://archive.org/details/...`) que cualquier tribunal (CIDH), perito o ciudadano puede consultar.

---

## 2. PASOS SENCILLOS PARA SUBIR TU CARPETA (SIN NECESIDAD DE SER EXPERTA)

### Opción A: Subida por Navegador Web (Arrastrar y Soltar)
1. Ingresa a **[https://archive.org](https://archive.org)** e inicia sesión con tu cuenta.
2. Haz clic en el icono de **Upload** (Subir) en la esquina superior derecha.
3. Arrastra las carpetas comprimidas `.zip` de tu disco externo (`claveros_pdf.zip` o las carpetas por departamentos).
4. **Metadatos Recomendados a Colocar:**
   * **Title:** `Colombia 2026 Presidential Elections - E-14 Raw Forensic Database (117,993 PDFs)`
   * **Description:** `Complete raw PDF database of E-14 voting tally sheets for the 2026 Presidential Elections in Colombia. Collected for forensic audit and international Human Rights documentation (IACHR - 0000113728).`
   * **Subject Tags:** `colombia-elections-2026`, `e14-forensic-audit`, `electoral-integrity`, `iaea-cidh`
   * **License:** `Public Domain / Creative Commons CC0`
5. Haz clic en **Upload and Create Item**.

---

### Opción B: Subida Automatizada desde la Terminal (Línea de Comandos)
Si prefieres que la carga se ejecute automáticamente en segundo plano desde tu computador:

1. Instala la herramienta oficial de Internet Archive:
   ```bash
   pip install internetarchive
   ```
2. Configura tus credenciales:
   ```bash
   ia configure
   ```
3. Ejecuta la subida directa del disco extraíble:
   ```bash
   ia upload e14-forensic-database-2026 "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf" --title="Colombia 2026 E14 Raw Forensic Database" --mediatype="data"
   ```

---

## 3. ASIGNACIÓN DE DOI ACADÉMICO EN ZENODO (OPCIONAL)
Si deseas que tu dataset tenga un identificador académico **DOI (Digital Object Identifier)** respaldado por el **CERN (Organización Europea para la Investigación Nuclear)**:

1. Ingresa a **[https://zenodo.org](https://zenodo.org)**.
2. Crea un nuevo **Upload / Dataset**.
3. Sube el resumen de hashes `firmas_criptograficas_sha256.txt` y los CSVs de preconteo.
4. Zenodo te otorgará un **DOI único** (ejemplo: `10.5281/zenodo.1234567`) que podrás citar en cualquier artículo científico o escrito judicial.

---

## 4. INTEGRACIÓN EN EL REPOSITORIO
Una vez completada la subida a Internet Archive o Zenodo, pega el enlace resultante en la sección **Bóveda de Evidencia Pesada** en el `README.md` del repositorio:

```markdown
- 📦 **Bóveda Completa de PDFs (100 GB - Internet Archive):** https://archive.org/details/e14-forensic-database-2026
- 🔬 **Registro DOI Académico (Zenodo):** https://doi.org/10.5281/zenodo.XXXXXX
```
