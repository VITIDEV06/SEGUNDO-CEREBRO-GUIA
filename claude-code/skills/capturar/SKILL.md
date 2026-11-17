---
name: capturar
description: "Guarda una idea o información nueva como captura en 00-INBOX sin interrumpir lo que estás haciendo."
argument-hint: "[texto de la idea]"
disable-model-invocation: true
---

Captura la siguiente información en la bandeja de entrada del segundo cerebro:

$ARGUMENTS

Instrucciones:
1. Crea un archivo nuevo en `00-INBOX/` con un título breve y descriptivo (sin caracteres prohibidos: `\ / : * ? " < > | # ^ [ ]`).
2. Contenido:
   - Frontmatter con `tipo: captura`, `estado: borrador`, `creado` y `actualizado` con la fecha de hoy.
   - El texto capturado tal cual, sin reinterpretarlo.
   - Una sección `## Posibles conexiones` con hasta 3 notas existentes relacionadas (búscalas por título y contenido). Si no encuentras ninguna, escribe "Ninguna encontrada".
3. No proceses ni clasifiques la captura: eso se hace con `/procesar-inbox`.
4. Responde solo con la ruta del archivo creado y las conexiones encontradas.
