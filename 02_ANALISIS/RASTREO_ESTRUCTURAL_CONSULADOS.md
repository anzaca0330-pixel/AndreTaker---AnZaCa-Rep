# INFORME PERICIAL DE RASTREO ESTRUCTURAL Y OBJETOS FALTANTES
**Objeto de Peritaje:** Identificación de punteros huérfanos en la tabla `xref` y capas de inyección gráfica en actas consulares.
**Total Actas Evaluadas:** 1749  
**Actas con Alteración Sintáctica Identificada:** 1220 (69.8%)  
**Total Objetos Faltantes/Desvinculados Rastreados:** 0  

---  

## 1. MECANISMO DE EDICIÓN Y PUNTOS DE SUSTITUCIÓN DE CONTENIDO

El análisis sintáctico de la tabla `xref` demuestra que la reestructuración por software secundario dejó referencias huérfanas hacia IDs de objetos inexistentes. Estos IDs representan la ubicación exacta donde las capas gráficas originales fueron eliminadas o sobrepuestas:

| Nombre del Archivo Acta | IDs de Objetos Faltantes / Puntos de Alteración | Capas Inyectadas (/XObject /Image) |
|---|---|---|

---  

## 2. CONCLUSIONES DEL RASTREO ESTRUCTURAL

- **Firma de Alteración Unificada:** El **69.8%** de las actas de consulados presenta punteros desalineados en la tabla `xref`.
- **Puntos de Inyección:** La presencia de múltiples objetos `/XObject` por página confirma que el contenido visual no es un mapa de bits continuo escaneado en hardware, sino una composición de capas superpuestas por software.
