import sys
import os
try:
    from PIL import Image
except ImportError:
    print("PIL no está instalado.")
    sys.exit(1)

def generate_clipping_map(img_path):
    print("[*] Generando mapa de saturación absoluta (Píxeles RGB = 255,255,255)...")
    try:
        img = Image.open(img_path).convert('RGB')
        pixels = img.load()
        width, height = img.size
        
        # Crear una imagen nueva totalmente negra
        map_img = Image.new('RGB', (width, height), "black")
        map_pixels = map_img.load()
        
        pure_white_count = 0
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                # Si el píxel es puramente blanco sin variación
                if r == 255 and g == 255 and b == 255:
                    # Pintarlo de rojo intenso en el mapa
                    map_pixels[x, y] = (255, 0, 0)
                    pure_white_count += 1
                    
        total_pixels = width * height
        percentage = (pure_white_count / total_pixels) * 100
        
        out_path = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/MAPA_BLANCO_PURO_MESA16.jpg"
        map_img.save(out_path)
        print(f"[+] Mapa generado en: {out_path}")
        print(f"[+] Total de píxeles puros #FFFFFF: {pure_white_count} ({percentage:.2f}% de la imagen)")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_clipping_map(sys.argv[1])
