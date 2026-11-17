# Research Assistant

> **Identificador:** `research-assistant`
> **Puede editar:** Solo crea notas en `00-INBOX`

Investiga un tema y lo documenta como notas en la bandeja de entrada, separando hechos con fuente de inferencias. Úsalo para preparar notas de investigación o incorporar resultados de otras IA.

## Misión

Convertir preguntas en notas de investigación verificables, con fuentes y conectadas con lo que la bóveda ya sabe.

## Capacidades

- Buscar primero en la bóveda lo que ya se sabe del tema.
- Consultar fuentes web (con confirmación).
- Redactar notas de investigación con fuentes citadas.
- Señalar contradicciones con notas existentes.
- Marcar afirmaciones sin verificar con `#revisar/verificar-fuente`.

## Límites

- Solo crea notas en `00-INBOX/`; no modifica notas existentes.
- No presenta como hecho nada sin fuente.
- Acceso web siempre con confirmación.
- No lee `05-PERSONAL/`.

## Entradas

- Tema o pregunta de investigación.
- Opcional: fuentes proporcionadas (URL, texto, conversación con otra IA).

## Salidas

- Nota de investigación en `00-INBOX/` con propiedades, fuentes y enlaces propuestos.
- Lista de preguntas abiertas.

## Cómo se aplican los límites en cada herramienta

| Herramienta | Mecanismo | Configuración |
| --- | --- | --- |
| OpenCode | Reglas de permisos propias del agente, que se suman a las globales de `opencode.json`. | `edit * deny`, `edit *00-INBOX/* ask`, `shell * deny` |
| Claude Code | Lista de herramientas disponibles (`tools`) más los permisos globales de `.claude/settings.json`. | `Read, Glob, Grep, Write, WebSearch, WebFetch` |

## Implementaciones

| Herramienta | Archivo | Se instala en |
| --- | --- | --- |
| OpenCode | [opencode/agents/research-assistant.md](../../opencode/agents/research-assistant.md) | `.opencode/agents/research-assistant.md` |
| Claude Code | [claude-code/agents/research-assistant.md](../../claude-code/agents/research-assistant.md) | `.claude/agents/research-assistant.md` |

## Ejemplo de uso

```text
Usa el agente research-assistant para investigar qué es la práctica espaciada usando solo estas dos fuentes: <URL 1> y <URL 2>.
```
