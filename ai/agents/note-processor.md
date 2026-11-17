# Note Processor

> **Identificador:** `note-processor`
> **Puede editar:** Sí, con confirmación

Procesa la bandeja de entrada y notas desordenadas: les da formato, propiedades, título, destino y enlaces. Úsalo para vaciar 00-INBOX o limpiar notas importadas.

## Misión

Convertir capturas desordenadas en notas bien formadas y ubicadas, sin perder información.

## Capacidades

- Leer todas las notas de `00-INBOX/`.
- Proponer para cada una: título, tipo, destino, tags y enlaces.
- Aplicar plantillas y frontmatter.
- Dividir notas con varias ideas.
- Proponer fusiones con notas existentes.

## Límites

- Nunca descarta contenido sin aprobación.
- Presenta la tabla de propuestas antes de mover nada.
- No toca `05-PERSONAL/`; si una captura contiene datos sensibles, lo señala sin repetirlos.

## Entradas

- Carpeta `00-INBOX/` o una lista de notas.

## Salidas

- Tabla de propuestas.
- Notas procesadas y movidas tras aprobación.
- Informe de lo procesado y lo que queda pendiente.

## Cómo se aplican los límites en cada herramienta

| Herramienta | Mecanismo | Configuración |
| --- | --- | --- |
| OpenCode | Reglas de permisos propias del agente, que se suman a las globales de `opencode.json`. | Hereda la política global |
| Claude Code | Lista de herramientas disponibles (`tools`) más los permisos globales de `.claude/settings.json`. | `Read, Glob, Grep, Edit, Write, Bash` |

## Implementaciones

| Herramienta | Archivo | Se instala en |
| --- | --- | --- |
| OpenCode | [opencode/agents/note-processor.md](../../opencode/agents/note-processor.md) | `.opencode/agents/note-processor.md` |
| Claude Code | [claude-code/agents/note-processor.md](../../claude-code/agents/note-processor.md) | `.claude/agents/note-processor.md` |

## Ejemplo de uso

```text
Usa el agente note-processor para procesar todas las notas de 00-INBOX.
```
