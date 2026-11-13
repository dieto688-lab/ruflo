# ¿Por qué Napoleón no se detuvo cuando iba ganando?
### Documental animado estilo *History Matters* · ~3:40 · 1280×720 · 24 fps

**Archivos entregados:**
- `napoleon-video.mp4` — video final con narración y subtítulos (5,1 MB)
- `index.html` — versión interactiva con mapa animado sincronizado (servida en el puerto 8000)
- `audio/escena1-5.mp3` — narración por escenas · `audio-full.mp3` — narración completa
- `build_video.py` — script que genera el MP4 (PIL + ffmpeg)

---

## GUION COMPLETO (locución)

### Escena 1 · El imperio en su cima (0:00–0:35)
> En 1799, Europa era un puzzle de reyes que se odiaban. En 1812, Napoleón había redibujado el mapa: Prusia era un estado vasallo, Austria humillada, Italia y España bajo control francés, y su hermano José reinaba en Madrid. *Fun fact:* en su punto máximo gobernaba, directa o indirectamente, a más de cuarenta millones de personas. Entonces, ¿por qué no se detuvo? ¿Por qué no declaró la paz, se coronó, y vivió feliz para siempre? Porque su imperio tenía un problema de diseño: necesitaba guerras para sobrevivir.

**[MAPA: Europa 1799 gris → 1812 azul francés se expande]**

### Escena 2 · El obstáculo: Gran Bretaña (0:35–1:30)
> El problema tenía nombre: Gran Bretaña. Napoleón era un genio en tierra, pero el Canal de la Mancha era un muro de agua. La Royal Navy lo hacía imposible: intentar invadir Inglaterra era como intentar cruzar el océano en una bici. Así que Napoleón inventó el Sistema Continental: prohibió todo comercio británico en Europa para asfixiarlos económicamente. ¿Funcionó? No. Por tres razones. Uno: sus propios aliados hacían trampa. Portugal y Rusia siguieron comprando productos británicos en secreto. Dos: el contrabando. El azúcar y el café británicos entraban por mil puertos falsos, con permisos sobornados. Y tres: los británicos contra-bloquearon. Si tú no nos vendes, nosotros no te vendemos, y además te hundimos los barcos. En resumen: Napoleón bloqueó a Gran Bretaña, y Gran Bretaña le bloqueó a él. Solo que ella tenía barcos.

**[MAPA: barcos Royal Navy patrullando el Canal · iconos de contrabando]**

### Escena 3 · La paz que no duró (1:30–2:17)
> Hubo paz. La Paz de Amiens en 1802 duró apenas un año. ¿Por qué? Porque Napoleón no sabía estar quieto en tiempos de paz. Mientras firmaba tratados, anexaba Piamonte, intervenía Suiza, y coronaba a su hijastro en Italia. Para Austria y Prusia, el mensaje era claro: si hoy es tu vecino, mañana eres tú. Así que en 1805, Austria se unió a Rusia y Gran Bretaña. Napoleón ganó en Austerlitz, la victoria perfecta. Y en vez de parar... pidió más. En 1809, Austria volvió a atacar. Napoleón ganó en Wagram. Y volvió a pedir más. Cada victoria creaba la siguiente coalición. Era un ciclo: ganar, anexar, provocar, ganar otra vez.

**[MAPA: flecha circular GANAR→ANEXAR→PROVOCAR]**

### Escena 4 · Por qué no podía parar (2:17–2:59)
> ¿Por qué no podía parar? Tres motivos. Primero, su personalidad. Napoleón no veía límites: cada tratado era un alto en el camino, no un destino. Segundo: no tenía aliados, tenía vasallos. Prusia, Austria, Polonia... todos habían sido derrotados y humillados. Un aliado te apoya cuando pierdes. Un vasallo te abandona en cuanto huele derrota. Y tercero: miedo ideológico. Los reyes absolutistas de Europa veían a Napoleón como un virus. No era solo un general francés: era la Revolución exportada. Si sus pueblos veían que un plebeyo podía coronarse emperador, ¿qué les impediría intentarlo? Mejor derrotarlo que contagiarse.

**[MAPA: Francia azul rodeada de vasallos grises]**

### Escena 5 · Ofertas rechazadas y caída (2:59–3:40)
> Al final, hasta le ofrecieron salir con vida. En 1813, en Fráncfort, la Coalición le ofreció la paz con las fronteras de 1792: Francia grande, pero sin hegemonía. Napoleón dudó... y rechazó. En 1814, en Châtillon, le ofrecieron lo mismo. Rechazó otra vez. Creía que aún podía ganar. No podía. En 1815, tras Waterloo, abdicó y los británicos lo exiliaron a Santa Elena, una isla perdida en el Atlántico Sur. Europa volvió a ser un puzzle de reyes. La lección: Napoleón no perdió porque fuera malo. Perdió porque nunca supo cuándo había ganado.

**[MAPA: azul se encoge a Francia → punto rojo en Santa Elena]**

---

## PROMPTS DE IMAGEN/VIDEO (inglés, para Sora / Runway / Pika)

| Escena | Prompt técnico |
|---|---|
| 1 | `2D minimalistic historical map of Europe 1799 vs 1812, flat vector style, parchment background, France in blue expanding over gray kingdoms, smooth color-fill animation, History Matters style, 16:9` |
| 2 | `2D flat vector animation of the English Channel, Royal Navy warships patrolling, red Great Britain island, blue France blocked by ships, smuggling boats sneaking at night, minimalistic educational style` |
| 3 | `2D animated map loop showing victory-annexation-provocation cycle, arrows forming a circle over Central Europe, Austerlitz 1805 and Wagram 1809 battle markers, flat vector, parchment style` |
| 4 | `2D flat vector map of Napoleonic Europe, blue France surrounded by gray vassal states, crown icons, ideological virus spreading, minimalistic History Matters style` |
| 5 | `2D flat vector map of Europe 1815, blue shrinking to France only, red dot on remote Saint Helena island in South Atlantic, Waterloo battle marker, parchment background, smooth animation` |

## Cómo regenerar el MP4
```bash
python3 video-napoleon/build_video.py
# Requiere: pip install --break-system-packages pillow imageio-ffmpeg
```
