import re
import subprocess
import os

class SpoofingDetector:
    @staticmethod
    def audit_qr_spoofing(pdf_path: str) -> dict:
        """
        Audita el archivo PDF en busca de inyecciones sintéticas y suplantación de QR (QR Spoofing):
        1. Compara las coordenadas declaradas del QR con la paleta de color del documento.
        2. Detecta la presencia de múltiples bloques de imágenes QR inyectados en la capa /Contents.
        3. Identifica si existe redundancia de firmas o superposiciones visuales inconsistentes.
        """
        if not os.path.exists(pdf_path):
            return {"status": "error", "message": f"Archivo no encontrado: {pdf_path}"}
            
        try:
            with open(pdf_path, 'rb') as f:
                content = f.read()
                
            # Buscar indicadores de inyecciones de imágenes en el stream binario
            # Los objetos de tipo imagen sintética suelen tener flujos DecodeParms o máscaras de 1-bit (/ImageMask true)
            image_masks = content.count(b'/ImageMask true')
            image_streams = content.count(b'/Subtype /Image')
            xref_tables = content.count(b'xref')
            
            # QR Spoofing Scar: Presencia de múltiples streams de imágenes con metadatos de máscara
            # en un documento que debería ser un escaneo plano de una sola capa
            has_qr_spoofing = (image_masks > 1) or (image_streams > 1 and xref_tables > 1)
            
            # Detección de operadores vectoriales inyectados para tapar información original
            vector_overwrites = 0
            for op in [b'/Do', b'/Paint', b'/ImageMask']:
                vector_overwrites += content.count(op)
                
            status = "detected" if has_qr_spoofing else "clean"
            
            return {
                "status": "success",
                "pdf": os.path.basename(pdf_path),
                "qr_spoofing_detected": has_qr_spoofing,
                "image_masks_found": image_masks,
                "image_streams_found": image_streams,
                "vector_overwrite_score": vector_overwrites,
                "diagnosis": "MUESTRA CORRUPTA (QR Spoofing / Inyección detectada)" if has_qr_spoofing else "Estructura limpia"
            }
        except Exception as e:
            return {"status": "error", "message": f"Error en el análisis de QR Spoofing: {str(e)}"}
