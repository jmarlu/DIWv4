"""Verifica la conservación del contenido de partida sin mostrar datos de evaluación."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--comparar-origen",action="store_true",help="Además, comparar DIWEBV3 actual con la instantánea histórica")
args=parser.parse_args()
R=Path(__file__).resolve().parents[1]
archive=R/'materiales-docentes/archivo-original'
manifest=json.loads((archive/'inventario.json').read_text())
source=R.parent/'DIWEBV3'
with ZipFile(archive/'DIWEBV3-original.zip') as z:
    assert len(z.namelist())==len(manifest), 'Número de archivos distinto'
    for item in manifest:
        data=z.read(item['ruta'])
        assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'], 'Archivo de conservación alterado'
        if args.comparar_origen:
            assert hashlib.sha256((source/item['ruta']).read_bytes()).hexdigest()==item['sha256'], 'DIWEBV3 actual difiere de la instantánea histórica'
print(f"OK: {len(manifest)} archivos de la instantánea histórica conservados.")
