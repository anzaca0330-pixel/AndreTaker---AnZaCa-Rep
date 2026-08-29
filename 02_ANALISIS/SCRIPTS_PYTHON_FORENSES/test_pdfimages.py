import subprocess
import os

pdf_dir = "/home/andrea-zabala-c/Desktop/actas/PAQUETE_FINAL/PDFs_Originales/"

print("🔍 PRUEBA DE LA NUEVA LÓGICA DE PDFIMAGES 🔍")
for f in os.listdir(pdf_dir):
    if f.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, f)
        
        proc = subprocess.run(["pdfimages", "-list", pdf_path], capture_output=True, text=True)
        lines = [l for l in proc.stdout.splitlines() if l.strip()]
        
        # OLD LOGIC
        old_multicapa = len(lines) > 3
        
        # NEW LOGIC
        new_multicapa = False
        if len(lines) > 2:
            data_lines = lines[2:]
            pages_count = {}
            for line in data_lines:
                parts = line.split()
                if not parts: continue
                page_num = parts[0]
                pages_count[page_num] = pages_count.get(page_num, 0) + 1
            if any(count > 1 for count in pages_count.values()):
                new_multicapa = True
                
        print(f"📄 {f}")
        print(f"  ➜ Lógica Antigua: {'🔴 FALSO POSITIVO (Multicapa)' if old_multicapa else '🟢 Limpio'}")
        print(f"  ➜ Lógica Nueva:   {'🔴 Multicapa Real' if new_multicapa else '🟢 Limpio (Capas Normales)'}")
        print("-" * 50)
