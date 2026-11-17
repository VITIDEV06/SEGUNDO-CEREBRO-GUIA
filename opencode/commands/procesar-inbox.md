---
description: "Procesa las notas de 00-INBOX: propone título, tipo, destino y enlaces, y aplica los cambios aprobados."
agent: note-processor
---

Procesa la bandeja de entrada del segundo cerebro. Alcance: $ARGUMENTS (si está vacío, todas las notas de `00-INBOX/` excepto `LEEME-inbox.md`).

Sigue `AGENTS.md` y `99-SYSTEM/rules/conventions.md`.

Paso 1 — Analiza cada nota y presenta esta tabla, sin modificar nada todavía:

| Nota actual | Nuevo título | Tipo | Destino | Enlaces propuestos | Observaciones |
| --- | --- | --- | --- | --- | --- |

En *Observaciones* indica: posibles duplicados, notas que deberían dividirse, información sensible (solo la ruta, sin repetir el dato) o capturas descartables.

Paso 2 — Pregunta qué filas apruebo. No continúes sin respuesta.

Paso 3 — Para cada fila aprobada: añade frontmatter según el tipo, aplica la estructura de la plantilla correspondiente de `10-TEMPLATES/`, conserva el texto original en `## Captura original` si lo reescribes, mueve el archivo al destino y añade los enlaces.

Paso 4 — Informa: notas procesadas (ruta final), notas pendientes y dudas.
