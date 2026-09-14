"""Comprobación automática del artefacto del alumnado al construir o servir."""
from pathlib import Path
import importlib.util
from mkdocs.exceptions import PluginError

spec=importlib.util.spec_from_file_location('diwv4_publicacion', Path(__file__).with_name('comprobar_publicacion.py'))
checker=importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

def on_post_build(config):
    if config.get('extra', {}).get('audiencia') == 'profesor':
        return
    try:
        checker.comprobar(config['site_dir'])
    except ValueError as error:
        raise PluginError(str(error)) from error
