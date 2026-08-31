import os
import sys
import unittest
import tempfile
import shutil
import sqlite3

# Insertar el directorio principal de BABAYAGA_CORE al path para asegurar importaciones
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from babayaga.core.forensics.xref import XrefAnalyzer
from babayaga.core.forensics.raster import RasterAnalyzer
from babayaga.core.forensics.spoofing import SpoofingDetector
from babayaga.core.intelligence.telephony import PhoneSpoofingDetector
from babayaga.core.intelligence.boot_watchdog import BootAttackWatchdog
from babayaga.core.custody import CustodyTracker
from babayaga.core.intelligence.mitigation import AntiPalantir
from babayaga.core.intelligence.network import NetworkAuditor
from babayaga.core.forensics.statistics import BenfordAnalyzer
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

    def test_qr_spoofing_detection(self):
        """Verifica la detección de firmas inyectadas y suplantación de QR (QR Spoofing)."""
        res = SpoofingDetector.audit_qr_spoofing(self.pdf_temporal)
        self.assertEqual(res['status'], 'success')
        self.assertIn('qr_spoofing_detected', res)
        self.assertIn('vector_overwrite_score', res)

    def test_esim_hijacking_detection(self):
        """Valida que el módulo de telefonía detecte intrusiones y líneas clónicas en registros."""
        # Crear un archivo de registro CDR simulado en el directorio temporal
        cdr_temporal = os.path.join(self.test_dir, "tmobile_cdr.txt")
        with open(cdr_temporal, "w", encoding="utf-8") as f:
            f.write("Call on Aug 09 from 414-4130 to 8360 (duration 15 min)\n")
            f.write("Outgoing call to Colombia +57 301 000 0000 from 8360\n")
            
        res = PhoneSpoofingDetector.audit_telephony_logs(cdr_temporal)
        self.assertEqual(res['status'], 'success')
        self.assertTrue(res['sim_hijacking_detected'])
        self.assertGreaterEqual(res['hijack_score'], 15)

    def test_benford_second_digit_math(self):
        """Valida que el módulo Benford procese correctamente la Ley del segundo dígito de Mebane."""
        # Datos normales simulados
        datos_aleatorios = [120, 230, 450, 670, 890, 110, 340, 560, 780, 900]
        res = BenfordAnalyzer.analizar_mebane_2bl(datos_aleatorios)
        self.assertTrue(res['suficiente_data'])
        self.assertIn('desviacion_chi2', res)

    def test_benford_first_digit_math(self):
        """Valida que el módulo Benford procese correctamente la Ley del primer dígito."""
        datos_aleatorios = [12, 23, 45, 67, 89, 11, 34, 56, 78, 90]
        res = BenfordAnalyzer.analizar_benford_1bl(datos_aleatorios)
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

        # Blindaje de puertos de hardware (USB/SATA Power Cut Shield)
        res_lock = AntiPalantir.lock_hardware_ports_power()
        self.assertEqual(res_lock['status'], 'success')

    def test_mirror_defense_engine(self):
        """Valida que el Núcleo de Protección Espejo v3.0 aprenda, sintetice reglas al vuelo y ejecute demonios de actualización."""
        from mirror_defense_engine import MasterMirrorDefenseEngine
        engine = MasterMirrorDefenseEngine(quarantine_dir="BABAYAGA_CORE/quarantine")
        
        # 1. Regla Zero-Day al vuelo
        rule = engine.analyze_payload_anomaly(b"TEST_PAYLOAD_WITH_PEGASUS_AND_/XObject_UNSEEN_VECTOR")
        self.assertTrue(rule['rule_id'].startswith("MIRROR-RULE-"))
        self.assertEqual(rule['status'], "INMUNIZADO")
        self.assertIn("DETECCION_VECTOR_PEGASUS_ZERO_CLICK", rule['anomalies'])

        # 2. Auditoría de puertos
        port_res = engine.audit_unauthorized_ports()
        self.assertEqual(port_res['status'], "SEGURO")

        # 3. Protección contra robo de identidad
        id_res = engine.protect_against_identity_theft("Usuario demo id 1234567890 correo test@domain.com")
        self.assertEqual(id_res['identity_shield'], "PROTEGIDO")
        self.assertIn("[ID-PERSONAL-REDACTADO]", id_res['sanitized_content'])

        # 4. Heurística Anti-Spyware
        spy_res = engine.scan_spyware_heuristics(["keylogger_service", "screen_grabber"])
        self.assertEqual(spy_res['shield_status'], "NEUTRALIZADO")

        # 5. Verificación Anti-MITM DNS
        dns_res = engine.verify_network_trust_and_dns("localhost")
        self.assertEqual(dns_res['mitm_shield'], "ACTIVO")

        # 6. Demon de actualización al vuelo (Hot-Reload Watcher Daemon)
        engine.start_realtime_hot_reload_watcher(interval_seconds=1)
        self.assertTrue(engine.hot_reload_active)
        engine.stop_realtime_hot_reload_watcher()

    def test_sqlite_database_persistence(self):
        """Valida que la base de datos de custodia guarde y persista la cadena de custodia."""
        conn = database.get_connection()
        cursor = conn.cursor()
        
        # Insertar caso y evidencia de test
        import time
        test_case_name = f"Caso de Test {time.time()}"
        cursor.execute("INSERT INTO casos (nombre, descripcion, fecha_creacion) VALUES (?, ?, ?)", 
                       (test_case_name, "Descripción de prueba", "2026-08-30"))
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

    def test_network_and_vpn_audit(self):
        """Verifica que el auditor de red detecte la configuración VPN e inspeccione puertos localmente."""
        res_vpn = NetworkAuditor.detect_active_vpn()
        self.assertIn('vpn_active', res_vpn)
        self.assertIn('status', res_vpn)
        
        puertos = NetworkAuditor.audit_listening_ports()
        self.assertIsInstance(puertos, list)

        res_ss7 = NetworkAuditor.detect_ss7_imsi_intercept()
        self.assertIn('intercept_detected', res_ss7)
        self.assertIn('status', res_ss7)

    def test_boot_attack_watchdog_logging(self):
        """Valida que el guardián de arranque detecte inyecciones EFI en BIOS y genere log forense."""
        res_boot = BootAttackWatchdog.audit_boot_integrity()
        self.assertIn('status', res_boot)
        self.assertIn('boot_attack_detected', res_boot)
        self.assertIn('grub_cfg_sha256', res_boot)

if __name__ == '__main__':
    print("🚀 Iniciando suite de pruebas unitarias forenses...")
    unittest.main()
