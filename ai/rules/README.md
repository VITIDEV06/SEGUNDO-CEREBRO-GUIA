# Reglas para agentes

Las reglas que siguen los agentes de IA **no están duplicadas aquí**: viven dentro de la plantilla de bóveda, porque es ahí donde los agentes las leen.

| Archivo | Contenido | Cómo lo carga OpenCode | Cómo lo carga Claude Code |
| --- | --- | --- | --- |
| [vault-template/AGENTS.md](../../vault-template/AGENTS.md) | Reglas principales, estructura y flujo de sesión. | Automático | `@AGENTS.md` en `CLAUDE.md` |
| [conventions.md](../../vault-template/99-SYSTEM/rules/conventions.md) | Nombres, propiedades, enlaces y ubicación. | `instructions` | `@99-SYSTEM/rules/conventions.md` |
| [note-quality.md](../../vault-template/99-SYSTEM/rules/note-quality.md) | Qué hace buena a una nota. | `instructions` | Se lee bajo demanda |
| [privacy.md](../../vault-template/99-SYSTEM/rules/privacy.md) | Qué es sensible y cómo tratarlo. | `instructions` | `@99-SYSTEM/rules/privacy.md` |
| [agent-behavior.md](../../vault-template/99-SYSTEM/rules/agent-behavior.md) | Flujo de aprobación y límites. | `instructions` | `@99-SYSTEM/rules/agent-behavior.md` |
| [tags.md](../../vault-template/99-SYSTEM/tags.md) | Taxonomía de tags. | Referenciado desde `AGENTS.md` | Referenciado desde `AGENTS.md` |

Reglas **específicas de una herramienta** (no compartidas):

| Herramienta | Archivo |
| --- | --- |
| OpenCode | [opencode/instructions/opencode-workflow.md](../../opencode/instructions/opencode-workflow.md) |
| Claude Code | [claude-code/rules/obsidian-markdown.md](../../claude-code/rules/obsidian-markdown.md) |

## Principios para escribir reglas

1. **Concretas y verificables.** "Al editar, actualiza la propiedad `actualizado`" funciona mejor que "mantén las notas al día".
2. **Cortas.** Los archivos de instrucciones se cargan en cada sesión y consumen contexto.
3. **Respaldadas por permisos.** Si una regla protege algo importante, añade también un permiso `deny` en la configuración: las instrucciones orientan, los permisos obligan.
4. **Una sola fuente.** Si una regla aplica a ambos agentes, va en la bóveda, no en la configuración de una herramienta.
