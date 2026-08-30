import os
import sys
import unittest
import tempfile
import shutil
import sqlite3

# Insertar el directorio principal de BABAYAGA_CORE al path para asegurar importaciones
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from babayaga.core.xref import XrefAnalyzer
from babayaga.core.raster import RasterAnalyzer
from babayaga.core.custody import CustodyTracker
from babayaga.core.defense import AntiPalantir
from babayaga.core.benford import BenfordAnalyzer
from babayaga.api import database

class TestBabaYagaCoreOffline(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Localizar el PDF de muestra dentro del repositorio
        cls.pdf_muestra = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 
            "../00_MUESTRAS_EVIDENCIA/2DA_VUELTA/E14_PRE_60_010_000_00_00_001_3085_Mesa_1.pdf"
        ))
        if not os.path.exists(cls.pdf_muestra):
            raise FileNotFoundError(f"No se encontró el PDF de control para las pruebas en: {cls.pdf_muestra}")

    def setUp(self):
        # Crear un directorio temporal para no ensuciar la evidencia real
        self.test_dir = tempfile.mkdtemp()
        self.pdf_temporal = os.path.join(self.test_dir, "evidencia_test.pdf")
        shutil.copy(self.pdf_muestra, self.pdf_temporal)
        
    def tearDown(self):
        # Remover directorio temporal
        shutil.rmtree(self.test_dir)

    def test_xref_structural_analysis(self):
        """Verifica la capacidad de auditoría estructural y reporte de cicatriz XREF."""
        resultado = XrefAnalyzer.analizar_estructura(self.pdf_temporal)
        self.assertEqual(resultado['exit_code'], 3)
        self.assertTrue(resultado['XREF_discrepancia'])
        self.assertIn("reported number of objects", resultado['stderr'])

    def test_raster_analysis_and_colorspace(self):
        """Verifica la extracción de imágenes y detección de varianza o score vectorial."""
        vec_res = RasterAnalyzer.detectar_elementos_vectoriales(self.pdf_temporal)
        self.assertIn('contiene_vectores', vec_res)
        self.assertIn('score_vectorial', vec_res)
        
        # Debe correr sin fallar
        img_res = RasterAnalyzer.analizar_imagenes(self.pdf_temporal, temp_dir=self.test_dir)
        self.assertNotIn('error', img_res)

    def test_benford_second_digit_math(self):
        """Valida que el módulo Benford procese correctamente la Ley del segundo dígito de Mebane."""
        # Datos normales simulados
        datos_aleatorios = [120, 230, 450, 670, 890, 110, 340, 560, 780, 900]
        res = BenfordAnalyzer.analizar_mebane_2bl(datos_aleatorios)
        self.assertTrue(res['suficiente_data'])
        self.assertIn('desviacion_chi2', res)

    def test_custody_tracker_hashing(self):
        """Verifica la inmutabilidad de la cadena de custodia mediante hashing SHA-256."""
        hash_calc = CustodyTracker.calcular_sha256(self.pdf_temporal)
        self.assertEqual(len(hash_calc), 64) # Largo estándar de SHA-256 en hexadecimal
        
        timestamps = CustodyTracker.obtener_timestamps_sistema(self.pdf_temporal)
        self.assertIn('fecha_creacion_sistema', timestamps)

    def test_active_anti_palantir_defense(self):
        """Valida que el protocolo Anti-Palantir mute el hash y limpie metadatos de forma efectiva."""
        hash_original = CustodyTracker.calcular_sha256(self.pdf_temporal)
        
        # Ejecutar protocolo
        res_ap = AntiPalantir.ejecutar_mitigacion(self.pdf_temporal)
        self.assertTrue(res_ap['metadata_cleaned'])
        self.assertTrue(res_ap['entity_spoofed'])
        self.assertTrue(res_ap['hash_mutated'])
        
        hash_nuevo = CustodyTracker.calcular_sha256(self.pdf_temporal)
        self.assertNotEqual(hash_original, hash_nuevo)
        self.assertEqual(res_ap['mutated_hash'], hash_nuevo)

    def test_sqlite_database_persistence(self):
        """Valida que la base de datos de custodia guarde y persista la cadena de custodia."""
        conn = database.get_connection()
        cursor = conn.cursor()
        
        # Insertar caso y evidencia de test
        cursor.execute("INSERT INTO casos (nombre, descripcion, fecha_creacion) VALUES (?, ?, ?)", 
                       ("Caso de Test", "Descripción de prueba", "2026-08-30"))
        caso_id = cursor.lastrowid
        
        cursor.execute(
            "INSERT INTO evidencias (caso_id, nombre_archivo, ruta_absoluta, sha256_original, fecha_registro) "
            "VALUES (?, ?, ?, ?, ?)",
            (caso_id, "test.pdf", self.pdf_temporal, "hash_simulado_sha256", "2026-08-30")
        )
        conn.commit()
        
        # Verificar inserción
        row = conn.execute("SELECT * FROM evidencias WHERE caso_id = ?", (caso_id,)).fetchone()
        self.assertEqual(row['nombre_archivo'], "test.pdf")
        self.assertEqual(row['estado_custodia'], "INTEGRO")
        
        conn.close()

if __name__ == '__main__':
    print("🚀 Iniciando suite de pruebas unitarias forenses...")
    unittest.main()
