"""Impide publicar por error los recursos docentes conocidos en el sitio del alumnado."""
from pathlib import Path
import sys
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1]
site = root / 'site'
forbidden = {'guion_docente', 'figma-plugin', 'mirada-ud1.zip', 'examenes',
             'node_modules', 'materiales-docentes', '.local-docente',
             'guion_clase_tailwind', 'guion_clase_tailwind.md', 'guia_clase', 'guia_clase.md',
             'panel_docente', 'cambios_diwv4', 'revision_unidades', 'soluciones'}
markers = ['Guion_docente', 'figma-plugin', 'mirada-ud1.zip',
           'Cargar la solución editable en Figma', 'const MODELO =', 'guion_clase_tailwind', 'GUIA_CLASE', 'Respuesta esperada:', 'Consejos para el Profesor', 'Panel_docente', 'Cambios_DIWv4', 'Revision_unidades', 'DIWEBV3-original.zip']
def comprobar(site):
    site = Path(site)
    if not (site / 'index.html').is_file():
        raise ValueError('Primero genera el sitio con MkDocs.')
    errors = []
    for path in site.rglob('*'):
        relative = path.relative_to(site)
        if any('_sol' in part.lower() for part in relative.parts):
            errors.append(f'{relative}: solución reservada')
        if path.is_file() and path.suffix == '.zip':
            with ZipFile(path) as archive:
                if any('_sol' in name.lower() or 'examenes/' in name.lower() or 'figma-plugin/' in name.lower() for name in archive.namelist()):
                    errors.append(f'{relative}: contenido reservado en ZIP')
        if any(part.lower() in forbidden or part.lower() == 'guion_docente.md'
               for part in relative.parts):
            errors.append(str(relative))
        if path.is_file() and path.suffix in {'.html', '.json', '.js', '.md', '.txt'}:
            content = path.read_text(errors='replace')
            if any(marker in content for marker in markers):
                errors.append(f'{relative}: referencia o contenido docente')
    if errors:
        raise ValueError('Publicación bloqueada:\n' + '\n'.join(errors[:30]))
    return 'OK: sin recursos docentes conocidos en el sitio público, buscador y ZIP.'

if __name__ == '__main__':
    try:
        print(comprobar(site))
    except ValueError as error:
        sys.exit(str(error))
