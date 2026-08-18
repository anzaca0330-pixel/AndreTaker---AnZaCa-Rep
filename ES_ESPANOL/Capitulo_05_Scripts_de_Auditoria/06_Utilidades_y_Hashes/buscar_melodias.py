import csv

def get_note(vote):
    # Mapping MIDI notes (C4 = 60). We can do a mod 12 mapping, or direct mapping if they are typical MIDI values.
    # We can print both the absolute number and the approximate note.
    notes = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
    
    # Simple mapping: note = notes[vote % 12]
    # But usually, if they used MIDI directly: 60 = Do, 62 = Re, 64 = Mi...
    return f"{vote} ({notes[vote % 12]})"

def main():
    csv_path = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/MESAS_FRAUDULENTAS_OUTLIERS.csv"
    
    dpto_sequences = {}
    
    try:
        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                dpto = row.get("Dpto")
                votos_abelardo = int(row.get("Votos_Espriella", 0))
                
                if dpto not in dpto_sequences:
                    dpto_sequences[dpto] = []
                    
                dpto_sequences[dpto].append(votos_abelardo)
                
        # Analyze sequences per department
        for dpto, seq in dpto_sequences.items():
            if len(seq) > 2:
                print(f"\n--- DEPARTAMENTO {dpto} ---")
                # Print sequence of numbers
                print(f"Secuencia cruda: {seq[:20]}")
                
                # Print as notes (assuming MIDI or Modulo 12)
                notes_mod12 = [get_note(v) for v in seq[:20]]
                print(f"Melodía: {', '.join(notes_mod12)}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
