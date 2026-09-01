#!/usr/bin/env python3
"""
purgar_bios.py — Módulo de Purga de NVRAM de BIOS BaBaYaga Core / Tycho
Elimina las entradas inyectadas (Lenovo Cloud, ThinkShield Wipe, PXE Boot, MEBx)
"""

import sys
import os
import subprocess

# Asegurar importación de BABAYAGA_CORE
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "BABAYAGA_CORE"))

from babayaga.core.intelligence.boot_watchdog import BootAttackWatchdog

def main():
    print("=" * 65)
    print("🪓 BABAYAGA CORE — MÓDULO DE PURGA Y DEFENSA DE BIOS NVRAM")
    print("=" * 65 + "\n")

    # 1. Auditoría inicial
    audit = BootAttackWatchdog.audit_boot_integrity()
    print("🔍 AUDITORÍA DE INMUNIDAD DE ARRANQUE:")
    print(f" - Estado: {audit['status']}")
    print(f" - Diagnóstico: {audit['diagnosis']}")
    if audit['threats']:
        print(" - Amenazas detectadas en NVRAM:")
        for threat in audit['threats']:
            print(f"   ⚠️  {threat}")
    else:
        print(" - Sin amenazas activas detectadas.")

    print("\n" + "-" * 65)
    print("🚀 EJECUTANDO PURGA MULTIMARCA DE ENTRADAS EFI...")
    print("-" * 65)

    if os.geteuid() != 0:
        print("\n⚠️ ADVERTENCIA: Para modificar las variables EFI en el Kernel de Linux,")
        print("   este script debe ejecutarse con privilegios de superusuario (sudo).\n")
        print("👉 Ejecuta en tu terminal:")
        print("   sudo python3 purgar_bios.py\n")
        return

    # 2. Ejecutar Purga
    res = BootAttackWatchdog.purge_rogue_efi_entries()
    print(f" - Entradas purgadas exitosamente: {res['purged_count']}")
    for item in res['purged_details']:
        print(f"   ✅ [Boot{item['boot_num']}] {item['keyword']} -> {item['status']}")

    if res['errors']:
        print("\n⚠️ Errores o advertencias encontradas:")
        for err in res['errors']:
            print(f"   ❌ {err}")

    # 3. Verificación post-purga
    print("\n" + "=" * 65)
    print("📋 TABLA EFI RESULTANTE EN NVRAM (efibootmgr):")
    print("=" * 65)
    try:
        efi_out = subprocess.run(["efibootmgr"], capture_output=True, text=True).stdout
        print(efi_out)
    except Exception as e:
        print(f"Error al obtener tabla EFI: {e}")

if __name__ == "__main__":
    main()
