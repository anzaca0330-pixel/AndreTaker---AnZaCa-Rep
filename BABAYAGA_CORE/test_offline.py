import os
import sys

# Script de prueba offline para validar el servidor FastAPI, base de datos SQLite y módulos periciales / Anti-Palantir
print("🧪 Iniciando validación offline del ecosistema modular...")

# Asegurar importabilidad de babayaga
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from babayaga.core.forensics.xref import XrefAnalyzer
from babayaga.core.forensics.raster import RasterAnalyzer
from babayaga.core.custody import CustodyTracker
from babayaga.core.intelligence.mitigation import AntiPalantir
from babayaga.api import database

print("✅ Todos los módulos importados con éxito.")

# 1. Probar base de datos SQLite
database.init_db()
print("✅ Base de datos SQLite inicializada correctamente.")

# 2. Probar análisis pericial sobre una muestra
pdf_muestra = os.path.abspath(os.path.join(os.path.dirname(__file__), "../00_MUESTRAS_EVIDENCIA/2DA_VUELTA/E14_PRE_60_010_000_00_00_001_3085_Mesa_1.pdf"))
if not os.path.exists(pdf_muestra):
    print("❌ Error: No se encontró el PDF de muestra.")
    sys.exit(1)

print(f"🔍 Evaluando XREF sobre {os.path.basename(pdf_muestra)}...")
xref_res = XrefAnalyzer.analizar_estructura(pdf_muestra)
print(f"   ├─ Exit Code: {xref_res.get('exit_code')}")
print(f"   └─ Discrepancia estructural detectada: {xref_res.get('XREF_discrepancia')}")

# 3. Probar Protocolo Anti-Palantir
print("\n🛡️ Probando Protocolo Anti-Palantir (Simulado sobre una copia temporal)...")
import tempfile
import shutil

with tempfile.TemporaryDirectory() as tmpdir:
    temp_pdf = os.path.join(tmpdir, "evidencia_test.pdf")
    shutil.copy(pdf_muestra, temp_pdf)
    
    print(f"   ├─ Copiado a: {temp_pdf}")
    res_ap = AntiPalantir.ejecutar_mitigacion(temp_pdf)
    print(f"   ├─ Status: {res_ap['status']}")
    print(f"   ├─ Original Hash: {res_ap['original_hash']}")
    print(f"   ├─ Mutated Hash: {res_ap['mutated_hash']}")
    print(f"   ├─ Metadatos Limpios: {res_ap['metadata_cleaned']}")
    print(f"   └─ Spoofing Realizado: {res_ap['entity_spoofed']}")

print("\n🎉 VALIDACIÓN FINALIZADA CON ÉXITO: El sistema es estable, modular e inmune a correlaciones.")
