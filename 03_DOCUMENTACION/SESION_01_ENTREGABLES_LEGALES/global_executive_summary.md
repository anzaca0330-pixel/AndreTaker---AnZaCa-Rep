# GLOBAL EXECUTIVE SUMMARY: TECHNICAL ANALYSIS OF E-14 TALLY SHEETS (ABROAD)
## OVERALL CONSOLIDATED REPORT — 2026 PRESIDENTIAL ELECTIONS

**Complainant:** Andrea Zabala Carcamo  
**Date:** July 2026  

---

## 1. CONTEXT AND SCOPE OF ANALYSIS

This document constitutes a global executive summary derived from automated forensic analysis on electoral material (E-14 tally sheets) digitized abroad. This report synthesizes findings from three independent sample populations evaluated using an identical technical and methodological pipeline (`QPDF`, `ExifTool`, `mutool`, `zbarimg`).

The three data populations analyzed and maintained independently in their respective reports are:
1. **United States Consulates:** 987 tally sheets.
2. **Spain Consulates:** 696 tally sheets.
3. **Control Group (Various):** 25,061 tally sheets.

### 1.1 Methodological Origin and Investigation Traceability

The development of this international forensic audit originated from field observations and civic oversight conducted on **June 2, 2026**, covering the 19 polling tables at Station 02 of the **Consulate of Los Angeles, California (USA)**. In that primary inspection, the investigator documented three fundamental empirical anomalies:
1. **Suppression and Unreadability of QR Codes:** Complete failure of automated reading on printed QR codes across that polling station's tally sheets.
2. **Hybrid E-14 Folio Formatting:** Irregular mixing of original color pages and photocopied/reprinted black-and-white pages within identical official electoral packets (e.g., Tables 011, 012, and 015 in color versus Tables 013, 014, and 018 in B&W).
3. **Atypical Statistical Behavior:** Cloning of numerical patterns across contiguous tables (e.g., Tables 001 to 003) and an abrupt collapse in turnout across the final tables at the station (Tables 015 to 019 with merely 12, 7, and 9 voters).

These initial findings prompted formal complaint filings before the **National Electoral Council (CNE)**, the **Inspector General's Office (Procuraduría)**, **URIEL**, and the **Electoral Observation Mission (MOE)**, supported by legal briefs on Council of State precedents regarding mandatory software audits.

From this test case in Los Angeles, the methodology was systematized and automated through an open-source pipeline (`QPDF`, `ExifTool`, `mutool`, `zbarimg`), scaling the forensic sweep to all tally sheets from the **United States (987 tally sheets)**, **Spain (696 tally sheets)**, and constructing a massive **Control Group (25,061 tally sheets)** to objectively validate the findings.

---

## 2. CONTROL GROUP: DOCUMENT INTEGRITY BASELINE

A massive volume of **25,061 PDF files** from various regions was processed to establish a technical baseline regarding standard behavior of digitization hardware and software.

> [!NOTE]
> **Importance of the Control Sample**
> Out of 25,061 evaluated files, automated filtering confirmed that **over 25,050 files (99.96%) were structurally clean and preserved factory metadata**, isolating only 10 documents (0.04%) with mechanical or physical scanning issues (corruption, missing pages, or unreadability). 
> 
> This analysis demonstrates that it is fully viable for tally sheets to be digitized and transmitted while preserving metadata traceability and PDF structural integrity.

---

## 3. FINDINGS AND FORMAL STATISTICAL COMPARISON

In sharp contrast to the control group, scrutiny of tally sheets from the United States and Spain constituencies revealed a statistically highly significant deviation from the baseline:

| Forensic Indicator | Control Group (n=25,061) | Spain (n=696) | US (n=987) | Relative Risk (RR) | Odds Ratio (OR) | Significance ($p$-value) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Purged Metadata (`Creator`/`Producer`)** | 0.00% (0) | 100.0% (696) | 100.0% (987) | $> 25,000$ | $\infty$ | $p < 0.0001$* |
| **QPDF Structural Warnings (`xref`)** | 0.00% (0) | 100.0% (696) | 100.0% (987) | $> 25,000$ | $\infty$ | $p < 0.0001$* |
| **Absent or Unreadable QR Code** | 0.008% (2) | 21.7% (151) | 23.3% (230) | $> 2,700$ | $> 3,200$ | $p < 0.0001$* |
| **Isolated Logical Errors (Empty/Incomplete)** | 0.04% (10) | 0.00% (0) | 0.00% (0) | N/A | N/A | N/A |

*\* Calculated using Fisher's exact test and Chi-squared test ($\chi^2$).*

### 3.1 Synthesis of Technical Observations and Inferences
- **Purged Metadata and Structural Warnings (100% impact in US and Spain):** All 1,683 files from these two geographic regions present total purging of traceability attributes and QPDF `xref` table warnings. This is consistent with the existence of a shared secondary document-processing workflow.
- **QR Code Behavior and 1-bit Images:** Rates of QR unreadability (21.7% in Spain and 23.3% in US) and 1-bit `DeviceGray` images were detected in both samples. This indicates image binarization or optimization occurred in the document workflow, hindering immediate automated auditing.

---

## 4. INTEGRATED CONCLUSIONS

1. **Statistically Proven Differentiation:** Objective comparison demonstrates statistically highly significant differences ($p < 0.0001$) between the Spain and US datasets and the control group.
2. **Processing Workflow Consistency:** The findings are consistent with the existence of a document-processing workflow distinct from that observed in the control sample.
3. **Need for Source System Audits:** Forensic evidence alone does not determine the intent or cause of anomalies; additional examination of original acquisition systems, receiving server logs, and native PDF files is required.

---

## 5. NEXT STEPS IN THE AUDIT

> [!TIP]
> **Expansion of Global Forensic Sweeps**
> Automated analysis continues across remaining overseas constituencies using the same forensic pipeline (`QPDF`, `ExifTool`, `mutool`, `zbarimg`) to determine the geographic scope of these technical deviations relative to the control group.
