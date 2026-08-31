#!/usr/bin/env python3
"""
💻 ANDRETAKER — BABAYAGA CORE NATIVE DESKTOP APPLICATION LAUNCHER
Abre la suite autónoma como una ventana nativa de escritorio independiente.
"""

import os
import sys
import subprocess

def launch_native_app():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'index.html'))
    target_url = f"file://{html_path}"
    
    print("================================================================================")
    print("💻 LANZANDO APLICACIÓN DE ESCRITORIO NATIVA — ANDRETAKER BABAYAGA CORE")
    print("================================================================================")
    print(f"🚀 Iniciando ventana independiente en: {target_url}")
    
    # Intentar ejecutar con Brave / Chrome / Chromium en modo App standalone (--app=...)
    browsers = ['/snap/bin/brave', 'brave-browser', 'google-chrome-stable', 'google-chrome', 'chromium-browser', 'chromium', 'firefox']
    launched = False
    
    for b in browsers:
        try:
            cmd = [b, f"--app={target_url}", f"--user-data-dir={os.path.expanduser('~/.babayaga_pwa_profile')}"]
            subprocess.Popen(cmd)
            print(f"✅ Aplicación nativa iniciada exitosamente con: {b}")
            launched = True
            break
        except FileNotFoundError:
            continue
            
    if not launched:
        import webbrowser
        webbrowser.open(target_url)
        print("✅ Apertura completada en navegador por defecto.")

if __name__ == '__main__':
    launch_native_app()
