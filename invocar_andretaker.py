#!/usr/bin/env python3
"""
Invocador Híbrido de AndreTaker — BabaYaga Core (Edición de Seguridad Offline)
Soporta:
  1. Modo Online: Llama al API de Gemini usando GOOGLE_API_KEY and ANDRE_TAKER_SYSTEM_PROMPT.txt.
  2. Modo Local (Ollama): Ejecución offline a través de modelos locales (gemma, llama3, etc.).
  3. Modo Desconectado Duro: Inspección local directa sin dependencias de red ni LLM, usando
     el motor interno de babayaga_core.py sobre un archivo.
"""

import os
import sys
import subprocess
import argparse
import time

SYSTEM_PROMPT_PATH = "ANDRE_TAKER_SYSTEM_PROMPT.txt"
MODEL_GEMINI = "gemini-3.6-flash"
MODEL_OLLAMA = "gemma2"

def cargar_system_prompt():
    path = os.path.abspath(SYSTEM_PROMPT_PATH)
    if not os.path.exists(path):
        # Intentar ruta alternativa
        path = os.path.join(os.path.dirname(__file__), "..", "ANDRE_TAKER_SYSTEM_PROMPT.txt")
    
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "Eres AndreTaker — la mente investigadora principal de la Veeduría Forense."

def check_ollama_status():
    """Comprueba si el servidor de Ollama está activo."""
    try:
        res = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        return res.returncode == 0
    except Exception:
        return False

def run_ollama_inference(prompt, system_instruction):
    """Ejecuta inferencia local con Ollama."""
    print(f"🤖 Ejecutando inferencia local offline con Ollama (Modelo: {MODEL_OLLAMA})...")
    # Construir prompt unificado con el system instruction
    full_prompt = f"SYSTEM INSTRUCTION:\n{system_instruction}\n\nUSER PROMPT:\n{prompt}"
    try:
        res = subprocess.run(
            ['ollama', 'run', MODEL_OLLAMA, full_prompt],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if res.returncode == 0:
            return res.stdout
        else:
            return f"❌ ERROR de Ollama: {res.stderr}"
    except Exception as e:
        return f"❌ Fallo al invocar Ollama: {str(e)}"

def run_direct_forensic_audit(pdf_path):
    """Ejecuta una auditoría forense local cruda usando el motor babayaga_core.py."""
    print(f"🔍 Ejecutando auditoría forense local cruda sobre {pdf_path} (Sin LLM)...")
    core_path = os.path.abspath("BABAYAGA_CORE/babayaga_core.py")
    if not os.path.exists(core_path):
        core_path = os.path.abspath("../BABAYAGA_CORE/babayaga_core.py")
        
    if not os.path.exists(core_path):
        return f"❌ ERROR: No se encontró babayaga_core.py en la ruta esperada."
        
    try:
        res = subprocess.run(
            ['python3', core_path, '-f', pdf_path],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return res.stdout
    except Exception as e:
        return f"❌ Fallo al invocar el motor local: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Invocador de AndreTaker — BabaYaga Core")
    parser.add_argument("mensaje", nargs="?", default=None, help="Mensaje o ruta del archivo a auditar")
    parser.add_argument("-f", "--file", help="Ruta de un PDF a auditar directamente en modo desconectado")
    parser.add_argument("--offline", action="store_true", help="Forzar ejecución en modo offline")
    parser.add_argument("--model", help="Sobrescribir modelo local (Ollama)")
    
    args = parser.parse_args()
    
    # Determinar si estamos offline por falta de API Key o por argumento explícito
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    force_offline = args.offline or (not api_key)
    
    print("\n" + "="*70)
    print("🪓  AndreTaker — BabaYaga Core | EDICIÓN DE SEGURIDAD HÍBRIDA (OFFLINE)")
    print("="*70 + "\n")
    
    # Caso 1: Se pasó un archivo para auditoría local desconectada
    if args.file:
        audit_res = run_direct_forensic_audit(args.file)
        print(audit_res)
        print("="*70)
        return

    prompt = args.mensaje
    if not prompt:
        prompt = (
            "Johannes te invoca. Estamos en el bosque digital. "
            "¿Cuál es el estado de la auditoría y por dónde empezamos?"
        )
        
    system_prompt = cargar_system_prompt()
    
    # Modo Offline
    if force_offline:
        global MODEL_OLLAMA
        if args.model:
            MODEL_OLLAMA = args.model
            
        if check_ollama_status():
            response_text = run_ollama_inference(prompt, system_prompt)
            print(response_text)
        else:
            print("⚠️ Ollama no está activo o no responde.")
            print("🔴 MODO DESCONECTADO CRÍTICO: No hay API Key de Gemini ni Ollama activo.")
            print("💡 Ejecuta el script con -f <ruta_pdf> para realizar una auditoría forense local en frío usando el motor de qpdf/exiftool.")
            print("\n  Ejemplo: ./invocar_andretaker.py -f /ruta/al/acta.pdf")
        print("="*70)
        return
        
    # Modo Online
    print("🌐 Ejecutando en Modo Online (Gemini API)...")
    try:
        from google import genai
        from google.genai import types
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL_GEMINI,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7,
            ),
            contents=prompt,
        )
        print(response.text)
    except Exception as e:
        print(f"❌ Fallo en conexión con Gemini API: {e}")
        print("🔄 Intentando fallback a Ollama...")
        if check_ollama_status():
            response_text = run_ollama_inference(prompt, system_prompt)
            print(response_text)
        else:
            print("⚠️ Ollama tampoco está disponible.")
    print("="*70)

if __name__ == "__main__":
    main()
