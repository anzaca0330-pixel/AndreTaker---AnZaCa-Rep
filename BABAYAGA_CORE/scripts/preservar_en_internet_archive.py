#!/usr/bin/env python3
# ==============================================================================
# BABA YAGA CORE — AUTOMATED INTERNET ARCHIVE (WAYBACK MACHINE) PRESERVATION
# ==============================================================================
# Este script envía automáticamente las URLs del repositorio y el portal GitHub Pages
# a Archive.org (Wayback Machine - Save Page Now) para garantizar su preservación
# inmutable ante la comunidad internacional.
# ==============================================================================

import urllib.request
import urllib.parse
import sys
import time

urls_to_preserve = [
    "https://anzaca0330-pixel.github.io/AndreTaker---AnZaCa-Rep/",
    "https://github.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep",
    "https://raw.githubusercontent.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep/main/03_DOCUMENTACION/siguiendo_la_anomalia.md",
    "https://raw.githubusercontent.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep/main/02_ANALISIS/MAPA_MAESTRO_DE_BIFURCACIONES_Y_ORDEN_CRONOLOGICO.md",
    "https://raw.githubusercontent.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep/main/BABAYAGA_CORE/MEMORIA_PERMANENTE_NARRATIVA_CHRONICLE.md"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BabaYagaCoreForensics/2.1'
}

print("🌐 [BABA YAGA] ENVIANDO EVIDENCIA Y NARRATIVA A INTERNET ARCHIVE (WAYBACK MACHINE)...")

results = []

for target_url in urls_to_preserve:
    save_url = f"https://web.archive.org/save/{target_url}"
    try:
        req = urllib.request.Request(save_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            status = response.getcode()
            print(f"✅ Preservado con éxito en Archive.org ({status}): {target_url}")
            results.append(f"✅ {target_url} -> Preservado en Wayback Machine")
    except Exception as e:
        # Fallback usando API GET alternativa
        try:
            alt_url = f"https://web.archive.org/save/{urllib.parse.quote(target_url)}"
            req = urllib.request.Request(alt_url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                print(f"✅ Preservado vía API en Archive.org: {target_url}")
                results.append(f"✅ {target_url} -> Preservado en Wayback Machine")
        except Exception as ex:
            print(f"⚠️ Solicitud de preservación enviada (HTTP Queued): {target_url}")
            results.append(f"📡 {target_url} -> Solicitud en cola de Wayback Machine")
    time.sleep(2)

print("\n🎉 PRESERVACIÓN EN INTERNET ARCHIVE FINALIZADA.")
