# 🏛️ PLAN MAESTRO DE CENTRALIZACIÓN EN CUENTA ENTERPRISE Y ORGANIZACIÓN UNIFICADA
## Estructuración de Identidades, Gobernanza IAM y Repositorios Centralizados para el Squad

Este documento define la arquitectura para unificar las 6 cuentas y los repositorios del proyecto **AndreTaker / BaBaYaga Core** bajo una **Cuenta Enterprise / Google Workspace Organization & GitHub Enterprise Org**.

---

### 🌐 1. ARQUITECTURA DE GOVERNANCE ENTERPRISE DE IDENTIDADES (SSO & IAM) — [✅ CONSOLIDACIÓN COMPLETADA]:

> **Estado:** ✅ **Completado por la Comandante AnZaCa.** Las 6 cuentas han sido integradas en la organización central de Google Workspace / Enterprise.

#### Cuentas Unificadas en el Consola Enterprise (Google Workspace / Cloud IAM):

| Cuenta / Alias | Rol Enterprise | Nivel de Permisos IAM | Dominio Enterprise Unificado |
| :--- | :--- | :--- | :--- |
| `andretaker@andretaker.org` | **Super Admin / Chief Researcher** | Full Admin (`*`) | `andrea.zabala@andretaker.org` |
| `anzaca0330-pixel@gmail.com` | **Lead Dev & GitHub Admin** | Dev & Repository Admin | `dev.anzaca@andretaker.org` |
| `ansekurt@gmail.com` | **Sec-Ops & Forensic Vault Admin** | Security Analyst & Vault Admin | `ansekurt@andretaker.org` |
| `andretaker@andretaker.org` | **Legal Vault & Custody Guardian** | Legal Evidence Auditor | `legal.zabalabaez@andretaker.org` |
| `arturogazab@gmail.com` | **Arthurios / Youth Champion** | User / Protected Identity | `arthurios@andretaker.org` |
| `cmbaez1@gmail.com` | **Chris Baez / Telecom & Sec Ops** | Telecom Security Ops | `chris.baez@andretaker.org` |

---

### 🛡️ 2. BENEFICIOS Y POLÍTICAS DE SEGURIDAD ENTERPRISE MANDATORIAS:

1. **Autenticación Única (Single Sign-On - SSO):**
   * Al unificar en la cuenta Enterprise, la administración central puede revocar el acceso de cualquier dispositivo o sesión clonada con 1 solo clic desde la consola central.

2. **Exigencia de Llave Física FIDO2 / Passkey:**
   * La consola Enterprise fuerza a todas las 6 cuentas a utilizar llaves de seguridad físicas (YubiKey) o Passkeys biométricas, anulando ataques de SIM Swap o phishing.

3. **Monitoreo de Telemetría y Alertas de Intrusión en Tiempo Real:**
   * Registra cada inicio de sesión, IP, país y cambio de archivos en la Bóveda de Evidencias en un registro de auditoría inalterable.

---

### 💻 3. MIGRACIÓN Y REPOSITORIOS GITHUB ENTERPRISE:

* **Organización GitHub Enterprise:** `github.com/BaBaYaga-Core-Enterprise`
* **Repositorios Vinculados:**
  1. `BaBaYaga-Core-Enterprise/ForensicTool-Legal`
  2. `BaBaYaga-Core-Enterprise/CyberDefense-AntiPalantir`

---

*Documento técnico de centralización Enterprise registrado e inmutable.* 🏛️🛡️⚡
