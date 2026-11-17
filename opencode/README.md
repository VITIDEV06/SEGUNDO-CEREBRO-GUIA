# Configuración para OpenCode

Archivos listos para instalar en tu bóveda. Guía completa: [docs/07-opencode-setup.md](../docs/07-opencode-setup.md).

> Formato **V2** de OpenCode (documentación oficial, noviembre de 2026): `permissions` como lista de reglas, acción `shell`, carpetas `agents/` y `commands/`.

## Contenido

| Archivo o carpeta | Se instala en la bóveda como | Función |
| --- | --- | --- |
| [opencode.example.json](opencode.example.json) | `opencode.json` | Permisos, instrucciones adicionales y agente por defecto. |
| [agents/](agents/) | `.opencode/agents/` | 7 agentes especializados (`mode: all`). |
| [commands/](commands/) | `.opencode/commands/` | 7 comandos: `/capturar`, `/procesar-inbox`, `/nuevo-proyecto`, `/contexto-proyecto`, `/revision-semanal`, `/auditar-boveda`, `/sincronizar`. |
| [instructions/](instructions/) | `.opencode/instructions/` | Instrucciones específicas de OpenCode, cargadas por `instructions`. |

`AGENTS.md` no está aquí: forma parte de la plantilla de bóveda ([vault-template/AGENTS.md](../vault-template/AGENTS.md)) porque lo comparten OpenCode y Claude Code.

## Instalación rápida

```bash
# Desde la raíz de este repositorio (en macOS/Linux usa python3)
python scripts/install-agents.py --tool opencode --vault "<ruta-de-tu-bóveda>"
```

## Política de permisos

| Acción | Efecto |
| --- | --- |
| `read`, `glob`, `grep` en toda la bóveda | `allow` |
| `read` en `05-PERSONAL/` | `ask` |
| `read` de `.env` | `deny` |
| `edit` en general | `ask` |
| `edit` en `05-PERSONAL/`, `.obsidian/`, `.git/`, `.opencode/`, `opencode.json` | `deny` |
| `shell` en general | `ask` |
| `git status`, `git diff`, `git log` | `allow` |
| `rm`, `rmdir`, `del`, `Remove-Item`, `git push`, `git reset --hard`, `git clean`, `git checkout --` | `deny` |
| `webfetch`, `websearch`, `external_directory` | `ask` |

Recuerda: **la última regla que coincide gana**. Las excepciones van después de la regla general.

## Agentes y sus permisos propios

| Agente | Reglas añadidas |
| --- | --- |
| `knowledge-manager` | Ninguna (política global). Agente por defecto. |
| `research-assistant` | Solo edita en `00-INBOX/`; sin terminal. |
| `project-manager` | Solo edita en `01-PROJECTS/` y `07-MEETINGS/`. |
| `note-processor` | Ninguna (política global). |
| `learning-assistant` | Solo edita en `03-RESOURCES/` y `00-INBOX/`. |
| `memory-assistant` | Solo lectura; terminal solo para `git log`; sin web. |
| `vault-auditor` | Solo lectura; terminal solo para `git status`; sin web. |

## Validar el JSON

```bash
python -m json.tool opencode/opencode.example.json
```
