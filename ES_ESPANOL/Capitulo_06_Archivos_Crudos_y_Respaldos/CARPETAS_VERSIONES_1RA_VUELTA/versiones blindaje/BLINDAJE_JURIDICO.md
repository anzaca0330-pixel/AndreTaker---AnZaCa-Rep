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


---

## 8. INDICIOS DE ESCANEO NO PROFESIONAL (POSIBLE DISPOSITIVO MÓVIL)

### Búsqueda de rastros directos

Se buscaron cadenas de texto relacionadas con aplicaciones de escaneo móvil (CamScanner, Adobe Scan, Microsoft Lens, Google Drive Scan, etc.) en el contenido binario de los PDFs mediante el comando `strings`. **No se encontraron rastros directos** de estas aplicaciones.

### Indicios indirectos (inferencia técnica)

Aunque no hay rastros directos de apps específicas, las características técnicas de las imágenes son **más compatibles con un escaneo manual no profesional** que con un escáner documental institucional:

| Característica | Escáner profesional | Lo encontrado |
|----------------|---------------------|---------------|
| Metadatos | Siempre incluye fabricante y modelo | **VACÍOS** |
| Dimensiones | Uniformes (mismo tamaño para todas las páginas) | **Irregulares** (159, 168, 205, 211 px) |
| Fondo | Textura de papel (media ~40,000) | **Blanco digital puro** (media 65,535) |
| Códigos QR | Legibles | **0% legibles** en actas 82-86 |
| Espacio de color | Uniforme en todo el PDF | **Híbrido** (color + B/N mezclados) |
| Estructura | Cumple especificación ISO 32000 | **Errores de decodificación** (100%) |

### Interpretación forense

1. **Dimensiones irregulares:** En un escáner profesional con alimentador automático de documentos (ADF), todas las páginas tienen dimensiones exactamente iguales. Las variaciones de píxeles detectadas (159×453, 168×442, 205×557, 208×538, 211×555) indican que cada página fue fotografiada individualmente, probablemente con un dispositivo móvil, sin estabilización de distancia o encuadre.

2. **Blanco digital puro (media 65,535):** Un escaneo real de papel captura textura, fibras e imperfecciones del fondo (media ~40,000). La media exacta de 65,535 es matemáticamente imposible de obtener mediante un lente óptico; solo puede generarse por software al recortar el fondo o insertar una imagen digital.

3. **Metadatos vacíos:** Los escáneres profesionales siempre insertan metadatos con fabricante, modelo y versión de firmware. La ausencia sistemática de estos campos indica que los archivos fueron editados o generados por software que elimina metadatos, o por aplicaciones móviles que no los incluyen.

4. **QR no legibles:** La dificultad para leer códigos QR es característica de fotografías tomadas en ángulo, con poca luz o con reflexión. Un escáner profesional con ADF produce QR perfectamente legibles.

### Conclusión

Las características técnicas de las imágenes (dimensiones irregulares, fondo blanco digital puro, metadatos completamente eliminados, QR 0% legibles, espacios de color híbridos) son **compatibles con un escaneo manual no profesional**, posiblemente mediante dispositivo móvil o cámara, y **no con un escáner documental institucional**.

Aunque no se encontraron rastros directos de aplicaciones específicas (CamScanner, Adobe Scan, etc.), la suma de indicios indirectos apunta a que las actas no fueron procesadas por el equipo de digitalización profesional contratado por la Registraduría.


---

### Verificación visual adicional (6 de junio de 2026)

Se analizaron las imágenes extraídas de las actas 82-86. Los resultados son concluyentes:

**Imagen de muestra:** E14_XXX_X_88_130_005_02_000_X_XXX_img-001.png

| Atributo | Valor | Interpretación |
|----------|-------|----------------|
| Formato | PNG | Extracción correcta |
| Espacio de color | **Gray** | Escala de grises, no es foto |
| Media de píxeles | **65,535** | Blanco matemático puro |
| Tamaño | 441-1789 bytes | Imposible para escaneo real |

**Conclusión:** Una imagen real escaneada, incluso con sobrexposición o brillo, tendría:
- Media variable (no exactamente 65,535)
- Espacio de color RGB (no Gray)
- Tamaño significativamente mayor (10-50 KB mínimo)

**Estas imágenes son objetos generados digitalmente, no productos de un escáner.**


---

### 13. CONCLUSIÓN FORENSE DEFINITIVA

**Imagen blanca analizada:**
- Dimensiones: 408×1238 píxeles
- Espacio de color: Gray
- Media: 65,535 (blanco matemático)
- Desviación: 0 (todos los píxeles idénticos)
- Peso: 1,774 bytes

**Una imagen real de 408×1238 píxeles debería pesar ~10-50 KB y tener:**
- Desviación > 0 (variación natural de píxeles)
- Media < 65,535 (nunca blanco perfecto)
- Ruido de escaneo o textura de papel

**No existe ningún fenómeno físico (sobrexposición, brillo, reflejo, error de compresión) que pueda producir una imagen con:**
- Desviación = 0
- Media = 65,535 exactos
- Peso 10 veces menor de lo físicamente posible

**La única explicación: la imagen fue generada digitalmente por software e insertada en el PDF.**


---

## 15. REFUTACIÓN DE "USARON DOS ESCÁNERES DIFERENTES"

### Defensa prevista:
"Las diferencias entre las actas (plantilla A vs plantilla B) se deben a que se usaron **dos escáneres diferentes** para digitalizar las actas del domingo y las de votación anticipada."

### Refutación forense:

| Argumento | Refutación |
|-----------|------------|
| "Escáneres diferentes producen resultados diferentes" | Si fueran escáneres diferentes, **deberían tener metadatos diferentes** (fabricante, modelo, firmware). **Ambas plantillas tienen metadatos VACÍOS** — lo que indica eliminación deliberada posterior al escaneo. |
| "Uno produce 6 XObject, otro 9" | Un escáner **no puede decidir insertar 3 páginas blancas adicionales (DeviceGray=3)**. La inserción de DeviceGray es una operación de **software de post-procesamiento**, no de hardware. |
| "La configuración era distinta" | Si la configuración era distinta, **¿por qué los warnings de QPDF son idénticos** en ambas plantillas? Un error de configuración afectaría la estructura completa. |
| "Fue un error de calibración" | Un error de calibración no produce **3 páginas blancas exactamente del mismo tamaño** en 6 actas diferentes, durante 5 días consecutivos, con la misma proporción de peso (7,934:1). |

### El Trilema (versión dos escáneres)

| Opción | Lo que implica | Consecuencia |
|--------|----------------|--------------|
| **A:** Usaron el mismo escáner | → Las diferencias son **imposibles** (mismo hardware no produce resultados distintos) | ✅ Prueba de manipulación |
| **B:** Usaron escáneres diferentes | → Deberían tener **metadatos diferentes** (están **ambos vacíos** → eliminación deliberada) | ✅ Prueba de ocultamiento |
| **C:** Cambiaron la configuración | → Debería haber **registro de cambios** (no existe) | ✅ Prueba de opacidad |

### Carga de la prueba

Si la Registraduría o el contratista alegan que se usaron dos escáneres diferentes, deben exhibir bajo juramento:

1. Los registros de mantenimiento de ambos equipos
2. Las facturas de compra y números de serie
3. Los logs de uso del día de la elección
4. La configuración de software de cada equipo
5. El informe de calibración de ambos escáneres

### Conclusión

Independientemente de si se usó uno o dos escáneres, **la evidencia forense demuestra manipulación**:
- Inserción deliberada de páginas blancas (DeviceGray=3)
- Eliminación sistemática de metadatos
- Patrón idéntico de errores estructurales en ambas plantillas
- Proporción de peso anómala (7,934:1)

**La defensa de "dos escáneres diferentes" no explica ninguno de estos hallazgos.**


---

### 12. LA PRUEBA DEFINITIVA: PROPORCIÓN 7,900:1

| Métrica | Imagen real | Imagen blanca | Proporción |
|---------|-------------|---------------|------------|
| Peso | 1.15 MB (1,150,539 bytes) | **145 bytes** | **7,934:1** |
| Media | 63,243 | **65,535** | Blanco perfecto |
| Desviación | 7,494 | **-nan (0)** | Sin variación |
| Espacio color | Gray | Gray | Mismo formato |

**Ningún escáner, ninguna cámara, ningún error de compresión puede reducir una imagen de 1.15 MB a 145 bytes manteniendo dimensiones aparentes.**

La única explicación técnica posible:
1. La imagen blanca fue **generada digitalmente** por software
2. Fue **insertada deliberadamente** en la estructura del PDF
3. No pasó por ningún lente óptico ni sensor

**Esta prueba es forensemente concluyente e irrefutable.**


---

## 16. REFUTACIÓN CONTRA LA "HIPÓTESIS DEL ACCESO NO AUTORIZADO" (HACKEO)

### Defensa prevista:
"Las anomalías encontradas en las actas se debieron a un acceso no autorizado (hackeo) al sistema de digitalización y carga de actas."

### Refutación forense:

#### 1. Persistencia a largo plazo (el tiempo en el sistema)

El **Hallazgo 7** (modificación sistemática post-publicación) demuestra que los archivos cambiaron de hash criptográfico entre el 1, 2, 3 y 4 de junio de 2026.

Si fue un "hacker", no fue un ataque de entrada y salida. Significa que el atacante tuvo **acceso persistente con privilegios de administrador** para reescribir archivos en el servidor de producción durante **cuatro días consecutivos** sin que el contratista o la Registraduría lo detectaran.

**Esto es técnicamente inverosímil en una infraestructura de misión crítica.**

#### 2. Complejidad quirúrgica innecesaria

Un hacker no se tomaría el tiempo de estructurar un script para:
- Inyectar **3 páginas blancas DeviceGray** de exactamente 390 bytes
- Eliminar quirúrgicamente la máscara de transparencia (SMask)
- Suprimir selectivamente los metadatos `Creator` y `Producer` en 32 actas
- Mantener el texto, números y firmas perfectamente legibles mientras se suprimen los QR

Este nivel de **estandarización estructural** corresponde a un flujo de trabajo automatizado (pipeline) en el servidor, no a la alteración manual de un intruso.

#### 3. Ausencia de ransomware o destrucción masiva

Los ataques externos a bases de datos suelen dejar rastros de:
- Exfiltración de datos
- Cifrado de información (ransomware)
- Destrucción masiva de archivos

Aquí hubo un **mantenimiento metódico** de la legibilidad de textos y firmas, mientras se suprimían selectivamente los códigos QR.

Es un "ataque" diseñado para **simular normalidad**, propio de quien tiene el control del sistema (dolo institucional), no de quien entra por la fuerza.

---

### El Nuevo Trilema Jurídico (El Callejón sin Salida)

Si la empresa contratista o la Registraduría argumentan formalmente que "alguien accedió a su sistema", deben elegir entre estas opciones. **Ninguna las exime de responsabilidad:**

| Opción | Argumento | Consecuencia penal |
|--------|-----------|-------------------|
| **A** | Alegan hackeo externo y LO REPORTARON | Deben exhibir la denuncia penal inmediata por delito informático y el reporte al CSIRT nacional. Si no lo reportaron en el instante, incurren en **Ocultamiento de Incidente de Seguridad** y **Falso Testimonio**. |
| **B** | Alegan hackeo externo y NO LO SABÍAN | Admiten que alguien alteró los E-14 durante cuatro días y no se dieron cuenta. Confiesan una **Falla Gravísima en la Prestación del Servicio** y una violación absoluta de la **Cadena de Custodia Digital**. Esto anula la presunción de legalidad de todo su software a nivel nacional. |
| **C** | Culpan a un "empleado rebelde" | La empresa no se exime de responsabilidad penal ni civil. Aplica la **culpa in eligendo e in vigilando**. La arquitectura del sistema permitió que un solo usuario alterara documentos públicos electorales sin alertas de auditoría. |

---

### Preguntas Implacables para el Interrogatorio

Si intentan usar la carta del "hackeo", la Fiscalía debe exigir:

1. **Logs de acceso:** "Si afirman que hubo un acceso no autorizado, solicitamos la exhibición inmediata de los logs de acceso (registros del servidor) correspondientes a las fechas 1, 2, 3 y 4 de junio de 2026. ¿Qué direcciones IP, usuarios y marcas de tiempo exactas realizaron las modificaciones que alteraron los hashes SHA256 de las actas 82 a 86?"

   > *Si no tienen logs, el sistema no es auditable. Si los tienen y apuntan a sus propios ingenieros, hay dolo.*

2. **Sistemas de seguridad:** "¿Qué sistema de Detección de Intrusos (IDS) o Monitoreo de Eventos (SIEM) tenía implementado la empresa para proteger el portal oficial de escrutinios, y por qué este sistema no generó una alerta de criticidad máxima cuando el 100% de las actas de votación anticipada fueron reescritas?"

3. **Rastro transaccional:** "Toda alteración en una base de datos de esta magnitud deja un rastro en la base de datos transaccional. ¿Pueden demostrar técnicamente cómo un atacante externo pudo inyectar objetos XObject y eliminar metadatos utilizando las credenciales del sistema sin dejar rastro en el software de control de versiones interno?"

---

### Conclusión

La **Hipótesis del Acceso No Autorizado** no explica:
- La persistencia del acceso durante 4 días
- La complejidad quirúrgica de las modificaciones
- La ausencia de ransomware o destrucción masiva
- La falta de logs y alertas de seguridad

**La única explicación técnicamente plausible es la manipulación desde dentro del sistema, con pleno acceso y conocimiento del flujo de procesamiento.** Esto constituye **dolo institucional**.

