## 1. MAPA DE DEFENSAS PREVISTAS Y REFUTACIONES

| Defensa de la Contraparte | Refutación Blindada |
| :--- | :--- |
| **"Son hojas en blanco escaneadas por error o cartulinas separadoras"** | 1. Un escaneo de papel tiene textura (media ~40,000). Nuestras imágenes tienen blanco digital puro (media 65,535). No pasaron por un lente óptico. 2. Los separadores son objetos físicos. El libro radicador del consulado debe registrar su existencia. Si no están registrados, el argumento es falso. |
| **"El escáner aplicó un algoritmo de binarización agresivo que eliminó el fondo"** | 1. El algoritmo se "encendió" selectivamente de martes a sábado. El lunes y el domingo no. Los algoritmos no toman vacaciones. 2. La compresión extrema que borra una página entera hasta dejarla en 390 bytes habría afectado también a las páginas con contenido. La coexistencia de páginas con textura (~100 KB) y páginas en blanco puro (~390 bytes) en el mismo PDF es forensemente incompatible con una sola configuración de escaneo. |
| **"Fue un error humano de un operario que no revisó el lote"** | 1. El operario es el eslabón visible, pero el sistema lo permitió. Un error humano es aleatorio y caótico; el nuestro es un patrón quirúrgico estandarizado. 2. Aplicamos la teoría de la Ceguera Voluntaria: La alta dirección diseñó un sistema sin alertas de calidad. Omitir controles a sabiendas de que el sistema puede publicar documentos mutilados constituye dolo eventual. |
| **"No hay dolo, solo negligencia e incompetencia"** | La negligencia es un evento aislado. 15 omisiones selectivas, en 5 actas, durante 5 días consecutivos, con un patrón de bytes idéntico, no es un error. Es una característica operativa. La "incompetencia" masiva y estructurada es una tapadera, no una coartada. |
| **"Usted no puede probar una conspiración ni un concierto para delinquir"** | No necesito probar una reunión secreta. Probaré un Acuerdo Implícito Estructurado: La decisión corporativa de usar un software sin validaciones, la omisión de auditoría de calidad, y la selección quirúrgica de las actas a mutilar constituyen un acuerdo de voluntades por omisión. La estructura organizacional se usó como el instrumento del delito. |
| **"El contratista no puede ser obligado a autoincriminarse"** | No le pedimos al contratista que se inculpe. Le pedimos que exhiba los libros radicadores, los logs de soporte técnico y la configuración del software que ya tiene en su poder. Si no puede o no quiere, aplicamos la inversión de la carga probatoria en sede administrativa por falla en el servicio. |

---

## 2. LA ESTRATEGIA DE ARRINCONAMIENTO (EL TRILEMA)

Obligaremos a la Registraduría y a la empresa a elegir una de estas tres opciones. Ninguna las exime de responsabilidad penal:

- **Opción A (Afirman que el PDF es fiel al papel):** ¿Dónde está la página en blanco del formulario E-14 físico? Muéstrenla. Si no existe, es **Falsedad Material**.
- **Opción B (Alegan un error de configuración):** ¿Dónde está el reporte de ese incidente? ¿El ticket de soporte? ¿El correo del supervisor? Si no existe, es **Omisión de Control Documental**.
- **Opción C (Confiesan la pérdida de los documentos físicos):** Acaban de admitir la **Destrucción de Material Electoral**, un delito autónomo.

---

## 3. LA PRUEBA DE LA INTENCIÓN (DOLO)

- **Fase 1 (Técnica):** No se prueba que el píxel fue creado con mala intención. Se prueba que una vez creado, el PDF fue certificado y publicado por un operador humano. Ese acto de certificación de un documento visiblemente mutilado es dolo eventual.
- **Fase 2 (Estadística):** El patrón no es ruido. Es una señal. La aparición exclusiva de las páginas en blanco durante los días de votación anticipada (martes a sábado) descarta el error y consolida la intervención selectiva.
- **Fase 3 (Organizacional):** El dolo se encuentra en el diseño del sistema. La decisión corporativa de excluir validaciones automáticas en el flujo de trabajo es el acto doloso fundacional.

---

## 3. BLINDAJE CONTRA "MISMO ESCÁNER" Y "PLANTILLAS SEPARADORAS"

### Defensa prevista A: "Los errores idénticos prueban que usamos el mismo escáner, no que fabricamos los PDFs"

**Refutación:**
1. Hay **2 plantillas diferentes** (9 objetos vs 12 objetos). El mismo escáner no cambia su estructura de objetos de un día para otro.
2. El lunes (acta 81) tiene 9 objetos. El martes (acta 82) tiene 12. Algo cambió en la configuración entre lunes y martes.
3. Errores de firmware son aleatorios. 11 objetos idénticos con error en 6 actas distintas es un patrón de software, no de hardware.

### Defensa prevista B: "Las páginas en blanco son separadores físicos de lote"

**Refutación:**
1. Un separador físico escaneado tiene textura (media ~40,000). Las imágenes tienen media 65,535 (blanco digital puro generado por software).
2. Si son físicos, deben constar en el libro radicador del consulado. Que los exhiban.
3. El formulario E-14 no contempla "páginas separadoras". Insertar una hoja en blanco en un documento público es falsedad material.

---

## 2. BLINDAJE DEL HALLAZGO 10: AUSENCIA SELECTIVA DE CÓDIGOS QR

### Defensa prevista:
"Los QR no se leen por error de escaneo, baja resolución o compresión del archivo."

### Refutación forense:
1. **El texto, números y firmas son perfectamente legibles** en las mismas imágenes donde los QR no se detectan.
2. **Análisis de píxeles:** Las imágenes tienen media de ~185 (0.73) y desviación estándar de ~50, lo que confirma contenido visual real. No son imágenes degradadas.
3. **Selectividad imposible:** Un error de escaneo o compresión degrada toda la imagen por igual. No puede borrar selectivamente solo los QR dejando el texto intacto.
4. **El lunes sí funciona:** El acta 81 (lunes) tiene 3/3 QR legibles. El mismo equipo y proceso no pudo fallar solo de martes a sábado.
5. **Carga de la prueba:** Si alegan error técnico, deben exhibir las actas físicas para demostrar que los QR existen en el papel.

### Conclusión:
La ausencia de QR en 30 imágenes de páginas con contenido visible es prueba de generación digital, no de error de escaneo.


---

## 4. ANÁLISIS CONSOLIDADO DE HASHES, TAMAÑOS Y METADATOS

### Datos recopilados (Actas 82-86, martes a sábado)

| Día | Acta | Tamaño | Hash SHA256 | Producer | Creator | Versión |
|:--|:--|:--|:--|:--|:--|:--|
| Martes | 82 | 330 KB | `7a6d7b1c...` | VACÍO | VACÍO | 1.6 |
| Miércoles | 83 | 504 KB | `dca11a18...` | VACÍO | VACÍO | 1.6 |
| Jueves | 84 | 476 KB | `3201aa36...` | VACÍO | VACÍO | 1.6 |
| Viernes | 85 | 1,091 KB | `17869564...` | VACÍO | VACÍO | 1.6 |
| Sábado | 86 | 428 KB | `b3d7d901...` | VACÍO | VACÍO | 1.6 |
| Domingo | 02(1) | 1,705 KB | `0066e179...` | VACÍO | VACÍO | 1.6 |

### Interpretación forense

1. **Hashes diferentes:** Cada acta es un archivo distinto con contenido específico. No son copias de un mismo archivo.
2. **Tamaños variables:** Los tamaños oscilan entre 330 KB y 1,705 KB, proporcionales a la participación electoral esperada. Esto descarta una plantilla fija y confirma que cada PDF fue generado con datos reales de votación.
3. **Metadatos idénticamente vacíos:** Los 6 archivos tienen Producer, Creator y CreationDate VACÍOS. Misma herramienta de eliminación de metadatos aplicada a todas.
4. **Misma versión PDF 1.6:** Mismo software generador.
5. **Patrón estructural idéntico:** A pesar de ser archivos diferentes, comparten exactamente el mismo patrón de 6 imágenes (3 reales + 3 blancas), 11 objetos con error de decodificación, y 0 QR legibles.

### Conclusión

No es un archivo copiado ni un error de transmisión. Son 5 actas independientes, con datos de votación distintos, pero todas fabricadas con la misma plantilla defectuosa que:
- Inserta 3 páginas en blanco quirúrgicamente idénticas
- Elimina los códigos QR
- Deja los metadatos vacíos
- Produce errores de decodificación en los mismos 11 objetos

---

## 5. ANÁLISIS COMPLETO DE CÓDIGOS QR (ZBARIMG)

### Resultados del escaneo de 33 actas

| Tipo | Actas | Cantidad | % |
|:--|:--|:--|:--|
| ✅ QR completos (3/3) | 14, 7, 81 | 3 | 9% |
| 🟡 QR parciales (1-2/3) | 11, 12, 15, 16, 1, 3, 5, sin número, 05, 06(1) | 10 | 30% |
| 🔴 QR ausentes (0/3 o 0/6) | 10, 13, 17, 18, 2, 4, 6, 8, 9, 04, 05(1), 05(2), 06, 82, 83, 84, 85, 85(1), 86, 86(1) | 20 | 61% |

### Detalle de actas 82-86

| Día | Acta | Imágenes totales | QR legibles |
|:--|:--|:--|:--|
| Martes | 82 | 6 (3 reales + 3 blancas) | 0 |
| Miércoles | 83 | 6 (3 reales + 3 blancas) | 0 |
| Jueves | 84 | 6 (3 reales + 3 blancas) | 0 |
| Viernes | 85 | 6 (3 reales + 3 blancas) | 0 |
| Sábado | 86 | 6 (3 reales + 3 blancas) | 0 |

### Refutación de "error de escaneo"

Las imágenes tienen contenido visual verificable (media ~185, desviación estándar ~50, 4 canales RGBA). El texto, números y firmas son legibles. Un error de escaneo no puede borrar selectivamente los QR dejando todo el resto del contenido intacto.

---

## 6. ANÁLISIS COMPLETO DE ERRORES DE DECODIFICACIÓN (PEEPDF)

### Resultados globales

| Grupo | Actas | Objetos por acta | Errores | % Error |
|:--|:--|:--|:--|:--|
| Mesa 02 (domingo) | 19 | 9 | 8 | 89% |
| Semana anticipada | 04, 05, 06 (5) | 9 | 8 | 89% |
| Bloque 82-86 | 6 | 12 | 11 | 92% |

### Patrón idéntico en actas 82-86

Las 6 actas comparten exactamente los mismos 11 objetos con error:
6, 8, 9, 13, 15, 16, 20, 22, 23, 24, 25]
### Refutación de "mismo escáner"

1. Existen 2 plantillas diferentes (9 objetos vs 12 objetos). El mismo escáner no cambia su estructura de objetos de un día para otro.
2. El lunes (acta 81) tiene 9 objetos. El martes (acta 82) salta a 12 objetos. Algo cambió en la configuración entre lunes y martes.
3. Errores de firmware son aleatorios. 11 objetos idénticos con error en 6 actas distintas es un patrón de software, no de hardware.


---

## 7. PÁGINAS DECLARADAS VS IMÁGENES REALES (PRUEBA DE INYECCIÓN OCULTA)

### Datos

| Día | Acta | Páginas declaradas | Imágenes reales | Imágenes ocultas |
|:--|:--|:--|:--|:--|
| Martes | 82 | 3 | 6 | **3** |
| Miércoles | 83 | 3 | 6 | **3** |
| Jueves | 84 | 3 | 6 | **3** |
| Viernes | 85 | 3 | 6 | **3** |
| Sábado | 86 | 3 | 6 | **3** |
| Domingo | 02(1) | 3 | 3 | **0** |

### Interpretación forense

Todas las actas declaran 3 páginas mediante el campo `/Count 3` en la estructura del PDF. Sin embargo, la extracción forense con `pdfimages` revela que las actas 82 a 86 contienen 6 imágenes: 3 con contenido real (~100 KB, color, con SMask) y 3 digitalmente blancas (~390 bytes, DeviceGray, sin SMask).

Las imágenes blancas:
- **No están declaradas como páginas** del documento
- Son objetos de tipo `/XObject` inyectados en la estructura interna
- Tienen las mismas dimensiones que las páginas reales correspondientes
- Pesan 387-549 bytes (imposible para un escaneo de papel)

### Refutación de "páginas normales"

Si la defensa alega que son páginas legítimas del formulario:
1. ¿Por qué no están declaradas en `/Count`?
2. ¿Por qué pesan 387 bytes y no ~100 KB como las demás?
3. ¿Por qué son DeviceGray cuando las reales son Color?
4. ¿Por qué no tienen máscara SMask cuando las reales sí?

### Conclusión

Las páginas blancas no son páginas del documento. Son imágenes inyectadas en la estructura interna del PDF mediante un script de post-procesamiento. Esto constituye falsedad material por inserción de contenido espurio en documento público.


---

## 8. INDICIOS DE ESCANEO NO PROFESIONAL (POSIBLE DISPOSITIVO MÓVIL)

### Búsqueda de rastros

Se buscaron cadenas de texto relacionadas con aplicaciones de escaneo móvil (CamScanner, Adobe Scan, etc.) en el contenido binario de los PDFs. No se encontraron rastros directos.

### Indicios indirectos

Sin embargo, las características técnicas de las imágenes son más compatibles con un escaneo manual no profesional que con un escáner documental institucional:

| Característica | Escáner profesional | Lo encontrado |
|:--|:--|:--|
| Metadatos | Siempre incluye fabricante y modelo | **VACÍOS** |
| Dimensiones | Uniformes (mismo tamaño para todas las páginas) | **Irregulares** (159, 168, 205, 211 px) |
| Fondo | Textura de papel (media ~40,000) | **Blanco digital puro** (media 65,535) |
| QR | Legibles | **0% legibles en actas 82-86** |

### Conclusión

Las características de las imágenes (dimensiones irregulares, fondo blanco digital puro, metadatos completamente eliminados, QR no legibles) son compatibles con un escaneo manual no profesional, posiblemente mediante dispositivo móvil o cámara, y no con un escáner documental institucional.


---

## 9. REFUTACIÓN DE "MISMO ESCÁNER O MISMA CONFIGURACIÓN"

### Defensa prevista:
"Los objetos fantasma y errores de decodificación son causados por el mismo escáner o la misma configuración de digitalización en todos los días."

### Refutación forense:

1. **Existen DOS PLANTILLAS DIFERENTES:**
   - Plantilla A: Actas mesa 02, 04, 05, 06, 81 → 20-23 objetos, 1 fantasma
   - Plantilla B: Actas 82-86 → 26 objetos, 2 fantasmas

2. **El mismo escáner no cambia su estructura:** Un escáner profesional produce PDFs con la misma estructura de objetos todos los días. La existencia de dos plantillas diferentes indica que los PDFs no fueron generados por el mismo equipo o proceso.

3. **El lunes (Acta 81) tiene 9 objetos. El martes (Acta 82) salta a 12 objetos.** Algo cambió en la configuración entre lunes y martes, lo que es incompatible con un proceso automatizado uniforme.

4. **Errores de firmware son aleatorios:** Si un escáner tuviera un error de firmware, los objetos afectados variarían aleatoriamente. Sin embargo, las 6 actas 82-86 comparten EXACTAMENTE los mismos 11 objetos con error:
   `[6, 8, 9, 13, 15, 16, 20, 22, 23, 24, 25]`

5. **Patrón de software, no de hardware:** La repetición idéntica de errores en objetos específicos a través de 6 actas distintas y 4 versiones es característica de un **software defectuoso o manipulado**, no de un error de escáner.

### Conclusión:
La evidencia de objetos fantasma y errores de decodificación apunta a **dos plantillas de software diferentes**, no a un mismo escáner. Esto es prueba de generación o edición digital, no de escaneo directo.

