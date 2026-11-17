# 11 — Uso avanzado

> **Objetivo:** ampliar el sistema cuando ya dominas lo básico: nuevos agentes y comandos, Bases más ricas, mapas de contenido, configuración global y uso no interactivo.
> **Requisito:** haber completado las guías 01 a 10.

Anterior: [10 — Workflows](10-workflows.md) | [Inicio](../README.md) | Siguiente: [12 — Seguridad y privacidad](12-security-privacy.md)

---

## 1. Crear tu propio agente

Supongamos que quieres un agente **Writing Assistant** que convierta notas permanentes en borradores de artículos.

### Paso 1 — Especificación neutral

Crea `ai/agents/writing-assistant.md` (en tu copia de este repositorio) con la misma estructura que los demás: misión, capacidades, límites, entradas y salidas. Esto obliga a pensar los límites antes de escribir el prompt.

### Paso 2 — Implementación en OpenCode

`.opencode/agents/writing-assistant.md` en tu bóveda:

```markdown
---
description: "Convierte notas permanentes enlazadas en borradores de artículos. Solo crea borradores en 00-INBOX."
mode: all
permissions:
  - action: edit
    resource: "*"
    effect: deny
  - action: edit
    resource: "*00-INBOX/*"
    effect: ask
---

Eres el Writing Assistant de un segundo cerebro. A partir de las notas que te indiquen,
y de las notas que enlazan, escribe un borrador de artículo en 00-INBOX/ citando cada
nota de origen con [[enlace]]. No añadas afirmaciones que no estén en las notas.
```

### Paso 3 — Implementación en Claude Code

`.claude/agents/writing-assistant.md` en tu bóveda:

```markdown
---
name: writing-assistant
description: "Convierte notas permanentes enlazadas en borradores de artículos. Solo crea borradores en 00-INBOX."
tools: Read, Glob, Grep, Write
---

Eres el Writing Assistant de un segundo cerebro. A partir de las notas que te indiquen,
y de las notas que enlazan, escribe un borrador de artículo en 00-INBOX/ citando cada
nota de origen con [[enlace]]. No añadas afirmaciones que no estén en las notas.
```

### Paso 4 — Documentarlo

Añade el agente a la tabla de `AGENTS.md` o de `.opencode/instructions/` y `CLAUDE.md` para que el agente principal sepa que existe.

## 2. Crear tu propio comando

| Herramienta | Archivo | Se ejecuta con |
| --- | --- | --- |
| OpenCode | `.opencode/commands/borrador.md` | `/borrador` |
| Claude Code | `.claude/skills/borrador/SKILL.md` | `/borrador` |

OpenCode:

```markdown
---
description: "Genera un borrador de artículo a partir de una nota y sus enlaces."
agent: writing-assistant
---

Escribe un borrador de artículo a partir de la nota $ARGUMENTS y de las notas que enlaza.
```

Claude Code:

```markdown
---
name: borrador
description: "Genera un borrador de artículo a partir de una nota y sus enlaces."
argument-hint: "[nombre de la nota]"
disable-model-invocation: true
---

Usa el subagente writing-assistant para escribir un borrador de artículo a partir
de la nota $ARGUMENTS y de las notas que enlaza.
```

## 3. Bases más útiles

### Filtrar por tag y limitar resultados

```yaml
filters:
  and:
    - file.hasTag("tema/aprendizaje")
    - 'tipo == "permanente"'
views:
  - type: table
    name: Aprendizaje
    limit: 30
    order:
      - file.name
      - note.actualizado
      - file.backlinks
```

### Reuniones de un proyecto

```yaml
filters:
  and:
    - file.inFolder("07-MEETINGS")
    - 'tipo == "reunion"'
views:
  - type: table
    name: Reuniones
    order:
      - file.name
      - note.proyecto
      - note.asistentes
```

Propiedades de archivo disponibles en Bases: `file.name`, `file.path`, `file.folder`, `file.ext`, `file.size`, `file.ctime`, `file.mtime`, `file.tags`, `file.links`, `file.backlinks`, `file.embeds`, `file.properties`, `file.file`. Las propiedades de la nota se escriben con o sin el prefijo `note.`.

> `file.backlinks` es costoso de calcular en bóvedas grandes; úsalo en vistas con `limit`.

Las Bases también admiten fórmulas (`formulas:`). Consulta la [sintaxis oficial](https://obsidian.md/help/bases/syntax) antes de usarlas: es una función que evoluciona con cada versión de Obsidian.

## 4. Mapas de contenido (MOC)

Cuando un tema supera unas 10 notas, crea `03-RESOURCES/MOC - Tema.md`:

```markdown
---
tipo: moc
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
tags:
  - tema/aprendizaje
---

# MOC - Aprendizaje

## Fundamentos
- [[La práctica espaciada mejora la retención]] — por qué repartir el estudio.
- [[La recuperación activa supera a la relectura]] — cómo estudiar.

## Técnicas
- [[Técnica Feynman]] — detectar lagunas explicando con palabras simples.

## Preguntas abiertas
- ¿Cómo combinar práctica espaciada con proyectos reales?
```

Prompt: [13 — Crear un mapa de conocimientos](../ai/prompts/13-mapa-de-conocimientos.md).

## 5. Configuración global frente a configuración de la bóveda

| Ámbito | OpenCode | Claude Code |
| --- | --- | --- |
| Solo esta bóveda | `opencode.json`, `.opencode/` | `CLAUDE.md`, `.claude/settings.json`, `.claude/` |
| Todos tus proyectos | `~/.config/opencode/opencode.json`, `~/.config/opencode/AGENTS.md`, `~/.config/opencode/agents/` | `~/.claude/settings.json`, `~/.claude/CLAUDE.md`, `~/.claude/agents/` |

Mantén la configuración de la bóveda **en la bóveda**: así viaja con ella y queda versionada. Usa la global solo para preferencias personales que apliquen a todos tus proyectos.

## 6. Uso no interactivo de Claude Code

Claude Code puede ejecutar un prompt y terminar, útil para scripts:

```bash
# Bash, PowerShell o CMD, desde la raíz de la bóveda
claude -p "Lista las notas de 00-INBOX con más de 7 días. No modifiques nada."
```

Con `-p` no hay nadie para aprobar acciones con efecto `ask`, así que úsalo para tareas de **solo lectura**.

## 7. Varias bóvedas

Puedes tener varias bóvedas (por ejemplo, una personal y otra de trabajo). Cada una tiene su propio `AGENTS.md`, configuración de agentes y repositorio Git. Abre el agente en la raíz de la bóveda que quieras usar: la configuración se carga desde la carpeta actual.

## 8. Ampliar con herramientas externas (MCP)

Ambos agentes soportan el *Model Context Protocol* (MCP) para conectarse a servicios externos (calendarios, gestores de tareas, bases de datos). Esta guía no incluye configuraciones MCP porque cada servidor tiene requisitos y riesgos propios. Si lo exploras:

- Consulta la documentación oficial de cada herramienta: [OpenCode](https://opencode.ai/docs/) y [Claude Code](https://code.claude.com/docs/en/mcp).
- Cada servidor MCP es código de terceros con acceso a lo que le permitas: revisa su origen y sus permisos.

---

Anterior: [10 — Workflows](10-workflows.md) | [Inicio](../README.md) | Siguiente: [12 — Seguridad y privacidad](12-security-privacy.md)
