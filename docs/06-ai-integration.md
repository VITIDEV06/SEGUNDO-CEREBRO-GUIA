# 06 — Integración con IA: una arquitectura, dos agentes

> **Objetivo:** entender cómo OpenCode y Claude Code trabajan sobre la misma bóveda sin duplicar reglas ni conocimiento, y qué archivo configura qué.
> **Tiempo estimado:** 25 minutos.

Anterior: [05 — Arquitectura de la bóveda](05-vault-architecture.md) | [Inicio](../README.md) | Siguiente: [07 — OpenCode](07-opencode-setup.md)

---

## 1. Qué es un agente de programación y por qué sirve para notas

**OpenCode** y **Claude Code** son *agentes* que se ejecutan en la terminal. A diferencia de un chat, pueden **leer archivos, buscar en carpetas, editar archivos y ejecutar comandos** en la carpeta donde los abres, siempre según los permisos que configures.

Fueron diseñados para programar, pero una bóveda de Obsidian es exactamente lo que mejor manejan: una carpeta de archivos de texto. Por eso pueden:

- Resumir las notas de un proyecto.
- Encontrar notas duplicadas o huérfanas.
- Convertir capturas desordenadas en notas bien formadas.
- Recuperar el contexto de un proyecto de hace meses.

## 2. El principio: la bóveda es la fuente de verdad

```mermaid
flowchart TB
    subgraph Boveda[Bóveda: fuente de verdad]
        AG[AGENTS.md<br/>reglas compartidas]
        RU[99-SYSTEM/rules/*.md<br/>convenciones detalladas]
        MEM[09-AI-MEMORY/<br/>contexto persistente]
        NOTAS[Notas 00 a 08]
    end
    subgraph OpenCode
        OJ[opencode.json<br/>permisos e instrucciones]
        OA[.opencode/agents/]
        OCm[.opencode/commands/]
    end
    subgraph ClaudeCode[Claude Code]
        CM[CLAUDE.md<br/>importa AGENTS.md]
        CS[.claude/settings.json<br/>permisos]
        CA[.claude/agents/]
        CSk[.claude/skills/]
    end
    AG -->|lectura nativa| OpenCode
    OJ -->|instructions| RU
    CM -->|@AGENTS.md| AG
    CM -->|@99-SYSTEM/rules/...| RU
    OpenCode --> NOTAS
    ClaudeCode --> NOTAS
    OpenCode --> MEM
    ClaudeCode --> MEM
```

- **Lo compartido** (qué carpetas existen, cómo se nombran las notas, qué propiedades usar, qué es privado) vive **una sola vez** dentro de la bóveda: `AGENTS.md` y `99-SYSTEM/rules/`.
- **Lo específico de cada herramienta** (formato de permisos, definición de agentes y comandos) vive en su carpeta de configuración: `.opencode/` y `opencode.json`, o `.claude/` y `CLAUDE.md`.

Si mañana cambias de herramienta, tus reglas siguen intactas.

## 3. Cómo lee cada herramienta las reglas compartidas

| Archivo | OpenCode | Claude Code |
| --- | --- | --- |
| `AGENTS.md` en la raíz | Lo lee automáticamente. | Lo lee automáticamente **si no hay** `CLAUDE.md`. Con `CLAUDE.md`, lo incluimos con la línea `@AGENTS.md`. |
| `CLAUDE.md` | Solo lo usa si **no** existe `AGENTS.md`. | Lo lee automáticamente. |
| `99-SYSTEM/rules/*.md` | Vía el campo `instructions` de `opencode.json`. | Vía importaciones `@ruta` dentro de `CLAUDE.md`. |

Fuentes: [OpenCode Rules](https://opencode.ai/docs/rules/) y [Claude Code Memory](https://code.claude.com/docs/en/memory).

## 4. Equivalencias entre herramientas

Los conceptos son parecidos pero **los formatos no son iguales**. No copies un archivo de una herramienta a la otra.

| Concepto | OpenCode | Claude Code |
| --- | --- | --- |
| Instrucciones de proyecto | `AGENTS.md` | `CLAUDE.md` (o `AGENTS.md`) |
| Reglas adicionales | `instructions` en `opencode.json` | Importaciones `@ruta` o `.claude/rules/*.md` |
| Configuración y permisos | `opencode.json`, clave `permissions` (lista de reglas `action` / `resource` / `effect`) | `.claude/settings.json`, clave `permissions` con listas `allow` / `ask` / `deny` |
| Agentes especializados | `.opencode/agents/<nombre>.md` con `mode: subagent` | `.claude/agents/<nombre>.md` con `name` y `description` |
| Comandos personalizados | `.opencode/commands/<nombre>.md` → `/nombre` | `.claude/skills/<nombre>/SKILL.md` → `/nombre` |
| Argumentos del comando | `$ARGUMENTS`, `$1`, `$2` | `$ARGUMENTS`, `$0`, `$1` |
| Prioridad de reglas | La **última** regla que coincide gana. | `deny` gana sobre `ask`, y `ask` sobre `allow`. |

> **Atención a la prioridad.** En OpenCode se escriben primero las reglas generales y después las excepciones. En Claude Code el orden dentro del archivo no importa: un `deny` siempre gana.

## 5. Modelo de permisos de la plantilla

Ambas configuraciones de ejemplo implementan la misma política:

| Acción | Política | Motivo |
| --- | --- | --- |
| Leer notas y buscar | Permitido | Consultar es el uso principal y no tiene riesgo de pérdida. |
| Leer `05-PERSONAL/` | Preguntar | Datos sensibles: decides en cada caso. |
| Leer `.env` y archivos de secretos | Denegado | Nunca deben llegar al modelo. |
| Crear o editar notas | Preguntar | Revisas cada cambio antes de aplicarlo. |
| Editar `05-PERSONAL/`, `.obsidian/`, `.git/` | Denegado | Información sensible y configuración interna. |
| `git status`, `git diff`, `git log` | Permitido | Solo lectura. |
| Otros comandos de terminal | Preguntar | Por defecto, confirmación. |
| Borrar archivos (`rm`, `del`, `Remove-Item`), `git push`, `git reset --hard`, `git clean` | Denegado | Acciones destructivas o que publican datos. |
| Acceso web | Preguntar | Evita fugas de información. |

> **Las reglas en `AGENTS.md` son orientaciones; los permisos son obligatorios.** Un modelo puede ignorar una instrucción escrita, pero no puede saltarse un `deny` de la configuración. Por eso la política se aplica en los dos niveles.

## 6. Los siete agentes

| Agente | Responsabilidad | Puede editar |
| --- | --- | --- |
| Knowledge Manager | Organiza, clasifica y enlaza conocimiento. | Sí, con confirmación |
| Research Assistant | Investiga y documenta temas. | Solo crea notas en `00-INBOX` |
| Project Manager | Crea y mantiene proyectos. | `01-PROJECTS`, `07-MEETINGS` |
| Note Processor | Procesa la bandeja de entrada. | `00-INBOX` y destinos |
| Learning Assistant | Organiza el aprendizaje y prepara sesiones de estudio. | Notas de aprendizaje |
| Memory Assistant | Recupera contexto de proyectos y decisiones. | No (solo lectura) |
| Vault Auditor | Revisa estructura, duplicados y privacidad. | No (solo lectura) |

Especificación completa: [ai/agents/](../ai/agents/README.md).

## 7. Qué agente usar

| Prefieres... | Elige |
| --- | --- |
| Código abierto y libertad de proveedor de modelos | OpenCode |
| Integración directa con modelos Claude y suscripción Pro/Max | Claude Code |
| No decidir todavía | Cualquiera: la bóveda funciona con ambos. |

## 8. Errores frecuentes

| Error | Solución |
| --- | --- |
| Copiar `CLAUDE.md` y `AGENTS.md` con el mismo contenido. | Duplicación. Usa `@AGENTS.md` dentro de `CLAUDE.md`. |
| Dar permisos de edición total "para que no pregunte tanto". | Usa permisos amplios solo en carpetas de bajo riesgo como `00-INBOX`. |
| Abrir el agente en la carpeta equivocada. | Abre siempre la terminal en la **raíz de la bóveda**. |
| Pensar que la IA recuerda la sesión anterior. | Guarda el contexto en `09-AI-MEMORY`. |

## 9. Resultado esperado

Sabes qué archivo controla qué cosa en cada herramienta, y entiendes que tus reglas de conocimiento viven en la bóveda, no en la herramienta.

---

Anterior: [05 — Arquitectura de la bóveda](05-vault-architecture.md) | [Inicio](../README.md) | Siguiente: [07 — OpenCode](07-opencode-setup.md)
