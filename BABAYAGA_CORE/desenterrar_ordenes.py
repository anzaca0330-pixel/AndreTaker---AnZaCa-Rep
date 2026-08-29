#!/usr/bin/env python3
import os
import json
import glob
from datetime import datetime

def main():
    print("🧙‍♀️ BabaYaga desenterrando la memoria del bosque...")
    
    brain_dir = "/home/andrea-zabala-c/.gemini/antigravity-ide/brain"
    desenterrados_dir = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/03_DOCUMENTACION/DESENTERRADOS"
    
    pattern1 = os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    pattern2 = os.path.join(desenterrados_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    
    files = glob.glob(pattern1) + glob.glob(pattern2)
    
    all_orders = []
    processed_convs = set()
    
    for f in files:
        # Extraer el ID de la conversación de la ruta
        parts = f.split(os.sep)
        # La ruta es .../brain/<conv_id>/.system_generated/logs/transcript.jsonl
        # El ID está en la posición -4
        conv_id = parts[-4]
        
        if conv_id in processed_convs:
            continue
        processed_convs.add(conv_id)
        
        # Obtener fecha de modificación del archivo como referencia temporal
        try:
            mtime = os.path.getmtime(f)
            timestamp = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            timestamp = "Desconocido"
            mtime = 0
            
        try:
            with open(f, 'r', encoding='utf-8') as file_handle:
                for line in file_handle:
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        if data.get("type") == "USER_INPUT":
                            content = data.get("content", "").strip()
                            if content:
                                all_orders.append({
                                    "mtime": mtime,
                                    "timestamp": timestamp,
                                    "conv_id": conv_id,
                                    "step": data.get("step_index", 0),
                                    "content": content
                                })
                    except Exception:
                        pass
        except Exception as e:
            print(f"⚠️ Error leyendo {f}: {e}")
            
    # Ordenar por fecha de modificación del archivo transcript.jsonl
    all_orders.sort(key=lambda x: (x["mtime"], x["step"]))
    
    output_md = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/03_DOCUMENTACION/HISTORIAL_DE_ORDENES.md"
    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    
    with open(output_md, 'w', encoding='utf-8') as out:
        out.write("# 📜 HISTORIAL DE ÓRDENES Y CONVERSACIONES DESENTERRADAS\n")
        out.write(f"**Fecha del Ritual:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        out.write("**Origen:** Historial de logs del sistema de IA Antigravity (Gemini)  \n\n")
        out.write("---  \n\n")
        
        current_conv = None
        for order in all_orders:
            if order["conv_id"] != current_conv:
                current_conv = order["conv_id"]
                out.write(f"\n## 📁 Conversación `{current_conv}` ({order['timestamp']})\n\n")
                
            out.write(f"* **Paso {order['step']}:** {order['content']}\n")
            
    print(f"✅ Se han desenterrado {len(all_orders)} órdenes.")
    print(f"📄 Historial guardado en: {output_md}")

if __name__ == "__main__":
    main()
