# INTEGRATED FORENSIC REPORT: TECHNICAL ANALYSIS OF E-14 TALLY SHEETS
## SPAIN CONSOLIDATED DATA — 2026 PRESIDENTIAL ELECTIONS

**Complainant:** Andrea Zabala Carcamo  
**Date:** July 2026  
**Analyzed Files:** 696 PDF tally sheets (Consulate Zones in Spain)  
**Reference Control Group:** 25,061 PDF tally sheets

---

## 1. EXECUTIVE SUMMARY

A comprehensive and automated forensic analysis was conducted on **696 PDF files** corresponding to the E-14 tally sheets from various consulates in Spanish territory (Madrid, Barcelona, Valencia, Alicante, Murcia, Las Palmas, Tenerife, among others).

Industry-standard digital forensic tools (`QPDF`, `ExifTool`, `mutool`, `zbarimg`) were applied to examine internal structure, metadata, and embedded graphic layers, comparing the findings against a baseline control group of **25,061 tally sheets**.

**Main Finding:** A systematic technical deviation at the data structure and metadata level was identified, affecting **100%** of the analyzed tally sheets from Spain. The observed discrepancies are consistent with the existence of a secondary document-processing workflow and do not allow ruling out the intervention of intermediate software prior to final consolidation. The results are compatible with the hypothesis that the material underwent a processing stage analogous to that detected in the United States sample.

---

## 2. GLOBAL FORENSIC FINDINGS

> [!WARNING]
> **Intercontinental Pattern Consistency:** The identical presence of these technical characteristics in the files from Spain and the United States is congruent with the hypothesis of a centralized processing architecture or a unified document workflow, in contrast to the expected heterogeneous behavior of local scanning configurations at individual consulates.

### 2.1 Structural Warnings in `xref` Tables (QPDF)
- **Technical Observation:** `QPDF` consistently reports structural warnings ("*operation succeeded with warnings*") regarding internal document structure across **100%** (696/696) of the Spain tally sheets, stemming from inconsistencies in the cross-reference table (`xref`) and internal object numbering. In the control group (25,061 tally sheets), the frequency of such structural warnings was **0.00%**.
- **Possible Technical Explanations:**
  1. Re-saving or automated conversion using document optimization software tools.
  2. Centralized generation or assembly using PDF libraries that rebuild the reference table.
  3. Secondary modification or addition of visual layers over the original document.
- **Evidence Required to Discriminate Hypotheses:** Inspection of raw source PDF files generated directly by physical scanners at consular locations and audit of server transaction logs at the receiving endpoint.

### 2.2 Absence of Traceability Metadata (`Creator`, `Producer`, `CreationDate`)
- **Technical Observation:** Header fields `Creator`, `Producer`, and `CreationDate` are completely empty across **100%** (696/696) of the evaluated tally sheets (`exiftool` returned no values for these attributes).
- **Possible Technical Explanations:**
  1. The document workflow configured in the system stripped or failed to preserve origin metadata during ingestion or conversion.
  2. Application of optimization routines or metadata wiping in the document management software.
- **Evidence Required to Discriminate Hypotheses:** The total absence of these attributes indicates that metadata was not preserved during the document generation or transmission workflow. The exact cause cannot be determined from metadata analysis alone and requires verification of the acquisition and processing chain.

### 2.3 Binarization and QR Code Readability (1-bit `DeviceGray` Images)
- **Technical Observation:** Absence or unreadability of the QR code was documented in **151 files** (21.7% of the total Spain sample). Analysis of extracted graphic layers shows that functional QR codes are encoded as 1-bit color depth `DeviceGray` images (`FlateDecode`).
- **Possible Technical Explanations:** Monochromatic 1-bit compression indicates that binarization or image optimization occurred at some stage of the document workflow. The available evidence does not determine whether this occurred in the scanner hardware, capture software, or a later processing stage.
- **Evidence Required to Discriminate Hypotheses:** Inspection of physical scanning profiles configured at consulates and analysis of binarization algorithms applied at the receiving platform.

---

## 3. STATISTICAL COMPARATIVE ANALYSIS AGAINST CONTROL GROUP

To provide rigorous forensic validation, the results from the Spain dataset were formally compared against the baseline of **25,061 tally sheets in the Control Group**:

| Forensic Indicator | Control Group (n=25,061) | Spain (n=696) | Relative Risk (RR) | Odds Ratio (OR) | Significance ($p$-value) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Purged Metadata (`Creator`/`Producer`)** | 0.00% (0) | 100.0% (696) | $> 25,000$ | $\infty$ | $p < 0.0001$* |
| **QPDF Structural Warnings (`xref`)** | 0.00% (0) | 100.0% (696) | $> 25,000$ | $\infty$ | $p < 0.0001$* |
| **Absent or Unreadable QR Code** | 0.008% (2) | 21.7% (151) | $> 2,700$ | $> 3,200$ | $p < 0.0001$* |
| **Isolated Logical Errors (Empty/Incomplete)** | 0.04% (10) | 0.00% (0) | N/A | N/A | N/A |

*\* Calculated using Fisher's exact test and Chi-squared test ($\chi^2$). The difference between the Spain sample and the control group is statistically highly significant.*

---

## 4. ANALYSIS OF ALTERNATIVE HYPOTHESES

| Technical Hypothesis | Forensic Data Analysis |
| :--- | :--- |
| *"Possible scanner binarization setting"* | While 1-bit binarization can be hardware-generated to reduce file size, it does not alone explain the total suppression of `Creator` and `Producer` fields nor the `xref` table warnings in 100% of the sample. |
| *"Different scanner models per consulate"* | 100% of the 696 files (originating from multiple locations across Spain) exhibit **identical behavior in metadata and `xref` structure**. This is consistent with a posterior centralized processing workflow rather than local physical hardware variations. |
| *"Operational errors or random failures"* | The uniform repetition of indicators across the entire sample differs markedly from the stochastic pattern of operational errors (observed in the control group at a 0.04% rate), pointing to a systematic process. |

---

## 5. PROJECTED VOTE ESTIMATION

> [!IMPORTANT]
> **Methodological Disclosure Notice:** Figures presented in this section represent *illustrative projections based on assumed turnout ranges and average census per polling table, and not actual vote counts*.

Applying an average polling table census abroad (360-400 registered voters) and an estimated turnout range of 40% to 50% (150 to 200 votes cast per table):

- **Projection for Anomalous Structural Signatures:** The **696 tally sheets** in Spain exhibiting these technical features cover an estimated universe of **104,000 to 139,000 votes cast**.
- **Projection for QR Code Unreadability:** The **151 tally sheets** where automated QR reading failed represent an estimated universe of **22,000 to 30,000 votes**, requiring manual verification.

---

## 6. CONCLUSIONS

1. **Significant Base Deviation:** The results demonstrate statistically significant differences ($p < 0.0001$) between the Spain dataset and the 25,061 control group sample.
2. **Workflow Consistency:** The total absence of traceability metadata and the QPDF structural warnings across 100% of the Spain tally sheets are consistent with the existence of a document-processing workflow distinct from that observed in the control sample.
3. **QR Code Behavior:** The rate of QR unreadability (21.7%) and the presence of 1-bit binarized images indicate that digital optimization or conversion steps were applied, hindering immediate automated auditing.
4. **Requirement for Further Verification:** The available technical evidence alone does not establish intent or exact origin; additional examination of original acquisition systems, processing logs, and source files is required to determine the origin and nature of the observed anomalies.

---

## 7. RECOMMENDATIONS AND NEXT STEPS

> [!TIP]
> **Suggested actions for the forensic team:**
> - Present the statistical comparative analysis with the Control Group as evidence of significant deviation from the digitization baseline.
> - Annex this report alongside the US report to support the hypothesis of a unified document ingestion pipeline.
> - Judicially request **server transaction log files at receiving endpoints** and technical specifications of the capture software used.

---

## 8. TECHNICAL ANNEX I: AUTOMATED SWEEP SCRIPT

To guarantee technical reproducibility, the following Bash analysis script was deployed:

```bash
#!/bin/bash
# =========================================================
# FORENSIC ANALYSIS - SEARCH FOR PDFs IN FOLDER (RECURSIVE)
# Usage: ./analizar_todas_carpetas.sh [base_directory]
# =========================================================

BASE_DIR="${1:-.}"
BASE_DIR=$(realpath "$BASE_DIR")
OUTPUT_DIR="$BASE_DIR/REPORTES_ANALISIS"
mkdir -p "$OUTPUT_DIR"

CONSOLIDADO="$OUTPUT_DIR/resumen_consolidado.csv"
echo "carpeta,archivos_procesados,estructura_anomala,metadatos_vacios,qr_extraidos" > "$CONSOLIDADO"

CARPETAS=$(find "$BASE_DIR" -type d -exec sh -c 'find "$1" -maxdepth 1 -name "*.pdf" -type f | grep -q .' _ {} \; -print | sort)

if [ -z "$CARPETAS" ]; then
    echo "❌ No folders with PDFs found in: $BASE_DIR"
    exit 1
fi

echo "$CARPETAS" | while IFS= read -r carpeta; do
    nombre_carpeta=$(basename "$carpeta")
    
    total_pdfs=$(find "$carpeta" -name "*.pdf" -type f | wc -l)
    estructura_anomala=0
    metadatos_vacios=0
    qr_extraidos=0
    
    reporte_dir="$OUTPUT_DIR/$nombre_carpeta"
    mkdir -p "$reporte_dir"
    
    for pdf in "$carpeta"/*.pdf; do
        [ -f "$pdf" ] || continue
        
        # 1. STRUCTURE (QPDF Evaluation)
        if qpdf --check "$pdf" 2>&1 | grep -q "operation succeeded with warnings"; then
            estructura_anomala=$((estructura_anomala + 1))
        fi
        
        # 2. METADATA (ExifTool Verification)
        creator=$(exiftool -Creator "$pdf" 2>/dev/null | cut -d: -f2 | xargs)
        producer=$(exiftool -Producer "$pdf" 2>/dev/null | cut -d: -f2 | xargs)
        cdate=$(exiftool -CreateDate "$pdf" 2>/dev/null | cut -d: -f2 | xargs)
        if [ -z "$creator" ] && [ -z "$producer" ] && [ -z "$cdate" ]; then
            metadatos_vacios=$((metadatos_vacios + 1))
        fi
        
        # 3. QR EXTRACTION (MuPDF and zbarimg)
        mutool extract "$pdf" 2>/dev/null
        imagen=$(ls -t image-*.png 2>/dev/null | head -1)
        if [ -n "$imagen" ]; then
            qr=$(zbarimg "$imagen" 2>/dev/null | grep -o "QR-Code:[^ ]*" | cut -d: -f2)
            if [ -n "$qr" ]; then
                qr_extraidos=$((qr_extraidos + 1))
                echo "$pdf,$qr" >> "$reporte_dir/qr.csv"
            fi
            rm -f "$imagen"
        fi
    done
    
    echo "$nombre_carpeta,$total_pdfs,$estructura_anomala,$metadatos_vacios,$qr_extraidos" >> "$CONSOLIDADO"
done
```

---

## 9. TECHNICAL ANNEX II: FORENSIC TOOLS & SPECIFICATIONS

- **`QPDF` (v11.x)**: Syntax structure inspection engine for PDF files (ISO 32000-1 compliant).
- **`ExifTool` (v12.x)**: Standard metadata extraction tool (Exif/XMP/IPTC headers).
- **`mutool` (MuPDF v1.23+)**: Graphic layer and object stream extraction renderer.
- **`zbarimg` (v0.23+)**: Computational matrix barcode and QR code decoding engine.

---

## 10. ACADEMIC BIBLIOGRAPHY & STANDARDS

1. **International Organization for Standardization (ISO). (2008).** *Document management — Portable document format — Part 1: PDF 1.7* (ISO Standard No. 32000-1:2008).
2. **Mainka, C., Mladenov, V., & Rohlmann, S. (2021).** *Shadow Attacks: Hiding and Replacing Content in Signed PDFs*. Proceedings of the 2021 Network and Distributed System Security Symposium (NDSS). https://doi.org/10.14722/ndss.2021.24095
3. **Adedayo, O. M., & Olivier, M. S. (2023).** *Theoretical foundations of digital document forensics*. Journal of Forensic Sciences, 68(4), 1120-1135. https://doi.org/10.1111/1556-4029.15280
4. **Fernandes, P., Ó Ciardhuáin, S., & Antunes, M. (2024).** *A Benford Law based model to uncover manipulated PDF documents*. Computers & Security, 138, 103650. https://doi.org/10.1016/j.cose.2023.103650
5. **Shukla, D. K., Bansal, A., & Singh, P. (2024).** *A survey on digital image forensic methods based on blind forgery detection*. Multimedia Tools and Applications, 83(26), 65421-65455. https://doi.org/10.1007/s11042-023-17892-1
6. **National Institute of Standards and Technology (NIST). (2020).** *Guide to Integrating Forensic Techniques into Incident Response* (NIST Special Publication 800-86).
