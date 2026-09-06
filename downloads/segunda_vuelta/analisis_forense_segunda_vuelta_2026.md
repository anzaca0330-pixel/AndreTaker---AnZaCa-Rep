# Análisis estadístico forense — Segunda vuelta presidencial de Colombia, 21 de junio de 2026

## 0. Origen y contexto de este análisis

Este documento nació de la revisión de una conversación con otro asistente de IA (Gemini) que construía un caso de fraude electoral. A partir de ahí se fue ampliando con datos cada vez más granulares aportados por el usuario: resultados municipales oficiales, resultados por mesa individual (122,017 mesas), coordenadas geográficas, población municipal completa, y censo electoral histórico 2018–2026 por grupo de edad.

En este punto se sumó también la narración de un segundo ejercicio ciudadano independiente —un proyecto de "control político ciudadano con IA" documentado en un video/guion aportado por el usuario— que hizo un análisis paralelo con metodología propia (usando el preconteo oficial, no el escrutinio final, y una fuente de población distinta) y llegó a conclusiones notablemente similares a las de este documento, incluyendo el mismo punto exacto de quiebre en la curva de municipios ordenados por población (Almaguer, Cauca → Cajamarca, Tolima).

Ese ejercicio parte de una motivación legítima y documentada: el Artículo 74 de la Constitución (acceso a información pública), la Ley 1712 de 2014 (datos abiertos y machine-readable) y los Artículos 40 y 270 (participación y control social) — y señala, con razón, que la Registraduría publica los resultados por mesa únicamente como imágenes escaneadas de las actas E-14 (más de 120,000 archivos, sin un anexo de metadatos tabulado), lo que hace que un análisis ciudadano exhaustivo sea extremadamente costoso de construir sin herramientas automatizadas. Esa dificultad de acceso es un hecho verificable y compartido, independientemente de cuál sea la conclusión final sobre el resultado electoral.

La sección 11 de este documento hace la verificación cruzada, afirmación por afirmación, entre lo que planteó ese ejercicio y lo que se pudo recalcular aquí de forma independiente con los datos crudos disponibles. La sección 12 profundiza en un hallazgo nuevo que surgió de esa verificación: el comportamiento del censo electoral por grupo de edad entre 2018 y 2026.

---

## 1. Verificación de integridad y totales nacionales

**Metodología:** Todas las cifras de este documento fueron recalculadas directamente desde los archivos crudos del proyecto (`segunda_vuelta_results.json`, `primera_vuelta_results.json`, `departmentsTree.json`, `municipios_registro_superior_100pct.csv`) y, a partir de la sección 10.3, desde `RESULTADOSCOMPLETOS.csv` (122,017 mesas individuales, aportado por el usuario) — no copiadas de resúmenes previos ni de la conversación con Gemini. Donde una cifra de la conversación con Gemini coincide o difiere de lo recalculado aquí, se indica explícitamente.

**Corrección respecto a un turno anterior:** en una respuesta previa afirmé que la cifra de "Cúcuta +230,467" no cuadraba con los datos del proyecto. Eso fue un error: comparé esa cifra con el clúster de 5 municipios fronterizos pequeños (un cálculo distinto), no con Cúcuta como ciudad. Al recalcular directamente desde el JSON crudo, la cifra de Cúcuta es exacta (ver sección 8).

Fuente: `segunda_vuelta_results.json`, 1,189 registros municipales (1,122 nacionales + 67 consulares).

| Ámbito | Cepeda | Espriella | Margen (Espriella − Cepeda) |
|---|---|---|---|
| Nacional total (doméstico + exterior) | 12,705,116 | 12,953,317 | **+248,201** |
| Doméstico (sin consulados) | 12,495,274 | 12,568,591 | **+73,317** |
| Exterior (todos los consulados) | 209,842 | 384,726 | **+174,884** |

**Cobertura del escrutinio:** 121,956 de 122,020 mesas (99.95%). Quedan 5 municipios con mesas pendientes de escrutar en este corte de datos.

**Consistencia externa:** el margen doméstico recalculado (+73,317) coincide de forma exacta con el reportado en `analisis_segunda_vuelta_resumen.md`, y el margen total (+248,201) es muy cercano al margen del preconteo oficial reportado por prensa el mismo día (+250,830, según Registraduría/El Tiempo/CNN). La diferencia de ~2,629 votos (~1%) es consistente con que este archivo capture un corte del preconteo al 99.95% de mesas, no el escrutinio final certificado. Esto no es una anomalía — es exactamente lo que se espera de datos de preconteo con un remanente de mesas por transmitir.

---

## 2. Votantes por mesa (carga de las mesas de votación)

Media nacional: **198.9** votantes/mesa (σ = 37.4).

| Municipio | Departamento | Votantes | Mesas | Votantes/mesa | z-score |
|---|---|---|---|---|---|
| Villapinzón | Cundinamarca | 11,672 | 42 | 277.9 | +2.11 |
| Guatavita | Cundinamarca | 4,423 | 16 | 276.4 | +2.07 |
| Cajicá | Cundinamarca | 54,751 | 199 | 275.1 | +2.04 |
| Jambaló | Cauca | 9,071 | 33 | 274.9 | +2.03 |
| Tenjo | Cundinamarca | 15,335 | 56 | 273.8 | +2.00 |
| Cogua | Cundinamarca | 13,683 | 50 | 273.7 | +2.00 |
| Chía | Cundinamarca | 96,920 | 355 | 273.0 | +1.98 |
| Tocancipá | Cundinamarca | 34,671 | 127 | 273.0 | +1.98 |

Solo **5 municipios** superan z = 2, y **ninguno** supera z = 3. La lectura de la Sabana Centro de Cundinamarca (Cajicá, Cogua, Tocancipá, Tenjo, Chía, Villapinzón) como bloque de alta carga por mesa es real y reproducible, pero se trata de una anomalía **moderada**, no del "techo de participación algorítmicamente perfecto" que se describió en la conversación con Gemini. Es, además, el mismo patrón que el propio proyecto ya había documentado para Rionegro/La Ceja/Retiro/Guatapé en Antioquia, y allí la lectura fue de infraestructura de mesas rezagada frente al crecimiento poblacional — no fraude. No hay razón estadística para tratar el caso de Cundinamarca de forma distinta.

---

## 3. Voto en blanco y voto nulo

Media nacional: blanco 1.31% (σ = 0.60), nulo 0.87% (σ = 0.54). Correlación blanco–nulo: **r = 0.601** (los mismos municipios generan ambos tipos de voto no sustantivo — coherente con causas administrativas/logísticas locales, no con manipulación dirigida a un candidato).

**Municipios con mayor z-score en voto en blanco:**

| Municipio | Departamento | % blanco | z-score |
|---|---|---|---|
| Anorí | Antioquia | 5.06% | +6.22 |
| Florencia | Cauca | 4.49% | +5.27 |
| Angostura | Antioquia | 4.25% | +4.87 |
| Toledo | Antioquia | 4.23% | +4.83 |
| Campamento | Antioquia | 4.22% | +4.82 |
| Remedios | Antioquia | 4.11% | +4.64 |
| Guadalupe | Antioquia | 3.89% | +4.28 |
| Amalfi | Antioquia | 3.88% | +4.26 |

Este clúster (Anorí, Angostura, Campamento, Guadalupe, Remedios) es idéntico al "Grupo A" que `analisis_antioquia_resumen.html` ya había identificado de forma independiente. Lo reproduzco aquí desde cero con los datos crudos y el resultado es el mismo: es un patrón real y geográficamente concentrado en el norte de Antioquia, con z-scores altos y estadísticamente sólidos — el hallazgo con mayor solidez estadística de todo este documento.

---

## 4. Crecimiento de participación, primera → segunda vuelta

Media nacional: **16.55%** de crecimiento (mediana 13.46%, σ = 11.68).

| Municipio | Departamento | Votantes 1ª | Votantes 2ª | Crecimiento | z-score |
|---|---|---|---|---|---|
| Campamento | Antioquia | 2,074 | 4,717 | **+127.4%** | +9.50 |
| Anorí | Antioquia | 3,813 | 7,208 | +89.0% | +6.21 |
| Barbacoas | Nariño | 8,127 | 15,071 | +85.4% | +5.90 |
| Manaure | La Guajira | 13,466 | 24,216 | +79.8% | +5.42 |
| Angostura | Antioquia | 3,667 | 6,544 | +78.5% | +5.30 |
| López (Micay) | Cauca | 4,845 | 8,634 | +78.2% | +5.28 |
| Ricaurte | Nariño | 6,949 | 11,817 | +70.1% | +4.58 |
| Uribia | La Guajira | 22,886 | 37,678 | +64.6% | +4.12 |
| Tumaco | Nariño | 55,220 | 86,464 | +56.6% | +3.43 |

18 municipios superan z = 3 en este eje. **Campamento (Antioquia)** es, por lejos, el caso más extremo del país (z = 9.5) — y coincide exactamente con el municipio que Wikipedia (artículo "Elecciones presidenciales de Colombia de 2026") cita textualmente como el ejemplo que la oposición señaló para el argumento de "voto fusil" (presión armada), señalando que Cepeda "llegó a quintuplicar su votación" entre ambas vueltas. El mismo artículo recoge también la posición contraria: que la periferia colombiana ha votado históricamente por la izquierda y que atribuir esto a coacción estigmatiza un voto legítimo. Ninguna de las dos lecturas es verificable con los datos agregados de este proyecto — solo el hecho estadístico (el salto es real y es un outlier extremo) es verificable aquí.

### 4.1 ¿El crecimiento es de naturaleza distinta en zonas dispersas que en zonas urbanas?

Se probó directamente la hipótesis: en zonas dispersas, donde votar implica viajar largas distancias, es razonable que la gente prefiera hacer el viaje una sola vez —en la vuelta que define al presidente— en vez de en ambas. En zonas urbanas, donde votar no tiene ese costo, el mismo crecimiento no tendría esa explicación gratuita.

**Metodología:** el archivo `DIVIPOLA_Municipios.xlsx` trae coordenadas (longitud/latitud) de cada municipio, que no se habían usado hasta ahora. Se emparejaron 1,034 de los 1,122 municipios domésticos (92%) por nombre, se calculó la distancia al municipio vecino más cercano de cada uno (como proxy de aislamiento/dispersión — a mayor distancia al vecino más próximo, más aislado y con mayor probabilidad de que votar implique un desplazamiento largo), y se dividió el país en cuartiles de aislamiento.

| Cuartil | Distancia al vecino más cercano (prom.) | Crecimiento turnout 1ª→2ª (prom.) | % Espriella |
|---|---|---|---|
| Q1 — más denso/urbano | 4.4 km | **13.3%** | 57.2% |
| Q2 | 7.7 km | 13.9% | 55.5% |
| Q3 | 11.6 km | 16.2% | 47.3% |
| Q4 — más disperso/aislado | 32.4 km | **21.2%** | 46.0% |

**El patrón es exactamente el que se planteó, y es monótono:** a mayor aislamiento geográfico, mayor crecimiento de participación entre vueltas (de 13.3% en el cuartil más denso a 21.2% en el más disperso), y el cuartil más disperso es, a la vez, el que menos favorece a Espriella. Es decir, el crecimiento más alto del país se concentra justamente donde la explicación de "un solo viaje" es más plausible, y ese crecimiento no está sesgado hacia el candidato que se cuestionó — más bien lo contrario.

**Verificación directa sobre los 18 municipios con crecimiento extremo (z>3, sección 4):**

- **15 de 18 (83%)** están en el cuartil más disperso (Q4).
- Los otros 3 —Campamento, Angostura y Guadalupe, los mismos de Antioquia ya señalados por Wikipedia en el contexto del debate sobre "voto fusil"— están en el cuartil Q3 (también por encima de la mediana de aislamiento).
- **Ninguno de los 18 outliers extremos está en las zonas más densas/urbanas del país (Q1 o Q2).**

**Y a la inversa — se buscó específicamente si existía un caso "urbano" comparable, que sería la señal real que se planteó:** dentro del cuartil más denso (Q1), el mayor crecimiento encontrado es Condoto (Chocó), con z = 2.15 — muy por debajo de los z > 3 del grupo disperso, y sin un sesgo partidista consistente entre los principales casos de ese cuartil (van desde 8.6% hasta 78.1% de votación por Espriella, sin patrón claro). **No se encontró ningún municipio urbano/denso con un salto de participación comparable en magnitud a los del grupo disperso.**

**Conclusión de este chequeo:** la hipótesis se sostiene con fuerza en los datos. Prácticamente todo el crecimiento extremo de participación detectado en este documento tiene una explicación logística disponible y verificable (aislamiento geográfico), y el patrón agregado no favorece de forma sistemática a ningún candidato — de hecho, el cuartil más aislado (donde más creció el turnout) es el menos favorable a Espriella. Esto no descarta que alguno de los 18 casos puntuales merezca revisión por otras razones (como el propio debate político sobre "voto fusil" en Campamento), pero sí quita fuerza a la idea de que el crecimiento de participación, como patrón general, sea indicio de manipulación — es, mayoritariamente, el comportamiento esperable de electores rurales en un balotaje.

**Actualización con datos de mesa individual — ver sección 6.1 para la curva cronológica reconstruida con `RESULTADOSCOMPLETOS.csv`.**

---

## 5. Ley de Benford (dígito inicial y dígito final)

Aplicada sobre los 1,122 conteos municipales de votos por candidato (χ² con 8 y 9 grados de libertad respectivamente):

| Prueba | Candidato | χ² | p-valor | ¿Significativo (p<0.05)? |
|---|---|---|---|---|
| Primer dígito | Cepeda | 10.43 | 0.236 | No |
| Primer dígito | Espriella | 16.58 | 0.035 | Marginal |
| Último dígito (uniforme) | Cepeda | 18.48 | 0.030 | Marginal |
| Último dígito (uniforme) | Espriella | 13.04 | 0.161 | No |

**Lectura honesta:** hay desviaciones débiles y marginalmente significativas en 2 de las 4 pruebas, no en las 4. Con n = 1,122, hasta desviaciones pequeñas producen p-valores bajos — es el mismo punto metodológico que ya señala `analisis_segunda_vuelta_resumen.md` sobre correlaciones. Además, la Ley de Benford tiene una limitación conocida y documentada en la literatura de forensia electoral: los conteos de votos no son un proceso libre de escala como el que Benford modela originalmente — están acotados por el tamaño poblacional de cada municipio, cuya distribución en Colombia ya no es Benford-uniforme por sí sola. Esta prueba, aplicada así, **no aporta evidencia sólida ni en un sentido ni en el otro**.

---

## 6. Comportamiento en el tiempo: curva cronológica real de transmisión

A diferencia de la "curva de margen acumulado" de la conversación con Gemini (que ordenaba municipios por tamaño de población, no por tiempo real), aquí se usa el campo `mdhm` de cada municipio — la hora real (hh:mm) en que se transmitió/actualizó cada resultado el 21 de junio, entre las **16:06 y las 18:54**.

| Hora de inicio del bloque | Municipios | Votantes del bloque | % Espriella del bloque | Margen del bloque | % Espriella acumulado | Margen acumulado |
|---|---|---|---|---|---|---|
| 16:00 | 2 | 160 | 46.2% | −12 | 46.2% | −12 |
| 16:15 | 6 | 8,013 | 71.9% | +3,399 | 71.4% | +3,387 |
| 16:30 | 99 | 339,302 | 66.4% | +108,181 | 66.5% | +111,568 |
| 16:45 | 436 | 3,073,473 | 58.0% | +477,708 | 58.8% | +589,276 |
| 17:00 | 355 | 6,027,750 | 53.2% | +377,030 | 55.2% | +966,306 |
| 17:15 | 131 | 5,619,266 | 47.6% | **−259,938** | 52.4% | +706,368 |
| 17:30 | 50 | 6,894,695 | 44.5% | **−731,715** | 49.9% | **−25,347** |
| 17:45 | 28 | 918,916 | 51.3% | +23,023 | 50.0% | −2,324 |
| 18:00 | 6 | 1,011,270 | 40.3% | −192,999 | 49.6% | −195,323 |
| 18:15 | 7 | 1,745,846 | 60.1% | +340,286 | 50.3% | +144,963 |
| 18:45 | 2 | 92,273 | 10.3% | −71,646 | 50.1% | **+73,317** |

**Hallazgo central de esta sección:** dividiendo el conteo en mitad temprana (antes de las 17:00) y mitad tardía (después de las 17:00):

| Ventana | N municipios | Votantes promedio/municipio | % Espriella |
|---|---|---|---|
| Temprana (16:06–17:00) | 543 | 6,300 | **58.8%** |
| Tardía (17:00–18:54) | 579 | 38,532 | **48.8%** |

Los municipios que transmiten primero son, en promedio, **6 veces más pequeños** que los que transmiten después, y el bloque temprano favorece a Espriella con fuerza (58.8%), mientras el bloque tardío favorece levemente a Cepeda (Espriella cae a 48.8% en esos votos). El margen acumulado incluso llega a ser negativo (a favor de Cepeda) hacia las 17:30, antes de cerrar en +73,317 para Espriella.

### 6.1 La misma curva, con resolución de mesa individual (no municipio)

`RESULTADOSCOMPLETOS.csv` trae la hora de reporte (`timestamp_reporte`) de cada una de las 122,017 mesas, con el número de boletín (`num_boletin`) como desempate dentro del mismo minuto — esto permite reconstruir la curva con mucha más resolución que la de arriba (que agrupaba por hora de actualización del municipio completo):

| Bloque de 15 min | Mesas | % Espriella del bloque | Margen del bloque | Margen acumulado | % Espriella acumulado |
|---|---|---|---|---|---|
| 16:00 | 622 | 45.6% | −2,115 | −2,115 | 45.6% |
| 16:15 | 16,950 | 51.4% | +72,776 | +70,661 | 51.3% |
| 16:30 | 59,758 | 51.0% | +254,809 | +325,470 | 51.1% |
| 16:45 | 34,983 | 49.4% | −98,893 | +226,577 | 50.5% |
| 17:00 | 5,017 | 45.4% | −109,706 | +116,871 | 50.2% |
| 17:15 | 692 | 40.3% | −30,471 | +86,400 | 50.2% |
| 17:30 | 157 | 38.2% | −7,699 | +78,701 | 50.2% |
| 17:45–18:45 | 132 | ~20% | −4,614 | +74,087 | 50.1% |
| (cola final, 1 mesa) | 1 | 0% | −7 | **+74,080** | 50.1% |

Confirma el mismo patrón con mucha más nitidez: el grueso del país (59,758 mesas, hacia las 16:30) reporta con un ligero sesgo pro-Espriella (51.0%), y **cada bloque posterior a las 16:45 tiene margen negativo** (favorece a Cepeda) — son las mesas más grandes y las zonas de transmisión más lenta las que llegan al final, y recortan la ventaja de forma consistente y monótona. El margen converge a +74,080, prácticamente idéntico al +73,317 usado en el resto del documento.

Este es un patrón **mecánico y bien documentado en la literatura electoral internacional** (efecto conocido en inglés como "red mirage / blue shift"): los municipios pequeños tienen pocas mesas y terminan de escrutar y transmitir más rápido; las grandes ciudades, con miles de mesas, tardan más en consolidarse. Que el candidato que lidera en los primeros minutos no sea necesariamente el que gana al final es la firma esperada de este efecto de orden de transmisión — **no**, por sí sola, evidencia de manipulación. Es exactamente el tipo de análisis que la conversación con Gemini prometía hacer ("Argumento 3") pero no hizo: allí se usó el orden por tamaño poblacional acumulado, que mide algo distinto (composición del país por tamaño de municipio), no el orden cronológico real de transmisión.

---

## 7. Municipios con censo electoral superior a la población ("doble anomalía")

Fuente propia del proyecto: `municipios_registro_superior_100pct.csv` (95 municipios), cruzada aquí con los resultados reales de 2ª vuelta.

### 7.1 El grupo completo (95 municipios)

- Margen neto del grupo: Cepeda 228,584 / Espriella 321,328 → **+92,744 para Espriella**.
- **78 de 95** municipios del grupo favorecen a Espriella; **17 de 95** favorecen a Cepeda — **no es un patrón unidireccional**.
- Concentración geográfica: Boyacá (23), Antioquia (10), Cundinamarca (10), Santander (9), Tolima (7), Valle (7). Boyacá por sí sola concentra casi una cuarta parte del grupo.

### 7.2 Verificación caso por caso de los municipios citados textualmente en la conversación con Gemini

| Municipio | Población | Censo electoral | Registro % | Votantes reales | Turnout real (votantes/censo) | Cepeda | Espriella | Margen real |
|---|---|---|---|---|---|---|---|---|
| Cumbitara (Nariño) | 5,780 | 7,738 | 133.9% | 5,752 | 74.3% | 5,384 | 263 | **−5,121 (Cepeda)** |
| Policarpa (Nariño) | 9,799 | 12,814 | 130.8% | 9,737 | 76.0% | 9,012 | 470 | **−8,542 (Cepeda)** |
| San Pedro (Antioquia) | 18,196 | 24,029 | 132.1% | 15,937 | 66.3% | 3,272 | 12,054 | +8,782 (Espriella) |
| Nariño (Nariño, no el depto.) | 4,355 | 5,225 | 120.0% | 3,970 | 76.0% | 2,644 | 1,242 | **−1,402 (Cepeda)** |
| Charta (Santander) | 2,963 | 3,469 | 117.1% | 2,606 | 75.1% | 339 | 2,234 | +1,895 (Espriella) |
| Chivatá (Boyacá) | 2,890 | 3,355 | 116.1% | 2,534 | 75.5% | 928 | 1,563 | +635 (Espriella) |
| Jordán (Santander) | 1,371 | 1,488 | 108.5% | 1,135 | 76.3% | 118 | 1,000 | +882 (Espriella) |

**Esto es lo más importante de todo el documento:** de los 7 municipios que se citaron textualmente en la conversación con Gemini como evidencia de la "Doble Anomalía" (censo inflado + participación casi total, presentado como indicio de fraude a favor de Espriella), **3 de los 7 en realidad los ganó Cepeda de forma aplastante** — Cumbitara por 20 a 1, Policarpa por 19 a 1. Si el mecanismo fuera relleno de urnas o inflado de censo dirigido a favorecer a un candidato, no debería aparecer con esa fuerza en los bastiones más sólidos del otro candidato. El patrón es mucho más consistente con una causa estructural común a ambos lados del espectro — probablemente censos desactualizados en zonas rurales con alta migración/envejecimiento, tal como ya documentó `analisis_segunda_vuelta_resumen.md` (el 43% de estos 95 casos desaparece por completo al usar cifras de población del DANE más recientes en vez del CSV original) — que con una operación de fraude dirigida a un solo bando.

**Inconsistencia detectada dentro de la propia conversación con Gemini:** en un mensaje se reportó el censo electoral de Cumbitara como 7,738 (que coincide exactamente con el dato real), y en un mensaje posterior, dentro del mismo argumento del "techo del 74%", se citó para el mismo municipio una cifra distinta de "votantes registrados" (6,782) sin explicar la discrepancia. Ese tipo de inconsistencia interna —no frente a mis datos, sino frente a sus propios datos citados minutos antes— es una señal de que los números se regeneraron en cada turno en vez de mantenerse trazables a una sola fuente.

### 7.3 La prueba del techo de población adulta — separando la señal "visible" (turnout) de la señal "sutil" (padrón inflado)

Hay una distinción conceptual importante que conviene dejar explícita, porque el resto del documento la usa de forma implícita: **el turnout (participación real) y el tamaño del padrón (censo electoral) frente a la población son dos señales de naturaleza distinta.**

- El **turnout** es una señal *visible*: está acotado entre 0% y 100% por definición, y un valor extremo (85%, 95%, "más gente de la que puede votar") salta a la vista casi de inmediato, incluso en un vistazo superficial a una tabla.
- El **padrón inflado frente a la población** es una señal *sutil*: un municipio puede tener un censo electoral demográficamente imposible (más personas registradas para votar de las que la estructura de edad del lugar permite) y aun así mostrar un turnout perfectamente normal — 50%, 60%, nada que llame la atención — simplemente porque el turnout se calcula *sobre ese mismo padrón ya inflado*. La inflación queda oculta en el denominador, no en el resultado.

Esto significa que un análisis que solo mira turnout puede pasar por alto exactamente el tipo de problema que más importa: un padrón que ya viene mal desde el registro, independientemente de cuánta gente haya ido a votar sobre él.

**La conversación con Gemini trató el censo electoral (padrón) como si fuera equivalente a votos efectivamente emitidos**, y declaró "imposibilidad biológica" usando un techo aproximado del 74%. La cifra precisa del DANE para 2025 es que **el 73.0% de la población colombiana es mayor de edad** (38,726,789 de 53,057,212 habitantes) — se usa ese valor exacto aquí en lugar del 74% aproximado.

**Con el techo preciso del 73.0%, sobre los 95 municipios con censo > población:**

| Nivel de la señal | Definición | N° de municipios | Margen neto (Espriella − Cepeda) |
|---|---|---|---|
| **Señal del padrón (sutil)** | Censo electoral > 73% de la población | **95 / 95** (100%) | +92,744 (todo el grupo) |
| **Señal del turnout (visible, dura)** | Votantes reales > 73% de la población | **26 / 95** (27%) | +44,067 |
| **La zona ciega — donde el turnout NO habría avisado nada** | Censo > 73% de población, pero turnout entre 40% y 75% (nada anómalo a simple vista) | **67 / 95** (71%) | +42,915 |

**El tercer grupo es la respuesta más directa a lo que se señaló: son 67 municipios (más de dos tercios del total) donde el padrón es demográficamente imposible, pero el turnout —lo único que la mayoría de análisis de "fraude por participación" miran— parece completamente normal.** Ningún filtro basado en turnout habría detectado estos 67 casos. Solo se detectan comparando el tamaño del padrón contra la población, sin pasar por cuánta gente votó.

**Una forma de cuantificar el tamaño del problema del padrón, independientemente del turnout:** sumando cuánto excede cada censo electoral al techo del 73% de su población, el exceso total en estos 95 municipios es de **321,560 registros por encima de lo demográficamente plausible — el 34.3% del censo electoral combinado de todo el grupo.** Esa cifra no depende de cuánta gente votó; describe el tamaño del problema en el padrón mismo.

*Ejemplos de la "zona ciega" (padrón imposible + turnout que no llamaría la atención por sí solo):*

| Municipio | Departamento | Población | Censo electoral | Techo 73% | Turnout real | Margen |
|---|---|---|---|---|---|---|
| Santiago | Norte de Santander | 3,754 | 5,249 | 2,740 | 44.3% | +1,670 (Espriella) |
| Mutatá | Antioquia | 15,069 | 16,472 | 11,000 | 44.6% | −1,450 (Cepeda) |
| Arroyo Hondo | Bolívar | 9,022 | 10,952 | 6,586 | 44.9% | +2,201 (Espriella) |
| Puerto Carreño | Vichada | 21,007 | 21,237 | 15,335 | 45.0% | +1,830 (Espriella) |
| San Cayetano | Norte de Santander | 7,975 | 10,193 | 5,822 | 50.7% | +3,550 (Espriella) |

**Nota de honestidad metodológica:** este análisis de "zona ciega" solo se pudo hacer para los 95 municipios que ya tenían población conocida (la lista precalculada del proyecto). Es razonable sospechar que existan más casos del mismo tipo entre los ~1,027 municipios restantes del país que no están en esa lista — municipios cuyo censo *no* supera a la población total, pero sí supera el techo del 73% de adultos, sin que nadie los haya señalado todavía porque el filtro original del proyecto usó el 100% de la población (no el 73% de adultos) como corte. **No se puede descartar que la "zona ciega" real sea más grande que estos 67 casos** — solo se puede decir con certeza que, dentro de los 95 ya identificados, es mayoritaria.

**Intento de extender esto a nivel de departamento (con cautela):** usando cifras de población departamental del DANE 2025 obtenidas por separado, dos de los departamentos con más municipios en la lista de 95 —Antioquia y Boyacá— muestran un censo electoral departamental que también supera el 73% de su población total (78.6% y 80.5% respectivamente). **Esto no se presenta como hallazgo confirmado:** aplicar el 73.0% nacional de forma uniforme a un departamento específico es exactamente el mismo error metodológico que se critica en este documento cuando lo hace la conversación con Gemini a nivel municipal — la estructura de edad de Boyacá y Antioquia, con población rural más envejecida que el promedio nacional (menor natalidad, migración de jóvenes hacia las ciudades), puede legítimamente tener una proporción de adultos mayor al 73% nacional, lo que resolvería esta cifra sin necesidad de fraude. Verificarlo bien requeriría la estructura de edad específica de cada departamento, que no se pudo obtener de forma confiable para los 34 departamentos en esta sesión. Se deja anotado como pregunta abierta, no como conclusión.

---

### 7.4 La prueba del 73% a escala nacional (con el anexo de población completo)

*Actualización: el usuario aportó el anexo de Wikipedia "Municipios de Colombia por población", que trae población oficial (DANE) para prácticamente todos los municipios del país — no solo los 95 ya identificados. Esto permite repetir la prueba de la sección 7.3 (votos reales > 73% de la población) para todo el país, no solo para el subconjunto ya filtrado por censo > población.*

Se logró emparejar población para 1,049 de los 1,122 municipios domésticos (93.5%) por nombre y departamento.

**Primer intento — advertencia de integridad de datos:** el emparejamiento automático por nombre produjo un caso que parecía el más extremo del país con diferencia: "Santuario" (Antioquia), con votos un 147% por encima del techo de población. Al verificarlo, resultó ser un error de cruce: el municipio de Antioquia se llama oficialmente **"El Santuario"** (población 38,336), y el emparejamiento automático lo confundió con el municipio homónimo pero distinto **"Santuario" de Risaralda** (población 12,782) porque el archivo de resultados electorales usa el nombre corto "Santuario" sin el artículo. Corrigiendo esto (población real 38,336), el caso deja de ser una anomalía: 23,054 votantes está muy por debajo de su techo real (27,985). **Este error se descubrió y se corrigió antes de incluirlo en este documento** — se deja documentado aquí precisamente para mostrar el tipo de riesgo de cruce de datos por nombres homónimos que ya había anticipado `analisis_segunda_vuelta_resumen.md` (el mismo problema que identificó para "Riosucio").

**Resultado nacional, ya corregido:**

- **29 municipios en todo el país** (de 1,049 con población conocida) tienen votos reales por encima del techo del 73% de su población.
- Margen neto de esos 29: Cepeda 74,454 / Espriella 115,797 → **+41,343 para Espriella**.
- **24 de esos 29 ya estaban en la lista original de 95 municipios** (censo > población). Solo **5 son nuevos** — municipios que no tenían censo electoral superior a su población total, pero cuyos votos reales sí superan el techo de adultos: Sutamarchán, Tuta, Oicatá (Boyacá), Palmas del Socorro (Santander) y Florencia (Cauca, no la ciudad del Caquetá). Su aporte conjunto al margen es de solo **+2,805 votos**.

**Esto confirma, con cobertura casi completa del país, lo que la sección 7.3 ya estimaba con el subconjunto de 95:** el número de municipios con votos demográficamente imposibles es pequeño (29 en total), geográficamente disperso, y su impacto conjunto en el resultado nacional (+41,343) es modesto frente al margen final (+73,317) — significativo, pero lejos de explicarlo por sí solo. La ampliación a escala nacional no reveló un universo oculto mucho más grande de casos: el trabajo original del proyecto, aunque parcial, ya capturaba la gran mayoría del fenómeno real.

---

## 8. Voto exterior: verificación numérica directa


Usando los 67 registros de `dept = 88 (CONSULADOS)` del archivo crudo:

| Sede | Votantes | Cepeda | Espriella | Margen |
|---|---|---|---|---|
| Estados Unidos | 214,566 | 38,247 (17.8%) | 174,050 (81.1%) | **+135,803 (Espriella)** |
| España | 134,638 | 66,945 (49.7%) | 65,426 (48.6%) | −1,519 (Cepeda, prácticamente empate) |
| Venezuela | 24,787 | 4,911 (19.8%) | 19,682 (79.4%) | +14,771 (Espriella) |
| Canadá | 43,168 | 15,585 (36.1%) | 26,504 (61.4%) | +10,919 (Espriella) |

**La cifra de "Consulados EE.UU.: +135,803" de la conversación con Gemini es matemáticamente exacta** (174,050 − 38,247 = 135,803). No es un número inventado.

Lo que sí falta en la conversación con Gemini es el contexto comparativo: el voto en Estados Unidos no es un caso aislado ni extremo dentro del voto exterior — el voto en **Venezuela** tiene un sesgo proporcional casi idéntico (79.4% vs. 81.1%), y el propio artículo de prensa consultado atribuye el patrón de EE.UU. a la composición socioeconómica de esa diáspora (empresarios con mayor afinidad al programa del candidato de derecha), mientras que en el caso venezolano la explicación más obvia es política (comunidad de exiliados de un régimen de izquierda votando en contra del continuismo). Ninguna de esas dos explicaciones requiere fraude, y ninguna de las dos se puede confirmar ni descartar solo con estos datos agregados.

**Cúcuta:** votantes 390,453, Cepeda 76,069, Espriella 306,536, margen **+230,467 (Espriella)** — también exacto frente a lo citado en la conversación con Gemini. Es simplemente la ciudad más grande de un departamento (Norte de Santander) que en su totalidad votó ~76% por Espriella; su peso en votos absolutos es grande porque su población es grande, del mismo modo que Medellín es, por tamaño, el mayor contribuyente individual al margen de Espriella en Antioquia. Tamaño poblacional × sesgo departamental real explica esta cifra sin necesidad de invocar manipulación — igual que ya se explicó para Antioquia en `analisis_antioquia_resumen.html`.

**"Enviado" era Envigado (Antioquia).** El nombre se transcribió mal en el turno anterior de este documento. Envigado es un municipio del Valle de Aburrá, uno de los de mayor ingreso per cápita del país y tradicionalmente de voto conservador. Su resultado real: 166,653 votantes, Cepeda 35,667, Espriella 126,432 → margen **+90,765 (Espriella)** — coincide de forma exacta con la cifra citada en la conversación con Gemini. Igual que con Cúcuta y los consulados de EE.UU., es una cifra real, no inventada: simplemente el mayor contribuyente individual de votos en un municipio grande y homogéneamente inclinado hacia un candidato, el mismo mecanismo (tamaño × sesgo local real) explicado para Cúcuta y Medellín.

---

## 9. Síntesis: qué de la conversación con Gemini se sostiene y qué no

| Afirmación | Los números crudos | Evaluación |
|---|---|---|
| Margen doméstico +73,317 | Coincide exactamente | ✅ Exacto |
| Consulados EE.UU. +135,803 | Coincide exactamente | ✅ Exacto |
| Cúcuta +230,467 | Coincide exactamente | ✅ Exacto |
| "Enviado" +90,765 | Era un error de transcripción: es Envigado (Antioquia). Coincide exactamente (166,653 votantes, margen +90,765) | ✅ Exacto — el nombre estaba mal transcrito, no el número |
| Votantes reales de Jambaló, Balboa, Cajicá, Cogua, Tocancipá, Villapinzón, El Tambo, Florencia | Coinciden con los datos reales | ✅ Exactos como cifras crudas |
| Esos mismos municipios como "clúster coordinado" a favor de un solo candidato | Cauca (Jambaló, Balboa, El Tambo) es arrasadoramente Cepeda; Cundinamarca es mixto (Cogua casi empatado) | ❌ La interpretación no se sostiene: el bloque no es unidireccional |
| Cumbitara/Policarpa como evidencia de "votos fantasma" a favor de Espriella | Ambos los ganó Cepeda por márgenes de 19–20 a 1 | ❌ La interpretación contradice el propio dato citado |
| Censo electoral > población en 95 municipios | Confirmado, cifras exactas | ✅ El hecho es real |
| Ese exceso de censo = personas que efectivamente votaron ("imposibilidad biológica") | Solo 20 de 95 municipios tienen votantes reales (no solo censo) por encima del techo del 74% | ⚠️ Conflación entre padrón y voto emitido |
| Turnout de Cumbitara "99.5%" citado como base del argumento de imposibilidad | Es 99.5% de la *población*, no del censo electoral (que da 74.3%) — la propia conversación había explicado la diferencia entre ambos conceptos un turno antes | ❌ Inconsistencia interna |
| "Curva de margen acumulado" (Argumento 3) | Se construyó ordenando por tamaño de municipio, no por tiempo real de transmisión | ⚠️ Etiquetada como fenómeno temporal sin serlo |
| Petición de congelar servidores / "Noticia Criminal" basada en estos hallazgos | Ningún hallazgo agregado de este tipo constituye, por sí mismo, prueba forense de manipulación de un sistema | ❌ Salto no respaldado por el tipo de evidencia disponible |

---

## 10. Hallazgos correlacionados adicionales (verificados contra los datos crudos)

Esta sección responde punto por punto a cinco patrones señalados posteriormente para enriquecer el contexto forense. Cada uno se probó directamente contra `segunda_vuelta_results.json` y `primera_vuelta_results.json`; donde no fue posible verificarlo con lo que hay en el proyecto, se dice explícitamente.

### 10.1 Municipios con censo electoral atípico (≥85–100%): tamaño y magnitud de la victoria

Usando el grupo de 95 municipios con censo electoral > población (sección 7):

- Población promedio del grupo: **8,871 habitantes** (mediana 5,098). **88 de 95 (93%)** tienen población menor a 16,000. Esto confirma el patrón señalado: son, en efecto, poblaciones pequeñas de forma sistemática, no una muestra aleatoria de tamaños.
- **57 de los 95** municipios los gana Espriella con margen ≥70%. La mayoría de esos 57 se concentra en Norte de Santander, Boyacá, Santander y Antioquia — es decir, sí hay una correlación real entre "censo electoral inflado" y "victoria arrolladora de Espriella" **dentro de este grupo específico**. (La sección 7 ya mostró la contraparte: dentro del mismo grupo de 95, otros 17 municipios —incluidos Cumbitara y Policarpa— los gana Cepeda de forma igual de arrolladora. Ambos hechos son ciertos a la vez: la mayoría del grupo favorece a Espriella, y la minoría que no lo hace, lo contradice con la misma intensidad.)

*Nota de alcance: no fue posible replicar esto para el grupo más amplio de "≥85% de registro" (397 municipios, según `plantilla_analisis_departamental.md`) porque ese cálculo requiere el archivo de población DANE 2020–2035 usado en el análisis original del proyecto, que no está entre los archivos disponibles aquí — solo el subconjunto ya materializado de 95 municipios con censo > 100% incluye población municipal.*

### 10.2 Asimetría en las victorias arrolladoras

| Umbral de victoria | Municipios Espriella | Margen neto Espriella | Municipios Cepeda | Margen neto Cepeda |
|---|---|---|---|---|
| ≥70% | 383 | +1,650,054 | 177 | +1,427,147 |
| ≥75% | 278 | +1,221,529 | 138 | +1,023,781 |
| ≥80% | 184 | +840,740 | 96 | +746,059 |
| ≥85% | 78 | +252,571 | 69 | +553,944 |
| ≥90% | 17 | +48,438 | 37 | +202,355 |

**Esto confirma parcialmente el patrón señalado, con un matiz importante que no debe omitirse:** en los umbrales de 70–80%, Espriella efectivamente tiene más municipios arrolladores y mayor margen neto acumulado que Cepeda — la asimetría es real ahí. Pero el patrón **se invierte en los umbrales más extremos (≥85% y ≥90%)**: en ese rango Cepeda tiene menos municipios pero con victorias proporcionalmente más extremas y un margen neto mayor. Estos son los bastiones más monolíticos del país — territorios indígenas y afrocolombianos del Pacífico y la Amazonía (Cauca, Nariño, Chocó, Putumayo, Amazonas), donde Cepeda supera el 90% en varios municipios. Los bastiones más arrolladores de Espriella (Santander, Antioquia, Boyacá, Norte de Santander, Cundinamarca) son numéricamente más y en conjunto pesan más en votos, pero individualmente rara vez superan el 90%.

Dicho de otro modo: **Espriella gana por volumen** (muchos municipios ganados con márgenes de 70–85%), **Cepeda gana por intensidad** (menos municipios, pero con márgenes de 85–95%+ en sus bastiones históricos). Ambos patrones son consistentes con la geografía electoral colombiana documentada desde hace años (el bloque Pacífico/Amazónico como bastión de izquierda, el eje andino-oriental como bastión de derecha) — no son, por sí solos, indicio de manipulación en ninguna de las dos direcciones.

### 10.3 Votos "de más" por mesa — verificado con datos reales a nivel de mesa individual

*Actualización: el usuario aportó `RESULTADOSCOMPLETOS.csv`, con el detalle de las 122,017 mesas individuales del país (departamento, municipio, puesto, número de mesa, blancos, nulos, votos por candidato y hora de reporte). Esto reemplaza la limitación señalada en la versión anterior de este documento — ahora sí se puede probar la afirmación directamente.*

**Consistencia con los datos usados en el resto del documento:** el total doméstico de este archivo (Cepeda 12,495,572 / Espriella 12,568,593, margen +73,021) coincide, con una diferencia de apenas 296 votos (0.0002%), con el total ya usado en las secciones 1–9 (+73,317). Son dos extracciones distintas del mismo proceso electoral, prácticamente idénticas.

**No existe un umbral "natural" que dé exactamente 15,333 mesas.** Se probaron varias definiciones razonables de "mesa con votos por encima de lo normal":

| Definición de "mesa anómala" | N° mesas | Margen neto (Espriella − Cepeda) |
|---|---|---|
| Tope legal histórico de una mesa (>400 sufragantes) | 396 (302 son consulados) | +51,536 |
| Solo mesas **domésticas** >400 | 94 | **−2,204** (favorece a Cepeda) |
| z-score > 1 sobre el tamaño de la mesa (la más cercana a 15,333) | **14,437** | **+807,678** |
| Top 12.56% de mesas más grandes del país (=15,333 exactas) | 15,599 | +849,637 |

**La cifra de ~800,000 votos que se mencionó es real y se sostiene con datos duros:** usando el umbral estadístico más natural (mesas con más de una desviación estándar por encima del tamaño promedio, z > 1 → 14,437 mesas, prácticamente el mismo orden de magnitud que las 15,333 mencionadas), el margen neto es de **+807,678 votos para Espriella** — más de tres veces el margen nacional final (+248,201). Esta es, con diferencia, la anomalía de mayor magnitud absoluta de todo este documento, y a diferencia del umbral legal de 400 (que si acaso favorece levemente a Cepeda, con solo 94 mesas domésticas), esta sí tiene un tamaño de muestra y un efecto lo bastante grandes como para no ser ruido.

**Lo que hay que mirar con más cuidado antes de leerlo como fraude — el patrón por departamento:**

| Departamento | N° mesas (z>1) | Margen dentro del grupo z>1 | Margen del departamento completo (todas las mesas) |
|---|---|---|---|
| Antioquia | 1,794 | +322,738 | +1,052,153 |
| Bogotá D.C. | 4,506 | **+157,581** | **−302,271** (¡Bogotá la ganó Cepeda!) |
| Consulados | 857 | +122,910 | +177,809 |
| Santander | 777 | +105,051 | +391,041 |
| Cundinamarca | 1,577 | +49,037 | +128,466 |
| Norte de Santander | 223 | +43,292 | +428,500 |
| Valle | 586 | +11,024 | **−534,083** (Valle la ganó Cepeda) |
| Atlántico | 269 | +16,451 | **−227,312** (Atlántico la ganó Cepeda) |
| Nariño | 532 | −73,653 | (bastión de Cepeda) |
| Cauca | 649 | −98,169 | (bastión de Cepeda) |

**Este es el hallazgo más importante de esta actualización.** El patrón no se limita a los departamentos que Espriella ya ganaba en general — **en Bogotá, Valle del Cauca y Atlántico, tres departamentos que Cepeda ganó en su resultado global, las mesas más grandes de esos mismos departamentos favorecen a Espriella** de forma sistemática (en Bogotá por +157,581, a pesar de que Cepeda ganó la ciudad completa por −302,271). Es decir: dentro de casi cualquier departamento del país —sea bastión de uno u otro candidato— **las mesas con más votantes tienden a favorecer más a Espriella que el promedio de ese mismo departamento**. De los 29 departamentos con mesas en este grupo, 23 muestran esta misma dirección; solo Cauca, Nariño, Chocó, Amazonas, Putumayo, Sucre, Córdoba, Bolívar, Magdalena, Caquetá y Guaviare van en sentido contrario (y son, no por casualidad, los bastiones más consolidados de Cepeda).

Dos lecturas compiten aquí, y ninguna de las dos se puede zanjar solo con este archivo:

- **Lectura no fraudulenta:** las mesas con más votantes suelen estar en zonas urbanas densas, de estrato medio/alto o de rápido crecimiento suburbano (el mismo fenómeno ya documentado en la sección 2 para Rionegro, La Ceja, Retiro, Guatapé y la Sabana Centro de Cundinamarca), y ese perfil socioeconómico puede inclinarse más hacia Espriella de forma perfectamente orgánica dentro de cualquier ciudad, incluidas las que en conjunto ganó Cepeda.
- **Lectura que sí ameritaría auditoría:** si hubiera manipulación concentrada en mesas específicas (más fácil de alterar cuantos más votos agrega cada una), el patrón esperado sería exactamente este — un exceso sistemático y transversal a favor de un solo candidato, concentrado en las mesas de mayor tamaño.

**Ninguna de las dos se puede confirmar con datos agregados.** Lo que sí se puede recomendar de forma concreta: dado que este patrón es reproducible, grande (+807,678) y transversal a 23 de 29 departamentos, es un candidato mucho más sólido para una auditoría física de actas E-14 que cualquiera de los hallazgos citados en la conversación original con Gemini — empezando por las 4,506 mesas de Bogotá D.C. y las 1,794 de Antioquia, que concentran más de la mitad del efecto total.

**Verificación adicional — el tope legal de 400 votantes por mesa:** solo 94 mesas domésticas superan ese tope (frente a las 302 mesas consulares que sí pueden tener capacidades mayores por logística de la votación en el exterior). Esas 94 se concentran en puestos de votación específicos y grandes (Tunja y Sogamoso en Boyacá, Pasto en Nariño, Chaparral en Tolima) — probablemente centros de votación grandes con varias mesas reportadas bajo un mismo puesto, no relleno de votos. Su margen neto es de solo −2,204 (prácticamente neutro, y levemente a favor de Cepeda). Este umbral, el único con respaldo legal directo, **no muestra ninguna anomalía relevante** — la anomalía real está en el umbral estadístico (z>1), no en el legal.

**Ley de Benford a nivel de mesa (n=122,017, no ya n=1,122):** con este tamaño de muestra mucho mayor, la desviación de Benford es enorme y estadísticamente "significativa" de forma aplastante (χ² = 33,330 para Cepeda, χ² = 15,989 para Espriella, p ≈ 0 en ambos casos). **Esto no es evidencia de fraude — es la prueba de que Benford no aplica a este tipo de dato.** Se puede demostrar de forma directa: el campo `TOTAL MESA` (el tamaño total de la mesa — una cifra que nadie puede "fraguar" con intención partidista, porque no favorece a ningún candidato en particular) también viola Benford de forma extrema (61.6% de las mesas tienen un total que empieza con el dígito 2, frente al 17.6% que predice Benford). La razón es mecánica, no fraudulenta: el 92% de las mesas del país tienen entre 100 y 399 votantes, porque ese es, por diseño, el tamaño típico de una mesa de votación colombiana. Un conjunto de números acotado a un rango angosto (100–400) nunca sigue la Ley de Benford, sin importar si el proceso es limpio o no — es un error metodológico bien documentado en la literatura de forensia electoral (aplicar Benford a resultados por mesa, en vez de a totales sin acotar), y es la razón por la que esta prueba, aquí, no aporta nada en ningún sentido.

**Agrupamiento en números redondos:** se revisó si `TOTAL MESA` se acumula de forma sospechosa en múltiplos de 50 (una señal clásica de actas prellenadas). El resultado es débil e inconcluyente: los valores redondos (150, 200, 300) aparecen entre 1.1 y 1.3 veces más que sus vecinos inmediatos, una desviación pequeña y explicable por que las mesas suelen asignarse una capacidad nominal redonda (200, 250, 300 votantes) desde su creación — no por manipulación del conteo final.

### 10.4 Crecimiento del censo electoral desde 2018 — verificado con el censo histórico real

*Actualización: el usuario aportó el censo electoral oficial por puesto de votación para 2018, 2019, 2022–2026 (mismo esquema de códigos de la Registraduría que el resto de este análisis, lo que permite un cruce exacto, no por nombre). Se agregó `potencial_electoral` por municipio para las elecciones presidenciales de 2018 y 2026, y se emparejó con 1,121 de los 1,122 municipios domésticos (99.9%).*

**Verificación de integridad:** los valores de censo electoral 2026 de este archivo coinciden de forma exacta, municipio por municipio, con los que ya se venían usando en todo este documento (Cumbitara 7,738; Policarpa 12,814; San Pedro-Antioquia 24,029) — confirma que la fuente de censo electoral usada desde la sección 1 es correcta. El total nacional (41,421,973) también coincide de forma exacta con la cifra pública citada por El Tiempo.

**Crecimiento nacional 2018 → 2026:** 36,219,940 → 41,421,973 = **+14.4%** en 8 años (agregado nacional; +12.0% es el promedio simple municipio por municipio, con mediana de +10.75%) — un crecimiento demográfico y de cobertura de registro razonable para ese periodo, sin nada alarmante a nivel agregado.

**La prueba específica que se planteó — municipios con victoria arrolladora de Espriella (≥70%) Y crecimiento del censo >30% desde 2018:**

| | |
|---|---|
| Municipios que cumplen ambas condiciones | **11**, de 1,122 |
| Margen neto de esos 11 | **+110,014** |
| Votantes totales de esos 11 | 187,493 |

**Esto no confirma la cifra de +400,000 votos que se planteó — el resultado real es de +110,014, un 27% de lo esperado.** Los 11 municipios son, en su mayoría, del clúster fronterizo de Norte de Santander ya identificado en la sección 7 (Duranía, Santiago, Puerto Santander, Bochalema, Ragonvalia, Herrán) más Sabaneta y Retiro en el oriente antioqueño (ya documentados en la sección 2 como zona de infraestructura electoral rezagada frente al crecimiento poblacional).

**El hallazgo más importante de esta verificación va en la dirección contraria a la hipótesis original:** mirando los 30 municipios con **mayor crecimiento de censo desde 2018 en todo el país, sin filtrar por ganador**, el margen neto conjunto es **negativo: −61,561 (a favor de Cepeda)**, y Espriella gana solo 11 de esos 30. Ampliando a los 100 municipios de mayor crecimiento censal, el margen sigue siendo negativo (−95,849) y Espriella gana solo 40 de 100. Los casos de mayor crecimiento censal absoluto del país son, de hecho, bastiones o municipios competitivos de Cepeda: Barrancominas (Guainía, +140.5%, 92% Cepeda), Puerto Gaitán (Meta, +105.2%, mayoría Cepeda), Soacha (Cundinamarca, +58.6%, el municipio más poblado de este grupo, −84,738 para Cepeda), Madrid y Mosquera (sabana de Bogotá, ambos Cepeda). **La correlación entre crecimiento del censo 2018–2026 y % de voto por Espriella es de −0.248 a nivel nacional** — negativa, no positiva.

**Conclusión de esta sección:** con datos reales, verificados y de cobertura casi completa, la afirmación de que el crecimiento del censo desde 2018 está concentrado en zonas de victoria arrolladora de Espriella y suma más de 400,000 votos **no se sostiene**. El crecimiento censal más extremo del país se concentra, en su mayoría, en municipios de Cepeda o competitivos (particularmente en la periferia de Bogotá y la Orinoquía/Amazonía), no en los bastiones de Espriella.

### 10.5 El proceso legal ya se completó — resultado del escrutinio oficial

Todo lo anterior es un análisis estadístico de datos agregados. Colombia también corrió, en paralelo, el proceso que sí tiene autoridad legal para revisar actas físicas una por una: el escrutinio oficial. Vale la pena registrar su resultado aquí, porque es el tipo de evidencia que ningún análisis de datos agregados puede sustituir.

- El escrutinio nacional terminó el **24 de junio de 2026**. El Consejo Nacional Electoral (CNE) declaró a Abelardo de la Espriella presidente electo mediante el acta E-26.
- Resultado final certificado: **Espriella 12,959,542 (49.66%) — Cepeda 12,708,712 (48.70%)**, prácticamente idéntico al preconteo usado en todo este documento. El presidente del CNE, Cristian Quiroz, describió la variación entre preconteo y escrutinio como "por debajo de cero".
- La campaña de Cepeda presentó **57,000 reclamaciones formales** durante el escrutinio (más de las 33,000 mesas anunciadas inicialmente), incluyendo denuncias puntuales de alteración de formularios E-14.
- Antes de la declaratoria, Cepeda y su fórmula vicepresidencial **aceptaron formalmente sus curules** en el Congreso bajo el estatuto de oposición.

Esto no reemplaza ni descarta nada de lo encontrado en este documento —los 57,000 reclamaciones puntuales no necesariamente cubrieron, mesa por mesa, el clúster de ~14,400 mesas grandes identificado en la sección 10.3, que sigue siendo el candidato más razonable para una revisión dirigida—, pero sí es la pieza de evidencia más fuerte disponible sobre el resultado final: un proceso con autoridad legal, mirando actas físicas, revisó decenas de miles de objeciones específicas y el resultado no se movió de forma significativa.

### 10.6 La curva de margen acumulado ordenada por tamaño de municipio (reconstruida con datos reales)

Como se explicó en la sección 6, no hay un archivo de población para los 1,122 municipios completos — solo para el subconjunto de 95. Para esta curva se usó **votantes totales por municipio como aproximación del tamaño poblacional** (están altamente correlacionados por construcción), ordenando de mayor a menor.

| % acumulado de votos (municipios de mayor a menor tamaño) | Margen acumulado (Espriella − Cepeda) |
|---|---|
| 50% | −119,023 |
| 70% | −336,599 |
| 78.6% (punto más bajo de la curva) | **−521,876** |
| 80% | −471,244 |
| 85% | −459,125 |
| 88% | −459,937 |
| 90% | −408,645 |
| 92% | −362,245 |
| 95% | −262,848 |
| 97% | −204,371 |
| 99% | −35,829 |
| 100% | **+73,317** |

**El patrón que se describió es real, con la cifra exacta ligeramente distinta:** el margen acumulado, ordenado de más a menos poblado, favorece a Cepeda de forma sostenida y creciente hasta cerca del **78.6% de los votos** (no el 88%), donde llega a su punto más bajo: **−521,876** (no "casi 600 mil", pero del mismo orden de magnitud). A partir de ahí la curva se revierte, y lo hace de forma **gradual a lo largo de todo el último 20% de los votos**, no en un quiebre abrupto concentrado solo en el último 11%.

Aun así, el dato más contundente de esta curva es otro: el **último 11% de los votos** (los 666 municipios más pequeños del país) aporta, por sí solo, un swing neto de **+521,281 votos a favor de Espriella** — una cifra que, casi por coincidencia numérica, es del mismo tamaño que el déficit que Cepeda había acumulado hasta el 78.6%. En otras palabras: **el resultado nacional se decide casi enteramente en el último 11% del padrón**, concentrado en los municipios más chicos del país.

De ese swing de +521,281 en los municipios más pequeños, **solo el 18.3% (+95,452 votos) proviene de los 95 municipios con censo electoral > población** (83 de esos 95 municipios sí caen dentro de este último 11%, pero son una minoría de los 666 municipios de esa cola). El **81.7% restante del swing viene de municipios pequeños con censo electoral normal** — es decir, la mayor parte de por qué la periferia decidió la elección **no tiene relación con censos inflados**; es simplemente que la periferia rural, con censo normal, votó de forma abrumadora por Espriella. Esto no descarta que el subconjunto de 95 municipios sea un problema real de calidad de datos que merece auditoría — pero sí acota su peso real dentro del resultado nacional a una fracción menor del total.

**Verificación con población real (no solo el proxy de votantes):** repitiendo esta misma curva usando la población real de 1,049 municipios (anexo de Wikipedia, sección 7.4) en vez de votantes como proxy de tamaño, el patrón direccional es el mismo — la curva cae a territorio negativo (favorable a Cepeda) entre el 70% y el 90% de los votos acumulados (mínimo de −254,444 al 80.5%, en Corinto, Cauca) y se recupera en el tramo final. La cobertura de este chequeo es del 81% de los votos (no el 100%, por los municipios sin población emparejada), así que las cifras exactas no son directamente comparables voto a voto con la curva basada en votantes — pero confirma que el hallazgo no es un artefacto de usar votantes como proxy de tamaño poblacional.

### 10.7 Participación real (turnout) por departamento — verificada con censo electoral real

Hasta ahora, la mayoría del documento usó proxies de tamaño (votantes, mesas) porque no había censo electoral (padrón) para todo el país. `primera_vuelta_results.json` sí trae el censo electoral real por departamento (`centota`), que se puede cruzar con los votos reales de la 2ª vuelta de `RESULTADOSCOMPLETOS.csv`. **El censo nacional que resulta de sumar los 34 departamentos es 41,421,973 — coincide de forma exacta con la cifra que reportó El Tiempo el día de la elección**, lo que confirma que este campo es real y fiable.

**Turnout nacional real, 2ª vuelta:** 25,701,914 votantes domésticos / 40,007,312 censados = **64.24%** (con exterior: 63.53%). Coincide con lo ya documentado en `analisis_segunda_vuelta_resumen.md` (64.32%).

**Turnout por departamento (2ª vuelta), de mayor a menor:**

| Departamento | Turnout 2ª vuelta | % Espriella |
|---|---|---|
| Cundinamarca | 73.4% | 53.9% |
| **Cauca** | **73.1%** | **23.2%** (bastión de Cepeda) |
| Casanare | 71.8% | 70.2% |
| Boyacá | 71.2% | 61.2% |
| Bogotá D.C. | 70.6% | 46.4% (la ganó Cepeda) |
| **Nariño** | **70.0%** | **22.4%** (bastión de Cepeda) |
| Santander | 68.9% | 65.6% |
| ... | ... | ... |
| Guainía | 41.6% | 35.7% |

**Correlación turnout vs. %Espriella a nivel departamental: r = 0.227** — positiva, pero débil. Y lo más importante: **los dos departamentos con mayor turnout de todo el país después de Cundinamarca son Cauca y Nariño — los dos bastiones más sólidos de Cepeda**, no de Espriella. Esto pesa directamente en contra de leer "turnout alto" como señal genérica de manipulación a favor de un candidato: aquí el turnout más alto del país aparece tanto en territorio de Cepeda como de Espriella.

**El hallazgo más importante de esta sección — crecimiento del turnout entre la 1ª y la 2ª vuelta, por departamento:**

| Departamento | Turnout 1ª vuelta | Turnout 2ª vuelta | Crecimiento (p.p.) | % Espriella |
|---|---|---|---|---|
| Putumayo | 51.1% | 64.4% | **+13.3** | 20.4% |
| Nariño | 57.2% | 70.0% | +12.7 | 22.4% |
| Chocó | 40.7% | 52.5% | +11.8 | 17.9% |
| Caquetá | 53.4% | 64.7% | +11.2 | 49.8% |
| Córdoba | 51.0% | 61.7% | +10.7 | 41.2% |
| ... | ... | ... | ... | ... |
| Norte de Santander | 54.2% | 57.9% | +3.7 | 77.6% |
| Cundinamarca | 69.6% | 73.4% | +3.8 | 53.9% |
| Bogotá D.C. | 68.0% | 70.6% | +2.7 | 46.4% |

**Correlación entre el crecimiento del turnout (en puntos porcentuales) y el % de Espriella: r = −0.771** — fuerte y negativa. Los departamentos donde más creció la participación entre la primera y la segunda vuelta son, de forma consistente, los bastiones de Cepeda (Putumayo, Nariño, Chocó, Caquetá, La Guajira, Vaupés — el bloque Pacífico/Amazónico), no los de Espriella. Los departamentos donde menos creció son, en cambio, algunos de los bastiones más fuertes de Espriella (Norte de Santander, apenas +3.7 p.p., con 77.6% de votación por él).

**Esto es una contrapieza real frente al énfasis que puso la conversación con Gemini en el crecimiento de participación como señal de fraude a favor de Espriella.** A nivel de departamento, con censo electoral real (no un proxy), el patrón agregado va en la dirección contraria: es la periferia de izquierda la que más aumentó su participación en la segunda vuelta — compatible con una movilización política real de última hora a favor de Cepeda (razonable en cualquier balotaje, donde el candidato que no encabezó la primera vuelta suele consolidar votos dispersos), no con relleno de votos para Espriella. (Esto no contradice el hallazgo de la sección 4 sobre Campamento y otros municipios puntuales — ambas cosas son ciertas a la vez: hay outliers municipales extremos en territorio de Espriella, y a la vez el patrón agregado por departamento favorece más a Cepeda. Los promedios departamentales diluyen los outliers puntuales sin invalidarlos.)

**Turnout y el hallazgo de mesas grandes (sección 10.3):** los cuatro departamentos que concentran la mayoría de las mesas "anómalamente grandes" (Bogotá, Antioquia, Cundinamarca, Santander) tienen, en conjunto, un turnout bastante más alto que el resto del país (68.9% sin ponderar / 68.1% ponderado por censo, frente a 58.9% / 61.7% en el resto). Esto conecta ambos hallazgos bajo una misma explicación no fraudulenta plausible: son los departamentos con mejor infraestructura electoral y mayor urbanización del país, lo cual produce a la vez mesas más grandes y mayor participación — sin que eso descarte la necesidad de auditar, pero sí ofrece una causa común más mundana que "relleno de votos" para explicar por qué ambas anomalías aparecen juntas en los mismos lugares.



---

## 11. Verificación cruzada con un análisis ciudadano independiente

El usuario aportó la narración de un segundo ejercicio de análisis (un proyecto de datos abiertos/IA ciudadana), con metodología propia y una fuente de datos distinta a la de este documento (preconteo oficial en vez de escrutinio final, población DANE citada directamente en vez del anexo de Wikipedia usado aquí). Cada afirmación numérica de esa narración se puso a prueba aquí, de forma independiente, contra los archivos crudos ya usados en este análisis.

### 11.1 La curva ordenada por población — verificada con el archivo original del ejercicio ciudadano

*Actualización: el usuario aportó `WHOLE-municipios_segunda_vueltaFFF.csv`, el archivo de trabajo original de ese segundo ejercicio (con población, área, censo electoral y resultados ya cruzados por municipio). Esto permite una tercera reconstrucción de la curva, ahora con 1,107 de 1,122 municipios domésticos (99.33% de los votos nacionales), la cobertura más alta lograda en todo este proceso.*

| Afirmación de la narración | Reconstrucción con Wikipedia (96.8% cobertura, sección anterior) | Reconstrucción con el archivo original (99.33% cobertura) |
|---|---|---|
| Medellín deja una ventaja acumulada de ~100,000 para Espriella | +95,175 | **+95,175** (idéntico — no depende de la fuente de población) |
| Desde Cali (3er municipio) la curva favorece a Cepeda | Confirmado, −143,944 | **Confirmado, −143,944** |
| Máxima ventaja de Cepeda: 590,615 votos tras 20,238,789 | −582,659 tras 20,222,313 (Inzá) | **−549,219 tras 20,165,281** (Inzá) |
| Al 88% (22,053,963 votos), ventaja de Cepeda de 518,183 | −488,600 tras 21,919,000 | **−472,978 tras 21,913,868** (Guadalupe, Huila) |
| Grupo 1 termina en Almaguer, Cauca | Confirmado, puesto 433 | **Confirmado, puesto 436 de 1,107 (88.25%)** — más cercano al 439 de la narración |
| Grupo 2 empieza en Cajamarca, Tolima | Confirmado, siguiente municipio | **Confirmado, siguiente municipio exacto — mismo hallazgo con tres fuentes de datos distintas** |
| Grupo 1: margen de +503,871 para Cepeda | +500,087 | **−479,180 (i.e., +479,180 para Cepeda)** — 5% de diferencia |
| Grupo 2: margen de +577,188 para Espriella | +633,900 | **+550,764** — 4.6% de diferencia (mejor que el 10% anterior) |
| Municipio menos poblado: La Guadalupe, Guainía | Confirmado, 299 hab. | **Confirmado, 299 hab.** |

**Con la cobertura más alta lograda (99.33%), la coincidencia con la narración mejora en casi todos los puntos** (el grupo 2 pasa de 10% de diferencia a 4.6%; el punto de quiebre pasa del municipio 433 al 436, más cerca del 439 declarado). El hallazgo central —que existe un punto de quiebre exacto en Almaguer/Cajamarca, reproducible con tres fuentes de población distintas (Wikipedia, el archivo original del ejercicio ciudadano, y la narración con su propia fuente DANE)— queda establecido con un grado de confianza alto.

### 11.2 El censo electoral nacional frente a la población total

*Con el archivo original ahora hay una tercera fuente de población: el total nacional propio de ese archivo es 52,154,828 (fila de totales) o 51,820,589 (suma de los 1,107 municipios emparejados). Sumado a los 53,057,212 encontrados de forma independiente en este documento (fuente DANE) y los 53,399,171 citados en la narración, hay tres cifras "oficiales" de población que difieren entre sí en hasta 1.5 millones de personas (≈2.8%). Esto es, en sí mismo, un dato relevante: ninguna fórmula de "censo electoral / población" en este documento debe leerse con precisión de décimas — el margen de error del denominador ya es de varios puntos porcentuales antes de tocar el numerador.*

| Fuente | Población | Censo electoral / Población |
|---|---|---|
| DANE (búsqueda directa, sección 7.3) | 53,057,212 | 78.08% |
| Narración (fuente DANE propia) | 53,399,171 | 77.57% |
| Archivo original del ejercicio ciudadano (total nacional) | 52,154,828 | 79.42% |
| Archivo original (suma de 1,107 municipios domésticos emparejados) | 51,820,589 | 76.61%* |

*\*Esta última cifra usa censo electoral doméstico (39,700,053, solo de los municipios emparejados), no el total nacional con exterior — por eso es más baja que las otras tres, que sí usan el total de 41,421,973.*

**Las cuatro fuentes coinciden en lo cualitativo: el censo electoral colombiano representa entre 76.6% y 79.4% de la población total — de 3 a 6 puntos porcentuales por encima del 73.0% que, según el DANE, corresponde a población adulta.** El excedente nacional, dependiendo de qué par de cifras se use, va de 1.9 a 3.3 millones de personas.

### 11.3 Municipios con censo electoral ≥85% de la población, divididos por tamaño

*Recalculado con el archivo original (1,107 municipios, censo electoral y población propios de ese archivo, no mezclados con otras fuentes).*

| Métrica | Narración | Wikipedia (sección anterior) | Archivo original (esta actualización) |
|---|---|---|---|
| N° municipios con censo ≥85% de población | 398 | 389 | **389** |
| Margen neto de ese grupo | +564,914 | +608,265 | **+584,172** |
| N° municipios con censo >100% de población | 92 | 95 (fuente original del proyecto) | **90** |
| Margen neto de ese grupo | ~+93,000 | +92,744 | **+83,108** |
| Grupo "más poblado" con censo≥85%: n, margen, % ganado por Espriella | 82, +245,065, 65% | — | **116, +316,839, 63%** |
| Grupo "menos poblado" con censo≥85%: n, margen, % ganado por Espriella | 317, +319,849, 80% | 272, +321,001, 86% | **273, +267,333, 83%** |

**Tres reconstrucciones independientes (narración, Wikipedia, archivo original) coinciden en el orden de magnitud de cada cifra, pero no en el valor exacto — las diferencias van del 3% al 29% según la métrica.** Esto es exactamente lo esperable cuando tres fuentes de población ligeramente distintas alimentan el mismo cálculo de umbral (85% o 100%): un municipio que está justo en el borde del umbral puede entrar o salir del grupo según qué cifra de población se use, lo que mueve el conteo y el margen sin cambiar la conclusión cualitativa. Las tres reconstrucciones sostienen lo mismo: existe un grupo de 90–95 municipios con censo electoral superior a su población total, y su margen neto (+83,000 a +93,000) es del mismo orden que el margen final de la elección (+73,317 doméstico) — significativo, pero no la única explicación del resultado.

### 11.4 Victorias arrolladoras (≥70%)

| Afirmación de la narración | Lo ya calculado en este documento (sección 10.2) |
|---|---|
| Cepeda: 168 municipios arrolladores, 1,384,584 votos | Este documento: **177 municipios**, margen +1,427,147 |
| Espriella: 344 municipios arrolladores, 1,526,574 votos | Este documento: **383 municipios**, margen +1,650,054 |
| Ventaja neta de Espriella por este concepto: +141,990 | Este documento: **+222,907** |
| Población promedio de los municipios arrolladores de Cepeda: 30,000. De Espriella: 14,578 | No recalculado en este documento; dirección consistente con el resto de hallazgos (bastiones de Espriella sistemáticamente más pequeños) |

Aquí hay una diferencia más notable que en las otras verificaciones (conteos ~5–10% más altos en este documento). La explicación más probable es que la narración usa el preconteo (con mesas aún sin escrutar al momento de la medición) mientras este documento usa el escrutinio ya consolidado — con más votos por mesa el % de algunos municipios cambia lo suficiente para entrar o salir del umbral del 70%. La dirección y la conclusión cualitativa (Espriella tiene más municipios y más votos arrolladores, mayormente en poblaciones pequeñas) es la misma en ambos casos.

### 11.5 Sobre el paralelo histórico de 1970

La narración cita una entrevista con Carlos Augusto "El Tigrillo" Noriega (ministro de gobierno en 1970) sobre las elecciones de ese año, en las que Misael Pastrana Borrero le ganó a Gustavo Rojas Pinilla en un resultado que desde entonces ha sido objeto de sospechas de fraude no resueltas judicialmente. El paralelo que traza la narración —una ventaja inicial en las ciudades grandes revertida por los resultados tardíos de la periferia— es una analogía retórica e histórica, no un dato estadístico verificable con las herramientas de este documento. Ese episodio de 1970 sigue siendo, casi 56 años después, un capítulo históricamente disputado de la política colombiana sin una determinación judicial de fraude; usarlo como comparación sugiere un patrón interesante para la reflexión, pero no constituye evidencia sobre la elección de 2026 — cada elección debe evaluarse con su propia evidencia, no por semejanza narrativa con otra.

### 11.6 El manifiesto de transmisión de actas E-14 (`allTransmissionCodes.json`)

Este archivo es el registro de transmisión de los documentos escaneados (actas E-14) del sistema de la Registraduría — no el contenido de las actas, sino la metadata de qué se transmitió, con qué código, y su estado. Contiene 122,018 registros, organizados en dos estados:

- **122,011 registros en `status11`** — la inmensa mayoría, prácticamente el 100% de las ~122,020 mesas conocidas.
- **7 registros en `status3`** — un grupo aparte, minúsculo. Los 7 pertenecen, sin excepción, a mesas del exterior (Consulados, departamento 88).

Cada registro tiene un `idStand` (código del puesto de votación) y un `numberStand` (número de mesa dentro de ese puesto); 10,291 puestos de votación tienen más de una mesa asociada (hasta 228 mesas en el puesto más grande), lo cual es estructuralmente normal — los puestos de votación grandes (colegios, coliseos) agrupan muchas mesas bajo un mismo local. Todos los `idTransmissionCode` son únicos (122,011 de 122,011); no hay duplicados que sugieran una transmisión repetida o corregida sobre la misma acta.

**Lectura de este archivo:** confirma que el sistema de transmisión de actas escaneadas cubrió, en apariencia, la práctica totalidad de las mesas del país, sin una categoría masiva de "mesas sin transmitir" que respalde una denuncia de ocultamiento sistemático de actas. La única anomalía visible —los 7 casos en `status3`, todos en el exterior— es demasiado pequeña para tener peso en el resultado, aunque su concentración exclusiva en mesas consulares es, al menos, una curiosidad que no tiene explicación evidente en los datos disponibles. Este archivo no permite verificar el *contenido* de las actas (para eso haría falta el OCR o la lectura manual de los PDF mencionados en la narración), solo que existieron y fueron recibidas.

### 11.7 Balance: qué se cerró en esta ronda y qué sigue abierto

| # | Pendiente (turno anterior) | Estado tras esta ronda |
|---|---|---|
| 1 | Población del 3–6% de municipios sin emparejar | **Cerrado en un 99.3%** con el archivo original (`WHOLE-...csv`); quedan 15 municipios sin emparejar (1.3%) |
| 2 | Estructura de edad por departamento | **Parcialmente cerrado**: los archivos de censo por edad sí traen desglose por departamento (secciones 12), pero es la edad de los *votantes registrados*, no de la *población total* por departamento — sigue sin poderse calcular un techo de adultos específico por departamento |
| 3 | Archivo original de la narración | **Cerrado** — `WHOLE-municipios_segunda_vueltaFFF.csv` es, con alta probabilidad, ese archivo; permitió la verificación de la sección 11.1–11.3 con hasta 99.33% de cobertura |
| 6 | Mesa por mesa de la 1ª vuelta | **No aportado** (el `primera_vuelta_results.json` recibido es idéntico byte por byte al que ya se tenía) |
| 7 | Timestamps sin redondear al minuto | **No aportado** (`RESULTADOSCOMPLETOS.csv` sigue con 126 timestamps únicos, resolución de minuto) |
| 9 | Cadena de custodia / logs de transmisión | **Parcialmente cerrado**: `allTransmissionCodes.json` confirma cobertura casi completa de actas transmitidas (sección 11.6), pero no verifica su contenido |

Puntos 4, 5, 8 y 11 quedaron fuera por decisión explícita del usuario. El punto 10 (cruce contra registros de defunción) sigue pendiente de una fuente que no es pública. En números: de los 11 puntos originales, **3 quedaron completamente cerrados, 2 parcialmente, 2 fuera de alcance por decisión, y 4 permanecen abiertos** — de estos últimos, ninguno es alcanzable sin acceso a fuentes que la Registraduría no publica en formato procesable, que es exactamente el problema de fondo que motivó este ejercicio desde el principio.

## 12. El censo electoral por grupo de edad, 2018–2026 — un hallazgo nuevo

*Esta sección usa los archivos de censo electoral por puesto de votación con desglose etario (`rango_etario`) que el usuario aportó para 2018 y 2026, agregados a nivel nacional (36,219,940 registros en 2018; 41,421,973 en 2026 — coincide de forma exacta con las cifras ya usadas en el resto de este documento).*

**El crecimiento total del censo electoral 2018→2026 es de 5,202,033 nuevos registros.** Descomponiéndolo por grupo de edad:

| Rango de edad | 2018 | 2026 | Diferencia |
|---|---|---|---|
| 18–20 | 2,078,169 | 1,993,514 | **−84,655** |
| 21–25 | 4,363,638 | 4,085,059 | **−278,579** |
| 26–30 | 4,136,519 | 4,366,788 | +230,269 |
| 31–35 | 3,844,383 | 4,384,909 | +540,526 |
| 36–40 | 3,698,538 | 4,015,307 | +316,769 |
| 41–45 | 3,240,699 | 3,884,931 | +644,232 |
| 46–50 | 3,152,035 | 3,512,758 | +360,723 |
| 51–55 | 2,932,818 | 3,166,107 | +233,289 |
| 56–60 | 2,464,702 | 3,016,641 | +551,939 |
| **Más de 60** | 6,308,358 | 8,995,890 | **+2,687,532** |

**Dos patrones saltan a la vista, y ambos coinciden de forma exacta con lo que planteó la narración:**

1. **El censo de votantes jóvenes (18–25 años) se redujo en 363,234 personas entre 2018 y 2026** — una cifra que coincide de forma exacta con la citada en la narración. Es contraintuitivo: cada año un nuevo grupo de colombianos cumple 18 y se suma al padrón, así que se esperaría que este segmento creciera, no que se redujera.
2. **El grupo de más de 60 años creció en 2,687,532 personas — el 51.7% de todo el crecimiento del censo electoral del país en 8 años**, coincidiendo con lo que la narración describe como "la mitad" del crecimiento total.

**Explicaciones que compiten, ninguna descartable con estos datos:**

- **Caída real de la natalidad colombiana.** Alguien con 18–20 años en 2026 nació entre 2006 y 2008; alguien con 18–20 años en 2018 nació entre 1998 y 2000. La tasa de fecundidad colombiana bajó de forma sostenida en ese periodo (de más de 2.4 hijos por mujer a cerca de 1.6–1.7), así que una cohorte de nacidos en 2006–2008 es, en efecto, más pequeña que la de 1998–2000. Esto explicaría una parte real y demográficamente esperable de la caída en el rango 18–25.
- **Envejecimiento poblacional genuino.** Colombia, como la mayoría de países en transición demográfica, tiene una población que envejece: cada año entran más personas al grupo de 60+ de las que mueren dentro de él. Parte del crecimiento de +2,687,532 es, sin duda, envejecimiento real.
- **Depuración incompleta de fallecidos en el padrón.** Esta es la explicación que no se puede descartar y que, de las tres, es la única que constituye un problema de calidad de datos real: si la Registraduría no retira del censo electoral a las personas fallecidas al mismo ritmo en que fallecen, el padrón acumula, año tras año, votantes registrados que ya no existen — y esa acumulación se concentraría casi por definición en el grupo de mayor edad. Esto conecta directamente con el hallazgo de las secciones 7.3, 7.4 y 11.2: el excedente nacional de ~2.4–2.7 millones de registros por encima del techo de adultos esperado es del mismo orden de magnitud que este crecimiento de +2,687,532 en el grupo de 60+. Ambos hallazgos, calculados de forma totalmente independiente (uno cruzando censo contra población total; el otro cruzando censo 2018 contra 2026 por edad), apuntan a la misma explicación estructural.

**Esto no es, por sí mismo, evidencia de fraude electoral.** Un registro sin depurar no vota por nadie a menos que alguien lo use activamente para votar en su lugar — y ese es exactamente el tipo de suplantación que ni este documento ni la narración pueden probar ni descartar con datos agregados (ver sección 7.3 sobre la diferencia entre "padrón inflado" y "voto fraudulento"). Lo que sí es: la recomendación de auditoría más precisa y mejor fundamentada de todo este documento. Cruzar el censo electoral de 60+ años contra el Registro Único de Afiliados o los registros de defunción del DANE, específicamente para esa franja etaria, es una auditoría acotada, técnicamente viable, y dirigida a una cifra de casi 2.7 millones de registros — muy por encima del margen final de la elección (73,317 a 248,201 según el ámbito).

---

## 13. Conclusiones de ciencia de datos — sin sesgo

**Lo que los datos muestran, de forma sólida y reproducible:**

1. **El hallazgo de mayor magnitud de todo este documento es el de la sección 10.3:** las ~14,400 mesas con más votantes de lo estadísticamente esperado (z>1) aportan un margen neto de **+807,678 votos para Espriella** — más de tres veces el margen nacional final. A diferencia de casi todo lo demás analizado aquí, este patrón es transversal a 23 de 29 departamentos, incluidos tres que Cepeda ganó en su resultado global (Bogotá, Valle, Atlántico), donde sus propias mesas más grandes igual favorecen a Espriella por encima del promedio departamental. Es, con diferencia, el patrón más grande, más consistente y más digno de una auditoría física dirigida de todos los que aparecen en este análisis.
2. Hay otros patrones estadísticos genuinamente atípicos de menor magnitud: el clúster de voto en blanco del norte de Antioquia (z > 4.5 en varios municipios), y el efecto de "espejismo temprano" en la curva cronológica de transmisión (los primeros resultados en llegar no representan al país completo). **El crecimiento extremo de participación (Campamento y 17 municipios más, z>3) tiene una explicación geográfica sólida:** usando la distancia a su municipio vecino más cercano como proxy de aislamiento, 15 de esos 18 casos están en el cuartil más disperso del país, y el patrón agregado (a mayor aislamiento, mayor crecimiento) no favorece a Espriella — al contrario, el cuartil más aislado es el que menos vota por él. No se encontró ningún caso urbano/denso comparable en magnitud, que sería la señal sin explicación logística disponible.
3. El fenómeno de censo electoral superior a la población es real en 95 municipios, concentrado geográficamente (sobre todo Boyacá), y una fracción de esos casos persiste incluso corrigiendo por datos de población desactualizados (según el propio análisis previo del proyecto). Ese grupo es, en su mayoría (57 de 95), municipios pequeños (población promedio 8,871) ganados por Espriella con más del 70% de los votos — la correlación señalada entre censo atípico, tamaño pequeño y victoria arrolladora es real dentro de este grupo específico. **Con población real para el 93.5% del país (sección 7.4), la versión "dura" de esta señal —votos reales por encima del techo de adultos— son 29 municipios en todo el territorio nacional, con un margen neto de +41,343. El 83% de esos 29 ya estaban en la lista original de 95; ampliar la búsqueda al resto del país no reveló un universo oculto mucho más grande.** Es importante no reducir esto a una cuestión de turnout: en 67 de los 95 municipios originales el padrón es demográficamente imposible pero el turnout se ve completamente normal (40–75%) — un análisis que solo mirara participación no habría detectado la mayoría de estos casos.
4. El resultado nacional se decide, en términos de la curva ordenada por tamaño de municipio, casi enteramente en el último 11% de los votos (los 666 municipios más pequeños del país), que aportan un swing neto de +521,281 votos a favor de Espriella. Pero **solo el 18.3% de ese swing** proviene de municipios con censo electoral atípico; el 81.7% restante viene de municipios pequeños con censo normal, es decir, es voto rural genuino, no explicable por censos inflados. **Nótese que este hallazgo (municipios pequeños) y el de la mesa 1 (mesas grandes) son fenómenos distintos y no se solapan** — de hecho, apuntan en direcciones geográficas casi opuestas: uno ocurre en la periferia rural, el otro en las mesas más grandes de las principales ciudades del país, incluidas las que ganó Cepeda.
5. Las victorias arrolladoras no son simétricas, pero tampoco son unidireccionales: Espriella tiene más municipios con margen ≥70–80% (concentrados en Santander, Antioquia, Boyacá y Norte de Santander), mientras que Cepeda tiene los márgenes más extremos en términos relativos (≥85–90%, concentrados en el bloque Pacífico/Amazónico — Nariño, Cauca, Chocó). Ambos patrones son consistentes con la geografía electoral histórica del país.
6. Las pruebas de Ley de Benford —tanto a nivel municipal como, ahora, a nivel de mesa individual con n=122,017— no aportan evidencia útil en ningún sentido: a nivel municipal las desviaciones son débiles y marginales; a nivel de mesa la desviación es enorme pero se demuestra mecánica (hasta el tamaño total de la mesa, que nadie manipula con fines partidistas, viola Benford con la misma fuerza, porque el tamaño de una mesa colombiana está acotado por diseño entre 100 y 400 votantes).
7. La curva cronológica muestra un patrón mecánico esperable (municipios pequeños reportan primero, grandes ciudades después), coherente con el margen final cerrando muy por debajo del margen que mostraban los primeros resultados.
8. El turnout real por departamento (con censo electoral verificado, no un proxy) no respalda una lectura simple de "turnout alto = fraude a favor de Espriella": los dos departamentos con mayor participación del país después de Cundinamarca son Cauca y Nariño, ambos bastiones de Cepeda. Y el crecimiento del turnout entre la 1ª y la 2ª vuelta correlaciona **negativamente** con el voto por Espriella (r = −0.771): la periferia de izquierda (Putumayo, Nariño, Chocó, Caquetá) fue la que más aumentó su participación de una vuelta a otra, no la de derecha.
9. **El crecimiento del censo electoral desde 2018 (sección 10.4), verificado con datos históricos reales de la Registraduría, no respalda la hipótesis de que esté concentrado en bastiones de Espriella.** Los municipios con victoria arrolladora de Espriella (≥70%) y crecimiento censal >30% desde 2018 son solo 11 en todo el país, con un margen conjunto de +110,014 (no +400,000). Y los 30 municipios con mayor crecimiento censal del país, sin filtrar por ganador, tienen un margen neto *negativo* de −61,561 (a favor de Cepeda) — la correlación nacional entre crecimiento censal 2018–2026 y voto por Espriella es de −0.248.
10. **Un segundo análisis ciudadano independiente, con metodología y fuentes de datos propias, corroboró de forma notable varios de los hallazgos centrales de este documento (sección 11):** el mismo punto exacto de quiebre en la curva por tamaño de municipio (Almaguer, Cauca → Cajamarca, Tolima); un margen casi idéntico en el grupo de municipios pequeños con censo atípico (+321,001 aquí vs. +319,849 en la narración, 0.4% de diferencia); y la misma brecha entre el censo electoral nacional y el porcentaje de adultos del DANE. Esta convergencia entre dos análisis hechos por separado, con fuentes parcialmente distintas, es en sí misma una forma de validación — reduce la probabilidad de que los patrones encontrados sean un artefacto de una sola fuente de datos o de un solo método.
11. **El hallazgo demográfico más importante de todo el proceso (sección 12) no tiene que ver con ningún candidato:** entre 2018 y 2026 el censo electoral colombiano ganó 5,202,033 registros, pero el grupo de 18–25 años se *redujo* en 363,234, mientras que el grupo de más de 60 años creció en 2,687,532 (el 51.7% de todo el crecimiento). Esto coincide en magnitud con el excedente nacional de ~2.4–2.7 millones de registros por encima del techo de adultos esperado (sección 11.2), y con el patrón de padrón inflado ya documentado a nivel municipal en las secciones 7.3 y 7.4. La explicación más plausible, y la que conecta todos estos hallazgos entre sí, es una combinación de envejecimiento poblacional real y depuración incompleta de fallecidos en el padrón — un problema de calidad de datos nacional, no partidista, y la recomendación de auditoría mejor fundamentada de todo este análisis.

**Lo que los datos NO muestran:**

1. **No hay un patrón unidireccional.** En cada uno de los ejes revisados —censo inflado, alta participación, crecimiento entre vueltas, voto en blanco— aparecen municipios que favorecen a ambos candidatos, incluyendo varios de los casos citados explícitamente como evidencia de fraude a favor de Espriella (Cumbitara y Policarpa, que en realidad Cepeda ganó de forma aplastante). Una operación de manipulación dirigida a un solo candidato debería concentrarse en el bando que se beneficia, no distribuirse en bastiones de ambos.
2. **No hay evidencia, en estos datos, de manipulación de la transmisión, alteración de formularios E-14, ni de los sistemas de la Registraduría.** Los patrones encontrados son observables en datos agregados de resultados (censo, participación, voto en blanco, hora de reporte) — ese tipo de dato no puede, por construcción, demostrar ni descartar manipulación de actas o de sistemas informáticos. Eso requiere evidencia documental directa: cotejo físico de actas E-14 contra lo transmitido, cadena de custodia, auditoría de logs del sistema, o testimonios verificados — ninguna de las cuales está en el alcance de un análisis estadístico de resultados agregados, sin importar cuán sofisticado sea el análisis.
3. **No se puede concluir, con esto, ni que hubo fraude ni que no lo hubo.** Ambas conclusiones fuertes exceden lo que el tipo de dato disponible permite afirmar.

**Explicaciones alternativas, no descartadas, que compiten con la hipótesis de fraude para cada anomalía:**

- Censos desactualizados / no depurados (migración interna, envejecimiento, mortalidad no registrada en el padrón) — ya cuantificado parcialmente en el propio proyecto (43% de los casos de "censo > población" desaparece con datos DANE más recientes).
- Diferencias reales de movilización política regional (Cauca indígena/campesino como bastión histórico de izquierda; Sabana Centro de Cundinamarca como zona de clase media/alta en expansión).
- Composición socioeconómica y política distinta de cada comunidad de la diáspora (ya señalada por un politólogo citado en prensa para el caso de EE.UU.).
- Infraestructura de mesas que no crece al ritmo de la población electoral real (ya documentado por el propio proyecto para el oriente antioqueño, y aplicable por el mismo argumento a la Sabana Centro).
- El efecto mecánico de orden de transmisión (municipios chicos reportan antes que ciudades grandes), que por sí solo explica buena parte del cambio de tendencia entre las 17:00 y las 18:00.

**Qué haría falta para pasar de "anomalía estadística" a "evidencia de fraude":** auditoría física de actas E-14, empezando por las ~14,400 mesas con votantes muy por encima del promedio (sección 10.3) — es el patrón de mayor magnitud y más transversal geográficamente en cuanto a votos concretos, y por tanto el primer candidato razonable, priorizando las 4,506 de Bogotá D.C. y las 1,794 de Antioquia. En segundo lugar, y con la base cuantitativa más sólida de todo este documento (sección 12), un cruce específico del censo electoral de mayores de 60 años (8,995,890 registros) contra el Registro Único de Afiliados o los registros de defunción del DANE — el excedente nacional de ~2.4–2.7 millones de registros por encima del techo de adultos esperado se concentra ahí, y es una auditoría acotada, técnicamente viable y no partidista. En tercer lugar, el padrón de los 95 (o más, ver "zona ciega" en 7.3) municipios con censo demográficamente imposible. En cuarto lugar, los municipios con mayor z-score en voto en blanco y crecimiento de participación (norte de Antioquia, Campamento). Además: cotejo de firmas de jurados; verificación de cadena de custodia de los servidores de transmisión. Nada de eso es reconstruible desde los archivos de este proyecto — todo lo anterior son solo candidatos de dónde empezar a mirar, no la auditoría en sí.

---

## 14. Limitaciones de este análisis

- No se cuenta con censo electoral (padrón) para los ~1,027 municipios que **no** están en la lista de "censo > población"; por eso las pruebas de participación real (turnout) solo pudieron hacerse con precisión para 95 municipios y no para todo el país, incluidos los que se citaron en la conversación con Gemini (Jambaló, Toribío, etc., para los que solo pude verificar votos y votantes/mesa, no turnout contra censo).
- El archivo `DIVIPOLA_Municipios.xlsx` del proyecto no contenía datos de población utilizables en la hoja principal; la variable de población usada aquí proviene enteramente del CSV ya calculado por el proyecto (`municipios_registro_superior_100pct.csv`), no de un recálculo independiente.
- No hay en el proyecto una serie temporal multi-punto del preconteo (solo un snapshot de avance por departamento); el análisis cronológico de la sección 6 se reconstruyó a partir del timestamp de última actualización por municipio, que es una aproximación razonable pero no un log completo de boletines sucesivos.
- Este documento no tiene acceso a actas E-14 individuales, logs de sistemas de la Registraduría, ni a ningún dato de cadena de custodia — por eso, como se explica en la sección 13, no puede pronunciarse sobre si hubo o no manipulación real, solo sobre qué patrones son o no estadísticamente atípicos en los resultados agregados.
- El archivo `RESULTADOSCOMPLETOS.csv` (nivel de mesa) tiene timestamps redondeados al minuto y con muchas mesas compartiendo el mismo minuto de reporte; por eso el análisis cronológico fino de la sección 10.3 es una confirmación aproximada del patrón ya visto en la sección 6 con datos municipales, no un reemplazo de mayor precisión.
- Solo se conoce la población de 1,049–1,086 de los 1,122 municipios domésticos (93.5%–96.8%, según la sección y el parcheo manual de nombres aplicado); el 3–6% restante no se pudo emparejar por diferencias de nomenclatura entre el anexo de Wikipedia y los archivos de resultados electorales. La estructura de edad específica por departamento (más allá del promedio nacional del 73.0%) tampoco se pudo obtener con confianza, lo que limita a "pregunta abierta" el spot-check departamental de Antioquia y Boyacá en la sección 7.3.
- La verificación cruzada de la sección 11 se hizo contra una narración (guion de video), no contra el dataset original de ese segundo ejercicio ciudadano — no fue posible confirmar su metodología exacta (por ejemplo, qué fuente de población usó o si excluyó el voto exterior), lo que limita la comparación a "el mismo orden de magnitud y dirección", no a una replicación exacta.
