import os
import random
import string
import subprocess
import hashlib

class AntiPalantir:
    @staticmethod
    def calcular_sha256(filepath: str) -> str:
        """Calcula el hash criptográfico SHA-256 de un archivo pericial."""
        sha256 = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(65536):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            return f"error: {str(e)}"

    @classmethod
    def ejecutar_mitigacion(cls, filepath: str) -> dict:
        """
        Ejecuta el protocolo activo de contra-inteligencia sobre un archivo:
        1. Sanitización de metadatos (limpieza exif/XMP).
        2. Spoofing de autoría y fechas aleatorias.
        3. Padding aleatorio al final del archivo para mutación de hash SHA-256.
        """
        if not os.path.exists(filepath):
            return {"status": "error", "message": f"Ruta no encontrada: {filepath}"}
            
        hash_previo = cls.calcular_sha256(filepath)
        
        # 1. Sanitización
        meta_purged = False
        try:
            subprocess.run(['exiftool', '-all=', '-overwrite_original', filepath], capture_output=True)
            meta_purged = True
        except Exception:
            pass
            
        # 2. Spoofing
        meta_spoofed = False
        autores_falsos = ["Veeduría Ciudadana", "Anonymous Veedor", "System Operator", "User_Node_12", "Forensic Analyst"]
        autor_fake = random.choice(autores_falsos)
        fecha_fake = f"2026:08:{random.randint(10,28)} {random.randint(10,23)}:{random.randint(10,59)}:{random.randint(10,59)}"
        try:
            subprocess.run([
                'exiftool',
                f'-Author={autor_fake}',
                f'-CreateDate={fecha_fake}',
                f'-ModifyDate={fecha_fake}',
                '-overwrite_original',
                filepath
            ], capture_output=True)
            meta_spoofed = True
        except Exception:
            pass
            
        # 3. Mutación de Hash (Padding)
        hash_mutated = False
        try:
            rand_padding = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            if filepath.lower().endswith('.pdf'):
                with open(filepath, 'ab') as f:
                    f.write(f"\n% AP_PAD_{rand_padding}\n".encode('utf-8'))
                hash_mutated = True
            else:
                with open(filepath, 'ab') as f:
                    f.write(f"\n# AP_PAD_{rand_padding}\n".encode('utf-8'))
                hash_mutated = True
        except Exception:
            pass
            
        hash_nuevo = cls.calcular_sha256(filepath)
        
        return {
            "status": "success",
            "file": os.path.basename(filepath),
            "metadata_cleaned": meta_purged,
            "entity_spoofed": meta_spoofed,
            "hash_mutated": hash_mutated,
            "original_hash": hash_previo,
            "mutated_hash": hash_nuevo
        }
