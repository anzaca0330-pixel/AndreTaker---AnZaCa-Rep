#!/usr/bin/env python3
"""
🎮 GUARDIANES DIGITALES: JUEGO TÁCTICO DE CIBERDEFENSA (STANDALONE)
Protagonizado por Arthurios (11 años), Chris Báez, Tobías el perro, Tycho y Baba Yaga.
"""

import os
import sys
import webview if 'webview' in sys.modules else None
import webbrowser

def launch_game():
    print("================================================================================")
    print("🎮 GUARDIANES DIGITALES: JUEGO TÁCTICO DE CIBERDEFENSA (ANDRETAKER & ARTHURIOS)")
    print("================================================================================")
    print("🟢 Cargando interfaz táctica del juego...")
    
    html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.html')
    url = f"file://{os.path.abspath(html_path)}#tab-cyber-game"
    
    print(f"🚀 Abriendo juego táctico en: {url}")
    webbrowser.open(url)
    print("\n✅ ¡Juego cargado y listo para defender!")

if __name__ == '__main__':
    launch_game()
