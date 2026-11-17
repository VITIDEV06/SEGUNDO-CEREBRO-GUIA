---
name: contexto-proyecto
description: "Recupera el contexto completo de un proyecto o tema: cronología, decisiones, pendientes y fuentes. Solo lectura."
argument-hint: "[nombre del proyecto o tema]"
disable-model-invocation: true
context: fork
agent: memory-assistant
---

Recupera el contexto de: $ARGUMENTS

Busca, en este orden: `09-AI-MEMORY/contexto-activo.md`, `09-AI-MEMORY/decisiones.md`, la nota principal en `01-PROJECTS/` o `04-ARCHIVE/`, reuniones en `07-MEETINGS/`, notas diarias en `06-DAILY-NOTES/`, sesiones en `09-AI-MEMORY/sesiones/` y notas relacionadas en `03-RESOURCES/` y `08-IDEAS/`.

Responde con:

## Contexto de <tema>
**Resumen:** 3 a 5 frases.
### Cronología
### Decisiones
### Pendientes
### Personas involucradas
### Lagunas (lo que no aparece en la bóveda)

Cada afirmación lleva la ruta de la nota de origen entre comillas invertidas. No modifiques ningún archivo. No leas `05-PERSONAL/`.
