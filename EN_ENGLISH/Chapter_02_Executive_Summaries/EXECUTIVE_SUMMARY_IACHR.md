# IACHR – REQUEST FOR PRECAUTIONARY MEASURES – CASE NO. IACHR-0000113728
## Executive Summary of the E-14 Forensic Evidence Archive

**Investigator:** Andrea Zabala Cárcamo (Independent Citizen Investigator)  
**Date:** August 9, 2026  
**Location:** Canada

---

### 1. Introduction

I, **Andrea Zabala Cárcamo**, acting as an independent citizen investigator, have documented systemic algorithmic and structural manipulation of the E-14 tally sheets in the 2026 presidential elections in Colombia. The evidence was gathered directly from the official portal of the National Civil Registry between June 1 and August 9, 2026.

---

### 2. Main Finding

The forensic analysis of the PDF files revealed:

- **Synthetic Image Injection (Blind Masking):** Pure white canvas overlays (`#FFFFFF` DeviceGray) with luminance mean 65,535 and standard deviation $\sigma = 0$, impossible to obtain through physical optical scanning.
- **Selective QR Code Suppression:** 100% read failure in early voting tally sheets (tables 81-86) and key consulates.
- **Systematic Metadata Purging:** Absence of standard attributes (`Creator`, `Producer`, `CreationDate`).
- **Ghost Objects and Structural Violations:** Identical XREF inconsistency (*`reported 15 objects != highest 13`*) across 100% of all 32 departments.
- **Post-Publication Alterations:** Documented by SHA-256 cryptographic signature shifts between versions downloaded from June 1 to June 4, 2026.

**Technical conclusion:** The files are not the product of a physical scanner, but of a digital assembly process designed to break traceability and citizen verification.

---

### 3. Methodology

The investigation was conducted under the **ISO/IEC 27037** digital chain of custody standard. Open-source tools were used (`qpdf`, `exiftool`, `pdfimages`, `identify`, `zbarimg`, `sha256sum`), generating **over 114,386 SHA-256 cryptographic signatures** certifying file integrity.

---

### 4. Evidence and Coverage

- **Evidence Volume:** 136 GB of raw preserved evidence.
- **Consular Coverage:** 24 countries analyzed (including USA, Spain, Mexico, Canada).
- **Preserved Physical Disks:** `D A T A` (517 GB), `BACKUP` (279 GB), `ANZACA` (79.7 GB).
- **Public GitHub Repository:** [https://github.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep](https://github.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep)
- **Immutable Vault on Internet Archive:** [https://archive.org/details/colombia-e14-forensic-acervo-2026](https://archive.org/details/colombia-e14-forensic-acervo-2026)

---

### 5. Political Consequence

The candidate who benefited from these structural anomalies was declared the winner of the second round and assumed the presidency of the Republic of Colombia.

This is not a political statement, but a **logical inference derived from technical evidence**: the manipulation selectively affected tables and consulates where early voting was relevant, and the alteration pattern is consistent with a targeted operation.

---

### 6. Retaliation and Security Incidents

Following the public disclosure of these findings, I was targeted by:

- **Cyberattacks and Surveillance:** Rootkit infection, BIOS lockout, compromised accounts, and 1,650 location tracking attempts in 5 minutes.
- **Physical Sabotage:** Ambush and vehicle mechanical tampering.
- **Institutional Response:** The FBI referred the case to local police lacking technical capacity (Sheriff Ticket: `C20260617-0024-01`).
- **Diplomatic Protection:** Asylum processed via Mexico and subsequent relocation to Canada.

---

### 7. Requests to the Honorable Commission (IACHR)

In light of the above, I respectfully request the IACHR to:

1. **Grant and consolidate Precautionary Measures** (Case No. **`IACHR-0000113728`**) to protect my life, personal integrity, and freedom.
2. **Order an Independent International Forensic Audit** on all E-14 tally sheets across the Colombian electoral census.
3. **Issue an Official Request to the National Civil Registry** for the submission of the complete digital chain of custody, server logs, and layer correspondence tables.

---

### 8. Enclosed Annexes

- Official Cover Letter of the Evidence Archive
- Master Index of the Forensic Archive
- Timeline of Incidents and Retaliation
- SHA-256 Hash Manifest (`MANIFIESTO_HASHES_DISCO.txt`)
- Official GitHub and Internet Archive Links

---

**Sincerely,**

________________________________  
**Andrea Zabala Cárcamo**  
ID: 43.925.102  
Independent Citizen Investigator  
IACHR Case No.: `IACHR-0000113728`
