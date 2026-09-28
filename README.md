# Ruleta de Retos

Ruleta para streams: sortea un héroe y un reto aleatorio para jugar la partida.

- 53 héroes con 12–14 retos propios cada uno y 62 retos generales en 7 categorías.
- Cuatro modos de reto: del héroe, general, los dos a la vez o mezcla aleatoria.
- Filtros por rol, subrol, dificultad y categoría, y exclusión de héroes sueltos.
- Opciones para no repetir héroe o reto, re-tirar, contador de re-tiradas e historial copiable.
- Modo stream con fondo croma para OBS y pantalla completa. La barra espaciadora hace girar la ruleta.

## Uso

Abre `index.html` en el navegador. No necesita servidor ni dependencias.

## Estructura

| Archivo | Contenido |
|---|---|
| `src/page.html` | Interfaz, estilos y lógica de la ruleta |
| `src/data.js` | Héroes, subroles y retos (`window.OW_DATA`) |
| `build.py` | Une los dos en `index.html` |
| `index.html` | Página final lista para abrir o publicar |

## Editar retos

1. Cambia `src/data.js`. Cada reto es `{ t: "texto", d: 1|2|3 }`. Los generales llevan además `cat` y, opcionalmente, `roles`.
2. Ejecuta `python3 build.py`.

## Publicar en GitHub Pages

En el repositorio: Settings → Pages → Deploy from a branch → `main` / raíz.

Proyecto de fans sin relación con Blizzard Entertainment. No incluye logos ni imágenes oficiales.
