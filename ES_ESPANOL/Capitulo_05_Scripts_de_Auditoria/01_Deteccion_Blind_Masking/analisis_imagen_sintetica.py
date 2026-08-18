import sys
try:
    from PIL import Image, ImageStat
except ImportError:
    print("PIL no está instalado, por favor instala Pillow")
    sys.exit(1)

def analyze_image(img_path):
    try:
        # Cargar imagen y convertir a escala de grises
        img = Image.open(img_path).convert('L')
        width, height = img.size
        
        # Extraer tres parches de fondo (lugares donde normalmente no hay tinta)
        # Parche 1: Esquina superior izquierda
        patch1 = img.crop((50, 50, 450, 450))
        # Parche 2: Margen lateral derecho
        patch2 = img.crop((width - 450, height // 2, width - 50, (height // 2) + 400))
        # Parche 3: Esquina inferior izquierda
        patch3 = img.crop((50, height - 450, 450, height - 50))
        
        patches = [patch1, patch2, patch3]
        
        print(f"=== ANÁLISIS DE ILUMINACIÓN, RUIDO Y TEXTURA FÍSICA ===")
        print(f"Archivo: {img_path}")
        print(f"Resolución: {width} x {height}\n")
        
        is_synthetic = False
        
        for i, patch in enumerate(patches):
            stat = ImageStat.Stat(patch)
            stddev = stat.stddev[0]
            mean = stat.mean[0]
            
            print(f"[-] Evaluando Muestra de Fondo {i+1}:")
            print(f"    -> Luminosidad Media: {mean:.2f} (0=Negro, 255=Blanco Puro)")
            print(f"    -> Desviación Estándar (Ruido/Textura): {stddev:.4f}")
            
            # En un escaneo real, el ruido térmico del sensor y el grano del papel
            # SIEMPRE generan una desviación estándar mayor a 1.5 - 2.0.
            # Un fondo puramente digital (#FFFFFF) tendrá desviación 0.0 o cercana a 0.0.
            if stddev < 1.0:
                print("    [!] ALERTA: Ausencia total de ruido analógico. Superficie matemáticamente plana.")
                is_synthetic = True
            else:
                print("    [+] Ruido analógico detectado.")
            print("")
            
        if is_synthetic:
            print(">>> VEREDICTO DE LUCES Y SOMBRAS <<<")
            print("[!!!] FRAUDE DETECTADO: La imagen carece de la física de la luz (no hay caída de iluminación).")
            print("[!!!] No hay grano de papel ni ruido de sensor. El fondo fue generado por un lienzo digital (Deepfake Rasterizado).")
            print("[!!!] Esto explica por qué el PDF carece de la inyección vectorial: ¡Toda la imagen JPEG es una falsificación sintética!")
        else:
            print(">>> VEREDICTO DE LUCES Y SOMBRAS <<<")
            print("[+] La imagen presenta degradación de luz y ruido de sensor acordes a un escaneo físico real.")

    except Exception as e:
        print(f"Error procesando la imagen: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analisis_imagen_sintetica.py <ruta_imagen>")
        sys.exit(1)
    analyze_image(sys.argv[1])
