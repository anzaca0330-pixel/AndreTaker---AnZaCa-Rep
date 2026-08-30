#!/usr/bin/env python3
"""
Invocador Híbrido de AndreTaker — BabaYaga Core (Edición de Seguridad Offline)
Soporta:
  1. Modo Online: Llama al API de Gemini usando GOOGLE_API_KEY y ANDRE_TAKER_SYSTEM_PROMPT.txt.
  2. Modo Local (Ollama): Inferencia local con modelos de lenguaje offline.
  3. Modo Desconectado Duro: Auditoría estructural de actas usando el motor local babayaga_core.py.
  4. Protocolo Anti-Palantir (-ap / --anti-palantir): Mitigación activa contra sistemas de
     vigilancia y minería de datos mediante eliminación de metadatos, aleatorización de hashes 
     (SHA-256 padding) y spoofing estructural.
"""

import os
import sys
import subprocess
import argparse
import random
import string
import hashlib

SYSTEM_PROMPT_PATH = "ANDRE_TAKER_SYSTEM_PROMPT.txt"
MODEL_GEMINI = "gemini-3.6-flash"
MODEL_OLLAMA = "gemma2"

def cargar_system_prompt():
    path = os.path.abspath(SYSTEM_PROMPT_PATH)
    if not os.path.exists(path):
        path = os.path.join(os.path.dirname(__file__), "..", "ANDRE_TAKER_SYSTEM_PROMPT.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "Eres AndreTaker — la mente investigadora principal de la Veeduría Forense."

def check_ollama_status():
    try:
        res = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        return res.returncode == 0
    except Exception:
        return False

def run_ollama_inference(prompt, system_instruction):
    print(f"🤖 Ejecutando inferencia local offline con Ollama (Modelo: {MODEL_OLLAMA})...")
    full_prompt = f"SYSTEM INSTRUCTION:\n{system_instruction}\n\nUSER PROMPT:\n{prompt}"
    try:
        res = subprocess.run(
            ['ollama', 'run', MODEL_OLLAMA, full_prompt],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return res.stdout if res.returncode == 0 else f"❌ ERROR de Ollama: {res.stderr}"
    except Exception as e:
        return f"❌ Fallo al invocar Ollama: {str(e)}"

def run_direct_forensic_audit(pdf_path):
    print(f"🔍 Ejecutando auditoría forense local cruda sobre {pdf_path} (Sin LLM)...")
    core_path = os.path.abspath("BABAYAGA_CORE/babayaga_core.py")
    if not os.path.exists(core_path):
        core_path = os.path.abspath("../BABAYAGA_CORE/babayaga_core.py")
    if not os.path.exists(core_path):
        return f"❌ ERROR: No se encontró babayaga_core.py."
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

# =========================================================
# PROTOCOLOS ANTI-PALANTIR (Mitigación de Minería de Datos)
# =========================================================

def calcular_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def ejecutar_protocolo_anti_palantir(target_path):
    """
    Ejecuta el protocolo de protección contra ingesta y correlación de Palantir:
    1. Limpieza absoluta de metadatos exif/XMP (evita rastreo de dispositivo/autor).
    2. Spoofing de fechas y autores con valores aleatorios (rompe correlación de perfiles).
    3. Padding aleatorio al final del archivo (cambia el SHA-256 para evitar rastreo por hash).
    """
    if not os.path.exists(target_path):
        print(f"❌ ERROR: Ruta no encontrada: {target_path}")
        return

    # Si es un directorio, procesar recursivamente
    if os.path.isdir(target_path):
        print(f"📁 Iniciando protocolo anti-Palantir en lote para el directorio: {target_path}")
        for root, dirs, files in os.walk(target_path):
            for file in files:
                if file.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.txt', '.csv')):
                    ejecutar_protocolo_anti_palantir(os.path.join(root, file))
        return

    print(f"\n🛡️ Protegiendo archivo: {os.path.basename(target_path)}")
    hash_previo = calcular_sha256(target_path)
    print(f"  [Original HASH]  {hash_previo}")

    # 1. Stripping y Sanitización de Metadatos
    try:
        # Remover todos los metadatos conocidos
        subprocess.run(['exiftool', '-all=', '-overwrite_original', target_path], capture_output=True)
        print("  [OK] Limpieza y sanitización de metadatos (Exif/XMP) completada.")
    except Exception as e:
        print(f"  [!] Fallo en limpieza de metadatos (¿exiftool instalado?): {e}")

    # 2. Metadatos Spoofing (Datos sintéticos falsos para confundir analítica de Palantir)
    try:
        autores_falsos = ["Veeduría Ciudadana", "Anonymous Veedor", "System Operator", "User_Node_12", "Forensic Analyst"]
        autor_fake = random.choice(autores_falsos)
        fecha_fake = f"2026:08:{random.randint(10,28)} {random.randint(10,23)}:{random.randint(10,59)}:{random.randint(10,59)}"
        
        subprocess.run([
            'exiftool',
            f'-Author={autor_fake}',
            f'-CreateDate={fecha_fake}',
            f'-ModifyDate={fecha_fake}',
            '-overwrite_original',
            target_path
        ], capture_output=True)
        print(f"  [OK] Metadatos ofuscados (Autor: {autor_fake} | Fecha: {fecha_fake}).")
    except Exception as e:
        pass

    # 3. Hash Randomization (Evita link-analysis por huella digital SHA-256)
    try:
        rand_padding = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        if target_path.endswith('.pdf'):
            # Padding seguro para PDF como comentario al final del archivo
            with open(target_path, 'ab') as f:
                f.write(f"\n% AP_PAD_{rand_padding}\n".encode('utf-8'))
        else:
            # Padding genérico para binarios/imágenes al final del flujo
            with open(target_path, 'ab') as f:
                f.write(f"\n# AP_PAD_{rand_padding}\n".encode('utf-8'))
        
        hash_nuevo = calcular_sha256(target_path)
        print(f"  [OK] Mutación criptográfica completada.")
        print(f"  [Mutated HASH]   {hash_nuevo}")
    except Exception as e:
        print(f"  [!] Fallo en mutación de hash: {e}")

def main():
    parser = argparse.ArgumentParser(description="Invocador de AndreTaker — BabaYaga Core")
    parser.add_argument("mensaje", nargs="?", default=None, help="Mensaje o ruta del archivo")
    parser.add_argument("-f", "--file", help="Ruta de un PDF a auditar directamente en modo desconectado")
    parser.add_argument("--offline", action="store_true", help="Forzar ejecución en modo offline")
    parser.add_argument("--model", help="Sobrescribir modelo local (Ollama)")
    parser.add_argument("-ap", "--anti-palantir", help="Aplicar protocolo anti-Palantir (archivo o carpeta)")
    
    args = parser.parse_args()
    
    # Ejecutar protocolo Anti-Palantir si se solicita
    if args.anti_palantir:
        print("\n🛡️  ACTIVANDO PROTOCOLO ANTI-PALANTIR (Desordenamiento de Entidades y Correlación)")
        ejecutar_protocolo_anti_palantir(args.anti_palantir)
        print("\n🛡️  Protocolo ejecutado. Los archivos seleccionados ahora están ofuscados e inmunes a correlación por firmas estáticas.")
        return

    # Caso 1: Se pasó un archivo para auditoría local desconectada
    if args.file:
        audit_res = run_direct_forensic_audit(args.file)
        print(audit_res)
        return

    prompt = args.mensaje
    if not prompt:
        prompt = (
            "Johannes te invoca. Estamos en el bosque digital. "
            "¿Cuál es el estado de la auditoría y por dónde empezamos?"
        )
        
    system_prompt = cargar_system_prompt()
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    force_offline = args.offline or (not api_key)
    
    print("\n" + "="*70)
    print("🪓  AndreTaker — BabaYaga Core | EDICIÓN DE SEGURIDAD HÍBRIDA (OFFLINE)")
    print("="*70 + "\n")
    
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
            print("💡 Ejecuta el script con -f <ruta_pdf> para realizar una auditoría forense local.")
            print("🛡️ O usa -ap <archivo/directorio> para activar los protocolos anti-Palantir.")
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
