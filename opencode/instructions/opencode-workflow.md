# Instrucciones específicas de OpenCode

Este archivo complementa `AGENTS.md` con información que solo aplica a OpenCode. Se carga mediante el campo `instructions` de `opencode.json`.

## Agentes disponibles

| Agente | Úsalo para |
| --- | --- |
| `knowledge-manager` | Organizar, clasificar y enlazar notas; crear MOC. Es el agente por defecto. |
| `research-assistant` | Investigar un tema y crear una nota en `00-INBOX/`. |
| `project-manager` | Crear y actualizar proyectos y reuniones. |
| `note-processor` | Procesar `00-INBOX/`. |
| `learning-assistant` | Organizar estudio y preparar sesiones de repaso. |
| `memory-assistant` | Recuperar contexto (solo lectura). |
| `vault-auditor` | Auditar la bóveda (solo lectura). |

Si una tarea encaja claramente con un agente especializado, delégala en ese agente.

## Comandos disponibles

`/capturar`, `/procesar-inbox`, `/nuevo-proyecto`, `/contexto-proyecto`, `/revision-semanal`, `/auditar-boveda`, `/sincronizar`.

## Mover y renombrar notas

OpenCode no tiene una herramienta específica para mover archivos: usa el comando de terminal correspondiente (`git mv` si la bóveda está versionada; `mv` en Bash o `Move-Item` en PowerShell en caso contrario). Estos comandos piden confirmación según `opencode.json`. Después de mover, actualiza los enlaces `[[...]]` que apuntaban a la nota.

## Comandos que nunca debes intentar

Borrado de archivos (`rm`, `del`, `Remove-Item`), `git push`, `git reset --hard`, `git clean`. Están denegados en la configuración. Si una tarea parece requerirlos, explica por qué y deja que la persona los ejecute.
