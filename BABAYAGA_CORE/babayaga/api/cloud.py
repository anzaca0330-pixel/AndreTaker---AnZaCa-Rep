import os
import subprocess

class CloudSync:
    @staticmethod
    def subir_a_nube(filepath: str, bucket_name: str) -> dict:
        """
        Sube un archivo de evidencia a un bucket de Google Cloud Storage.
        Si la librería google-cloud-storage no está instalada, utiliza
        gcloud storage cp o gsutil cp como fallback de cero dependencias.
        """
        if not os.path.exists(filepath):
            return {"status": "error", "message": f"Archivo no encontrado: {filepath}"}
            
        destination = f"gs://{bucket_name}/{os.path.basename(filepath)}"
        print(f"☁️ Subiendo {os.path.basename(filepath)} a {destination}...")
        
        # 1. Intentar con librería de cliente oficial
        try:
            from google.cloud import storage
            client = storage.Client()
            bucket = client.bucket(bucket_name)
            blob = bucket.blob(os.path.basename(filepath))
            blob.upload_from_filename(filepath)
            return {"status": "success", "metodo": "google-cloud-storage-sdk", "destination": destination}
        except ImportError:
            pass # Fallback a herramientas CLI
        except Exception as e:
            print(f"⚠️ SDK falló o no tiene ADC configurado: {str(e)}. Intentando CLI fallback...")

        # 2. Fallback a gcloud CLI
        try:
            res = subprocess.run(
                ['gcloud', 'storage', 'cp', filepath, destination],
                capture_output=True, text=True
            )
            if res.returncode == 0:
                return {"status": "success", "metodo": "gcloud-cli", "destination": destination}
        except Exception:
            pass

        # 3. Fallback a gsutil CLI
        try:
            res = subprocess.run(
                ['gsutil', 'cp', filepath, destination],
                capture_output=True, text=True
            )
            if res.returncode == 0:
                return {"status": "success", "metodo": "gsutil-cli", "destination": destination}
        except Exception:
            pass

        return {
            "status": "error", 
            "message": "No se pudo sincronizar. Asegúrate de que gcloud o gsutil estén instalados y autenticados."
        }

    @classmethod
    def sincronizar_caso(cls, db_path: str, bucket_name: str) -> dict:
        """Sube la copia del archivo de base de datos sqlite a la nube para preservar el historial."""
        return cls.subir_a_nube(db_path, bucket_name)
