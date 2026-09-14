# Taller multimedia · Preparar, integrar y comprobar

Trabaja con el proyecto del módulo. Elige recursos propios o con condiciones de uso que permitan la práctica. No necesitas grabar personas: puedes fotografiar objetos y narrar un recorrido con contenido ficticio.

## MM1 · Inventario y decisiones

Selecciona una imagen, un audio y un vídeo breve. Registra nombre, autor, origen, licencia/condiciones, función, formato, duración o dimensiones y peso. Explica qué aporta cada recurso: si no ayuda a la tarea, úsalo en una página de pruebas.

Decide las alternativas antes de editar: texto alternativo de imágenes según su función, transcripción del audio y subtítulos del vídeo. Revisa si la información visual necesita descripción adicional. [Guía WAI para audio y vídeo](https://www.w3.org/WAI/media/av/).

## MM2 · Transformación

1. **Imagen:** conserva el original; recorta y exporta dos tamaños. Compara dos formatos disponibles en tu herramienta y registra peso y calidad a tamaño de uso. Distingue ilustración vectorial de fotografía.
2. **Audio:** crea o utiliza un clip breve, recorta el inicio/final, ajusta nivel evitando saturación y exporta dos formatos. Anota duración, tamaño y diferencias audibles.
3. **Vídeo:** selecciona un fragmento, ajusta tamaño y exporta una versión adecuada para la web. Registra herramienta, ajustes y relación entre peso y calidad.
4. **Animación de imágenes:** prepara tres o más fotogramas propios y genera una animación con tu herramienta. Conserva una alternativa estática y explica si aporta algo al proyecto. No confundirla con una transición de CSS.

Puedes emplear el editor disponible en el aula. Registra su versión y los pasos, no solo el nombre del programa. Entrega originales y exportaciones; compara antes de elegir.

## MM3 · Integración

Este es un patrón de estructura; sustituye las rutas por tus exportaciones:

```html
<figure>
  <img src="img/salida-800.webp" width="800" height="520"
       alt="Participantes observando la luz sobre una fachada">
  <figcaption>Recurso de la salida; autor y condiciones de uso.</figcaption>
</figure>
<audio controls preload="metadata">
  <source src="media/presentacion.mp3" type="audio/mpeg">
  Tu navegador no puede reproducir este audio.
</audio>
<p><a href="transcripcion.html">Leer la transcripción del audio</a></p>
<video controls preload="metadata" width="800">
  <source src="media/recorrido.mp4" type="video/mp4">
  <track kind="captions" src="media/recorrido-es.vtt" srclang="es"
         label="Español" default>
  Tu navegador no puede reproducir este vídeo.
</video>
```

El texto alternativo del ejemplo solo sirve si describe tu imagen real. No copies una descripción que no corresponde. Añade una alternativa textual completa al vídeo y descripción de información visual cuando sea necesaria; los subtítulos por sí solos no cubren todos los casos.

Ejemplo de archivo de subtítulos que debes sincronizar con tu clip:

```text
WEBVTT

00:00:00.000 --> 00:00:03.000
Bienvenidos al recorrido de la salida.
```

## Verificación y entrega

Prueba reproducción, pausa, volumen, teclado y subtítulos. Compara dos navegadores/dispositivos disponibles e indica cuáles utilizaste realmente. Evita reproducción automática con sonido.

Entrega `MM-v1`: inventario, originales, exportaciones, página funcional, alternativas y tabla de pruebas. Registra un problema y su corrección o indica que no se observó en las pruebas realizadas. No inventes compatibilidad con dispositivos no probados.
