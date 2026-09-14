# Actividades

## Actividades 1

1.  Instala Git en tu sistema operativo. Adjunta una captura de pantalla en la que aparezca el resultado de la ejecución del comando `git --version`.
2.  Realiza la **configuración de Git** según lo indicado en el tema (nombre, correo electrónico y editor de preferencia). Adjunta una captura de pantalla con el resultado de la ejecución de los comandos de configuración.
3.  Crea una carpeta denominada `S1R1`. Realiza las siguientes acciones en ella:
    1. Crea un repositorio Git.
    2. Crea un fichero denominado `libros.txt`. Añade tres títulos de libros cada uno en una línea distinta.
    3. Haz un primer /commit/.
    4. Añade dos libros al archivo `libros.txt`.
    5. Haz un segundo /commit/.
    6. Crea un fichero denominado `peliculas.txt`. Añade tres títulos de películas a dicho archivo.
    7. Haz una captura de pantalla del comando `git status`.
    8. Crea un fichero denominado `comidas.txt`. Añade tres nombres de comidas a dicho archivo.
    9. Haz un tercer /commit/ que incluya los archivos `peliculas.txt` y `comidas.txt`.
    10. Elimina el archivo `comidas.txt` desde el navegador de archivos.
    11. Añade dos películas más al archivo `peliculas.txt`.
    12. Haz una captura de pantalla que muestre los cambios en el directorio de trabajo.
    13. Añade los cambios al área de preparación.
    14. Haz una captura de pantalla del comando `git status`. Debe indicar que se ha borrado el archivo `comidas.txt` y que se ha modificado el archivo `peliculas.txt`.
    15. Haz un cuarto /commit/.
    16. Crea un archivo denominado `datos.bak`. Añade tres títulos de libros a dicho archivo. **¡IMPORTANTE! No añadas el archivo al área de preparación ni hagas ningún commit.**
    17. Crea una subcarpeta denominada `output`. Crea un archivo denominado `salida.txt` en su interior. Escribe tu nombre y apellidos en dicho archivo. **¡IMPORTANTE! No añadas los archivos al área de preparación ni hagas ningún commit.**
    18. Haz una captura de pantalla del comando `git status`. Deben aparecer el archivo `datos.bak` y la carpeta `output` como archivos nuevos (color rojo). Recuerda que, por defecto, `git` no muestra el contenido de una carpeta desconocida, sino solo el nombre de dicha carpeta; si se desea mostrar los archivos nuevos dentro de carpetas desconocidas se debe ejecutar `git status -u`.
    19. Crea un archivo `.gitignore` para que los ficheros con extensión `.bak` y el contenido de la carpeta `output/` no se incluyan en el repositorio.
    20. Haz una nueva captura de pantalla del comando `git status`. Ahora no deben aparecer los archivos `datos.bak` y `output/salida.txt` como archivos nuevos, sino que en su lugar debe aparecer únicamente el archivo `.gitignore`.
    21. Haz un último /commit/ para incluir el archivo `.gitignore` en el repositorio.
    22. Haz una captura de pantalla que muestre el histórico de cambios del repositorio.

## Actividades 2

Cuando se pida realizar un /commit/ recuerda que previamente hay que añadir los archivos al área de preparación si no se ha indicado antes en las instrucciones. En esos casos, un /commit/ significa ejecutar los comandos `git add` y `git commit`.

1. Crea una carpeta denominada `S2R1`. Realiza las siguientes acciones en ella:
   1. Crea un repositorio Git.
   2. Crea un fichero denominado `actores.txt`. Añade tres nombres de actores cada uno en una línea distinta.
   3. Haz un primer /commit/.
   4. Crea una rama denominada `test`.
   5. Cambia a la rama `test`
   6. En la rama `test` crea un fichero denominado `actrices.txt`. Añade tres nombres de actrices y realiza un /commit/ en dicha rama.
   7. Haz una captura de pantalla del resultado del comando `git log --graph --all`.
   8. Cambia a la rama `master`.
   9. Incorpora los cambios de la rama `test` a la rama `master`. Haz una captura de pantalla de los comandos que has utilizado y de su resultado.
   10. Crea una segunda rama denominada `test2`. La rama `test2` apunta al mismo /commit/ que la rama `master` en este momento.
   11. En la rama `master`, añade una actriz al fichero `actrices.txt` y haz un /commit/.
   12. Cambia a la rama `test2`
   13. En la rama `test2`, añade una actriz al fichero `actrices.txt` y haz otro /commit/.
   14. Haz una captura de pantalla del resultado del comando `git log --graph --all`. Debe haber dos caminos distintos: uno para la rama `master` y otro para la rama `test2`.
   15. Cambia a la rama `master`
   16. Incorpora los cambios de la rama `test2` a la rama `master`. ¿Se produce un conflicto? De ser así realiza una captura del comando `git status`.
   17. Resuelve el conflicto incorporando los dos nombres de actrices.
   18. Haz una captura de pantalla del resultado del comando `git log --graph --all`. Observa que se ha creado un nuevo /commit/ que integra los dos caminos anteriores.
2. Crea una carpeta denominada `S2R2-remoto`. Inicializa un repositorio Git en su interior mediante el comando `git init --bare`. Esta carpeta se utilizará como repositorio remoto.
3. Clona el repositorio `S2R2-remoto` en una carpeta denominada `S2R2`. Adjunta captura de pantalla del resultado del comando de clonado. A continuación realiza las siguientes acciones en el repositorio `S2R2`:
   1. Crea un archivo denominado `directores.txt`. Añade el nombre de tres directores de cine.
   2. Haz un /commit/.
   3. Realiza un /push/ al repositorio remoto. Adjunta captura de pantalla del resultado.
   4. Crea una rama denominada `version1`.
   5. Cambia a la rama `version1`.
   6. En la rama `version1` añade el nombre de dos directores de cine más al archivo `directores.txt` y haz un /commit/ de los cambios.
   7. Realiza un /push/ de la rama al repositorio remoto de manera que **quede asociada a la rama remota del mismo nombre**. Adjunta captura de pantalla del resultado.
4. Clona el repositorio `S2R2-remoto` en una segunda carpeta denominada `S2R3`. Realiza las siguientes acciones sobre ella:
   1. Muestra en la consola el contenido del fichero `directores.txt` y el resultado del comando `git status`. Debe mostrar tres directores.
   2. Cambia a la rama `version1`. Muestra el resultado del comando. Comprueba que se crea una rama local `version1` con el contenido de la rama remota `origin/version1` y enlazada con ella. Al clonar el repositorio la rama no existía (solo se clona la rama principal, `master`), pero al cambiar a una rama que existe en el remoto se produce su creación local y enlazado con su correspondiente remota.
   3. Muestra el contenido del fichero `directores.txt` por la pantalla. Comprueba que se muestran los 5 nombres de directores esperados. Adjunta captura de pantalla.
   4. Cambia a la rama `master`.
   5. Incorpora los cambios de la rama `version1` a la rama `master`.
   6. Sube la rama `master` actualizada al servidor. Adjunta captura de pantalla del resultado del comando.
5. Vuelve de nuevo a la carpeta `S2R2` y realiza las siguientes acciones:
   1. Obtén los cambios que hay en el repositorio remoto **sin fusionarlos en la rama local**. Adjunta captura de pantalla del resultado del comando utilizado.
   2. Actualiza la rama `master` local con el contenido de la rama `master` del repositorio remoto. Adjunta captura de pantalla del resultado del comando utilizado.
   3. Comprueba que aparecen los 5 nombres de directores esperados.

## Actividades 3

1. Creación de cuenta en GitHub
   1. Crea una cuenta en GitHub
   2. Añade tu dirección de correo de educación
   3. Solicita un descuento para uso educativo (ver enlace en apartado de Referencias)
2. Trabajo con repositorios, issues, forks y pull requests.
   1. Haz un fork del repositorio localizado en la siguiente url: . A partir de este momento todas las tareas que se indican se deben realizar en tu repositorio (el que has clonado mediante el fork).
      1. Realiza un primer commit para poner tu nombre y apellidos en el fichero README.md. Necesitaras hacer un clonado sobre el repositorio que has creado con el fork.
      2. Crea 3 issues con los siguientes títulos. Si no ves la pestaña de issues, actívala desde los ajustes (settings) del repositorio.
         1. Añadir 3 libros
         2. Añadir 3 películas
         3. Añadir 3 discos
      3. Modifica los ficheros correspondientes y realiza 3 commits para realizar cada una de las tareas que se indican en los issues. El mensaje del commit debe hacer que se cierren los issues correspondientes de manera automática.
      4. Haz una captura de pantalla de los comandos que has utilizado para hacer los commits y subir los cambios a GitHub.
      5. Incluye las capturas de pantalla en el repositorio dentro de la carpeta capturas. Añádelas también al repositorio de manera que queden guardadas en tu repositorio en GitHub.
      6. Realiza una pull request indicando en el mensaje que has completado la tarea.

!!! note "Entrega de la Actividad 1 y 2"

      Guarda el fichero con las capturas en formato PDF. La entrega del fichero se realizará a través de la plataforma Aules.

!!! note "Entrega de la Actividad 3"

      No hay que subir ningún archivo en la tarea de la plataforma Aules.
