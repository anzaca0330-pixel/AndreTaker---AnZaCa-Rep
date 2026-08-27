#!/usr/bin/env python3
# monitor_forense.py - Monitoreo forense avanzado
# Investigadora: Andrea Zabala Cárcamo

import os
import time
import subprocess
import hashlib
import json
from datetime import datetime
from pathlib import Path

class MonitorForense:
    def __init__(self, discos, intervalo=30):
        self.discos = discos
        self.intervalo = intervalo
        self.log_dir = "/media/andrea-zabala-c/D A T A1/04_BITACORA/NOTAS_DE_CAMPO"
        self.archivo_log = f"{self.log_dir}/monitor_forense_{datetime.now().strftime('%Y%m%d')}.json"
        self.alertas = []
        self.hashes_guardados = {}
        self.cargar_hashes()
        
    def cargar_hashes(self):
        """Carga hashes previos si existen"""
        try:
            with open(f"{self.log_dir}/hashes_guardados.txt", 'r') as f:
                for linea in f:
                    partes = linea.strip().split(' ', 1)
                    if len(partes) == 2:
                        self.hashes_guardados[partes[1]] = partes[0]
        except FileNotFoundError:
            pass
    
    def guardar_hashes(self):
        """Guarda hashes actuales"""
        with open(f"{self.log_dir}/hashes_guardados.txt", 'w') as f:
            for ruta, hash_val in self.hashes_guardados.items():
                f.write(f"{hash_val} {ruta}\n")
    
    def calcular_hash(self, ruta):
        """Calcula SHA-256 de un archivo"""
        try:
            with open(ruta, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except Exception:
            return None
    
    def verificar_archivos_criticos(self, disco):
        """Verifica archivos críticos en el disco"""
        criticos = [
            "INDICE_DISCO.md",
            "01_EVIDENCIA/HASHES/firmas_criptograficas_sha256.txt"
        ]
        for critico in criticos:
            ruta = f"{disco}/{critico}"
            if os.path.exists(ruta):
                hash_actual = self.calcular_hash(ruta)
                if hash_actual:
                    if ruta in self.hashes_guardados:
                        if self.hashes_guardados[ruta] != hash_actual:
                            self.alertar(f"¡ARCHIVO MODIFICADO! {ruta}")
                    self.hashes_guardados[ruta] = hash_actual
    
    def verificar_procesos(self):
        """Verifica procesos sospechosos"""
        procesos_sospechosos = ["nmap", "hydra", "john", "aircrack", "sqlmap", "metasploit", "nc", "netcat"]
        try:
            resultado = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            for proceso in procesos_sospechosos:
                if proceso in resultado.stdout:
                    self.alertar(f"Proceso sospechoso detectado: {proceso}")
        except Exception:
            pass
    
    def verificar_conexiones(self):
        """Verifica conexiones de red sospechosas"""
        try:
            resultado = subprocess.run(['netstat', '-tunap'], capture_output=True, text=True)
            lineas = resultado.stdout.split('\n')
            for linea in lineas:
                if "ESTABLISHED" in linea and any(puerto in linea for puerto in [":22", ":23", ":21", ":445", ":139", ":3389"]):
                    if "127.0.0.1" not in linea:
                        self.alertar(f"Conexión de red sospechosa: {linea.strip()}")
        except Exception:
            pass
    
    def verificar_usb(self):
        """Verifica nuevos dispositivos USB"""
        try:
            resultado = subprocess.run(['lsblk', '-o', 'NAME,SIZE,MODEL,MOUNTPOINT'], capture_output=True, text=True)
            lineas = resultado.stdout.split('\n')
            for linea in lineas:
                if "sd" in linea and "sda" not in linea:
                    self.alertar(f"Nuevo dispositivo detectado: {linea.strip()}")
        except Exception:
            pass
    
    def alertar(self, mensaje):
        """Registra una alerta"""
        timestamp = datetime.now().isoformat()
        alerta = {
            "timestamp": timestamp,
            "mensaje": mensaje
        }
        self.alertas.append(alerta)
        print(f"🚨 {timestamp} | {mensaje}")
        self.guardar_log()
    
    def guardar_log(self):
        """Guarda el log en formato JSON"""
        log_data = {
            "ultima_actualizacion": datetime.now().isoformat(),
            "alertas": self.alertas[-100:],  # Últimas 100 alertas
            "hashes": self.hashes_guardados
        }
        with open(self.archivo_log, 'w') as f:
            json.dump(log_data, f, indent=2)
    
    def ejecutar(self):
        """Bucle principal de monitoreo"""
        print("🛡️ INICIANDO MONITOREO FORENSE...")
        print(f"Discos monitoreados: {self.discos}")
        print(f"Intervalo: {self.intervalo} segundos")
        print("Presiona Ctrl+C para detener\n")
        
        try:
            while True:
                for disco in self.discos:
                    if os.path.exists(disco):
                        self.verificar_archivos_criticos(disco)
                self.verificar_procesos()
                self.verificar_conexiones()
                self.verificar_usb()
                self.guardar_hashes()
                self.guardar_log()
                
                # Mostrar estado
                print(f"✓ {datetime.now().strftime('%H:%M:%S')} - Monitoreo activo ({len(self.alertas)} alertas)")
                time.sleep(self.intervalo)
        except KeyboardInterrupt:
            print("\n🛑 Monitoreo detenido por el usuario")
            self.guardar_log()

if __name__ == "__main__":
    # Configurar discos a monitorear
    DISCOS = [
        "/media/andrea-zabala-c/D A T A1",
        "/media/andrea-zabala-c/BACKUP"
    ]
    
    monitor = MonitorForense(DISCOS, intervalo=30)
    monitor.ejecutar()
