# Verificación HTML Y SEO.

## Test de verificación HTML y herramientas útiles

Hay una gran cantidad de herramientas muy útiles para desarrolladores de forma online o que se instalan en los navegadores en forma de extensiones o plugins y que nos permiten funcionalidades extra. A continuación veremos algunas de ellas.

### Validador HTML, W3C

El W3C nos ofrece varias herramientas e información muy valiosa para la elaboración de nuestros desarrollos. Entre las herramientas destacadas se encuentra el validador HTML ([validator.w3.org](https://validator.w3.org/)) que nos permite encontrar errores en nuestros ficheros. Este validador HTML nos permite validar nuestras páginas seleccionando los ficheros HTML a validar o eligiendo directamente la url publicada.

Si los documentos se validan correctamente y no disponen de ningún error, se puede incluir en la página web desarrollada el icono que certifica que el código cumple con el estándar.

### HTMLHint, extensión para Visual Studio Code

Las páginas web se pueden validar en Visual Studio Code mediante la extensión HTMLHint.

### Firefox developer edition

Se trata de un navegador creado específicamente para desarrolladores web que ofrece herramientas muy interesantes como por ejemplo: panel de tipografías, editor de formas, inspector, consola o depurador, entre otras. mozilla.org/es-ES/firefox/developer/.

### Web developer

Consiste en una extensión disponible para Chrome, Firefox o IE que nos ofrece un control exhaustivo de varias partes de la web, tales como el CSS, los formularios o las imágenes. Con Web Developer instalado podemos, por ejemplo, alterar casi cualquier elemento final de la web en tiempo real y así aplicarlo a los archivos finales.

### CodePen

CodePen es una comunidad en línea para probar y mostrar fragmentos de código HTML, CSS y JavaScript. Funciona como un editor de código en línea y un entorno de aprendizaje de código abierto, donde los desarrolladores pueden crear y probar fragmentos de código, llamados «bolígrafos»

## Factores HTML clave para el SEO

SEO es un término que corresponde a las siglas en inglés Search Engine Optimization (optimización para buscadores). Mediante el posicionamiento web SEO conseguimos mejorar la visibilidad de un sitio web en los resultados orgánicos de los diferentes buscadores. Hay que tener en cuenta que los buscadores son las principales herramientas de consulta de información en Internet, por lo que si no aparece una web en ellos será muy difícil que los usuarios entren.

En Europa el buscador que más se utiliza es Google, aunque hay otros como Baidu, Bing, Yandex, Ecosia o DuckDuckGo. Cuando realizas una consulta en un buscador, aparecen los resultados orgánicos y los resultados patrocinados. El SEO se centra en los resultados orgánicos o naturales que son aquellos cuya posición está definida por el algoritmo del buscador. Para escalar posiciones en los resultados de búsqueda hay muchas tácticas que van desde la optimización de la página web hasta la generación de contenido, pasando por la obtención de links de forma natural y la relación con otras plataformas.

Observa entonces que la razón más importante para tener muy en cuenta el SEO en la estrategia de marketing digital de cualquier página web, es que ayuda a los motores de búsqueda a entender sobre qué trata cada una de las páginas y a mejorar los puestos en los resultados de los buscadores más utilizados.

Los elementos fundamentales para ello los vamos detallar, aunque en la siguiente [página](https://developers.google.com/search/docs) tenemos toda la documentación.

### Ayudar a Google a encontrar contenido

El primer paso para conseguir que tu sitio web se muestre en Google es asegurarte de que Google pueda encontrarlo. La mejor forma de hacerlo es mediante un sitemap. Un sitemap es un archivo que se encuentra en tu sitio y que informa a los buscadores sobre las páginas nuevas o modificadas de tu sitio.

### Informar a Google de las páginas que no quieres que rastree

Si quieres impedir que se rastree una página sin información sensible, utiliza un archivo robots.txt
Un archivo robots.txt indica a los buscadores si pueden acceder a determinadas partes de un sitio y, por tanto, rastrearlas. El archivo debe denominarse "robots.txt" y colocarse en el directorio "root" de tu sitio. Es posible que las páginas que se hayan bloqueado con un archivo de este tipo puedan rastrearse igualmente, por lo que debes utilizar un método más seguro si contienen información sensible.

### Permite que Google vea la página tal como la ven los usuarios

Cuando el robot de Google rastrea una página, debería verla exactamente igual que cualquier usuario. Para que Google pueda indexar y renderizar la página de la mejor manera posible, debes permitir que acceda a los archivos JavaScript, CSS y de imagen que usa tu sitio web.

#### Crea títulos de página únicos y precisos

Un elemento `<title>` indica a los usuarios y a los buscadores el tema de una página concreta. Coloca el elemento `<title>` dentro del elemento `<head>` del documento HTML y crea un texto de título único para cada página de tu sitio.

El elemento `<title>` de una página principal puede incluir el nombre del sitio web o de la empresa, así como otros datos importantes, como la ubicación física de la empresa o algunas de sus principales especialidades u ofertas.

Cosas que debes hacer:

- Describe con precisión el contenido de la página.
- Crea elementos `<title>` únicos para cada página.
- Utiliza elementos `<title>` breves pero descriptivos

#### Utiliza la etiqueta de metadescripción

La etiqueta de metadescripción de una página ofrece a Google y a otros buscadores un resumen del contenido de la página. El título de una página puede estar formado por unas cuantas palabras o por una frase, mientras que la etiqueta de metadescripción de una página puede contener una frase o dos, o incluso un párrafo breve. Al igual que el elemento `<title>`, la etiqueta de metadescripción se coloca dentro del elemento `<head>` del documento HTML.

```html
<html>
  <head>
    <title>
      Brandon's Baseball Cards - Buy Cards, Baseball News, Card Prices
    </title>
    <meta
      name="description"
      content="Brandon's Baseball Cards provides a large selection of vintage and modern baseball cards for sale. We also offer daily baseball news and events."
    />
  </head>
  <body>
    ...
  </body>
</html>
```

Cosas que debes hacer:

- Resume de forma precisa el contenido de la página
- Utiliza descripciones únicas en cada página

#### Añade etiquetas de encabezado para destacar el texto importante (H1,H2)

Con los encabezados adecuados, puedes indicar los temas importantes y crear una estructura jerárquica de tu contenido, de modo que los usuarios puedan navegar por el documento con más facilidad.

Cosas que debes hacer:

- No pongas demasiados encabezados en una página
- Imagina que haces un esquema

#### Optimizar las imágenes

Usa imágenes HTML

Inserta imágenes en tu contenido mediante elementos de imagen HTML.

- Usa los elementos HTML `<img> o <picture>`
- Usa el atributo alt.
- Usa nombres de archivo y texto alternativo breves y descriptivos.
- Introduce texto alternativo al utilizar imágenes como enlaces.
- Utiliza formatos de imagen estándar

#### Optimizar un sitio para móviles

Actualmente, el mundo es móvil. La mayoría de las personas que realizan búsquedas en Google utilizan dispositivos móviles. En algunos casos, la versión para ordenadores de un sitio web resulta difícil de ver y usar desde un dispositivo móvil. En consecuencia, es fundamental tener un sitio adaptado a los dispositivos móviles para mantener tu presencia online.

#### Incluye un favicon

Disponer de un favicon es otro de los elementos valorados por los buscadores para mejorar el posicionamiento online de una página web. Además, añadir un favicon a tu sitio es de gran utilidad porque le da un aspecto más serio y profesional, además de que aparece en la barra de navegación y los usuarios pueden ubicar tu página con mayor facilidad cuando tengan varias pestañas abiertas.

Para crear un favicon puedes utilizar la siguiente herramienta: http://www.favicon.pro/es/

Una vez hayas creado tu favicon.ico:

Sube el favicon.ico generado en tu sitio web (por ejemplo en la raíz del sitio). Verifica que está ahí escribiendo http://susitio.com/favicon.ico en el navegador.
Copia y pega el siguiente código HTML dentro de la etiqueta head de tu página web.

`<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">`

También se puede especificar un favicon mediante una imagen en png.

#### Optimiza el tiempo de carga de tu página

Los sitios rápidos mejoran la experiencia de usuario y contribuyen a mejorar la calidad general de la Web (especialmente para los usuarios con conexión a Internet lenta). Para probar el rendimiento de tus páginas, Google recomienda utilizar herramientas como [PageSpeed Insights](https://pagespeed.web.dev/) y [Webpagetest.org](https://www.webpagetest.org/).
