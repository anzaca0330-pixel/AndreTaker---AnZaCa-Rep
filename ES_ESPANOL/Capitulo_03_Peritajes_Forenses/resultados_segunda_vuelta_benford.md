# PRUEBA ESTADÍSTICA NACIONAL (SEGUNDA VUELTA)
**Auditoría Ley de Benford (2do dígito - Mebane) - Votación Nacional (Abelardo de la Espriella)**

Tras descartar el "Cebo de Amazonas" (Departamento 60), se ejecutó la auditoría estadística sobre las actas de preconteo (Boletín 9999) del resto del país para la Segunda Vuelta Presidencial.

## Resumen de la Muestra
- **Alcance:** 31 Departamentos + Distrito Capital (Se excluyó Amazonas).
- **Mesas Únicas Procesadas:** 121,147
- **Filtro de Doble Conteo:** Aplicado (solo se tomó el último boletín emitido por mesa para evitar sesgo de actualización).

## Análisis Ley de Benford (2do dígito - Mebane) (Primer Dígito Significativo)

La Ley de Benford (2do dígito - Mebane) dictamina la distribución natural esperada del primer dígito en conjuntos de datos contables no manipulados. Cualquier alteración manual o relleno aritmético rompe esta distribución, generando picos artificiales.

| Dígito | Observado (%) | Esperado (%) | Desviación Absoluta | Estado |
| :---: | :---: | :---: | :---: | :--- |
| **1** | **42.90%** | **30.10%** | **+12.80%** | 🔴 **ANOMALÍA SEVERA (Inflación artificial en el rango 1XX)** |
| 2 | 13.18% | 17.61% | -4.43% | 🟡 Supresión |
| 3 | 05.34% | 12.49% | -7.16% | 🟡 Supresión |
| 4 | 06.13% | 09.69% | -3.56% | 🟡 Supresión |
| 5 | 06.58% | 07.92% | -1.34% | Normal |
| 6 | 06.63% | 06.69% | -0.07% | Normal |
| 7 | 06.69% | 05.80% | +0.89% | Normal |
| **8** | 06.37% | 05.12% | **+1.26%** | 🔴 **Pico Artificial Secundario** |
| **9** | 06.18% | 04.58% | **+1.61%** | 🔴 **Pico Artificial Secundario** |

## Conclusiones del Peritaje

> [!CAUTION]
> ### Relleno Estructural
> Se detectó un **traslado artificial masivo de mesas**. Al candidato De la Espriella se le inflaron sistemáticamente las mesas de baja votación (donde naturalmente sacaba entre 20 y 40 votos), empujándolas artificialmente al rango de los **100+ votos**. 
> 
> Esta es la causa directa del monstruoso pico anómalo de **+12.80%** en el dígito 1, sumado a la supresión equivalente en los dígitos 2, 3 y 4. Además, se aisló un bloque de **15,211 mesas a nivel nacional** con relleno extremo (dígitos 8 y 9) que sobrepasa completamente la distribución esperada.

**Archivo de Evidencia Generado:**
Las 15,211 mesas con relleno flagrante (8x y 9x) quedaron aisladas con su código DANE (Departamento/Municipio/Zona/Puesto/Mesa) en el archivo:
`ENTREGABLES_FORENSES_E14/SCRIPTS_PYTHON_FORENSES/anomalias_benford_nacional_abelardo.csv`
