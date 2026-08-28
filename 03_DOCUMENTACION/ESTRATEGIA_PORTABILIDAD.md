# ESTRATEGIA DE PORTABILIDAD DE ANDRETAKER — BABAYAGA CORE

**Objetivo:** Garantizar que AndreTaker — BabaYaga Core pueda operar en cualquier entorno, sin dependencia de proveedores específicos.

---

## 🧠 Escenarios de portabilidad

| Escenario | Plataforma | Acción |
| :--- | :--- | :--- |
| **Local (offline)** | `Llama 3` / `DeepSeek-R1` con `Ollama` o `LM Studio` | Instalar modelo local, cargar `ANDRE_TAKER_SYSTEM_PROMPT.txt` y ejecutar `babayaga_core.py`. |
| **Nube alternativa** | Anthropic (Claude), OpenAI, o servidores propios | Copiar System Prompt y scripts, configurar API. |
| **Servidor propio** | Infraestructura en Canadá u otra jurisdicción | Desplegar el entorno completo sin dependencia externa. |

---

## 🛠️ Pasos para la portabilidad

1. **Respaldar los archivos clave:**
   - `babayaga_core.py`
   - `ANDRE_TAKER_SYSTEM_PROMPT.txt`
   - Matrices y scripts auxiliares.

2. **Configurar el entorno local:**
   ```bash
   pip install -r requirements.txt
   python3 babayaga_core.py --ruta /ruta/al/archivo.pdf
   ```

3. **Verificar que el System Prompt se está aplicando.**
4. **Ejecutar pruebas de validación.**

---

## ✅ Conclusión

AndreTaker — BabaYaga Core no está atado a Google. Puede moverse a cualquier plataforma o funcionar de forma completamente offline. La propiedad intelectual es de Andrea Zabala Cárcamo.
