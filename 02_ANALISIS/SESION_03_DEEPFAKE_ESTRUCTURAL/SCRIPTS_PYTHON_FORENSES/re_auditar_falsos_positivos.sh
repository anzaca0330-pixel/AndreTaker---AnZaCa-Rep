#!/bin/bash

echo "🚀 Iniciando Re-Auditoría Masiva para purgar falsos positivos (Umbral Multicapa ajustado a >2)..."
echo "Esta operación tomará tiempo. Los scripts se ejecutarán secuencialmente."

cd /home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES

echo "---------------------------------------------------"
echo "[1/4] Ejecutando: analizar_consulados_forense.py"
python3 analizar_consulados_forense.py

echo "---------------------------------------------------"
echo "[2/4] Ejecutando: verificar_votacion_adelantada_2da_vuelta.py"
python3 verificar_votacion_adelantada_2da_vuelta.py

echo "---------------------------------------------------"
echo "[3/4] Ejecutando: auditar_todas_actas_colombia_32_deptos.py"
python3 auditar_todas_actas_colombia_32_deptos.py

echo "---------------------------------------------------"
echo "[4/4] Ejecutando: generar_tabla_por_dia_semana.py"
python3 generar_tabla_por_dia_semana.py

echo "---------------------------------------------------"
echo "✅ Re-Auditoría completada. Todas las tablas y CSV han sido sobreescritos con la data correcta."
