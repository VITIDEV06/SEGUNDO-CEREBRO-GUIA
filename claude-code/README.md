# Configuración para Claude Code

Archivos listos para instalar en tu bóveda. Guía completa: [docs/08-claude-code-setup.md](../docs/08-claude-code-setup.md).

## Contenido

| Archivo o carpeta | Se instala en la bóveda como | Función |
| --- | --- | --- |
| [CLAUDE.md.example](CLAUDE.md.example) | `CLAUDE.md` | Importa `AGENTS.md` y las reglas de `99-SYSTEM/rules/`; añade lo específico de Claude Code. |
| [settings.example.json](settings.example.json) | `.claude/settings.json` | Permisos `allow` / `ask` / `deny`. |
| [agents/](agents/) | `.claude/agents/` | 7 subagentes. |
| [skills/](skills/) | `.claude/skills/` | 7 skills invocables con `/nombre`. |
| [rules/](rules/) | `.claude/rules/` | Reglas que se cargan al trabajar con archivos `.md`. |

> **Por qué `skills/` y no `commands/`:** la documentación de Claude Code indica que los comandos personalizados se fusionaron con las skills. Los archivos de `.claude/commands/` siguen funcionando, pero las skills son el formato recomendado para trabajo nuevo.

## Instalación rápida

```bash
# Desde la raíz de este repositorio (en macOS/Linux usa python3)
python scripts/install-agents.py --tool claude-code --vault "<ruta-de-tu-bóveda>"
```

Reinicia Claude Code después de instalar.

## Política de permisos

| Lista | Reglas | Efecto |
| --- | --- | --- |
| `allow` | `Read`, `Glob`, `Grep`, `git status/diff/log` (Bash y PowerShell) | Sin confirmación. |
| `ask` | `Edit`, `Read(./05-PERSONAL/**)`, `WebFetch`, `WebSearch` | Pide confirmación. |
| `deny` | Editar `05-PERSONAL/`, `.obsidian/`, `.claude/`; leer `.env` y claves; `rm`, `rmdir`, `Remove-Item`, `del`; `git push`, `git reset --hard`, `git clean`, `git checkout --` | Siempre rechazado. |

Orden de evaluación: **`deny` → `ask` → `allow`**. La primera lista que coincide decide.

## Subagentes

| Subagente | `tools` |
| --- | --- |
| `knowledge-manager` | `Read, Glob, Grep, Edit, Write, Bash` |
| `research-assistant` | `Read, Glob, Grep, Write, WebSearch, WebFetch` |
| `project-manager` | `Read, Glob, Grep, Edit, Write` |
| `note-processor` | `Read, Glob, Grep, Edit, Write, Bash` |
| `learning-assistant` | `Read, Glob, Grep, Edit, Write` |
| `memory-assistant` | `Read, Glob, Grep` |
| `vault-auditor` | `Read, Glob, Grep` |

`Bash` se incluye solo en los agentes que necesitan mover archivos (`git mv` o `mv`); los permisos globales siguen aplicándose.

## Skills

| Skill | Se ejecuta en | Qué hace |
| --- | --- | --- |
| `/capturar` | Sesión principal | Crea una captura en `00-INBOX/`. |
| `/procesar-inbox` | Sesión principal | Procesa la bandeja con aprobación. |
| `/nuevo-proyecto` | Sesión principal | Crea un proyecto. |
| `/contexto-proyecto` | Subagente `memory-assistant` (`context: fork`) | Recupera contexto, solo lectura. |
| `/revision-semanal` | Sesión principal | Revisión semanal guiada. |
| `/auditar-boveda` | Subagente `vault-auditor` (`context: fork`) | Auditoría, solo lectura. |
| `/sincronizar` | Sesión principal | Mantenimiento completo por fases. |

Las skills que modifican archivos se ejecutan en la sesión principal porque necesitan tu aprobación paso a paso.

## Validar el JSON

```bash
python -m json.tool claude-code/settings.example.json
```

Dentro de Claude Code, `/permissions` muestra las reglas activas y `claude doctor` (en la terminal) informa de errores de validación.
