# Forensic Analysis - Claveros & Preconteo (2026)

This repository contains the official forensic scripts, cryptographic hashes, and statistical evidence proving the alteration of electoral data (E-14 forms vs Official Preconteo) during the 2026 election.

## Repository Contents

### 1. Structural Analysis (Claveros)
Scripts and reports demonstrating that the official PDFs of the E-14 forms contain multiple superimposed image layers and deleted creation metadata, proving digital forgery.
- `auditar_todas_actas_colombia_32_deptos.py`
- `AUDITORIA_NACIONAL_32_DEPARTAMENTOS_COLOMBIA.md`

### 2. Statistical Anomalies & Benford's Law
Scripts proving that the numbers within the forged PDFs were mathematically generated, violating Benford's law and exhibiting artificial variance (robotic behavior).
- `ejecutar_analisis_estadistico_nacional.py`
- `ESTUDIO_ESTADISTICO_NACIONAL.md`

### 3. Chain of Custody (Cryptographic Hashes)
Scripts to verify the SHA-256 hashes of the files.
- `generar_hashes_cadena_custodia.py`
- `comparar_hashes_e14.py`
- `REPORTE_COMPARATIVO_HASHES_2DA_VUELTA.md`

## Usage
These scripts are written in Python 3. To re-run the audits locally, ensure you have the raw E-14 PDFs and the Preconteo CSVs mounted in the correct directories as specified in the source code.
