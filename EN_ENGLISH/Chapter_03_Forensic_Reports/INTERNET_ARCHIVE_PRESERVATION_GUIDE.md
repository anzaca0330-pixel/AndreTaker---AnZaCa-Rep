# IMMUTABLE PRESERVATION GUIDE: INTERNET ARCHIVE (ARCHIVE.ORG) AND ZENODO
## Protocol for Ingesting the Heavy Raw Database (100 GB - 117,993 PDFs)

**Objective:** Guarantee the unalterable, decentralized, and immutable preservation of the complete 100 GB E-14 PDF database under open science and international human rights standards.

---

## 1. WHY INTERNET ARCHIVE (ARCHIVE.ORG)?
1. **Censorship Immunity:** Once committed to the Internet Archive, files are permanently frozen. No government, CDN, or administrator can alter or delete the evidence.
2. **Unlimited and Free Capacity:** Supports uploading the full 100 GB dataset at zero cost.
3. **Universal Public Access:** Generates permanent URLs (`https://archive.org/details/...`) accessible to courts (IACHR), expert auditors, and global citizens.

---

## 2. SIMPLE STEPS TO UPLOAD YOUR FOLDER (NO EXPERT SKILLS REQUIRED)

### Option A: Web Browser Upload (Drag and Drop)
1. Go to **[https://archive.org](https://archive.org)** and log into your account.
2. Click the **Upload** icon in the upper right corner.
3. Drag the compressed `.zip` folders from your external hard drive (`claveros_pdf.zip` or departmental folders).
4. **Recommended Metadata:**
   * **Title:** `Colombia 2026 Presidential Elections - E-14 Raw Forensic Database (117,993 PDFs)`
   * **Description:** `Complete raw PDF database of E-14 voting tally sheets for the 2026 Presidential Elections in Colombia. Collected for forensic audit and international Human Rights documentation (IACHR - 0000113728).`
   * **Subject Tags:** `colombia-elections-2026`, `e14-forensic-audit`, `electoral-integrity`, `iaea-cidh`
   * **License:** `Public Domain / Creative Commons CC0`
5. Click **Upload and Create Item**.

---

### Option B: Automated Terminal Upload (Command Line)
If you prefer an automated background upload from your computer:

1. Install the official Internet Archive tool:
   ```bash
   pip install internetarchive
   ```
2. Configure your credentials:
   ```bash
   ia configure
   ```
3. Run the direct upload from your external drive:
   ```bash
   ia upload e14-forensic-database-2026 "/media/andrea-zabala-c/D A T A1/segundaVuelta/claveros_pdf" --title="Colombia 2026 E14 Raw Forensic Database" --mediatype="data"
   ```

---

## 3. ACADEMIC DOI ASSIGNMENT ON ZENODO (OPTIONAL)
To obtain an academic **DOI (Digital Object Identifier)** backed by **CERN (European Organization for Nuclear Research)**:

1. Go to **[https://zenodo.org](https://zenodo.org)**.
2. Create a new **Upload / Dataset**.
3. Upload `firmas_criptograficas_sha256.txt` and the preconteo CSVs.
4. Zenodo will issue a unique **DOI** (e.g., `10.5281/zenodo.1234567`) for legal and scientific citations.
