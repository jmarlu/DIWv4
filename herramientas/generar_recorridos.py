"""Genera guías coordinadas de clase; los objetivos compartidos tienen una única fuente."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
units=json.loads((R/'curso/secuencia.json').read_text())
private_notes = R/'materiales-docentes/indicaciones.json'
notes = json.loads(private_notes.read_text()) if private_notes.exists() else {}

unit_guidance = {
 'Multimedia': {
  'student': 'Organización orientativa: tres bloques de 60–90 minutos. Imagen, audio y vídeo son obligatorios; la animación es ampliación. Consulta la [lista de entrega y matriz de evaluación](taller.md#entrega-y-matriz-de-evaluacion).',
  'teacher': {
   'B01': ('Compara un recurso pertinente y otro decorativo. Completa en directo una fila del inventario, incluida licencia y alternativa.', 'Confundir «encontrado en Internet» con permiso de uso o escribir textos alternativos sin atender a la función.', 'No se edita ningún recurso hasta que origen, función y alternativa estén decididos.'),
   'B02': ('Exporta una misma imagen a dos anchos y formatos; compara peso y calidad a tamaño real. Repite el razonamiento con un clip.', 'Premiar el archivo más pequeño aunque presente artefactos o no funcione en el navegador elegido.', 'Cada elección conserva original, ajustes, dimensiones o duración, formato y peso.'),
   'B03': ('Integra un ejemplo con picture, audio, vídeo y VTT; desconecta una fuente para mostrar el fallback.', 'Dar por accesible el vídeo solo porque contiene subtítulos automáticos.', 'La tabla identifica navegador, acción, resultado real, incidencia y corrección.'),
  }},
 'Accesibilidad': {
  'student': 'Organización orientativa: tres bloques de 60–90 minutos. Evalúa un recorrido concreto, no todo el sitio. Consulta la [matriz mínima WCAG y la evaluación](taller.md#matriz-minima-de-comprobacion).',
  'teacher': {
   'B01': ('Delimita una tarea y relaciona cada paso con una comprobación WCAG 2.2 de la matriz mínima.', 'Copiar el resultado de una herramienta automática como si certificara todo el sitio.', 'La matriz incluye página, criterio, procedimiento reproducible y tecnología utilizada.'),
   'B02': ('Recorre un caso defectuoso solo con teclado, a 200 % de zoom y a 320 CSS px; verbaliza qué evidencia observas.', 'Confundir inspección del HTML con una prueba de lector de pantalla.', 'Cada incidencia contiene pasos, resultado obtenido, resultado esperado y evidencia.'),
   'B03': ('Corrige primero una barrera que impide completar la tarea y repite exactamente el mismo procedimiento.', 'Presentar una captura posterior sin demostrar que la barrera dejó de reproducirse.', 'Conserva antes/después, nueva prueba y pendientes; evita afirmar conformidad completa.'),
  }},
 'Usabilidad': {
  'student': 'Organización orientativa: tres bloques de 60–90 minutos. Trabaja con dos tareas y registra cada sesión sin datos personales. Consulta el [protocolo, las plantillas y la matriz de evaluación](taller.md#entrega-y-matriz-de-evaluacion).',
  'teacher': {
   'B01': ('Convierte una instrucción guiada en una tarea neutral y fija éxito, abandono y ayuda antes de probar.', 'Redactar tareas que nombran el botón o la ruta y anticipan la solución.', 'El protocolo contiene bienvenida, consentimiento, tareas, registro y cierre.'),
   'B02': ('Modela una sesión breve: el observador guarda silencio, toma hechos y separa después sus hipótesis.', 'Ayudar para que la persona termine y registrar el resultado como éxito sin asistencia.', 'Cada sesión identifica condiciones, finalización, ayudas, dudas y observaciones literales.'),
   'B03': ('Clasifica tres dificultades por impacto y frecuencia, cambia una y repite la tarea con el mismo criterio.', 'Atribuir toda mejora al cambio cuando participa la misma persona y ya conoce el recorrido.', 'La comparación declara muestra, familiaridad, límites y decisión mantenida o pendiente.'),
  }},
}
for unit in units:
 key=unit['id'];dest=R/'docs'/key;dest.mkdir(exist_ok=True)
 student=f"# {key} · {unit['titulo']}\n\nPartimos de **{unit['entrada']}**. Al terminar conservarás **{unit['entrega']}**.\n\n"
 student+='Sigue estos bloques en el orden indicado. Las fechas y entregas se comunican en clase. Aplica lo aprendido a tu proyecto y conserva las evidencias con el identificador del bloque.\n\n'
 if key in unit_guidance:student+=unit_guidance[key]['student']+'\n\n'
 if key=='UD1':student+='[Mirada: ejemplo guiado](Ejemplo_Figma_Mirada.md) · [Actividades A1–A21](Actividades.md) · [Guía de objetivos y criterios](objetivos.md). Mirada es un ejemplo explicado paso a paso y no tiene ninguna entrega. La actividad 21 es la única actividad obligatoria y su proyecto evolucionará a lo largo del curso. El docente decidirá cuáles de las demás actividades se entregan y lo comunicará en clase. Trabaja en un archivo de prácticas y otro del proyecto propio. DesignPro es apoyo y A20 un ensayo breve.\n\n'
 teacher=f"# {key} · Guion del profesor\n\nEntrada: **{unit['entrada']}**. Salida: **{unit['entrega']}**.\n\n"
 teacher+='Esta secuencia comparte identificadores, actividades y evidencias con la guía del alumnado. No cambia ponderaciones ni asigna automáticamente horas oficiales. Divide cada bloque en las sesiones que requiera el grupo.\n\n'
 if key=='UD1':teacher+='Mirada es un ejemplo explicado paso a paso y no tiene ninguna entrega. La actividad 21 es la única actividad obligatoria y su proyecto evolucionará a lo largo del curso. El docente decidirá cuáles de las demás actividades se entregan y lo comunicará en clase.\n\nPara UD1 se proponen 12 bloques de hasta dos horas; los 24 periodos de 60 minutos son una opción de aula, pendiente de conciliar con las 12 sesiones de la programación. La antigua secuenciación detallada queda como referencia en la copia original; aquí prevalecen los bloques B01–B12 y los enunciados DIWv4.\n\n'
 for b in unit['bloques']:
  links=' · '.join(f'[{Path(p).stem}](<{p}>)' for p in b['recursos'])
  shared=f"## {b['id']} · {b['titulo']}\n\n**Consulta:** {links}.\n\n**Práctica:** {b['actividad']}.\n\n{b['trabajo']}\n\n**Evidencia para avanzar:** {b['evidencia']}\n\n"
  student+=shared
  teacher+=shared
  hint=notes.get(key,{}).get(b['id'])
  if hint:
   teacher+=f"**Demostración preparada:** {hint['demostracion']}\n\n**Dificultad previsible:** {hint['dificultad']}\n\n**Control del profesor:** {hint['control']}\n\n"
  specific=unit_guidance.get(key,{}).get('teacher',{}).get(b['id'])
  if specific:
   teacher+=f'''**Demostración preparada:** {specific[0]}

**Dificultad previsible:** {specific[1]}

**Control del profesor:** {specific[2]}

'''
  teacher+='''**Guion de intervención:**

1. Recupera la evidencia del bloque anterior y plantea la decisión que deben resolver.
2. Realiza la demostración preparada y verbaliza la relación entre procedimiento, evidencia y decisión.
3. Deja que ejecuten la comprobación o transformación y pide que registren el resultado antes de interpretarlo.
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
