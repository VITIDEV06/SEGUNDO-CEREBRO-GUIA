# 08 — Configuración de Claude Code

> **Objetivo:** instalar Claude Code, iniciar sesión y configurarlo sobre tu bóveda con `CLAUDE.md`, permisos, subagentes, skills y reglas.
> **Tiempo estimado:** 30 minutos.
> **Alternativa:** si prefieres OpenCode, ve a [07 — OpenCode](07-opencode-setup.md). No necesitas ambos.

Anterior: [07 — OpenCode](07-opencode-setup.md) | [Inicio](../README.md) | Siguiente: [09 — Git y GitHub](09-git-github.md)

---

> **Versión documentada.** Esta guía sigue la documentación oficial de Claude Code consultada en noviembre de 2026 ([code.claude.com/docs](https://code.claude.com/docs/en/setup)).

## 1. Qué es Claude Code

**Claude Code** es el agente de Anthropic que se ejecuta en la terminal (también existe como aplicación de escritorio y extensiones para VS Code y JetBrains). Lee y edita archivos de la carpeta donde lo abres y ejecuta comandos según los permisos que configures.

## 2. Requisitos de cuenta

Claude Code requiere una cuenta **Pro, Max, Ultra, Team, Enterprise** o **Console**. El plan gratuito de Claude no incluye Claude Code.

## 3. Instalación

### Windows

```powershell
# PowerShell (instalador oficial)
irm https://claude.ai/install.ps1 | iex
```

```cmd
:: CMD (instalador oficial)
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

```powershell
# PowerShell (WinGet; no se actualiza solo)
winget install Anthropic.ClaudeCode
```

> **Git for Windows** es recomendable: Claude Code usa Git Bash para su herramienta de terminal. Sin él, usa PowerShell. Lo instalaste en la [guía 03](03-installation.md#3-instalar-git).

### macOS, Linux y WSL

```bash
# Bash (instalador oficial)
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
# Bash (Homebrew; no se actualiza solo)
brew install --cask claude-code
```

### Comprobación

Abre una terminal **nueva** y ejecuta:

```bash
claude --version
```

Debe mostrar un número de versión. Para un diagnóstico completo:

```bash
claude doctor
```

Si aparece `'irm' is not recognized`, estás en CMD y no en PowerShell; si aparece `The token '&&' is not a valid statement separator`, estás en PowerShell y no en CMD.

## 4. Iniciar sesión

Entra en tu bóveda y ejecuta `claude`:

```powershell
# PowerShell (Windows)
cd "$HOME\Documents\SegundoCerebro"
claude
```

```bash
# Bash (macOS / Linux)
cd ~/Documents/SegundoCerebro
claude
```

La primera vez se abre el navegador para iniciar sesión. Con una suscripción no necesitas API key. Si usas una API key de Console, defínela como variable de entorno `ANTHROPIC_API_KEY` (nunca dentro de un archivo de la bóveda; ver [12 — Seguridad](12-security-privacy.md#2-variables-de-entorno)).

## 5. Instalar la configuración de la bóveda

### Opción A — Script

```powershell
# PowerShell (Windows)
python scripts/install-agents.py --tool claude-code --vault "$HOME\Documents\SegundoCerebro"
```

```bash
# Bash (macOS / Linux)
python3 scripts/install-agents.py --tool claude-code --vault ~/Documents/SegundoCerebro
```

### Opción B — Copia manual

| Copia desde este repositorio | A tu bóveda |
| --- | --- |
| `claude-code/CLAUDE.md.example` | `CLAUDE.md` |
| `claude-code/settings.example.json` | `.claude/settings.json` |
| `claude-code/agents/*.md` | `.claude/agents/` |
| `claude-code/skills/<nombre>/SKILL.md` | `.claude/skills/<nombre>/SKILL.md` |
| `claude-code/rules/*.md` | `.claude/rules/` |

### Resultado

```text
SegundoCerebro/
├── AGENTS.md                      reglas compartidas
├── CLAUDE.md                      importa AGENTS.md y 99-SYSTEM/rules
└── .claude/
    ├── settings.json              permisos
    ├── agents/                    7 subagentes
    ├── skills/                    7 skills (/capturar, /procesar-inbox, ...)
    └── rules/                     reglas que se cargan al tocar archivos .md
```

**Reinicia Claude Code** después de instalar: los directorios `.claude/agents/` y `.claude/skills/` creados durante una sesión no se cargan hasta reiniciar.

## 6. Cómo funciona cada pieza

### 6.1 `CLAUDE.md` y la importación de `AGENTS.md`

Claude Code lee `CLAUDE.md` al empezar cada sesión. Si existe `CLAUDE.md`, **no** lee `AGENTS.md` automáticamente, así que lo importamos:

```markdown
# Instrucciones para Claude Code

@AGENTS.md

## Convenciones detalladas

@99-SYSTEM/rules/conventions.md
@99-SYSTEM/rules/privacy.md
@99-SYSTEM/rules/agent-behavior.md
```

- `@ruta` incluye el contenido del archivo. Las rutas son relativas al archivo que contiene la importación.
- Si una ruta tiene espacios, escribe una barra invertida antes de cada espacio: `@Mis\ Reglas/archivo.md`.
- Una ruta entre comillas invertidas (`` `@AGENTS.md` ``) **no** se importa: se queda como texto.

> **Alternativa mínima:** si no creas `CLAUDE.md`, Claude Code lee `AGENTS.md` directamente. Pierdes las importaciones de reglas y las indicaciones específicas, pero funciona.

### 6.2 Permisos: `.claude/settings.json`

```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Bash(git status *)", "Bash(git diff *)", "Bash(git log *)"],
    "ask":   ["Edit", "Read(./05-PERSONAL/**)", "WebFetch", "WebSearch"],
    "deny":  ["Edit(./05-PERSONAL/**)", "Edit(./.obsidian/**)", "Read(./.env)",
              "Bash(rm *)", "Bash(git push *)", "Bash(git reset --hard *)",
              "PowerShell(Remove-Item *)"]
  }
}
```

*(Extracto. El archivo completo está en [claude-code/settings.example.json](../claude-code/settings.example.json).)*

**Cómo se evalúan:** primero `deny`, luego `ask`, luego `allow`. La primera lista que coincide decide, **sin importar lo específica que sea la regla**. Por eso:

- `Read` está permitido, pero `Read(./05-PERSONAL/**)` está en `ask` → leer esa carpeta pide confirmación.
- `Edit` está en `ask`, pero `Edit(./05-PERSONAL/**)` está en `deny` → editar esa carpeta se rechaza siempre.
- Una regla `allow` **no** puede abrir una excepción dentro de un `deny`.

**Sintaxis de rutas** (estilo `.gitignore`):

| Patrón | Significa |
| --- | --- |
| `./carpeta/**` | Relativo a la carpeta donde abriste Claude Code. |
| `/carpeta/**` | Relativo a la ubicación del archivo de configuración (en `.claude/settings.json`, la raíz del proyecto). |
| `~/carpeta/**` | Relativo a tu carpeta de usuario. |
| `//c/Users/...` | Ruta absoluta (en Windows, `C:\` se escribe `/c/`). |

`Edit(...)` cubre todas las herramientas que modifican archivos (Edit, Write). Las reglas `Bash(...)` aplican a Git Bash y las `PowerShell(...)` a la herramienta PowerShell de Windows; la plantilla incluye ambas.

**Archivos de configuración:**

| Archivo | Ámbito | ¿Se versiona? |
| --- | --- | --- |
| `.claude/settings.json` | Proyecto (la bóveda) | Sí |
| `.claude/settings.local.json` | Proyecto, solo tú | No (está en `.gitignore`) |
| `~/.claude/settings.json` | Todos tus proyectos | No |

> **Las instrucciones no son permisos.** Lo que escribes en `CLAUDE.md` orienta al modelo; lo que escribes en `permissions` lo hace cumplir Claude Code. Usa ambos.

### 6.3 Subagentes (`.claude/agents/`)

```markdown
---
name: vault-auditor
description: "Audita la estructura y consistencia de la bóveda... Solo lectura."
tools: Read, Glob, Grep
---

Eres el **Vault Auditor** de un segundo cerebro en Obsidian...
```

| Campo | Obligatorio | Función |
| --- | --- | --- |
| `name` | Sí | Identificador único. |
| `description` | Sí | Cuándo debe delegar Claude en este subagente. |
| `tools` | No | Herramientas disponibles. Si se omite, hereda todas. Los agentes de solo lectura tienen `Read, Glob, Grep`. |
| `model` | No | `sonnet`, `opus`, `haiku`, un ID completo o `inherit`. |

Formas de usar un subagente:

```text
Usa el subagente memory-assistant para recuperar el contexto del Taller de Python.
```

```text
@agent-vault-auditor revisa 03-RESOURCES
```

Claude también delega automáticamente cuando la tarea encaja con la `description`.

> **Límite real:** en Claude Code las restricciones por carpeta se configuran de forma global en `settings.json`, no por subagente. Por eso `project-manager` puede técnicamente editar fuera de `01-PROJECTS/`; lo que lo impide es su instrucción y la confirmación (`ask`) de cada edición. Los agentes de solo lectura sí están limitados de forma estricta por su lista `tools`.

### 6.4 Skills (`.claude/skills/<nombre>/SKILL.md`)

Las skills son los comandos personalizados de Claude Code: se ejecutan con `/nombre`. (Los antiguos comandos de `.claude/commands/` siguen funcionando, pero la documentación recomienda skills para trabajo nuevo.)

```markdown
---
name: contexto-proyecto
description: "Recupera el contexto completo de un proyecto o tema..."
argument-hint: "[nombre del proyecto o tema]"
disable-model-invocation: true
context: fork
agent: memory-assistant
---

Recupera el contexto de: $ARGUMENTS
...
```

| Campo | Función |
| --- | --- |
| `name` | Nombre del comando `/...`. Por defecto, el de la carpeta. |
| `description` | Qué hace y cuándo usarla. |
| `argument-hint` | Pista que aparece al autocompletar. |
| `disable-model-invocation: true` | Solo se ejecuta cuando tú la invocas; Claude no la lanza por su cuenta. |
| `context: fork` + `agent` | Ejecuta la skill en un subagente aislado. Lo usamos en las skills de solo lectura. |
| `$ARGUMENTS` | Todo lo que escribes después del comando (`$0`, `$1`... por posición). |

Skills incluidas: `/capturar`, `/procesar-inbox`, `/nuevo-proyecto`, `/contexto-proyecto`, `/revision-semanal`, `/auditar-boveda`, `/sincronizar`. Equivalen a los comandos de OpenCode.

### 6.5 Reglas por ruta (`.claude/rules/`)

Los archivos de `.claude/rules/` se cargan como instrucciones adicionales. Con el campo `paths` solo se cargan cuando Claude trabaja con archivos que coinciden:

```markdown
---
paths:
  - "**/*.md"
---

# Reglas al editar notas Markdown de Obsidian
- Conserva el bloque de propiedades YAML al inicio del archivo...
```

## 7. Uso diario: ejemplos

```text
/capturar Idea: usar Bases para ver todas las reuniones de un proyecto en una tabla.
```

```text
/nuevo-proyecto "Taller de Python" Impartir un taller introductorio de 4 sesiones para estudiantes de primer año.
```

```text
/auditar-boveda 03-RESOURCES
```

```text
Lee las notas diarias de esta semana y dime qué tareas quedaron sin completar. No modifiques nada.
```

Comandos útiles dentro de Claude Code:

| Comando | Función |
| --- | --- |
| `/permissions` | Ver y gestionar las reglas de permisos activas. |
| `/memory` | Ver y editar los archivos de memoria (`CLAUDE.md`). |
| `/agents` | Información sobre subagentes. |
| `/help` | Lista de comandos. |

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
| --- | --- | --- |
| `claude` no se reconoce. | La terminal se abrió antes de instalar o el `PATH` no se actualizó. | Abre una terminal nueva; ejecuta `claude doctor`. |
| Claude ignora `AGENTS.md`. | Existe `CLAUDE.md` sin `@AGENTS.md`. | Añade la línea `@AGENTS.md`. |
| Las skills o subagentes no aparecen. | Se crearon las carpetas con Claude abierto. | Reinicia Claude Code. |
| Una importación `@ruta` no se carga. | Ruta con espacios o entre comillas invertidas. | Escapa los espacios con `\`; no uses comillas invertidas. |
| Se puede leer `05-PERSONAL/` sin preguntar. | Permiso en la lista equivocada o ruta mal escrita. | Debe estar `Read(./05-PERSONAL/**)` en `ask`. Comprueba con `/permissions`. |
| Aviso de regla que "no coincide con ninguna herramienta". | Errata en el nombre de la herramienta. | Revisa mayúsculas: `Read`, `Edit`, `Bash`, `PowerShell`. |

## 9. Buenas prácticas

- Abre Claude Code siempre en la raíz de la bóveda.
- Mantén `CLAUDE.md` corto: las reglas compartidas viven en `AGENTS.md`.
- Haz un commit antes de sesiones con muchos cambios.
- Revisa tus permisos activos con `/permissions` después de cualquier cambio en `settings.json`.

## 10. Resultado esperado

- `claude` se abre en la bóveda con sesión iniciada.
- `/memory` muestra `CLAUDE.md` con `AGENTS.md` importado.
- `/auditar-boveda` devuelve un informe sin modificar archivos.
- Pedir una edición en `05-PERSONAL/` se rechaza.

---

Anterior: [07 — OpenCode](07-opencode-setup.md) | [Inicio](../README.md) | Siguiente: [09 — Git y GitHub](09-git-github.md)
