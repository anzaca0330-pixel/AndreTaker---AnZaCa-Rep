# 🛡️ MANUAL DE EVASIÓN DE FILTROS ALGORÍTMICOS & SHADOWBAN
## Protocolos Técnicos de Inmunización para Publicación en Redes Sociales

Si tus cuentas están sufriendo de **Shadowban**, **reducción forzada de alcance** o **bloqueo estático de enlaces y palabras clave**, aplica las siguientes 4 técnicas de evasión comprobadas de **BaBaYaga Core**:

---

### 🥷 1. Técnica de Ancho Cero (Zero-Width Invalidation):
Las plataformas emplean bots de scraping (Regex) que buscan cadenas como `github.com`, `duckdns.org` o `andretaker`.
* **Cómo funciona:** Nuestro script [`anti_filter_obfuscator.py`](BABAYAGA_CORE/anti_filter_obfuscator.py) inserta caracteres invisibles de ancho cero (`\u200B`) dentro de las palabras y enlaces.
* **Resultado:** Para el bot de filtrado de la red social, la palabra es irreconocible (ej: `g​ithu​b.com`), pero para el ojo humano se ve 100% idéntica y permite hacer clic sin ser bloqueada.

---

### 🖼️ 2. Eliminación de Hashing Perceptual en Imágenes (Exif & PDQ Hash):
Sistemas como Facebook/Instagram usan algoritmos (PDQ / Perceptual Hashing) para detectar imágenes que hayan sido censuradas anteriormente.
* **Solución:** Pasa las imágenes por el motor sanitizador de BaBaYaga Core:
  ```python
  from anti_filter_obfuscator import AntiFilterEngine
  AntiFilterEngine.sanitizar_imagen_media("mi_imagen.jpg", "imagen_inmune.jpg")
  ```
* **Efecto:** Elimina las coordenadas GPS, limpia marcas EXIF y altera imperceptiblemente la grilla de píxeles para generar una firma completamente nueva.

---

### 🌐 3. Estrategia de Enlace "Link in Bio" o Redirección Limpia:
* **Regla de Oro:** Evita poner el enlace directo en el cuerpo del Tweet/Post principal si la cuenta está bajo observación.
* **En su lugar utiliza:** *"Enlace directo en el primer comentario o en la biografía del perfil"*.

---

### 📢 4. Variación Dinámica de Hashtags:
* Intercala hashtags de alto tráfico neutro (`#DataScience`, `#OpenSource`, `#Python`, `#Tech`) con los hashtags del proyecto (`#AnZaCa`, `#AndreTaker`) para evitar que el algoritmo agrupe la cuenta en una categoría restringida.
