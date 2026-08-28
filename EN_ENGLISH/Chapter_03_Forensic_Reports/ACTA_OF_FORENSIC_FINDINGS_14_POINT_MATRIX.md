# ACTA OF FORENSIC FINDINGS: 14-POINT TECHNICAL MATRIX OF IMMUTABILITY AND PRE-COUNT VS. OFFICIAL SCRUTINY

**Author / Citizen Observer:** Andrea Zabala Cárcamo (Independent Researcher)  
**Origin:** Forensic Findings Report (Rescued from `markdownlive` browser cache post-intrusion)  
**Subject:** Consolidation of 14 structural and immutable anomalies identified in National Registry E-14 forms.

---

## 1. MATRIX OF THE 14 FUNDAMENTAL TECHNICAL FINDINGS

```
+-----------------------------------------------------------------------------------+
| 1. Optical Metrology (#FFFFFF, σ=0) ──> 2. Hybrid Architecture (sRGB/DeviceGray)  |
| 3. SHA-256 Mutation (4 Days Cont.)  ──> 4. XREF Errors (15 vs 13 Objects)           |
+-----------------------------------------------------------------------------------+
```

1. **Optical Pixel Metrology ($\sigma = 0$):**  
   True optical scans contain pixel variance, CMOS micro-noise, and paper texture. Analysis proves the surgical injection of pure white, mathematically sterile digital objects (`DeviceGray`), with zero standard deviation ($\sigma = 0$) and a unified maximum luminance of 65535.
2. **Hybrid PDF Architecture:**  
   19 out of 26 files in the primary sample unnaturally mix optical color scans (sRGB) with injected black-and-white objects (`DeviceGray`).
3. **Post-Publication SHA-256 Hash Mutation:**  
   $100\%$ of the sample presented cryptographic hash modifications across four consecutive days following initial publication on the official web portal, violating the chain of custody.
4. **Ghost Object XREF Declarations:**  
   All 32 analyzed tally sheets contain syntax errors declaring 15 reported internal objects versus only 13 actual existing objects (`reported 15 objects != highest 13`).
5. **Targeted QR Code Suppression:**  
   $0\%$ QR code readability within the cluster of altered tally sheets (files 82-86).
6. **Artificial Statistical Variance:**  
   An impossibly low standard deviation of just $2.5$ votes, aligning with an injected algorithmic rounding formula rather than human voter distribution.
7. **Scanner Hardware Incompatibility:**  
   Divergent page dimensions and destroyed creation metadata (`ExifTool`), ruling out the use of institutional-grade, certified Kodak Alaris scanners.
8. **Single-Sided Front Layer Intervention:**  
   Being single-sided forms (front side only without reverse), inserting the white mask acts to suppress the original optical capture of the vote counts.
9. **Chronometric Timestamp Mismatches:**  
   Inconsistency between file creation date and web publication date in the Registraduría database.
10. **PDF Container Signature Rupture:**  
    Alteration of the `/Contents` stream restructuring the source vector code.
11. **Absence of Thermal Granulometry:**  
    Intervened areas exhibit no optical JPEG compression degradation characteristic of physical paper scanning.
12. **Injection of Rounding Parameters:**  
    Presence of fixed numerical constants forcing proportional distribution.
13. **Syntactic Cloning between Delegates and Claveros:**  
    Identical XREF syntactic signature between the web version and the physical custody version.
14. **Read-Only Methodology:**  
    Verification via file descriptors without write permissions using `pdfimages`, `ImageMagick`, `qpdf`, and `sha256sum`.

---

## 2. TACTICAL DISTINCTION: PRE-COUNT VS. OFFICIAL SCRUTINY

The report highlights a crucial legal and technical distinction to understand the mechanism of fraud:

### A. The Pre-Count (Informational Media Narrative)
* **Mechanism:** Rapid transmission by voice/phone from polling tables to call centers.
* **Nature:** **Exclusively informational process with zero legal value**. Not extracted from the PDF code.
* **Tactical Function:** Used to install the media narrative of a "narrow victory margin" (under 1%).

### B. Official Scrutiny (Binding Legal Proof)
* **Mechanism:** Physical processing of E-14 forms before judges and scrutiny commissions.
* **Nature:** The **only count with binding legal validity**.
* **Software Injection:** By uploading PDF files with injected white masks (`DeviceGray`) and declared illegibility to web portals, the system destroyed the legal tool that would have allowed lawyers to challenge the numbers phoned in during pre-counting.

---

## 3. CONCLUSION
The strategy combined rapid phone transmission to establish the informational outcome with digital injection in PDFs to render judicial verification useless during official scrutiny.
