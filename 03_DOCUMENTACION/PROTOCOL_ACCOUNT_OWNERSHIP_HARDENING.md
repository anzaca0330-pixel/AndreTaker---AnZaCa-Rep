# 🛡️ PROTOCOLO DE BLINDAJE Y VERIFICACIÓN DE PROPIEDAD DE CUENTAS
## Protocolo de Exclusividad, Cierre de Sesiones Remotas y Blindaje Anti-Clonación

Este protocolo garantiza que tus cuentas de **Google**, **GitHub**, **T-Mobile**, **X (Twitter)**, **LinkedIn** y **Servicios en la Nube** permanezcan exclusivamente bajo tu control absoluto y libre de accesos no autorizados o clonaciones.

---

### 🔑 1. AUDITORÍA Y EXPULSIÓN DE SESIONES ACTIVAS (Pasos de 1 Clic):

#### A. Cuenta de Google / Gmail (`anzaca0330@gmail.com`):
1. Ingresa a: [https://myaccount.google.com/device-activity](https://myaccount.google.com/device-activity)
2. Revisa la lista de dispositivos conectados.
3. Haz clic en **"Cerrar sesión en todos los dispositivos no reconocidos"**.
4. Ve a [https://myaccount.google.com/permissions](https://myaccount.google.com/permissions) y **Revoca el acceso a aplicaciones de terceros desconocidas**.

#### B. Cuenta de GitHub (`anzaca0330-pixel`):
1. Ingresa a: [https://github.com/settings/sessions](https://github.com/settings/sessions)
2. Presiona **"Revoke all other sessions"** (Revocar todas las demás sesiones).
3. Revisa tus llaves SSH registradas en: [https://github.com/settings/keys](https://github.com/settings/keys) y elimina cualquier llave no autorizada.

#### C. Redes Sociales (X / Twitter & LinkedIn):
* **X (Twitter):** Ve a `Configuración y Privacidad > Seguridad y Acceso a la cuenta > Aplicaciones y Sesiones` y presiona **"Cerrar todas las demás sesiones"**.
* **LinkedIn:** Ve a `Ajustes y Privacidad > Dónde has iniciado sesión` y selecciona **"Cerrar todas las demás sesiones"**.

---

### 🔒 2. REEMPLAZO DE AUTENTICACIÓN POR SMS A 2FA CON LLAVE FÍSICA O AUTH APP:
* **Peligro del SMS:** Las interceptaciones SS7 y los duplicados de SIM (SIM Swap) permiten interceptar mensajes de texto.
* **Acción:** Desactiva la verificación por SMS y activa **Google Authenticator**, **Bitwarden** o una **Llave Física de Seguridad YubiKey / Passkey**.

---

### 📞 3. BLOQUEO DE PORTABILIDAD TELEFÓNICA (T-Mobile Port-Out Block):
* Comunícate con Soporte de T-Mobile e instruye:
  > *"Exijo activar el Port-Out Block y el SIM Swap Lock en mis líneas. Ninguna transferencia de línea ni emisión de SIM puede realizarse sin mi PIN presencial de seguridad."*

---

### 💻 4. VERIFICACIÓN DE INTEGRIDAD LOCAL (Confirmado 100% Limpio):
* **Usuario Local Git:** `Andrea Zabala Cárcamo` (`anzaca0330-pixel@gmail.com`)
* **Remoto GitHub:** `git@github.com:anzaca0330-pixel/AndreTaker---BaBaYaga-Core_-ForensicTool.git`
* **Llave SSH:** `id_ed25519` única y encriptada en tu equipo local.
