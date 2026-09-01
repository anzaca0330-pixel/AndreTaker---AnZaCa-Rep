#!/usr/bin/env python3
"""
===============================================================================
BABAYAGA CORE — AUTOMATED INTERNET ARCHIVE (WAYBACK MACHINE) SAVER
===============================================================================
Autores: AnZaCa (Andrea Zabala Cárcamo) & AndreTaker Cyberdefense Unit
Descripción: Script de preservación que solicita el guardado inmutable en el
Wayback Machine de Internet Archive (archive.org) para todas las URLs del acervo.
===============================================================================
"""

import urllib.request
import urllib.parse
import json
import sys
import time

URLS_TO_ARCHIVE = [
    "https://andretaker.duckdns.org",
    "https://github.com/anzaca0330-pixel/AndreTaker---BaBaYaga-Core_-ForensicTool",
    "https://github.com/anzaca0330-pixel/AndreTaker-BabaYaga-Core-CyberDefense",
    "https://zenodo.org/records/21922376",
    "https://doi.org/10.5281/zenodo.21922375"
]

def save_to_archive_org(url):
    save_url = f"https://web.archive.org/save/{url}"
    print(f"🏛️ Solicitando preservación en Archive.org para: {url}")
    req = urllib.request.Request(
        save_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) BaBaYagaCore/2.1"}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            print(f"✅ Respuesta Archive.org: Código {response.getcode()} — Captura enviada con éxito.")
            return True
    except Exception as e:
        print(f"⚠️ Nota de envío a Archive.org ({url}): {e}")
        return False

def main():
    print("=================================================================")
    print("🏛️ INTERNET ARCHIVE (WAYBACK MACHINE) — AUTOMATED PRESERVATION ENGINE")
    print("=================================================================")
    for target in URLS_TO_ARCHIVE:
        save_to_archive_org(target)
        time.sleep(2)
    print("=================================================================")
    print("✅ Proceso de preservación en Archive.org enviado.")

if __name__ == "__main__":
    main()
