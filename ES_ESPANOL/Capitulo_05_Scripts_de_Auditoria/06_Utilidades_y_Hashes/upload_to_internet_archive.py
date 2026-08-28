#!/usr/bin/env python3
"""
Script de Carga Automática e Inmutable a Internet Archive (Archive.org)
Soporta S3 API nativa sin requerir pip ni paquetes externos.
"""

import os
import sys
import urllib.request

def upload_file_to_ia(file_path, item_identifier, access_key, secret_key, remote_filename=None):
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo '{file_path}' no existe.")
        return False

    if not remote_filename:
        remote_filename = os.path.basename(file_path)

    url = f"https://s3.us.archive.org/{item_identifier}/{remote_filename}"
    file_size = os.path.getsize(file_path)
    print(f"🚀 Subiendo '{remote_filename}' ({file_size / (1024*1024):.2f} MB) a Internet Archive...")

    headers = {
        "Authorization": f"LOW {access_key}:{secret_key}",
        "x-archive-auto-make-bucket": "1",
        "x-archive-meta-title": "Colombia 2026 E-14 Raw Forensic Database & Legal Evidence",
        "x-archive-meta-mediatype": "data",
        "x-archive-meta-language": "spa;eng",
        "x-archive-meta-licenseurl": "http://creativecommons.org/publicdomain/zero/1.0/",
        "Content-Length": str(file_size)
    }

    try:
        with open(file_path, "rb") as f:
            req = urllib.request.Request(url, data=f, headers=headers, method="PUT")
            with urllib.request.urlopen(req) as resp:
                if resp.status in (200, 201):
                    print(f"✅ ¡Subida exitosa! Disponible en: https://archive.org/details/{item_identifier}/{remote_filename}")
                    return True
                else:
                    print(f"⚠️ Código de respuesta: {resp.status}")
                    return False
    except Exception as e:
        print(f"❌ Error durante la carga: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python3 upload_to_internet_archive.py <archivo_local> <ia_access_key> <ia_secret_key> [item_identifier]")
        sys.exit(1)
    
    local_file = sys.argv[1]
    acc_key = sys.argv[2]
    sec_key = sys.argv[3]
    item_id = sys.argv[4] if len(sys.argv) > 4 else "colombia-e14-forensic-acervo-2026"
    
    upload_file_to_ia(local_file, item_id, acc_key, sec_key)
