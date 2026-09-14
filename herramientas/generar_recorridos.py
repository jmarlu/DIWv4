"""Genera guías coordinadas de clase; los objetivos compartidos tienen una única fuente."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
units=json.loads((R/'curso/secuencia.json').read_text())
private_notes = R/'materiales-docentes/indicaciones.json'
notes = json.loads(private_notes.read_text()) if private_notes.exists() else {}
for unit in units:
 key=unit['id'];dest=R/'docs'/key;dest.mkdir(exist_ok=True)
 student=f"# {key} · {unit['titulo']}\n\nPartimos de **{unit['entrada']}**. Al terminar conservarás **{unit['entrega']}**.\n\n"
 student+='Sigue estos bloques en el orden indicado. Las fechas y entregas se comunican en clase. Aplica lo aprendido a tu proyecto y conserva las evidencias con el identificador del bloque.\n\n'
 if key=='UD1':student+='[Mirada: ejemplo guiado](Ejemplo_Figma_Mirada.md) · [Actividades A1–A21](Actividades.md) · [Guía de objetivos y criterios](objetivos.md). Trabaja en un archivo de prácticas y otro del proyecto propio. DesignPro es apoyo y A20 un ensayo breve.\n\n'
 teacher=f"# {key} · Guion del profesor\n\nEntrada: **{unit['entrada']}**. Salida: **{unit['entrega']}**.\n\n"
 teacher+='Esta secuencia comparte identificadores, actividades y evidencias con la guía del alumnado. No cambia ponderaciones ni asigna automáticamente horas oficiales. Divide cada bloque en las sesiones que requiera el grupo.\n\n'
 if key=='UD1':teacher+='Para UD1 se proponen 12 bloques de hasta dos horas; los 24 periodos de 60 minutos son una opción de aula, pendiente de conciliar con las 12 sesiones de la programación. La antigua secuenciación detallada queda como referencia en la copia original; aquí prevalecen los bloques B01–B12 y los enunciados DIWv4.\n\n'
 for b in unit['bloques']:
  links=' · '.join(f'[{Path(p).stem}](<{p}>)' for p in b['recursos'])
  shared=f"## {b['id']} · {b['titulo']}\n\n**Consulta:** {links}.\n\n**Práctica:** {b['actividad']}.\n\n{b['trabajo']}\n\n**Evidencia para avanzar:** {b['evidencia']}\n\n"
  student+=shared
  teacher+=shared
  hint=notes.get(key,{}).get(b['id'])
  if hint:
   teacher+=f"**Demostración preparada:** {hint['demostracion']}\n\n**Dificultad previsible:** {hint['dificultad']}\n\n**Control del profesor:** {hint['control']}\n\n"
  teacher+='''**Guion de intervención:**

1. Recupera la evidencia del bloque anterior y plantea la decisión que deben resolver.
2. Muestra un caso breve con Mirada o con el componente del proyecto de referencia. Explica el motivo antes de la operación.
3. Deja que construyan una variante; pide que expliquen qué cambia al modificar contenido o ancho.
4. Reserva tiempo para transferirlo al proyecto propio. Revisa primero a quienes no tienen la evidencia anterior.
5. Cierra localizando la evidencia y anotando una dificultad. Retómala en el siguiente inicio.

**Distribución orientativa por periodo de 60 min:** 5 de recuperación, 10 de explicación, 20 de práctica, 20 de transferencia y 5 de cierre. Repite o amplía práctica cuando el bloque lo requiera.

**Refuerzo:** facilita contenido y un paso inicial; comprueba una operación cada vez. **Ampliación:** cambia longitud, estado o contexto y pide justificar el resultado. No conviertas la ampliación en requisito oculto.

'''
 student+='## Cierre y continuidad\n\nRevisa tu entrega, guarda la versión y registra una decisión, su motivo y qué afecta después. [Ver el hilo del módulo](../mapaModulo.md).\n'
 teacher+='## Cierre docente\n\nContrasta con los criterios aplicables antes de calificar. Una prueba pendiente sigue pendiente; una captura o una solución generada no sustituye una modificación explicada. Revisa el material con la cuenta y herramientas del aula antes de impartirlo.\n'
 if key=='UD1':teacher+='\n[Preparar la explicación del brief de Mirada](Brief_Mirada_docente.md).\n'
 if key=='UD1':teacher+='\nEl generador nativo de Mirada no se ha ejecutado en Figma durante esta preparación; compruébalo antes de usarlo. La construcción manual puede impartirse sin él.\n'
 (dest/'guiaUnidad.md').write_text(student)
 td=R/'materiales-docentes/privado/docs'/key;td.mkdir(parents=True,exist_ok=True);(td/'Guion_docente.md').write_text(teacher)
print('Generadas',len(units),'parejas de recorridos coordinados.')
