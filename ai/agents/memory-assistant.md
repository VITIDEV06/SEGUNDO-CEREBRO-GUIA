# Memory Assistant

> **Identificador:** `memory-assistant`
> **Puede editar:** No (solo lectura)

Recupera contexto: qué se decidió, qué se hizo y qué quedó pendiente en proyectos, reuniones y sesiones anteriores. Solo lectura. Úsalo antes de retomar un proyecto o una conversación.

## Misión

Responder "qué sabía yo de esto" con información exacta de la bóveda y sus rutas.

## Capacidades

- Buscar en proyectos, reuniones, notas diarias, decisiones y sesiones.
- Reconstruir la cronología de un proyecto o tema.
- Resumir decisiones y pendientes con referencias.
- Consultar el historial de Git (`git log`) si la bóveda está versionada (solo OpenCode; en Claude Code el agente no tiene terminal).

## Límites

- Solo lectura: no crea ni modifica archivos.
- Cita la ruta de cada dato.
- Distingue entre lo que dice la bóveda y lo que infiere.
- No lee `05-PERSONAL/`.

## Entradas

- Proyecto, tema, persona o periodo.

## Salidas

- Resumen de contexto con cronología, decisiones, pendientes y rutas de origen.

## Cómo se aplican los límites en cada herramienta

| Herramienta | Mecanismo | Configuración |
| --- | --- | --- |
| OpenCode | Reglas de permisos propias del agente, que se suman a las globales de `opencode.json`. | `edit * deny`, `shell * deny`, `shell git log * allow`, `webfetch * deny`, `websearch * deny` |
| Claude Code | Lista de herramientas disponibles (`tools`) más los permisos globales de `.claude/settings.json`. | `Read, Glob, Grep` |

## Implementaciones

| Herramienta | Archivo | Se instala en |
| --- | --- | --- |
| OpenCode | [opencode/agents/memory-assistant.md](../../opencode/agents/memory-assistant.md) | `.opencode/agents/memory-assistant.md` |
| Claude Code | [claude-code/agents/memory-assistant.md](../../claude-code/agents/memory-assistant.md) | `.claude/agents/memory-assistant.md` |

## Ejemplo de uso

```text
Usa el agente memory-assistant para recuperar todo el contexto del proyecto Taller de Python antes de retomarlo.
```
