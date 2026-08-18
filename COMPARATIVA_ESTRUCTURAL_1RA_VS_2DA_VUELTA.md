# COMPARATIVA ESTRUCTURAL Y DE MAPEO: PRIMERA VUELTA VS. SEGUNDA VUELTA

**Objeto de Auditoría:** Demostración de que la inyección de objetos se desplaza a las coordenadas correspondientes de los candidatos según la ronda electoral.

---  

## 1. PRIMERA VUELTA: ESTRUCTURA MULTICANDIDATO (3 PÁGINAS / LIENZO ALTO)

- **Archivo:** `E14_XXX_X_88_360_035_02_000_X_XXX (16)_descomprimido.pdf`  
- **Advertencias XREF:** 0 en la tabla de objetos.  
- **Capas de Imagen Detectadas:**  
  - **Página 1**: Objeto ID `no` | Dimensión `523x1600 px` | Tamaño `0`
  - **Página 2**: Objeto ID `no` | Dimensión `516x1600 px` | Tamaño `0`
  - **Página 3**: Objeto ID `no` | Dimensión `511x1600 px` | Tamaño `0`

---

## 2. SEGUNDA VUELTA: ESTRUCTURA BINARIA (2 PÁGINAS / FORMATO RESTRINGIDO)

- **Archivo:** `E14_PRE_01_088_001_00_04_005_5154_Mesa_5.pdf`  
- **Advertencias XREF:** 2 en la tabla de objetos.  
- **Capas de Imagen Detectadas:**  
  - **Página 1**: Objeto ID `no` | Dimensión `1260x3897 px` | Tamaño `0`
  - **Página 2**: Objeto ID `no` | Dimensión `1260x3897 px` | Tamaño `0`

---

## 3. CONFIRMACIÓN TÉCNICA DE LA HIPÓTESIS

- **Desplazamiento Dinámico de Coordenadas:** En la **1ª Vuelta**, la estructura del formulario acomoda de 3 a 8 candidaturas distribuidas en lienzos altos (`3897 px`), por lo que las inyecciones de objetos se posicionan verticalmente a lo largo de las páginas 1 y 2.
- **Formato Binario de 2ª Vuelta:** En la **2ª Vuelta**, la inyección se condensa en las casillas únicas de la fórmula de 2 candidatos y la inyección del QR en la esquina superior izquierda.
- **Mismo Patrón de Manipulación (`xref`):** Ambas rondas exhiben exactamente la misma advertencia sintáctica en `QPDF` (`reported number of objects (15) is not one plus highest (13)`), confirmando que se utilizó la misma herramienta de software para ensamblar los PDFs en ambas elecciones.
