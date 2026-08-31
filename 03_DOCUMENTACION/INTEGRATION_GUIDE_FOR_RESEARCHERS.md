# 🔌 GUÍA DE INTEGRACIÓN RÁPIDA PARA INVESTIGADORES & DESARROLLADORES DE IA
## Quick Integration Guide for Researchers & AI Developers

Si eres un investigador, auditor de datos o desarrollador de IA y deseas integrar **BaBaYaga Core** a tus propios agentes, pipelines o scripts de análisis, aquí tienes las **3 formas inmediatas de integración**:

---

### 🐍 1. Instalación en 1 Línea como Paquete de Python (Python Package):

Puedes instalar e importar las bibliotecas forenses directamente en tu entorno:

```bash
pip install git+https://github.com/anzaca0330-pixel/AndreTaker-BabaYaga-Core-CyberDefense.git
```

#### Ejemplo de Uso en tu propio código Python:

```python
# Importar módulos forenses de BaBaYaga Core
from babayaga.core.custody import verify_sha256_custody
from babayaga.core.forensics.statistics import test_benford_2bl

# 1. Verificar custodia SHA-256 de un documento PDF
hash_val, is_valid = verify_sha256_custody("tu_documento.pdf")
print(f"🔒 Hash SHA-256: {hash_val} | Válido: {is_valid}")

# 2. Ejecutar prueba de Benford 2BL sobre tus propios datos
res = test_benford_2bl([12, 14, 18, 25, 34, 52, 91])
print(f"📊 Z-Score: {res['z_score']} | p-value: {res['p_value']}")
```

---

### 🤖 2. Cargar las Instrucciones del Sistema en tu propio Agente de IA (Gemini / OpenAI / Claude):

Para integrar la memoria, autoría y rigor de **BaBaYaga Core** a tu propio bot o sub-agente:

1. **Para Peritaje Legal & Auditoría de Datos:**  
   Copia el contenido de 👉 [SYSTEM_INSTRUCTIONS_NODE1_FORENSIC_LEGAL.md](file:///home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/BABAYAGA_CORE/SYSTEM_INSTRUCTIONS_NODE1_FORENSIC_LEGAL.md) en el campo *System Instructions* o *Prompt del Sistema* de tu modelo.

2. **Para Ciberseguridad & Autodefensa Anti-Palantir:**  
   Copia el contenido de 👉 [SYSTEM_INSTRUCTIONS_NODE2_CYBERDEFENSE.md](file:///home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/BABAYAGA_CORE/SYSTEM_INSTRUCTIONS_NODE2_CYBERDEFENSE.md).

---

### 🌐 3. Integración por API REST Local:

Ejecuta el servidor API local de BaBaYaga Core en tu equipo:

```bash
python3 BABAYAGA_CORE/babayaga/api/server.py
```

Tu agente o aplicación web puede consultar los endpoints localmente en `http://localhost:8000/api/v1/audit`.
