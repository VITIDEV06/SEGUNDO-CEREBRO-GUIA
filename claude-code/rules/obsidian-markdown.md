---
paths:
  - "**/*.md"
---

# Reglas al editar notas Markdown de Obsidian

Esta regla se carga cuando Claude Code lee o edita un archivo `.md` de la bóveda (campo `paths`).

- Conserva el bloque de propiedades YAML al inicio del archivo. Nunca dejes líneas antes del primer `---`.
- Actualiza la propiedad `actualizado` con la fecha de hoy en cada edición.
- Usa wikilinks `[[Nombre de nota]]`, no enlaces Markdown relativos, para enlazar notas de la bóveda.
- Dentro de las propiedades, los enlaces van entre comillas: `area: "[[Docencia]]"`.
- No cambies el nombre de un archivo editando su contenido: renombrar es mover, y requiere actualizar los enlaces entrantes.
- No conviertas wikilinks existentes en otro formato.
- Mantén las tablas Markdown con una fila de encabezado y una fila separadora `| --- |`.
