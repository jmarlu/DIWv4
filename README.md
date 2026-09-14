# DIWv4 · Diseño de interfaces web

Nueva versión de DIWEBV3, con contenido conservado y dos recorridos coordinados: alumnado y profesor.

## Preparación

```bash
cd /home/julio/Documentos/DIWEB/DIWv4
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

El entorno ya está preparado en esta copia local. En usos posteriores basta con activar `.venv`.

## Curso del alumnado

```bash
python -m mkdocs serve
```

Abre http://127.0.0.1:8000. Empieza en «UD1 · Diseño → Recorrido de clase».

## Profesor

En otra terminal, con el entorno activado:

```bash
python herramientas/vista_docente.py
```

Abre http://127.0.0.1:8001 y entra en «Profesor → Panel docente». Es una consulta local, no una web protegida por contraseña. Para incorporar modificaciones de las fuentes, detén y vuelve a ejecutar este comando.

## Carpetas

- `docs/`: únicamente material publicable del alumnado; teoría, guías, actividades y recursos.
- `curso/secuencia.json`: fuente común de objetivos, bloques y evidencias.
- `materiales-docentes/privado/docs/`: guiones, soluciones y panel del profesor.
- `materiales-docentes/archivo-original/`: ZIP íntegro de contenidos de partida e inventario; no se sirve.
- `materiales-docentes/evaluacion-original/`: evaluación anterior, fuera de ambos sitios.
- `herramientas/`: generación, consulta y comprobaciones.

Las carpetas privadas están excluidas de Git, pero eso no limita el acceso si compartes la carpeta completa. Haz una copia de seguridad privada; distribuye al alumnado solo la salida pública comprobada. El proyecto original permanece en `../DIWEBV3`.

## Comprobar antes de publicar

```bash
python herramientas/generar_recorridos.py
python -m mkdocs build --strict
python herramientas/comprobar_publicacion.py
python herramientas/verificar_recorridos.py
python herramientas/verificar_conservacion.py
```

La comprobación de recursos docentes conocidos también se ejecuta automáticamente al construir o servir la versión del alumnado. Para ensayar el filtro utiliza `python herramientas/probar_filtro.py`.

La publicación automática utiliza únicamente `site/`. No publiques `.local-docente`, `materiales-docentes` ni el archivo original.

## Publicación en GitHub Pages

El flujo `.github/workflows/pages.yml` construye y comprueba la web pública al enviar cambios a `main`. En GitHub, abre **Settings → Pages** y selecciona **GitHub Actions** en *Build and deployment*. Cuando termine la acción, el curso estará disponible en https://jmarlu.github.io/DIWv4/.

La documentación del profesor registra cambios y límites: tiempos y evaluación deben conciliarse con la programación del centro; Figma requiere comprobación en el editor. Las dependencias de ejecución y páginas generadas se pueden reconstruir; el contenido previo se conserva en el ZIP.
