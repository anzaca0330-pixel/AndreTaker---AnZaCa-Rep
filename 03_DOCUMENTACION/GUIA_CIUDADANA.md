# ¿QUÉ LE HICIERON A NUESTROS VOTOS? 
**Explicación sencilla de las trampas informáticas en las actas electorales**

Para descubrir si un documento oficial ha sido alterado, los peritos informáticos miramos las "tripas" de los archivos, buscando huellas que las personas normales no ven a simple vista. 

Al analizar casi **1.700 actas de votación** de colombianos en Estados Unidos y España (representando más de un cuarto de millón de votos), encontramos tres trampas digitales gravísimas. Como los términos técnicos son complejos, aquí los explicamos con ejemplos de la vida diaria para que cualquier ciudadano los pueda entender y verificar.

---

### Trampa 1: El carro con el chasis borrado (Los Metadatos)
**El hallazgo técnico:** *El 100% de los archivos tienen los campos de Creación y Origen vacíos.*

**¿Qué significa en lenguaje sencillo?**
Imagina que te venden un carro "recién salido de la fábrica". Para comprobarlo, tú buscas el número de chasis, la marca del motor y la placa. Pero al revisar, te das cuenta de que alguien lijó los números del motor y arrancó las placas. 

Eso es exactamente lo que pasó con los archivos PDF de las actas. Todo escáner legítimo del gobierno le pone un "sello de fábrica" invisible al archivo (fecha exacta, marca del escáner, hora). Sin embargo, **el 100% de las actas de España y EE. UU. tienen esos sellos completamente borrados**. Esto no pasa por accidente; fue hecho a propósito por un programa de computadora para ocultar quién, a qué hora y con qué software manipularon el documento.

### Trampa 2: Los compartimentos falsos (La Estructura)
**El hallazgo técnico:** *El 100% de las actas tienen inyección de "Objetos Fantasma" (Shadow Attacks).*

**¿Qué significa en lenguaje sencillo?**
Volvamos al ejemplo del carro. Abres el baúl y ves que, aunque por fuera parece normal, le soldaron compartimentos falsos (doble fondo) para esconder cosas. El manual del carro dice que tiene 5 partes, pero tú cuentas 8. 

En los archivos de las elecciones, el sistema oficial dice que el documento tiene solo 3 páginas normales. Sin embargo, nuestros programas descubrieron que **alguien inyectó "páginas invisibles" adicionales en las tripas del archivo**. Le metieron un doble fondo a los documentos de los votos. Un escáner normal de una oficina jamás hace eso; solo un falsificador informático inyecta compartimentos ocultos en un archivo.

### Trampa 3: La cinta sobre el código de barras (El Código QR)
**El hallazgo técnico:** *En el 23% de los casos hubo supresión quirúrgica del QR mediante "Blind Masking" e imágenes sintéticas (grises puros de 1 bit).*

**¿Qué significa en lenguaje sencillo?**
Imagina que vas al supermercado a comprar leche. El cajero pasa la caja por el lector láser, pero la máquina no hace *¡BIP!*. Al mirar la caja, te das cuenta de que alguien pegó un cuadrito de cinta blanca exactamente sobre el código de barras. La fecha de vencimiento y el nombre de la leche se leen perfecto, pero la máquina no puede registrar el producto.

Eso le hicieron a miles de votos. La Registraduría utiliza Códigos QR en las actas para que las máquinas sumen los votos de forma automática y los ciudadanos puedan auditar rápidamente. Nosotros descubrimos que un programa de computadora pegó **un "cuadrito blanco" invisible exactamente sobre los Códigos QR** de cientos de mesas (afectando a unos 40.000 votos). A esto se le llama enmascaramiento ciego. 

En otros casos, en lugar de poner cinta blanca, imprimieron un código QR falso. ¿Cómo sabemos que es falso? Porque la tinta del mundo real siempre tiene manchitas microscópicas e imperfecciones, pero los QR que encontramos son matemáticamente puros, como si fueran fabricados dentro del mismo computador en lugar de haber sido escaneados del papel que firmaron los jurados.

---

### LA CONCLUSIÓN PARA TODOS
Si juntas las tres trampas, el resumen es este: **Las actas que el gobierno subió a internet para Estados Unidos y España no son simples fotografías o escaneos de lo que pasó el día de las elecciones.** 

Son documentos que pasaron por una especie de "Photoshop" masivo automatizado para borrarles la identidad, meterles páginas ocultas y taparles los códigos de seguridad para que nadie pudiera contarlos automáticamente. Y como el patrón es exactamente igual en ciudades que están a miles de kilómetros de distancia (Miami, Nueva York, Madrid, Barcelona), sabemos que no fue un error de los cónsules, sino **una trampa montada en el sistema central de recepción de los archivos.**
