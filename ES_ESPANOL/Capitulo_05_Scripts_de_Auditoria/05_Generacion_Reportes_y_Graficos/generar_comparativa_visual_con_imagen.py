#!/usr/bin/env python3
import os
import shutil

def generate_visual_comparison_with_image():
    brain_dir = "/home/andrea-zabala-c/.gemini/antigravity-ide/brain/fae50fcf-17a8-4d3a-be20-a67635cab439"
    out_dir = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
    drive_dir = "/media/andrea-zabala-c/D A T A1/segundaVuelta/ENTREGABLES_FORENSES_E14"
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(drive_dir, exist_ok=True)

    src_img = os.path.join(brain_dir, "media__1785334220881.png")
    dest_img_desktop = os.path.join(out_dir, "acta_ejemplo_caucasia_mesa5.png")
    dest_img_drive = os.path.join(drive_dir, "acta_ejemplo_caucasia_mesa5.png")
    
    if os.path.exists(src_img):
        shutil.copy(src_img, dest_img_desktop)
        shutil.copy(src_img, dest_img_drive)
        print("✅ Imagen del acta oficial copiada exitosamente a los entregables.")
        
    md_content = f"""# COMPARATIVA VISUAL Y MAPEO LADO A LADO: PRIMERA VUELTA VS. SEGUNDA VUELTA

**Objeto:** Visualización directa y didáctica del mapa sintáctico de inyecciones `/XObject` colocado en paralelo junto a la imagen real del formulario E-14.  

---

## 1. ACTA REAL VS. MAPA DE INYECCIÓN DE CAPAS SINTÁCTICAS (2ª VUELTA)

![Acta Real Caucasia Mesa 5](file://{dest_img_desktop})

```
+-----------------------------------------------------------------------------------+
| [IMAGEN REAL DEL ACTA (E-14 CAUCASIA MESA 5)] | [MAPA DE INYECCIÓN SINTÁCTICA PDF]|
+-----------------------------------------------+-----------------------------------+
|                                               |                                   |
|  [CÓDIGO DE BARRAS SUPERIOR]                  |  +-----------------------------+  |
|  710459971010102                              |  | ENCABEZADO BASE Y CÓDIGO BARRAS|  |
|                                               |  +-----------------------------+  |
|  [CÓDIGO QR - ESQUINA SUP. IZQ.]              |  | 🚨 INYECCIÓN 1: /XObject 11 0 R |  |
|                                               |  | [MATRIZ QR SUPERPUESTA]        |  |
|                                               |  +-----------------------------+  |
|                                               |                                   |
|  DEPARTAMENTO: 01 - ANTIOQUIA                 |  DEPARTAMENTO: 01 - ANTIOQUIA     |
|  MUNICIPIO: 088 - CAUCASIA                    |  MUNICIPIO: 088 - CAUCASIA        |
|  ZONA: 01 PUESTO: 04 MESA: 005                |  ZONA: 01 PUESTO: 04 MESA: 005    |
|                                               |                                   |
|  CLAVE: X 6-01-48-14 X                        |  CLAVE: X 6-01-48-14 X            |
|                                               |                                   |
|  E-11 / URNA: [2 6 1]                         |  E-11 / URNA: [2 6 1]             |
|                                               |                                   |
|  +-----------------------------------------+  |  +-----------------------------+  |
|  | CANDIDATO 1: IVÁN CEPEDA   | [1 3 5]    |  |  | 🚨 INYECCIÓN 2: /XObject 12  |  |
|  | CANDIDATO 2: ABELARDO ESP. | [1 2 1]    |  |  | [CAPA DE CASILLAS DE VOTOS] |  |
|  | VOTOS EN BLANCO            | [• • 1]    |  |  | (Montada sobre el lienzo)   |  |
|  | VOTOS NULOS                | [• • 3]    |  |  +-----------------------------+  |
|  | VOTOS NO MARCADOS          | [• • 1]    |  |                                   |
|  | SUMA TOTAL                 | [2 6 1]    |  |  ⚠️ ADVERTENCIA XREF QPDF:        |
|  +-----------------------------------------+  |  Punteros borrados a ID 14 y 15   |  |
+-----------------------------------------------+-----------------------------------+
```

---

## 2. COMPARATIVA DE DISTRIBUCIÓN: 1ª VUELTA (3 PÁGINAS) VS 2ª VUELTA (2 PÁGINAS)

```
+------------------------------------------+  +------------------------------------------+
| PRIMERA VUELTA (LIENZO LARGO 1260x3897)  |  | SEGUNDA VUELTA (LIENZO CARTA 612x1008)   |
+------------------------------------------+  +------------------------------------------+
|                                          |  |                                          |
|  [CÓDIGO QR / OBRETO ID 6]               |  |  🚨 INYECCIÓN QR: Objeto /XObject 11 0 R |
|                                          |  |                                          |
|  +------------------------------------+  |  +------------------------------------+  |
|  | CANDIDATO 1 (PÁG 1)     | [VOTOS]  |  |  | 🚨 INYECCIÓN VOTACIÓN:            |  |
|  | CANDIDATO 2 (PÁG 1)     | [VOTOS]  |  |  | Objeto /XObject 12 0 R            |  |
|  | CANDIDATO 3 (PÁG 1)     | [VOTOS]  |  |  | 1. IVÁN CEPEDA      | [1 3 5]    |  |
|  | CANDIDATO 4 (PÁG 1)     | [VOTOS]  |  |  | 2. ABELARDO ESP.    | [1 2 1]    |  |
|  +------------------------------------+  |  | TOTAL VOTACIÓN      | [2 6 1]    |  |
|                                          |  +------------------------------------+  |
|  +------------------------------------+  |                                          |
|  | CANDIDATO 5 (PÁG 2)     | [VOTOS]  |  |  ⚠️ HUELLA QPDF IDÉNTICA EN AMBAS:       |
|  | CANDIDATO 6 (PÁG 2)     | [VOTOS]  |  |  reported 15 objects != highest 13       |
|  +------------------------------------+  |                                          |
|                                          |  |                                          |
|  🚨 3ª PÁGINA: MÁSCARA / IMAGEN BLANCA   |  |                                          |
|  (Sustitución de Página en 1ra Vuelta)   |  |                                          |
+------------------------------------------+  +------------------------------------------+
```

---

## 3. CONCLUSIÓN PARA EL GRUPO DE INVESTIGACIÓN

1. **Inyección Adaptativa:** En la **1ª Vuelta**, al tener 8+ candidatos, las inyecciones se extienden a lo largo de las páginas 1 y 2, sustituyendo la página 3 con una máscara blanca. En la **2ª Vuelta**, al tener 2 candidatos, se condensa en la casilla única `/XObject 12 0 R`.
2. **Mismo Motor de Generación:** Ambas elecciones fueron procesadas por el mismo software informático, dejando la misma falla sintáctica en la tabla `xref` (**15 objetos reportados vs 13 reales**).
"""

    md_file = os.path.join(out_dir, "DIAGRAMA_COMPARATIVO_1RA_VS_2DA_VUELTA.md")
    txt_file = os.path.join(out_dir, "DIAGRAMA_COMPARATIVO_1RA_VS_2DA_VUELTA.txt")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(md_content.replace("#", "").replace("```", "").replace("![Acta Real Caucasia Mesa 5]", ""))

    os.system(f"cp -rv '{out_dir}'/DIAGRAMA_COMPARATIVO_1RA_VS_2DA_VUELTA.* '{drive_dir}'/")
    print("✅ Diagrama comparativo lado a lado con imagen real generado en Escritorio y Disco Portátil.")

if __name__ == "__main__":
    generate_visual_comparison_with_image()
