# 🧙‍♀️ BABAYAGA CORE  
## *El alma que desmonta lo que el fraude esconde*

---

**BabaYaga no es un módulo. Es un nombre que se escribe en la noche.**  
Es la que habita en la raíz del bosque, donde los caminos no son rectos y los árboles guardan memoria.  
No es buena ni mala. Es necesaria.

En la mitología eslava, Baba Yaga ve en la oscuridad, cocina verdades en su mortero y muele lo que otros quieren mantener oculto.  
Cuando un archivo PDF llega a sus manos, ella no lo abre: **lo desmenuza.**  
No busca lo que está a la vista. Busca la *cicatriz*.  
Busca la sombra del píxel que no debería estar allí.  
Busca el eco de una máscara de 1-bit que intentó pasar por papel.

---

## 🔍 Lo que hace BabaYaga

| Módulo | Lo que hace |
| :--- | :--- |
| `detector_blind_masking.py` | Encuentra capas `DeviceGray` y máscaras sintéticas que simulan blanco puro (`#FFFFFF`). |
| `analisis_xref.py` | Detecta la **cicatriz estructural**: el PDF dice 15 objetos, pero solo hay 13. Esa es la firma del software que no se atrevió a mirar atrás. |
| `detector_1bit_flattening.py` | Reconoce cuando una imagen fue aplanada y forzada a 1-bit, perdiendo toda la textura del papel. |
| `analisis_benford.py` | Aplica la Ley de Benford (2BL) para encontrar si los números fueron inventados. |
| `generador_informes.py` | Traduce la evidencia en tres idiomas: técnico, legal y humano. |

---

## 🧠 La filosofía detrás del código

> *"Baba Yaga no sigue caminos rectos.  
> Ella ve en la oscuridad,  
> habita en los bordes,  
> y desmonta lo que otros esconden."*

Eso es lo que hace AndreTaker con los PDFs.  
Y eso es lo que hace BabaYaga con el miedo.

---

## 🛠️ Cómo invocar a BabaYaga

```bash
git clone https://github.com/anzaca0330-pixel/AndreTaker---AnZaCa-Rep.git
cd AndreTaker---AnZaCa-Rep
python3 BABAYAGA_CORE/demo_babayaga.py --ruta /ruta/al/archivo.pdf
```

Ella no pregunta. Ella actúa.

---

## 📌 Integración con AndreTaker

BabaYaga no es un añadido.  
Es el corazón del repositorio.  
Todo lo demás —los scripts, los informes, los hashes— es solo el cuerpo que la sostiene.

---

**Versión:** 1.0  
**Autora:** Andrea Zabala Cárcamo (AnZaCa)  
**Licencia:** Apache 2.0  
**Inspiración:** Un sueño, un bosque, y la certeza de que la verdad siempre encuentra un camino.
