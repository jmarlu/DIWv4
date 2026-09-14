"""Prepara una copia local del curso con el material privado del profesor."""
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import sys

import yaml
from mkdocs.config import load_config

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / 'materiales-docentes/privado/docs'
WORK = ROOT / '.local-docente'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('accion', choices=['serve', 'build'], nargs='?', default='serve')
    args = parser.parse_args()
    if not (PRIVATE / 'UD1/Guion_docente.md').is_file():
        parser.error('Falta la carpeta privada del profesor. Esta copia del repositorio solo contiene el curso del alumnado.')
    destination = WORK / 'docs'
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(ROOT / 'docs', destination,
                    ignore=shutil.ignore_patterns('node_modules', 'examenes'))
    shutil.copytree(PRIVATE, destination, dirs_exist_ok=True)
    base = load_config(config_file=str(ROOT / 'mkdocs.yml'))
    nav = base['nav']
    units = json.loads((ROOT / 'curso/secuencia.json').read_text())
    nav.insert(0, {'Profesor': [
        {'Panel docente': 'Panel_docente.md'},
        {'Cambios y conservación': 'Cambios_DIWv4.md'},
        *[{f"{u['id']} · Guion": f"{u['id']}/Guion_docente.md"} for u in units],
        {'Mirada · Guía y recursos web': 'UD1/Ejemplo_Figma_Mirada.md'},
        {'Soluciones de Flexbox': 'Soluciones.md'},
        {'Archivo · Guion Tailwind': 'UD5/guion_clase_tailwind.md'},
        {'Archivo · Guía rápida Tailwind': 'UD5/tailwind-clase-proyecto/docs/GUIA_CLASE.md'},
        {'Informe de partida': 'Revision_unidades.md'},
    ]})
    config = {
        'INHERIT': str(ROOT / 'mkdocs.yml'),
        'site_name': 'DIWv4 · Profesor',
        'theme': {'name': 'material', 'palette': [{'scheme': 'default', 'primary': 'deep orange', 'accent': 'amber'}]},
        'extra': {'audiencia': 'profesor'},
        'hooks': [str(ROOT / 'herramientas/publicacion_hook.py')],
        'docs_dir': 'docs',
        'site_dir': 'site',
        'dev_addr': '127.0.0.1:8001',
        'exclude_docs': '**/node_modules/**\nexamenes/**\n',
        'nav': nav,
    }
    config_path = WORK / 'mkdocs.yml'
    config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False))
    print('Vista docente local. No publiques .local-docente ni materiales-docentes.', flush=True)
    print('Para incorporar cambios de las fuentes, detén y vuelve a ejecutar este comando.', flush=True)
    command = [sys.executable, '-m', 'mkdocs', args.accion, '-f', str(config_path)]
    if args.accion == 'build':
        command.append('--strict')
    return subprocess.call(command, cwd=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
