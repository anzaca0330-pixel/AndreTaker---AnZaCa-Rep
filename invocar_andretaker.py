#!/usr/bin/env python3
"""
Invocador Híbrido de AndreTaker — BabaYaga Core (Edición de Seguridad Offline)
Soporta:
  1. Modo Online: Llama al API de Gemini usando GOOGLE_API_KEY y ANDRE_TAKER_SYSTEM_PROMPT.txt.
  2. Modo Local (Ollama): Inferencia local con modelos de lenguaje offline (Modelo: AndreTaker).
  3. Modo Desconectado Duro: Auditoría estructural de actas usando el motor local babayaga_core.py.
  4. Protocolo Anti-Palantir (-ap / --anti-palantir): Mitigación activa contra sistemas de
     vigilancia y minería de datos mediante eliminación de metadatos, aleatorización de hashes 
     (SHA-256 padding) y spoofing estructural.
"""

import os
import sys
import subprocess
import argparse

# Asegurar importabilidad de los sub-paquetes de babayaga
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "BABAYAGA_CORE")))

try:
    from babayaga.core.intelligence.mitigation import AntiPalantir
    from babayaga.core.forensics.xref import XrefAnalyzer
except ImportError:
    # Fallback local temporal
    class AntiPalantir:
        @staticmethod
        def calcular_sha256(filepath):
            import hashlib
            sha = hashlib.sha256()
            with open(filepath, 'rb') as f:
                while chunk := f.read(65536):
                    sha.update(chunk)
            return sha.hexdigest()
        @classmethod
        def ejecutar_mitigacion(cls, filepath):
            return {"status": "error", "message": "No se pudo cargar el núcleo de inteligencia."}

SYSTEM_PROMPT_PATH = "ANDRE_TAKER_SYSTEM_PROMPT.txt"
MODEL_GEMINI = "gemini-3.6-flash"
MODEL_OLLAMA = "AndreTaker"  # Apunta al modelo compilado localmente

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

def setup_local_ollama_model():
    """
    Genera dinámicamente el Modelfile e invoca a Ollama para crear el modelo
    pericial local 'AndreTaker' de forma 100% automatizada.
    """
    print("🧠 INICIANDO AUTOCOMPILACIÓN DE MODELO LOCAL (OLLAMA)...")
    system_prompt = cargar_system_prompt()
    
    # Escribir Modelfile
    modelfile_path = "Modelfile"
    modelfile_content = f"""FROM gemma2
PARAMETER temperature 0.3
SYSTEM \"\"\"{system_prompt}\"\"\"
"""
    try:
        with open(modelfile_path, "w", encoding="utf-8") as f:
            f.write(modelfile_content)
        print("  [OK] Modelfile generado exitosamente.")
        
        # Ejecutar ollama create
        print("  [Ollama] Compilando modelo 'AndreTaker'... (Esto puede demorar unos segundos)")
        res = subprocess.run(
            ['ollama', 'create', 'AndreTaker', '-f', modelfile_path],
            capture_output=True,
            text=True
        )
        
        # Limpiar Modelfile temporal
        if os.path.exists(modelfile_path):
            os.remove(modelfile_path)
            
        if res.returncode == 0:
            print("🎉 ¡COMPILACIÓN EXITOSA! El modelo 'AndreTaker' ya está activo y listo offline.")
        else:
            print(f"❌ Error al crear el modelo: {res.stderr}")
            print("💡 Asegúrate de tener instalado Ollama y de haber descargado la base con: ollama pull gemma2")
    except Exception as e:
        print(f"❌ Error inesperado en autocompilación: {str(e)}")

def run_ollama_inference(prompt, system_instruction):
    print(f"🤖 Invocando asistente pericial offline (Ollama: {MODEL_OLLAMA})...")
    # Si usamos el modelo compilado, ya tiene el SYSTEM prompt inyectado!
    try:
        res = subprocess.run(
            ['ollama', 'run', MODEL_OLLAMA, prompt],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        # Fallback si AndreTaker no está compilado
        if "not found" in res.stderr.lower() or res.returncode != 0:
            print("⚠️ Modelo 'AndreTaker' no detectado. Usando fallback básico 'gemma2'...")
            fallback_prompt = f"SYSTEM:\n{system_instruction}\n\nUSER:\n{prompt}"
            res = subprocess.run(
                ['ollama', 'run', 'gemma2', fallback_prompt],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
        return res.stdout if res.returncode == 0 else f"❌ ERROR de Ollama: {res.stderr}"
    except Exception as e:
        return f"❌ Fallo al invocar Ollama: {str(e)}"

def run_direct_forensic_audit(pdf_path):
    print(f"🔍 Ejecutando auditoría forense local cruda sobre {pdf_path} (Sin LLM)...")
    dir_path = os.path.dirname(os.path.abspath(__file__))
    core_path = os.path.join(dir_path, "BABAYAGA_CORE", "babayaga_core.py")
    if not os.path.exists(core_path):
        return f"❌ ERROR: No se encontró babayaga_core.py."
    try:
        res = subprocess.run(
            ['python3', core_path, 'scan', '--ruta', pdf_path, '--caso', 'Auditoria Invocador'],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if res.returncode == 0:
            status_res = subprocess.run(
                ['python3', core_path, 'status', '--caso', 'Auditoria Invocador'],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            return res.stdout + "\n" + status_res.stdout
        return res.stdout if res.stdout else res.stderr
    except Exception as e:
        return f"❌ Fallo al invocar el motor local: {str(e)}"

# =========================================================
# PROTOCOLOS ANTI-PALANTIR (Mitigación de Minería de Datos)
# =========================================================

def ejecutar_protocolo_anti_palantir(target_path):
    """
    Ejecuta el protocolo de protección contra ingesta y correlación de Palantir
    llamando directamente a la clase modular del núcleo de inteligencia.
    """
    if not os.path.exists(target_path):
        print(f"❌ ERROR: Ruta no encontrada: {target_path}")
        return

    if os.path.isdir(target_path):
        print(f"📁 Iniciando protocolo anti-Palantir en lote para el directorio: {target_path}")
        for root, dirs, files in os.walk(target_path):
            for file in files:
                if file.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.txt', '.csv')):
                    ejecutar_protocolo_anti_palantir(os.path.join(root, file))
        return

    print(f"\n🛡️ Protegiendo archivo: {os.path.basename(target_path)}")
    res = AntiPalantir.ejecutar_mitigacion(target_path)
    
    if res.get("status") == "success":
        print(f"  [Original HASH]  {res.get('original_hash')}")
        print("  [OK] Limpieza y sanitización de metadatos (Exif/XMP) completada.")
        print(f"  [OK] Metadatos ofuscados de forma segura.")
        print("  [OK] Mutación criptográfica completada.")
        print(f"  [Mutated HASH]   {res.get('mutated_hash')}")
    else:
        print(f"  [!] Fallo en mitigación: {res.get('message')}")

def main():
    parser = argparse.ArgumentParser(description="Invocador de AndreTaker — BabaYaga Core")
    parser.add_argument("mensaje", nargs="?", default=None, help="Mensaje o ruta del archivo")
    parser.add_argument("-f", "--file", help="Ruta de un PDF a auditar directamente en modo desconectado")
    parser.add_argument("--offline", action="store_true", help="Forzar ejecución en modo offline")
    parser.add_argument("--model", help="Sobrescribir modelo local (Ollama)")
    parser.add_argument("-ap", "--anti-palantir", help="Aplicar protocolo anti-Palantir (archivo o carpeta)")
    parser.add_argument("--setup-ollama", action="store_true", help="Generar Modelfile y compilar modelo AndreTaker")
    
    args = parser.parse_args()
    
    # Autocompilación de modelo local
    if args.setup_ollama:
        setup_local_ollama_model()
        return

    # Ejecutar protocolo Anti-Palantir si se solicita
    if args.anti_palantir:
        print("\n🛡️  ACTIVANDO PROTOCOLO ANTI-PALANTIR (Desordenamiento de Entidades y Correlación)")
        ejecutar_protocolo_anti_palantir(args.anti_palantir)
        print("\n🛡️  Protocolo ejecutado. Los archivos seleccionados ahora están ofuscados e inmunes a correlación por firmas estáticas.")
        return

    # Caso 1: Se pasó un archivo para auditoría local desconectada o se toma el PDF de muestra por defecto
    if args.file or args.offline:
        target_pdf = args.file if args.file else os.path.join(os.path.dirname(__file__), "00_MUESTRAS_EVIDENCIA", "2DA_VUELTA", "E14_PRE_60_010_000_00_00_001_3085_Mesa_1.pdf")
        if os.path.exists(target_pdf):
            audit_res = run_direct_forensic_audit(target_pdf)
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
