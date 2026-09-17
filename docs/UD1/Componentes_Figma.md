# Tutorial Completo: Creando Componentes en Figma

!!! example "Este apartado en Mirada"
    Auto Layout, variantes, instancias, estados, prototipo y microinteracciones.

    [Paso 12: Crear un botón con Auto Layout](Ejemplo_Figma_Mirada.md#paso-12-crear-un-boton-con-auto-layout) · [Paso 13: Separar tipo y estado](Ejemplo_Figma_Mirada.md#paso-13-separar-tipo-y-estado) · [Paso 14: Probar instancias](Ejemplo_Figma_Mirada.md#paso-14-probar-instancias) · [Paso 15: Construir la tarjeta de actividad](Ejemplo_Figma_Mirada.md#paso-15-construir-la-tarjeta-de-actividad) · [Paso 16: Crear campo, etiqueta, ayuda y error](Ejemplo_Figma_Mirada.md#paso-16-crear-campo-etiqueta-ayuda-y-error) · [Paso 17: Crear enlaces y cabecera](Ejemplo_Figma_Mirada.md#paso-17-crear-enlaces-y-cabecera) · [Paso 18: Montar la página de componentes](Ejemplo_Figma_Mirada.md#paso-18-montar-la-pagina-de-componentes) · [Paso 31: Conectar las pantallas](Ejemplo_Figma_Mirada.md#paso-31-conectar-las-pantallas) · [Paso 32: Añadir una microinteracción](Ejemplo_Figma_Mirada.md#paso-32-anadir-una-microinteraccion) · [Paso 33: Ensayar una ventana superpuesta](Ejemplo_Figma_Mirada.md#paso-33-ensayar-una-ventana-superpuesta) · [Paso 34: Revisar animación y desplazamiento](Ejemplo_Figma_Mirada.md#paso-34-revisar-animacion-y-desplazamiento).

    Mirada es un ejemplo paso a paso sin entrega.

## 📋 Introducción
En este documento aprenderás a crear componentes reutilizables en Figma, basándonos en el diseño de la landing page "DesignPro". Los componentes son elementos clave para mantener la consistencia y eficiencia en tus diseños.

**¿Qué vamos a crear?**
- Componentes básicos: Botones, tarjetas, y encabezados.
- Variantes de componentes.
- Organización de componentes en un sistema de diseño.

**Tiempo estimado:** 2-3 horas  
**Herramienta:** Figma Design en el navegador

---

## 🚀 Creando Componentes Básicos

### Paso 1: Crear un botón como componente

1. Crea el texto «Consultar actividad» con una fuente legible, por ejemplo Inter a 16 px.
2. Aplica Auto Layout al texto para crear un contenedor. Configura disposición horizontal, alineación centrada y relleno de 12 px vertical y 16 px horizontal.
3. Aplica al contenedor el color de acción de tu guía y un radio de 8 px. Comprueba el contraste con el texto.
4. Configura el ancho para ajustarse al contenido (Hug contents), en lugar de depender de un rectángulo de ancho fijo.
5. Convierte el contenedor en componente mediante «Create component» y nómbralo «Botón».
6. Crea una instancia y sustituye el texto por «Consultar todas las actividades». Comprueba que crece sin recortar el texto.

### Antes de seguir

El componente principal define una estructura reutilizable. Una instancia reutiliza esa definición y permite cambios de contenido. Comprueba la diferencia cambiando el radio en el principal y observando sus instancias.

### Paso 2: Crear variantes del botón

1. Crea variantes dentro de un conjunto de componentes.
2. Define una propiedad `Tipo` con valores `Primario` y `Secundario`.
3. Define otra propiedad `Estado` con `Normal`, `Hover`, `Foco` y `Deshabilitado` para las combinaciones que vayas a utilizar.
4. Distingue foco mediante un contorno visible y conserva contraste en los estados activos. El estado deshabilitado se debe explicar en el contexto de uso.
5. Nombra cada propiedad y prueba a cambiarla en una instancia.

Tipo y estado responden a preguntas diferentes: qué importancia tiene la acción y en qué situación se encuentra. No conviertas cada cambio de texto en una variante nueva.

---

## 🎨 Creando Tarjetas como Componentes

### Paso 3: Crear una tarjeta base

1. Crea un frame de unos 360 px de ancho con Auto Layout vertical, separación de 12 px y relleno de 16 px. Ajusta la altura al contenido.
2. Aplica un relleno blanco.
3. Redondea las esquinas a 12px.
4. Añade una sombra: X: 0, Y: 4, Blur: 20, Color: rgba(0,0,0,0.1).
5. Añade un título: "Título de la Tarjeta".
   - Fuente: Inter, 18px, SemiBold, color "Primary".
6. Añade un texto descriptivo: "Descripción breve de la tarjeta.".
   - Fuente: Inter, 14px, Regular, color "Muted Foreground".
7. Crea el componente «Tarjeta/Base» desde el frame. Prueba una instancia con título de dos líneas y otra sin imagen; el contenido no debe recortarse.

### Paso 4: Crear variantes de la tarjeta

1. Selecciona el componente "Tarjeta/Base".
2. Crea las siguientes variantes:
   - **Con ícono:** Añade un círculo de 48x48px con un ícono dentro.
   - **Con imagen:** Sustituye el fondo por una imagen.
3. Organiza las variantes en un contenedor de variantes.

---

## 🖼️ Creando Encabezados como Componentes

### Paso 5: Crear un encabezado

1. Crea un frame con Auto Layout horizontal para logo y navegación. Usa el ancho disponible en la página y relleno suficiente; evita fijar una altura que recorte el texto.
2. Aplica un relleno blanco.
3. Añade un texto: "Encabezado Principal".
   - Fuente: Inter, 24px, Bold, color "Primary".
4. Crea un componente desde el frame: «Encabezado/Principal». Prueba un ancho estrecho y define una composición alternativa cuando los elementos no quepan.

### Paso 6: Crear variantes del encabezado

1. Selecciona el componente "Encabezado/Principal".
2. Crea las siguientes variantes:
   - **Con logo:** Añade un logo a la izquierda.
   - **Con navegación:** Añade un menú de navegación centrado.
3. Organiza las variantes en un contenedor de variantes.

---

## Organización y reutilización

### Paso 7: Organizar los componentes

1. Crea una página en Figma llamada "Componentes".
2. Organiza los componentes en secciones: Botones, Tarjetas, Encabezados.
3. Asegúrate de nombrar todos los componentes y variantes de forma clara.

### Paso 8: Reutilizar los componentes

1. Usa los componentes en tus diseños para mantener la consistencia.
2. Si necesitas personalizar un componente, crea una instancia y realiza los cambios necesarios.

---


## 🎥 Añadiendo Animaciones a los Componentes

### Paso 9: Crear transiciones básicas

1. Selecciona un componente (por ejemplo, "Botón/Primario").
2. Ve a la pestaña "Prototype" en el panel derecho.
3. Haz clic en el componente y arrastra una flecha hacia otro frame o variante.
4. Configura la interacción:
   - **Trigger:** On Click.
   - **Action:** Navigate to para pasar a otra pantalla; Change to para cambiar entre variantes del mismo conjunto.
   - **Animation:** Smart Animate.
   - **Easing:** Ease In and Out.
   - **Duration:** 300ms.

### Paso 10: Crear microinteracciones

1. Selecciona un componente (por ejemplo, "Botón/Primario").
2. Crea una variante adicional para el estado "Hover".
   - Cambia el color de fondo conservando contraste; evita cambiar el tamaño del texto si provoca saltos de distribución.
3. Ve a la pestaña "Prototype" y conecta el estado base con el estado "Hover".
4. Configura la interacción:
   - **Trigger:** While Hovering.
   - **Action:** Change to, hacia la variante Hover del mismo conjunto.
   - **Animation:** Smart Animate.
   - **Easing:** Linear.
   - **Duration:** 200ms.

### Paso 11: Crear animaciones complejas

1. Diseña dos frames con diferentes estados de un componente (por ejemplo, un menú desplegable abierto y cerrado).
2. Ve a la pestaña "Prototype" y conecta los frames.
3. Configura la interacción:
   - **Trigger:** On Click.
   - **Animation:** Smart Animate.
   - **Easing:** Spring.
   - **Duration:** 500ms.

### Paso 12: Compartir el resultado

1. Comparte el enlace de consulta al prototipo y comprueba que el destinatario puede abrirlo.
2. Exporta las pantallas estáticas como PNG o PDF para conservar una evidencia local. La exportación estática no conserva las interacciones.
3. Si necesitas mostrar el recorrido en vídeo, puedes grabar una demostración. Identifica que es una grabación del prototipo.

La exportación de animaciones creadas con Figma Motion es un flujo específico: requiere seleccionar el frame correspondiente y utilizar la exportación animada. No se debe asumir que una transición de Smart Animate se exporta automáticamente como GIF o MP4. Consulta la [documentación de exportación animada](https://help.figma.com/hc/en-us/articles/41307983648407-Export-animations-from-Figma) si realizas esa ampliación; no es un requisito de esta práctica.

## Comprobar y transferir al proyecto

- Cambia el texto de una instancia sin deshacer su relación con el componente.
- Comprueba título largo, ancho estrecho y estados del botón.
- Representa también el foco como especificación visual. El teclado real se verificará al implementar en HTML.
- Crea un campo con etiqueta visible, ayuda y mensaje de error para practicar el componente que utilizarás en la actividad 21.

[Referencia de interacciones entre variantes](https://help.figma.com/hc/en-us/articles/360061175334-Create-interactive-components-with-variants). La ubicación de los controles puede variar con la interfaz de Figma; reconoce la acción y el objeto sobre el que se aplica.

## 🎓 Conceptos Aprendidos

- ✅ Crear componentes básicos en Figma.
- ✅ Crear variantes de componentes.
- ✅ Organizar componentes en un sistema de diseño.
- ✅ Reutilizar componentes para mantener la consistencia.
- ✅ Crear transiciones básicas entre componentes.
- ✅ Diseñar microinteracciones para mejorar la experiencia del usuario.
- ✅ Implementar animaciones complejas con Smart Animate.
- ✅ Compartir un prototipo y conservar una exportación estática, distinguiéndola de una animación exportada.

---

¡Felicidades! Ahora tienes una base sólida para trabajar con componentes en Figma. Esto te permitirá ahorrar tiempo y mantener la coherencia en tus diseños.

[Aplicar en la actividad 21](Actividades.md#actividad-21). Conserva los nombres, propiedades y estados para implementarlos en las siguientes unidades.

## Aplicación en un caso completo

En [Mirada](Ejemplo_Figma_Mirada.md) encontrarás botones, campos, tarjetas, enlaces, cabeceras e iconos dentro de un recorrido completo. Los pasos 12–18 explican su construcción; los pasos 31–34 conectan el prototipo. Incluye recursos visuales para construir y comprobar tu versión.
