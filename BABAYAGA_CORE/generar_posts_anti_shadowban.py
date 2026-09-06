#!/usr/bin/env python3
"""
🛡️ GENERADOR DE POSTS Y TEXTO INMUNIZADO (ANTI-SHADOWBAN) — PARTE 1
Aplica inyección de caracteres de ancho cero (\u200B) a todas las palabras clave sensibles
del expediente de fraude electoral en Colombia 2026 (Parte 1).
"""

import re

def inmunizar_texto(texto: str) -> str:
    zw = "\u200B"
    
    palabras_clave = [
        "fraude", "electoral", "colombia", "registraduria", "fiscalia", 
        "cne", "blindmasking", "blind masking", "e14", "e-14", "corrupcion",
        "andretaker", "anzaca", "babayaga", "github.com", "denuncia", "actas",
        "alteracion", "nulidad", "parte 1"
    ]
    
    texto_blindado = texto
    for palabra in palabras_clave:
        def replace_with_zw(match):
            word = match.group(0)
            if len(word) <= 2:
                return word
            mid = len(word) // 2
            return word[:mid] + zw + word[mid:]
            
        pattern = re.compile(re.escape(palabra), re.IGNORECASE)
        texto_blindado = pattern.sub(replace_with_zw, texto_blindado)
        
    return texto_blindado

def main():
    post_principal = """🇨🇴 ACERVO PROBATORIO OFICIAL: FRAUDE ELECTORAL COLOMBIA 2026 — [PARTE 1]

Parte 1: Descubrimiento científico de la investigadora Andrea Zabala Cárcamo (AnZaCa):
Demostración técnica del #BlindMasking (inyección de capas 1bpc #FFFFFF en streams /FlateDecode de actas E-14), QR sintéticos con divergencia textual y primeras denuncias radicadas (1 al 10 de Junio de 2026).

📦 Descarga directa de Denuncias Penales, Radicados Activos (Fiscalía, CNE, URIEL) y Dictamen Pericial:
👉 https://www.andretaker.org/fraude_electoral_colombia.html

#DataScience #DigitalForensics #OpenSource #Colombia #Democracia #AnZaCa #AndreTaker #Parte1"""

    post_inmune = inmunizar_texto(post_principal)
    
    with open("/home/andrea-zabala-c/AndreTaker---BaBaYaga-Core_-ForensicTool/03_DOCUMENTACION/POST_REDES_ANTI_SHADOWBAN.txt", "w", encoding="utf-8") as f:
        f.write(post_inmune)

if __name__ == "__main__":
    main()
