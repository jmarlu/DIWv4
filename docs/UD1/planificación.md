# Planificación

!!! example "Este apartado en Mirada"
    Del encargo y los perfiles al inventario, el mapa, el flujo y la prueba de tarea.

    [Paso 2: Escribir y entender el brief](Ejemplo_Figma_Mirada.md#paso-2-escribir-y-entender-el-brief) · [Paso 3: Del brief al inventario de contenido](Ejemplo_Figma_Mirada.md#paso-3-del-brief-al-inventario-de-contenido) · [Paso 4: Del brief al mapa y al flujo](Ejemplo_Figma_Mirada.md#paso-4-del-brief-al-mapa-y-al-flujo) · [Paso 35: Realizar una prueba de tarea](Ejemplo_Figma_Mirada.md#paso-35-realizar-una-prueba-de-tarea).

    Mirada es un ejemplo paso a paso sin entrega.

## Diseño centrado en el usuario

Diseñar una interfaz requiere entender quién la utiliza, qué quiere conseguir y en qué contexto. El proceso es iterativo: investigamos, proponemos una solución, observamos su uso y revisamos las decisiones.

Una preferencia como «quiero una página azul» no equivale a una necesidad como «necesito encontrar el horario antes de inscribirme». Primero identificamos la tarea; después decidimos cómo comunicar la información.

## Cuatro pasos que se repiten

1. **Conocer el contexto:** quién utiliza el servicio, con qué dispositivo y qué dificultades encuentra.
2. **Definir necesidades y requisitos:** qué tareas debe permitir y qué información hace falta para completarlas.
3. **Proponer soluciones:** organizar el contenido, dibujar alternativas y crear un prototipo.
4. **Evaluar:** observar si la tarea se completa y revisar lo que sea necesario.

Una entrevista aporta observaciones; una lluvia de ideas produce propuestas. No presentes una suposición del equipo como si fuera un resultado de investigación.

## Ejemplo guiado · Web de una asociación de fotografía

Este ejemplo ilustra los documentos, sin imponer la temática del proyecto ni describir entrevistas reales.

| Elemento | Ejemplo |
|---|---|
| Problema | La información de las actividades está dispersa |
| Usuario y contexto | Persona que consulta desde el móvil antes de decidir si asistir |
| Tarea | Encontrar el próximo paseo fotográfico y consultar sus requisitos |
| Contenido necesario | Fecha, duración, lugar, material y forma de contacto |
| Hipótesis pendiente | Suponemos que la fecha es el primer dato que busca |
| Cómo comprobarla | Pedir que elija una actividad usando un boceto y observar qué consulta |
| Alcance inicial | Principal y bocetos del recorrido hacia una actividad |

Incluye solo características del perfil que influyan en la tarea. No hace falta inventar nombre completo, estado civil o información personal para justificar una decisión.

## Tres documentos distintos

**Inventario:** lista el contenido que hay que preparar. Por ejemplo: título, fecha, descripción, requisitos y contacto de cada actividad.

**Mapa de navegación:** representa las páginas y sus relaciones.

```text
Inicio
├── Actividades
│   └── Detalle de actividad
└── Contacto
```

**Flujo de tarea:** representa los pasos que sigue una persona y sus decisiones.

```text
Consultar actividades → Abrir detalle → Leer fecha y requisitos
    → Si encaja: consultar cómo participar
    → Si no encaja: volver a actividades
```

El mapa muestra dónde está la información; el flujo ayuda a comprobar si el recorrido tiene sentido. Un wireframe es el boceto de la distribución de contenido de una pantalla: puede hacerse en papel antes de elegir colores.

## Qué es el brief y cómo utilizarlo

El brief es el documento breve que define el encargo antes de dibujar: problema, usuarios, tareas, requisitos, alcance y dudas. Se redacta con la información disponible y se revisa cuando aprendemos algo nuevo. El inventario concreta el contenido; el mapa organiza pantallas; el flujo representa la tarea.

En [Mirada, paso 2](Ejemplo_Figma_Mirada.md#paso-2-escribir-y-entender-el-brief) tienes el caso explicado apartado por apartado, un brief redactado y las instrucciones para llevarlo a Figma. Los pasos 3 y 4 muestran cómo obtener de él el inventario, el mapa y el flujo.

| Si escribes… | Concreta así… |
|---|---|
| «Quiero una web moderna» | Qué dificultad debe resolver y para quién |
| «El usuario pulsa un botón» | Qué quiere conseguir al pulsarlo |
| «La fecha es lo más importante» | Si lo has observado o es una hipótesis que vas a comprobar |
| «Habrá reservas» | Si solo representarás la solicitud o implementarás un servicio real |

El mapa de la sección anterior es un ejemplo genérico de asociación. Mirada acota el caso: las actividades aparecen como sección del inicio y solo una tiene el recorrido desarrollado. Cada proyecto debe justificar sus propias pantallas.

## Plantilla del brief

Copia este esquema en un documento del proyecto:

```text
Proyecto:
Problema que queremos resolver:
Dos perfiles y sus contextos de uso:
Tres tareas principales:
Contenido necesario:
Pantallas incluidas y funciones fuera del alcance:
Hipótesis pendientes y forma de contrastarlas:
Herramienta de diseño elegida y motivo:
```

## Probar sin dirigir la respuesta

Entrega una tarea como «Averigua qué necesitas para participar el sábado». No digas dónde pulsar. Observa el recorrido y anota dudas y resultado. Utiliza datos ficticios en cualquier formulario del prototipo.

| Observación | Interpretación pendiente | Decisión y comprobación |
|---|---|---|
| Busca el horario en dos pantallas | Quizá no está junto a la actividad | Acercarlo al título y repetir la tarea |

La tabla es un ejemplo de registro. En tu entrega, escribe solo lo observado. Puedes mantener una decisión si la prueba la respalda; no es obligatorio cambiar algo para demostrar que has revisado.

## Qué llevar a las siguientes unidades

El brief justifica el contenido; el mapa orienta las rutas HTML de UD2; el flujo se volverá a probar sobre la web implementada. Actualiza el registro si una decisión cambia.

[Aplicar en la actividad 8](Actividades.md#actividad-8) · [Integrar en la actividad 21](Actividades.md#actividad-21).
