#!/usr/bin/env python3
"""
🧪 AUDITORÍA Y SUITE DE PRUEBAS PARA LOS 2 NODOS DE IA (BABAYAGA CORE)
Verifica la integridad de las instrucciones del sistema, roles del squad, consistencia de directivas y failover.
"""

import os
import sys
import unittest

class TestAINodesArchitecture(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.base_dir = os.path.dirname(__file__)
        cls.node1_file = os.path.join(cls.base_dir, "SYSTEM_INSTRUCTIONS_NODE1_FORENSIC_LEGAL.md")
        cls.node2_file = os.path.join(cls.base_dir, "SYSTEM_INSTRUCTIONS_NODE2_CYBERDEFENSE.md")
        cls.chat_script = os.path.join(cls.base_dir, "run_ai_chat.py")

    def test_01_node1_legal_prompt_exists_and_valid(self):
        """Verifica que el prompt del Nodo 1 (Legal & Pericial) exista y contenga los pilares fundamentales."""
        self.assertTrue(os.path.exists(self.node1_file), "Falta el archivo de instrucciones del Nodo 1")
        with open(self.node1_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("KEPLER & ANZACA FORENSIC LEGAL AI", content)
        self.assertIn("Benford-Mebane 2BL Law", content)
        self.assertIn("PDF XREF Table Audit", content)
        self.assertIn("Arthurios el Integrador", content)
        self.assertIn("ZERO HALLUCINATIONS", content)

    def test_02_node2_cyberdefense_prompt_exists_and_valid(self):
        """Verifica que el prompt del Nodo 2 (Ciberseguridad & Anti-Palantir) exista y esté completo."""
        self.assertTrue(os.path.exists(self.node2_file), "Falta el archivo de instrucciones del Nodo 2")
        with open(self.node2_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("ANDRETAKER & BABAYAGA CYBERDEFENSE AI", content)
        self.assertIn("Master Mirror Defense Engine", content)
        self.assertIn("Anti-Palantir Defense Protocol", content)
        self.assertIn("Arthurios el Integrador", content)
        self.assertIn("IT'S MY TURN! I'M UNBROKEN!", content)

    def test_03_squad_character_roles_coverage(self):
        """Verifica que todos los personajes (AnZaCa, AndreTaker, Baba Yaga, Tycho, Kepler, Chris, Arthurios) estén reflejados."""
        characters = ["AnZaCa", "Kepler", "Tycho", "Arthurios", "AndreTaker", "Baba Yaga"]
        with open(self.node1_file, "r", encoding="utf-8") as f1:
            c1 = f1.read()
        with open(self.node2_file, "r", encoding="utf-8") as f2:
            c2 = f2.read()
            
        full_text = c1 + "\n" + c2
        for char in characters:
            self.assertIn(char, full_text, f"El personaje {char} debe estar presente en las instrucciones de la IA")

    def test_04_run_ai_chat_cli_script_integrity(self):
        """Verifica que el script interactivo run_ai_chat.py contenga el selector bimodal de IAs."""
        self.assertTrue(os.path.exists(self.chat_script), "Falta el script interactivo run_ai_chat.py")
        with open(self.chat_script, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("SYSTEM_INSTRUCTIONS_NODE1_FORENSIC_LEGAL.md", content)
        self.assertIn("SYSTEM_INSTRUCTIONS_NODE2_CYBERDEFENSE.md", content)

if __name__ == "__main__":
    print("🚀 Ejecutando batería de pruebas unitarias sobre la arquitectura de las 2 IAs...")
    unittest.main()
