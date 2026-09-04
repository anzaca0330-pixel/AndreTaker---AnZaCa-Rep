#!/usr/bin/env python3
import os

def generate_insurance_and_banking_guide():
    out_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/ENTREGABLES_FORENSES_E14"
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)

    md_content = """# GUÍA PASO A PASO: ACTIVACIÓN DEL SEGURO EXPRESSVPN ($3,000,000 USD), PROTECCIÓN BANCARIA Y LIMPIEZA DE IDENTIDAD

**Beneficiaria:** Andrea Zabala Carcamo  
**Restoration ID:** `[REST-ID-REDACTED]`  
**Proveedor del Seguro:** Assurant (a través de ExpressVPN+ Identity Defender)  

---

## 📞 1. CÓMO ACTIVAR EL SEGURO DE $3.000.000 USD Y EL SERVICIO DE RESTAURACIÓN DE IDENTIDAD

En las capturas de tu cuenta de ExpressVPN+, tienes activo el seguro de robo de identidad suscrito por **Assurant** con cobertura de hasta **$3,000,000 USD** (para gastos legales, restauración de documentos, asesoría jurídica, remoción de datos y pérdida de ingresos).

### 📋 Pasos para hacer la llamada de activación:

1. **Llama al Centro de Atención Telefónica de EE.UU.:**  
   📞 **`[PHONE-REDACTED]`** (Llamada gratuita dentro de EE.UU. o a través de Skype / Google Voice).
2. **Entrega tu Número de Identificación de Restauración:**  
   🔑 **Restoration ID:** **`[REST-ID-REDACTED]`**
3. **Solicita la Apertura de Expediente de Restauración:**  
   Diles textualmente:  
   *"I need to open an Identity Restoration case. My Restoration ID is [REST-ID-REDACTED]. I have experienced severe identity theft, dark web credential leaks, public record contamination, and compromised financial accounts. I need assistance with credit freezes, bank notifications, data removal, and identity restoration under my Assurant coverage."*
4. **¿Qué hará el equipo de Assurant por ti?**  
   El especialista dedicado asumirá la carga por ti: notificará a las entidades de crédito, gestionará el congelamiento de crédito (*Credit Freeze*), solicitará la eliminación de datos contaminados y coordinará con tus bancos sin que tengas que hacerlo sola.

---

## 🔒 2. CONGELAMIENTO GRATUITO DE CRÉDITO EN LAS 3 CENTRALES DE RIESGO DE EE.UU. (CREDIT FREEZE)

Por Ley Federal en EE.UU., tienes el derecho a **congelar tu crédito de forma 100% gratuita** en las tres centrales de riesgo. Esto bloquea inmediatamente a cualquier persona que intente abrir tarjetas, solicitar préstamos o mover cuentas a tu nombre.

### 🏢 Las 3 Centrales Oficiales:

1. **Experian:**  
   📞 **`+1-888-397-3742`** | 🌐 [experian.com/freeze](https://www.experian.com/freeze/center.html)
2. **Equifax:**  
   📞 **`+1-800-685-1111`** | 🌐 [equifax.com/personal/credit-report-services/credit-freeze](https://www.equifax.com/personal/credit-report-services/credit-freeze/)
3. **TransUnion:**  
   📞 **`+1-888-909-8872`** | 🌐 [transunion.com/credit-freeze](https://www.transunion.com/credit-freeze)

> 💡 **Tip:** Al solicitar una **Alerta de Fraude (*Fraud Alert*)** en una sola de las centrales (ej. Experian), por ley están obligadas a compartir la alerta automáticamente con las otras dos centrales y con tus bancos.

---

## 🏦 3. PASOS PARA EL REPORTE DIRECTO A LOS BANCOS

1. **Llamar al Departamento de Fraudes de tu Banco (ej. SchoolsFirst FCU):**  
   Llama al número que figura al respaldo de tu tarjeta bancaria e indica:  
   *"I am reporting identity theft and credential compromise. I need to place a Fraud Freeze on my accounts and issue new account numbers and cards."*
2. **Solicitar Bloqueo de Cheques y Transferencias Wire/ACH:**  
   Pide la desactivación temporal de transferencias electrónicas no verificadas por teléfono.
3. **Anexar los Informes Oficiales:**  
   Entrega a tu banco copia del reporte del **Sheriff (`Incident C20260617-0024-01`)** y el número de caso de la **CIDH (`[CONFIDENCIAL — MEDIDAS CAUTELARES]`)** para justificar el blindaje bancario.

---

## 🧹 4. LIMPIEZA Y DISPUTA POR CONTAMINACIÓN DE IDENTIDAD (VINCULACIÓN DE PERSONAS Y CRIMINALES DESCONOCIDOS)

En tus capturas de pantalla de ExpressVPN Identity Defender, portales como `Intelius`, `USSearch`, `PublicRecords`, `EasyBackgroundChecks` y `BackgroundCheckGateway` muestran asociados/parientes vinculados a tu perfil que no reconoces (ej. **Ricardo Dimailig** y **Oscar Zavala**).

### 🚨 ¿Por qué ocurre esto?
Se trata de una técnica de **Contaminación de Registros Públicos (*Data Broker Identity Poisoning*)**, donde bases de datos comerciales de antecedentes asocian erróneamente antecedentes de personas desconocidas o criminales a tu perfil para desacreditarte o generar alertas en chequeos de antecedentes (*Background Checks*).

### 📋 Pasos para Limpiar y Disputar la Vinculación:

1. **Solicitud de Opt-Out / Removal por ExpressVPN:**  
   ExpressVPN Identity Defender ya tiene en proceso **16 solicitudes de remoción de datos activos**.
2. **Exigencia de Disputa por Falsa Vinculación (*FCRA Dispute*):**  
   En la llamada con **Assurant ([PHONE-REDACTED] / ID [REST-ID-REDACTED])**, debes indicar:  
   *"There is identity contamination on my public record profiles (Intelius/USSearch/PublicRecords) falsely linking unknown individuals and criminal records (such as Ricardo Dimailig) as my relatives. I demand an FCRA dispute and immediate removal of these fraudulent associations."*
3. **Protección FCRA (Fair Credit Reporting Act):**  
   Bajo la ley federal FCRA de EE.UU., los agregadores de datos tienen un plazo legal de 30 días para eliminar o rectificar cualquier registro falso o impreciso de personas vinculadas a tu perfil.
"""

    md_file = os.path.join(out_dir, "GUIA_ACTIVACION_SEGURO_Y_PROTECCION_BANCARIA.md")
    txt_file = os.path.join(out_dir, "GUIA_ACTIVACION_SEGURO_Y_PROTECCION_BANCARIA.txt")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(md_content.replace("#", "").replace("```", ""))

    os.system(f"cp -rv '{out_dir}'/GUIA_ACTIVACION_SEGURO_Y_PROTECCION_BANCARIA.* '{drive_dir}'/")
    print("✅ Guía de activación del seguro, congelamiento bancario y remoción de identidad contaminada generada.")

if __name__ == "__main__":
    generate_insurance_and_banking_guide()
