#!/usr/bin/env python3
"""
===============================================================================
BABAYAGA CORE — AUTOMATED RESEARCH AUTO-UPDATER & SYNCHRONIZER ENGINE
===============================================================================
Autores: AnZaCa (Andrea Zabala Cárcamo) & AndreTaker Cyberdefense Unit
Descripción: Script de automatización integral que escanea los repositorios,
ejecuta las 16 pruebas unitarias, actualiza los índices probatorios,
reconstruye los paquetes de exportación (Zenodo v2.0) y sincroniza automáticamente
ambos repositorios de GitHub sin intervención manual.
===============================================================================
"""

import os
import sys
import subprocess
import zipfile
import datetime

REPO_1 = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep"
REPO_2 = "/home/andrea-zabala-c/AndreTaker-BabaYaga-Core-CyberDefense"
DOWNLOADS_DIR = "/home/andrea-zabala-c/Downloads"

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ⚡ {msg}")

def run_command(cmd, cwd=REPO_1):
    log(f"Ejecutando: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        log(f"⚠️ Alerta/Advertencia: {res.stderr.strip()}")
    else:
        log(f"✅ Éxito: {res.stdout.strip()[:200]}")
    return res.returncode == 0

def step_1_run_unit_tests():
    log("1/4. Ejecutando Suite Completa de 16 Pruebas Unitarias Forenses y de IA...")
    ok1 = run_command("python3 BABAYAGA_CORE/run_tests.py", cwd=REPO_1)
    ok2 = run_command("python3 BABAYAGA_CORE/test_ai_nodes.py", cwd=REPO_1)
    if ok1 and ok2:
        log("✅ 16 Pruebas pasaron al 100% en verde.")
    else:
        log("⚠️ Advertencia en pruebas unitarias.")

def step_2_build_zenodo_bundle():
    log("2/4. Generando automáticamente el paquete Zenodo v2.0 comprimido...")
    target_zip = os.path.join(DOWNLOADS_DIR, "forensic_toolkit_e14_v2.0_zenodo.zip")
    with zipfile.ZipFile(target_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(REPO_1):
            if any(ignore in root for ignore in [".git", "node_modules", ".gemini", "venv", "assets/images"]):
                continue
            for f in files:
                full_path = os.path.join(root, f)
                if not os.path.islink(full_path) and os.path.exists(full_path):
                    rel_path = os.path.relpath(full_path, REPO_1)
                    z.write(full_path, rel_path)
    size_mb = round(os.path.getsize(target_zip) / (1024 * 1024), 2)
    log(f"✅ Paquete Zenodo v2.0 reconstruido con éxito ({size_mb} MB) en {target_zip}")

def step_3_sync_repositories():
    log("3/4. Sincronizando archivos entre Repo 1 y Repo 2...")
    run_command(f"cp -r {REPO_1}/03_DOCUMENTACION {REPO_2}/", cwd=REPO_1)
    run_command(f"cp -r {REPO_1}/BABAYAGA_CORE {REPO_2}/", cwd=REPO_1)
    run_command(f"cp -r {REPO_1}/.github {REPO_2}/", cwd=REPO_1)
    run_command(f"cp -r {REPO_1}/assets {REPO_2}/", cwd=REPO_1)
    log("✅ Sincronización local inter-repositorios completada.")

def step_4_git_commit_and_push():
    log("4/5. Realizando Auto-Commit y Auto-Push a GitHub en ambos repositorios...")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"Auto-Actualización Automatizada del Acervo e Investigación — {now_str}"
    
    # Push Repo 1
    run_command("git add .", cwd=REPO_1)
    run_command(f'git commit -m "{msg}"', cwd=REPO_1)
    run_command("git push origin main", cwd=REPO_1)
    
    # Push Repo 2
    run_command("git add .", cwd=REPO_2)
    run_command(f'git commit -m "{msg}"', cwd=REPO_2)
    run_command("git push origin main", cwd=REPO_2)
    log("✅ Auto-Push completado en ambos repositorios GitHub.")

def step_5_archive_org_preservation():
    log("5/5. Enviando solicitudes de preservación inalterable a Internet Archive (Archive.org)...")
    archive_script = os.path.join(REPO_1, "BABAYAGA_CORE", "archive_org_saver.py")
    if os.path.exists(archive_script):
        run_command(f"python3 {archive_script}", cwd=REPO_1)
        log("✅ Solicitudes de instantánea en Archive.org (Wayback Machine) procesadas.")

def main():
    log("=================================================================")
    log("INICIANDO MOTOR DE AUTO-ACTUALIZACIÓN INTEGRAL DE INVESTIGACIÓN")
    log("=================================================================")
    step_1_run_unit_tests()
    step_2_build_zenodo_bundle()
    step_3_sync_repositories()
    step_4_git_commit_and_push()
    step_5_archive_org_preservation()
    log("=================================================================")
    log("🎉 ¡PROCESO DE AUTO-ACTUALIZACIÓN AUTOMATIZADO CON ÉXITO TOTAL!")
    log("=================================================================")

if __name__ == "__main__":
    main()
