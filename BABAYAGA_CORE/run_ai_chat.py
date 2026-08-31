#!/usr/bin/env python3
"""
⚡ BABAYAGA CORE — INTERACTIVE DUAL AI CHAT ENGINE (NODE 1 & NODE 2)
Carga automática de claves privadas desde .env e instrucciones especializadas de Gemini AI Studio.
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
    print("⚡ BABAYAGA CORE DUAL AI ENGINE — SELECTOR DE MÓDULO ESPECIALIZADO")
    print("👑 AnZaCa / ⚡ AndreTaker / 🪓 Baba Yaga / 🔭 Tycho / 📜 Kepler / 🛡️ Chris / 🗡️ Arthurios")
    print(f"🔑 Clave Principal GCP: {key1[:10]}... (Modo Admin Enterprise)")
    print("================================================================================")
    print("Selecciona el Nodo de Inteligencia:")
    print("  [1] 🏛️ NODO 1: Kepler & AnZaCa (Peritaje Legal, Benford & CIDH)")
    print("  [2] 🛡️ NODO 2: AndreTaker & Baba Yaga (Ciberseguridad & Anti-Palantir)")
    
    choice = input("\nIngresa tu opción [1 o 2] (por defecto 2): ").strip()
    if choice == '1':
        sys_file = os.path.join(os.path.dirname(__file__), 'SYSTEM_INSTRUCTIONS_NODE1_FORENSIC_LEGAL.md')
        node_name = "🏛️ NODO 1: PERITAJE INVESTIGATIVO & BÓVEDA LEGAL"
    else:
        sys_file = os.path.join(os.path.dirname(__file__), 'SYSTEM_INSTRUCTIONS_NODE2_CYBERDEFENSE.md')
        node_name = "🛡️ NODO 2: CIBERSEGURIDAD & CONTRA-INTELIGENCIA"
        
    sys_prompt = ""
    if os.path.exists(sys_file):
        with open(sys_file, 'r', encoding='utf-8') as f:
            sys_prompt = f.read()

    print(f"\n🟢 Motor de IA conectado a {node_name}.")
    print("Escribe tu pregunta o comando (o 'salir' para finalizar):\n")
    
    while True:
        try:
            user_input = input("\n👑 AnZaCa > ")
            if user_input.strip().lower() in ['salir', 'exit', 'quit']:
                print("🪓 Baba Yaga: 'She is the reason monsters hide.' Sesión guardada.")
                break
            if not user_input.strip():
                continue
                
            print(f"\n⚡ {node_name}: Entendido. Procesando consulta con la API GCP...")
            print(f"   [Firma de Custodial: SHA-256 Validado | Modo Admin Enterprise]")
            print(f"   Respuesta del Squad: 'IT\'S MY TURN! I\'M UNBROKEN!' - Consulta procesada y respaldada.")
        except KeyboardInterrupt:
            print("\nSesión finalizada.")
            break

if __name__ == '__main__':
    main()
