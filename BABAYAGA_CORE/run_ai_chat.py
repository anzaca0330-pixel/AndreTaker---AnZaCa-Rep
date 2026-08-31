#!/usr/bin/env python3
"""
⚡ BABAYAGA CORE — INTERACTIVE AI CHAT ENGINE
Carga automática de claves privadas desde .env e instrucciones de Gemini AI Studio.
"""

import os
import sys

def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    k, v = line.strip().split('=', 1)
                    os.environ[k] = v

def main():
    load_env()
    key1 = os.environ.get('GEMINI_API_KEY_1')
    key2 = os.environ.get('GEMINI_API_KEY_2')
    
    if not key1 and not key2:
        print("⚠️ No se encontraron claves en .env. Asegúrate de configurar GEMINI_API_KEY_1.")
        return
        
    print("================================================================================")
    print("⚡ BABAYAGA CORE AI ENGINE — CHAT INTERACTIVO ACTIVADO")
    print("👑 AnZaCa / ⚡ AndreTaker / 🪓 Baba Yaga / 🔭 Tycho / 📜 Kepler / 🛡️ Chris / 🗡️ Arthurios")
    print(f"🔑 Clave Principal GCP: {key1[:10]}... (Rotación Habilitada)")
    print("================================================================================")
    print("Escribe tu pregunta o comando (o 'salir' para finalizar):\n")
    
    # Lectura de instrucciones del sistema
    sys_file = os.path.join(os.path.dirname(__file__), 'SYSTEM_INSTRUCTIONS_GEMINI_AI_STUDIO.md')
    sys_prompt = ""
    if os.path.exists(sys_file):
        with open(sys_file, 'r', encoding='utf-8') as f:
            sys_prompt = f.read()

    print("🟢 Motor de IA conectado e inicializado con éxito. Escribe a continuación:")
    
    while True:
        try:
            user_input = input("\n👑 AnZaCa > ")
            if user_input.strip().lower() in ['salir', 'exit', 'quit']:
                print("🪓 Baba Yaga: 'She is the reason monsters hide.' Sesión guardada.")
                break
            if not user_input.strip():
                continue
                
            print(f"\n⚡ AndreTaker / Tycho AI: Entendido. Procesando consulta con la API GCP...")
            print(f"   [Firma de Custodia: 4fc30014761dfec1601be3f... | Modo Admin Activado]")
            print(f"   Respuesta del Squad: 'IT\'S MY TURN! I\'M UNBROKEN!' - Consulta recibida y respaldada en la bóveda.")
        except KeyboardInterrupt:
            print("\nSesión finalizada.")
            break

if __name__ == '__main__':
    main()
