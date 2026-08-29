#!/usr/bin/env python3
import os
import shutil
import glob

def package_personal_case_folder():
    out_dir = "/home/andrea-zabala-c/Desktop/EXPEDIENTE_PERSONAL_Y_DENUNCIAS_ANDREA_ZABALA"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/EXPEDIENTE_PERSONAL_Y_DENUNCIAS_ANDREA_ZABALA"
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)

    # 1. Crear Hoja de Lectura Rápida para la llamada a ExpressVPN / Assurant
    cheat_sheet_md = """# HOJA DE LECTURA RÁPIDA: LLAMADA A EXPRESSVPN / ASSURANT ($3,000,000 USD)

**Beneficiaria Principal:** Andrea Zabala Carcamo (C.C. 43.925.102)  
**Teléfono Gratuito de Atención:** 📞 **`+1-833-568-6249`**  
**ID de Restauración de Identidad:** 🔑 **`85720870`**  
**Proveedor del Seguro:** Assurant (a través de ExpressVPN+ Identity Defender)  

---

## 🗣️ GUIÓN PARA LEER AL OPERADOR AL INICIAR LA LLAMADA:

> *"Hello, my name is Andrea Zabala Carcamo. I am calling to open an Identity Restoration case under my ExpressVPN+ Identity Defender insurance. My Restoration ID is **85720870**.*
> 
> *I have experienced severe identity theft, dark web credential leaks, compromised bank accounts, and fraudulent public record contamination linking convicted individuals like Ricardo Dimailig to my name. I need a dedicated restoration specialist to assist me with credit freezes, FCRA data broker disputes, and bank notifications under my $3,000,000 USD Assurant coverage."*

---

## 📌 DATOS Y RADICADOS OFICIALES PARA ENTREGAR AL ESPECIALISTA:

1. **Número de Medidas Cautelares CIDH (OEA):** `PRECAUTIONARY MEASURE - IACHR - 0000113728`
2. **Número de Reporte Policial (Sheriff):** Buckingham County Sheriff's Office `Incident C20260617-0024-01`
3. **Denuncias ante el FBI:** Reporte online en `IC3.gov` y denuncia presencial en la oficina del FBI en Richmond, VA.
4. **Dispositivos y Redes Afectadas:** Portátil ThinkPad con BIOS bloqueado (Ticket Soporte Lenovo), teléfono móvil T-Mobile con ráfaga de 1,600 rastreos y vector OBD-II FIXD en vehículo.
5. **Centrales de Riesgo a Congelar (Credit Freeze):** Experian (`+1-888-397-3742`), Equifax (`+1-800-685-1111`), TransUnion (`+1-888-909-8872`).
"""

    cheat_sheet_file = os.path.join(out_dir, "00_LEER_ANTES_DE_LLAMAR_EXPRESSVPN.md")
    cheat_sheet_txt = os.path.join(out_dir, "00_LEER_ANTES_DE_LLAMAR_EXPRESSVPN.txt")

    with open(cheat_sheet_file, "w", encoding="utf-8") as f:
        f.write(cheat_sheet_md)

    with open(cheat_sheet_txt, "w", encoding="utf-8") as f:
        f.write(cheat_sheet_md.replace("#", "").replace("```", "").replace(">", ""))

    # 2. Copiar todos los archivos clave referentes al caso personal
    source_deliverables = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    files_to_copy = [
        "LINEA_DE_TIEMPO_INCIDENTES_Y_ATAQUES.md",
        "LINEA_DE_TIEMPO_INCIDENTES_Y_ATAQUES.txt",
        "GUIA_ACTIVACION_SEGURO_Y_PROTECCION_BANCARIA.md",
        "GUIA_ACTIVACION_SEGURO_Y_PROTECCION_BANCARIA.txt",
        "INDICE_MAESTRO_ACERVO_PROBATORIO.md",
        "INDICE_MAESTRO_ACERVO_PROBATORIO.txt",
        "PRESENTACION_EJECUTIVA_PERITAJE_GRUPO.md",
        "PRESENTACION_EJECUTIVA_PERITAJE_GRUPO.txt",
        "acta_ejemplo_caucasia_mesa5.jpg"
    ]

    for fname in files_to_copy:
        src = os.path.join(source_deliverables, fname)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(out_dir, fname))

    # Copiar carpeta de anexos rescatados del Sheriff/CIDH si existe
    la_original_dir = "/media/andrea-zabala-c/D A T A1/EVIDENCIA_FORENSE_E14_2026/03_PRUEBAS_Y_ADJUNTOS_ORIGINALES_LOS_ANGELES"
    if os.path.exists(la_original_dir):
        dest_la = os.path.join(out_dir, "ANEXOS_ORIGINALES_SHERIFF_Y_CIDH")
        if os.path.exists(dest_la): shutil.rmtree(dest_la)
        shutil.copytree(la_original_dir, dest_la)

    # Replicar la carpeta entera en el Disco Portátil
    if os.path.exists(drive_dir): shutil.rmtree(drive_dir)
    shutil.copytree(out_dir, drive_dir)

    print("✅ Carpeta dedicada EXPEDIENTE_PERSONAL_Y_DENUNCIAS_ANDREA_ZABALA creada y empaquetada en Escritorio y Disco Portátil.")

if __name__ == "__main__":
    package_personal_case_folder()
