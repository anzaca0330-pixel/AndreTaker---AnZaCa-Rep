import os
import sys
import hashlib
from colorama import init, Fore, Style

init(autoreset=True)

def calcular_hash_sha256(ruta_archivo):
    """Calcula el hash SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(ruta_archivo, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(Fore.RED + f"Error al leer {ruta_archivo}: {e}")
        return None

def comparar_directorios(dir_antes, dir_despues):
    print(Fore.CYAN + "="*70)
    print(Fore.CYAN + "🔍 COMPARADOR FORENSE DE SUSTITUCIÓN DE EVIDENCIA")
    print(Fore.CYAN + "="*70)
    print(f"Directorio Original (Ej. 1 de Junio): {dir_antes}")
    print(f"Directorio Modificado (Ej. 12 de Julio): {dir_despues}\n")
    
    if not os.path.exists(dir_antes) or not os.path.exists(dir_despues):
        print(Fore.RED + "❌ Error: Uno o ambos directorios no existen.")
        return

    archivos_antes = {f for f in os.listdir(dir_antes) if f.endswith('.pdf')}
    archivos_despues = {f for f in os.listdir(dir_despues) if f.endswith('.pdf')}
    
    archivos_comunes = archivos_antes.intersection(archivos_despues)
    solo_antes = archivos_antes - archivos_despues
    solo_despues = archivos_despues - archivos_antes
    
    archivos_alterados = 0
    archivos_intactos = 0
    
    print(Fore.YELLOW + f"[*] Analizando {len(archivos_comunes)} archivos comunes...\n")
    
    for archivo in archivos_comunes:
        ruta_antes = os.path.join(dir_antes, archivo)
        ruta_despues = os.path.join(dir_despues, archivo)
        
        hash_antes = calcular_hash_sha256(ruta_antes)
        hash_despues = calcular_hash_sha256(ruta_despues)
        
        if hash_antes and hash_despues:
            if hash_antes != hash_despues:
                print(Fore.RED + f"🚨 ¡EVIDENCIA SUSTITUIDA! Archivo: {archivo}")
                print(f"   Hash Original:   {hash_antes}")
                print(f"   Hash Modificado: {hash_despues}")
                archivos_alterados += 1
            else:
                archivos_intactos += 1
                
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.CYAN + "📊 REPORTE DE CADENA DE CUSTODIA")
    print(Fore.CYAN + "="*70)
    print(Fore.WHITE + f"Total de archivos comparados: {len(archivos_comunes)}")
    print(Fore.GREEN + f"Archivos Intactos (Mismo Hash): {archivos_intactos}")
    print(Fore.RED + f"Archivos Alterados Silenciosamente: {archivos_alterados}")
    
    if solo_antes:
        print(Fore.YELLOW + f"Archivos eliminados en el servidor: {len(solo_antes)}")
    if solo_despues:
        print(Fore.YELLOW + f"Archivos nuevos inyectados: {len(solo_despues)}")
        
    print(Fore.CYAN + "="*70)
    
    if archivos_alterados > 0:
        print(Fore.RED + "CONCLUSIÓN LEGAL: SE COMPRUEBA MANIPULACIÓN Y SUSTITUCIÓN DE EVIDENCIA")
        print(Fore.RED + "EN LA BASE DE DATOS OFICIAL DESPUÉS DE LA FECHA DE TRANSMISIÓN.")
    else:
        print(Fore.GREEN + "Los hashes coinciden. No hubo sustitución en los archivos con el mismo nombre.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 comparador_sustitucion_evidencia.py <directorio_antes> <directorio_despues>")
        sys.exit(1)
        
    dir_a = sys.argv[1]
    dir_b = sys.argv[2]
    comparar_directorios(dir_a, dir_b)
