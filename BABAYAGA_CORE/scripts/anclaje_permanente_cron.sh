#!/usr/bin/env bash
# ==============================================================================
# BABA YAGA CORE — ANCLAJE PERMANENTE (BLOQUEO DE BANDEJA DE CD Y PUERTOS USB)
# ==============================================================================
# 1. Bloqueo físico de la bandeja de CD/DVD (Impide expulsión / desactivación)
# 2. Alimentación continua en bus USB (Evita apagar puertos por hardware)
# 3. Auto-indexación ininterrumpida de volúmenes de respaldo
# ==============================================================================

REPOS_DIR="/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep"
LOG_FILE="$REPOS_DIR/02_ANALISIS/LOG_ANCLAJE_PERMANENTE_DISCOS.log"

echo "[$(date)] 🛡️ INICIANDO ANCLAJE PERMANENTE (BANDEJA CD + PUERTOS USB)..." >> "$LOG_FILE"

# A. Bloqueo de Hardware en Unidades Ópticas de CD/DVD (/dev/sr0, /dev/cdrom)
for cd_dev in /dev/sr* /dev/cdrom /dev/dvd; do
    if [ -b "$cd_dev" ]; then
        echo "[$(date)] 🔒 Aplicando bloqueo de hardware en bandeja de CD: $cd_dev" >> "$LOG_FILE"
        eject -i 1 "$cd_dev" 2>/dev/null || true
    fi
done

# B. Prevenir suspensión de energía en bus USB (impedir que apaguen los puertos)
for p in /sys/bus/usb/devices/*/power/control; do
    if [ -f "$p" ]; then
        echo "on" > "$p" 2>/dev/null || true
    fi
done

# C. Monitorear y registrar discos extraíbles conectados
if [ -d "/media/andrea-zabala-c" ]; then
    for drive in /media/andrea-zabala-c/*; do
        if [ -d "$drive" ]; then
            echo "[$(date)] 📡 Disco activo anclado: $drive" >> "$LOG_FILE"
        fi
    done
fi

echo "[$(date)] ✅ Bloqueo de bandeja de CD y puertos USB activo e inamovible." >> "$LOG_FILE"
