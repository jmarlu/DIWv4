"""Prueba que el filtro detecta rutas, contenido del buscador y archivos ZIP."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from comprobar_publicacion import comprobar

with TemporaryDirectory() as directory:
    root=Path(directory)
    (root/'index.html').write_text('<h1>Curso</h1>')
    comprobar(root)
    fixtures=[('Guion_docente.md','texto docente'),('search.json','{"title":"Panel_docente"}'),('archivo.zip',None)]
    for name,content in fixtures:
        path=root/name
        if content is None:
            with ZipFile(path,'w') as archive:archive.writestr('ejercicio_sol.html','solución')
        else:path.write_text(content)
        try:
            comprobar(root)
        except ValueError:
            pass
        else:
            raise AssertionError(f'El filtro no detectó {name}')
        finally:
            path.unlink()
    comprobar(root)
print('OK: el filtro acepta un sitio limpio y rechaza ruta docente, buscador reservado y solución en ZIP.')
