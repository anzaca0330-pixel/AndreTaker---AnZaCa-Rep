import hashlib
import os
import subprocess
import json
from datetime import datetime, timezone

class CustodyTracker:
    @staticmethod
    def calcular_sha256(filepath: str) -> str:
        """Calcula el hash criptográfico SHA-256 de un archivo pericial."""
        if not os.path.exists(filepath):
            return "error: archivo no encontrado"
            
        sha256 = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(65536):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            return f"error: {str(e)}"

    @staticmethod
    def obtener_timestamps_sistema(filepath: str) -> dict:
        """Obtiene fechas de creación y modificación física del sistema de archivos."""
        try:
            stat = os.stat(filepath)
            # Intentar obtener fecha de nacimiento (birthtime) si está disponible en la plataforma
            try:
                birth = stat.st_birthtime
            except AttributeError:
                # Fallback a ctime
                birth = stat.st_ctime
                
            return {
                'fecha_creacion_sistema': datetime.fromtimestamp(birth, timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                'fecha_modificacion_sistema': datetime.fromtimestamp(stat.st_mtime, timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            }
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def extraer_fechas_metadatos(filepath: str) -> dict:
        """Extrae marcas de tiempo de generación interna contenidas en el PDF."""
        try:
            res = subprocess.run(
                ['exiftool', '-CreateDate', '-ModifyDate', '-j', filepath],
                capture_output=True,
                text=True
            )
            if res.returncode == 0:
                data = json.loads(res.stdout)
                if data and isinstance(data, list):
                    return {
                        'fecha_creacion_pdf': data[0].get('CreateDate', 'No definida'),
                        'fecha_modificacion_pdf': data[0].get('ModifyDate', 'No definida')
                    }
            return {'metadata': 'No extraída'}
        except Exception as e:
            return {'error': str(e)}
