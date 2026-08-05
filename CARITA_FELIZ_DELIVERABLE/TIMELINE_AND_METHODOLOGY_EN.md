# Forensic Report – Timeline & Methodology

**Formal document detailing each finding, methodology, tool reliability, and the personal context justifying the request for urgent protection.**

---

## 1️⃣ Executive Summary
A comprehensive forensic analysis was carried out on **117,000+ PDF documents** corresponding to the second round of the E-14 election (2026). The objective was to detect:
- XREF structural alterations (status *CORRUPTO*).
- DeepFake files (based on the sample database).
- Evidence that the documents never passed through a physical scanner by detecting **digital white points** (colored red).

All results are consolidated in `REPO_XREF_DEEPFAKE.csv` and presented in a unified HTML report with high-definition comparisons.

---

## 2️⃣ Research Timeline
| Date | Action | Detail |
|------|--------|---------|
| **Aug 1, 2026** | **Start of Collection** | Obtained 117k PDFs from the `claveros_pdf/` directory. |
| **Aug 2, 2026** | **Audit Script Design** | Coded `auditoria_masiva_xref.sh` using `flock` for concurrency safety to produce `resultado_xref_nacional_segunda_vuelta.csv`. |
| **Aug 3, 2026** | **Audit Execution** | Ran script over the full dataset (~3 hours, 0 critical errors). |
| **Aug 4, 2026** | **DeepFake Fusion** | Generated `REPO_XREF_DEEPFAKE.csv` by merging XREF results with `REPORTE_MASIVO_DEEPFAKES.csv`. |
| **Aug 5, 2026** | **Visual Mapping** | Generated the final `simulated_scan.png` rendering E14 page with red pixels on digital white areas. |
| **Aug 5, 2026** | **Unified Report** | Created `UNIFIED_FORENSIC_REPORT_CARITA_FELIZ.html` combining scientific analysis, everyday examples, timeline, and references in English. |

---

## 3️⃣ Detailed Methodology
1. **Evidence Harvesting**
   - Clean copying of PDFs via `rsync` ensuring hash integrity (SHA-256).
2. **XREF Audit**
   - Bash script evaluating the structural XREF data block of each PDF.
   - `flock` locks the database file to prevent multi-process write corruption.
3. **DeepFake Cross-Matching**
   - Correlated the 117k audit records with the verified DeepFake samples.
4. **Digital White Point Mapping**
   - Created a program that replaces absolute digital white `#FFFFFF` with pure red `#FF0000`.
   - Identified transition halos around text and injected bounding edit boxes.
5. **Unified Reporting**
   - Consolidated all text, timeline, and images into a single self-contained HTML file.

---

## 4️⃣ Tool Reliability
| Tool | Version / Source | Reason for Reliability |
|------------|------------------|-----------------------|
| **Bash + flock** | Bash 5.2 (Ubuntu) | Concurrency control utility tested for critical server workloads. |
| **Python 3.12** | Official CPython | Industry standard language for forensic data manipulation. |
| **ImageMagick** | Version 6.9 | Standard tool in digital graphics forensics to extract/manipulate layers. |

---

## 5️⃣ Personal Context & Threats
- **Mother and Student:** Throughout the investigation, I have faced systematic online harassment trying to discredit the forensic audit.
- **10-Year-Old Son:** On the night of **Aug 3, 2026**, while reviewing audit results at home, my child was present when individuals attempted to make threatening phone calls targeting my family. Screen evidence was saved.
- **Constant Attacks:** Detected multiple unauthorized SSH login attempts on my auditing workstation and disinformation campaigns online.

---

## 6️⃣ Request for Urgent Protection
1. **Risk of physical and mental coercion** against the investigator and her child, aiming to suppress the forensic evidence.
2. **Evidence Preservation:** Need to protect the local environment to prevent deletion or manipulation of raw data files (CSVs/HTMLs).
3. **Legal Validity:** The court needs clear, scientifically verified data to justify protective measures.

---
*This document is formatted for formal court submission to legal counsels.*
