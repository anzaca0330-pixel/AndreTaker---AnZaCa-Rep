import os
import time
from datetime import datetime
import subprocess

WATCH_DIRS = [
    "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14",
    "/home/andrea-zabala-c/.ssh"
]
LOG_FILE = "/home/andrea-zabala-c/SCRIPTS_SEGURIDAD/INTRUSION_ALERTS.log"

def log_alert(msg):
    alert = f"[{datetime.now()}] ⚠️ ALERTA DE INTRUSIÓN: {msg}\n"
    with open(LOG_FILE, "a") as f:
        f.write(alert)
    print(alert.strip())
    # Opcional: Sonido de sistema o notificación en escritorio
    try:
        subprocess.run(["notify-send", "ALERTA DE SEGURIDAD", msg], capture_output=True)
    except:
        pass

def get_file_hashes():
    hashes = {}
    for d in WATCH_DIRS:
        if not os.path.exists(d):
            continue
        for root, dirs, files in os.walk(d):
            if ".git" in root:
                continue
            for f in files:
                filepath = os.path.join(root, f)
                try:
                    stats = os.stat(filepath)
                    hashes[filepath] = stats.st_mtime
                except Exception:
                    pass
    return hashes

def check_suspicious_processes():
    try:
        out = subprocess.check_output(["ps", "-eo", "pid,user,command"]).decode()
        suspicious = ["nc -", "netcat", "bash -i", "nmap", "wireshark", "tcpdump"]
        for line in out.splitlines():
            for s in suspicious:
                if s in line and "monitor_intrusos" not in line and "ps -eo" not in line:
                    log_alert(f"Proceso sospechoso detectado: {line.strip()}")
    except Exception:
        pass

def main():
    print(f"[*] Monitor IDS Iniciado. Protegiendo: {WATCH_DIRS}")
    log_alert("Sistema de Monitoreo IDS Inicializado y en guardia.")
    
    known_files = get_file_hashes()
    
    while True:
        time.sleep(5)
        
        # 1. Monitoreo de Integridad de Archivos (FIM)
        current_files = get_file_hashes()
        
        # Detectar eliminaciones o modificaciones
        for f, mtime in list(known_files.items()):
            if f not in current_files:
                log_alert(f"Archivo ELIMINADO: {f}")
                del known_files[f]
            elif current_files[f] != mtime:
                log_alert(f"Archivo MODIFICADO: {f}")
                known_files[f] = current_files[f]
                
        # Detectar creaciones nuevas (ej. llaves SSH plantadas o backdoors)
        for f, mtime in current_files.items():
            if f not in known_files:
                log_alert(f"Archivo CREADO: {f}")
                known_files[f] = mtime
                
        # 2. Monitoreo de Procesos
        check_suspicious_processes()

if __name__ == "__main__":
    main()
