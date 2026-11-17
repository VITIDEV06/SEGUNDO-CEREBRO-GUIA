---
name: nuevo-proyecto
description: "Crea un proyecto nuevo en 01-PROJECTS con la plantilla de proyecto, enlazado a su área y recursos."
argument-hint: "[nombre del proyecto] [descripción y objetivo]"
disable-model-invocation: true
---

Crea un proyecto nuevo en el segundo cerebro con esta información:

$ARGUMENTS

Instrucciones:
1. Busca en `01-PROJECTS/`, `08-IDEAS/` y `04-ARCHIVE/` si ya existe un proyecto o idea similar. Si existe, detente y pregunta si quiero reactivarlo o crear uno nuevo.
2. Crea `01-PROJECTS/<Nombre>/<Nombre>.md` con la estructura de `10-TEMPLATES/project.md`, sustituyendo las variables `{{...}}` por valores reales.
3. Completa solo con la información proporcionada. No inventes fechas, tareas ni responsables.
4. Busca un área en `02-AREAS/` y recursos en `03-RESOURCES/` relacionados y propón los enlaces.
5. Si existía una idea en `08-IDEAS/` que origina el proyecto, propón enlazarla y cambiar su estado.
6. Responde con: ruta creada, campos que faltan por completar y 3 preguntas para definir mejor el proyecto.
