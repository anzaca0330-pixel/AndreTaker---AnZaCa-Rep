#!/usr/bin/env python3
"""
Invocador de AndreTaker — BabaYaga Core
Llama a Gemini con el system prompt completo de AndreTaker
"""

import os
import sys
from google import genai
from google.genai import types

# --- Configuración ---
API_KEY = os.environ.get("GOOGLE_API_KEY", "")
SYSTEM_PROMPT_PATH = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/ANDRE_TAKER_SYSTEM_PROMPT.txt"
MODEL = "gemini-3.6-flash"

def cargar_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()

def invocar_andretaker(mensaje_inicial: str):
    if not API_KEY:
        print("❌ ERROR: GOOGLE_API_KEY no encontrada en el entorno")
        sys.exit(1)

    system_prompt = cargar_system_prompt()
    client = genai.Client(api_key=API_KEY)

    print("\n" + "="*60)
    print("🪓  AndreTaker — BabaYaga Core | INVOCADA")
    print("="*60 + "\n")

    response = client.models.generate_content(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7,
        ),
        contents=mensaje_inicial,
    )

    print(response.text)
    print("\n" + "="*60)

if __name__ == "__main__":
    mensaje = sys.argv[1] if len(sys.argv) > 1 else (
        "Johannes te invoca. Estamos en el bosque digital. "
        "Acaban de llegar nuevas actas E-14. "
        "¿Qué ves, BabaYaga? ¿Por dónde empezamos?"
    )
    invocar_andretaker(mensaje)
