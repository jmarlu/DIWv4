"""Comprueba que ambas vistas contienen los mismos bloques y evidencias."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
units=json.loads((R/'curso/secuencia.json').read_text())
for u in units:
    a=(R/'docs'/u['id']/'guiaUnidad.md').read_text()
    t=(R/'materiales-docentes/privado/docs'/u['id']/'Guion_docente.md').read_text()
    for b in u['bloques']:
        for value in [f"## {b['id']} · {b['titulo']}",b['actividad'],b['trabajo'],b['evidencia']]:
            assert value in a and value in t, (u['id'],b['id'])
        for resource in b['recursos']:
            assert (R/'docs'/u['id']/resource).is_file(),(u['id'],resource)
print(f'OK: {len(units)} pares de recorridos, {sum(len(u["bloques"]) for u in units)} bloques coordinados y recursos localizables.')
