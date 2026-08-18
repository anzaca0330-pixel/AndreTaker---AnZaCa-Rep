import csv
import math
import struct
import wave
import os

def parse_votes(csv_path, filter_func):
    sequence = []
    if not os.path.exists(csv_path):
        print(f"[!] Archivo no encontrado: {csv_path}")
        return sequence
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                if filter_func(row):
                    # Normalizamos la columna, a veces puede venir distinta
                    voto = 0
                    if "abelardo de la espriella" in row:
                        voto = int(row["abelardo de la espriella"])
                    elif "votos" in row:
                        voto = int(row["votos"])
                    sequence.append((row.get("mpio", "0"), voto))
            except Exception:
                pass
    return sequence

def generate_wav(frequencies, duration_per_note, filename):
    sample_rate = 44100.0
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(int(sample_rate))
        
        for freq in frequencies:
            if freq <= 0:
                for i in range(int(sample_rate * duration_per_note)):
                    wav_file.writeframesraw(struct.pack('<h', 0))
                continue
                
            for i in range(int(sample_rate * duration_per_note)):
                # Onda sinusoidal pura
                value = int(32767.0 * 0.5 * math.sin(2.0 * math.pi * freq * (i / sample_rate)))
                wav_file.writeframesraw(struct.pack('<h', value))

def votes_to_freq(votes):
    # Mapea los votos a frecuencias audibles (220Hz a 880Hz) usando escala logarítmica
    if votes <= 0:
        return 0
    val = math.log10(votes)
    normalized = min(val / 6.0, 1.0) # asumiendo max 1,000,000 votos
    freq = 220.0 + (normalized * 660.0)
    return freq

def main():
    print("=========================================================")
    print("🎵 SONIFICACIÓN FORENSE: EL SONIDO DE LA ANOMALÍA")
    print("=========================================================")
    
    csv_nacional = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/resultados_municipios_2026_limpio.csv"
    csv_exterior = "/home/andrea-zabala-c/Desktop/repo_github_comparacion/01_EVIDENCIA/ESTUDIO_ESTADISTICO_ANOMALIAS_CONSULADOS.csv"
    
    # 1. Analizar Antioquia
    print("[*] Leyendo datos Nacionales (Antioquia)...")
    antioquia_votes = parse_votes(csv_nacional, lambda r: int(r.get("dpto", 0)) == 1)
    
    # 2. Analizar Exterior
    print("[*] Leyendo datos del EXTERIOR (Consulados)...")
    exterior_votes = parse_votes(csv_exterior, lambda r: True)
    
    freqs = []
    print("[*] Convirtiendo anomalías de Antioquia a frecuencias de audio...")
    for _, v in antioquia_votes:
        freqs.append(votes_to_freq(v))
        
    print("[*] Convirtiendo anomalías del Exterior a frecuencias de audio...")
    # Diferenciamos el exterior con una nota base más aguda o simplemente añadimos la secuencia
    for _, v in exterior_votes:
        freqs.append(votes_to_freq(v) * 1.5) # Subimos el tono para distinguirlo acústicamente
        
    output_wav = "/home/andrea-zabala-c/Desktop/repo_github_comparacion/01_EVIDENCIA/anomalia_sonora_fraude.wav"
    os.makedirs(os.path.dirname(output_wav), exist_ok=True)
    
    print("[*] Sintetizando archivo .WAV...")
    generate_wav(freqs, 0.25, output_wav) # 0.25 seg por municipio/consulado
    
    print(f"\n[+] ¡Sonificación completa! Archivo de audio generado en:")
    print(f"    -> {output_wav}")
    print("=========================================================")

if __name__ == "__main__":
    main()
