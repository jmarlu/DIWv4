# Ejercicios

## Ejercicio 1

Crea la siguiente página web que se muestra en la siguiente imagen.

![primeraWeb](img/primeraWeb.png)

La versión de clase utiliza flujo normal y Flexbox. Como ampliación histórica, conserva el reto original: construir otra versión con float y otra con display de tabla, comparar dificultades y explicar por qué no las eliges para el proyecto actual. Estas dos versiones no son entregas adicionales obligatorias en el recorrido DIWv4.

Utiliza etiquetas que tengan sentido pertenecientes a la version **html5**.

**Para la zona de navegación**, podemos poner un elemento `<ul>`. Cada vínculo `<a>` está situado en elementos `<li>`.
Su código **html** es el siguiente:

```html
<nav>
  <ul id="menu">
    <li><a href="#">Inicio</a></li>
    <li><a href="#">Proyectos</a></li>
    <li><a href="#">Reportajes</a></li>
    <li><a href="#">Contacto</a></li>
  </ul>
</nav>
```

Los elementos `<li>` se muestran en modo de inline-block, a fin de que aparezcan alineados horizontalmente y de poder utilizar todas las propiedades de las cajas. Cada elemento `<li>` tiene un margen derecho de 20 píxeles.

Para las siguientes páginas utiliza HTML semántico y el CSS inicial del recorrido.

Crea la **página contacto.html** e inserta un formulario de contacto que solicite los siguientes datos.

- Nombre, admitiendo espacios y acentos.
- Email
- Como ensayo separado: edad con `type="number"`, `min="18"` y `max="99"`. No es necesaria para una consulta general.
- Teléfono opcional.
- Campo de consulta
- Checkbox de prueba con etiqueta visible; utiliza textos ficticios y no lo presentes como una política real.

Marca como obligatorios solo nombre, correo y consulta en este ejercicio. Todos los controles necesitan etiquetas; el placeholder es opcional. Conserva el orden natural del foco y comprueba la navegación con teclado. No utilices datos personales reales.

Crea ahora la página de **proyectos.html**. Incluye una tabla que contenga un mínimo de 3 columnas y 5 filas. Debe disponer de etiqueta de encabezado `<th>` y de etiqueta de `<caption>`. Describe los proyectos que ofreces o utiliza un lorem ipsum para rellenar los datos de la tabla.

## Ejercicio 2

Realiza la validación de tu código html y corrige los errores encontrados. Mediante la extensión HTMLHint y el validador w3.org. ¿Hay alguna diferencia?

## Ejercicio 3

Accede a la documentación de google mediante el link que te pongo en teoría. Investiga y contesta a las siguientes preguntas.

1. ¿El contenido copiado afecta al posicionamiento de la web en el buscador?
2. ¿Afecta en el posicionamiento la utilización de http en lugar de https?
3. ¿Cuál de las dos URL son mejores y por qué?
   `https://www.brandonsbaseballcards.com/folder1/22447478/x2/14032015.html https://www.brandonsbaseballcards.com/article/ten-rarest-baseball-cards.html`
4. ¿Qué es Search Console?

## Ejercicio 4

Verifica que cumples cada uno de los factores HTML clave para mejorar el SEO y aplica cambios necesarios en tu proyecto.

!!! note Forma de entrega

      Realiza todos los ejercicios.**UN FICHERO POR CADA EJERCICIO EN FORMATO MARKDOWN**. Revisa la documentación de como generar ficheros y su sintaxis básica de markdown. https://tutorialmarkdown.com/sintaxis. **SI EN EL EJERCICIO TE DICE QUE GENERES UNA PÁGINA HTML NO HACE FALTA QUE GENERES UN FICHERO MD**.
