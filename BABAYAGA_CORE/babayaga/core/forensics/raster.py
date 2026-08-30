import os
import subprocess

class RasterAnalyzer:
    @staticmethod
    def analizar_imagenes(pdf_path: str, temp_dir: str = ".") -> dict:
        """Extrae imágenes raster y analiza su espacio de color, media y varianza (std = 0)."""
        if not os.path.exists(pdf_path):
            return {'error': f'Archivo no encontrado: {pdf_path}'}
            
        try:
            base = os.path.basename(pdf_path).replace('.pdf', '_img')
            output_prefix = os.path.join(temp_dir, base)
            
            # Extraer imágenes como PNGs
            subprocess.run(['pdfimages', '-png', pdf_path, output_prefix], capture_output=True)
            imagenes = []
            
            # Escanear el directorio temp para encontrar las imágenes generadas
            base_name = os.path.basename(output_prefix)
            for archivo in os.listdir(temp_dir):
                if archivo.startswith(base_name) and archivo.endswith('.png'):
                    archivo_path = os.path.join(temp_dir, archivo)
                    resultado = subprocess.run(
                        ['identify', '-format', '%[colorspace],%[mean],%[standard-deviation]', archivo_path],
                        capture_output=True,
                        text=True
                    )
                    
                    output = resultado.stdout.strip()
                    colorspace = 'Desconocido'
                    mean_val = 0.0
                    std_val = 0.0
                    
                    if output and ',' in output:
                        parts = output.split(',')
                        colorspace = parts[0]
                        try:
                            mean_val = float(parts[1])
                            std_val = float(parts[2])
                        except (ValueError, IndexError):
                            pass
                    
                    imagenes.append({
                        'archivo': archivo,
                        'colorspace': colorspace,
                        'media': mean_val,
                        'desviacion_estandar': std_val,
                        'varianza_cero': (std_val < 1.0) or (std_val != std_val)
                    })
                    
                    try:
                        os.remove(archivo_path)
                    except Exception:
                        pass
                        
            return {'imagenes': imagenes}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def detectar_elementos_vectoriales(pdf_path: str) -> dict:
        """Busca trazas aproximadas de operadores vectoriales en el stream binario."""
        try:
            with open(pdf_path, 'rb') as f:
                content = f.read()
            
            trazados_detectados = 0
            if b' /Paint ' in content or b' /Pattern ' in content or b' /Shading ' in content:
                trazados_detectados += 10
                
            for op in [b' m ', b' l ', b' re ', b' f ', b' S ']:
                trazados_detectados += content.count(op)
                
            return {
                'contiene_vectores': trazados_detectados > 15,
                'score_vectorial': trazados_detectados
            }
        except Exception:
            return {
                'contiene_vectores': False,
                'score_vectorial': 0
            }
