# 07 — Configuración de OpenCode

> **Objetivo:** instalar OpenCode, conectarlo a un proveedor de modelos y configurarlo sobre tu bóveda con reglas, permisos, agentes y comandos.
> **Tiempo estimado:** 30 minutos.
> **Alternativa:** si prefieres Claude Code, ve a [08 — Claude Code](08-claude-code-setup.md). No necesitas ambos.

Anterior: [06 — Integración con IA](06-ai-integration.md) | [Inicio](../README.md) | Siguiente: [08 — Claude Code](08-claude-code-setup.md)

---

> **Versión documentada.** Esta guía sigue la documentación oficial de OpenCode consultada en noviembre de 2026 ([opencode.ai/docs](https://opencode.ai/docs/)), que usa el formato de configuración **V2**: permisos como lista de reglas (`permissions`), acción `shell` en lugar de `bash`, y carpetas `agents/` y `commands/` en plural. Si tu versión es anterior y no reconoce estas claves, actualiza OpenCode o consulta la documentación de tu versión.

## 1. Qué es OpenCode

**OpenCode** es un agente de IA de código abierto que se ejecuta en la terminal. Lee y edita los archivos de la carpeta donde lo abres, ejecuta comandos con tu permiso y puede conectarse a distintos proveedores de modelos de lenguaje.

En este proyecto lo usamos para consultar y mantener la bóveda: procesar la bandeja de entrada, recuperar contexto de proyectos, auditar la estructura, etc.

## 2. Instalación

### macOS y Linux

```bash
# Bash — script oficial
curl -fsSL https://opencode.ai/v2/install | bash
```

```bash
# Bash — Homebrew
brew install anomalyco/tap/opencode-v2
```

### Cualquier sistema con Node.js

```bash
# Bash, PowerShell o CMD
npm install -g @opencode/cli
```

### Windows

La documentación oficial indica que los gestores de paquetes de Windows (winget, Scoop, Chocolatey) **no están soportados**. Tienes dos opciones:

1. **Descarga directa:** en [opencode.ai/docs](https://opencode.ai/docs/) descarga el `.zip` de la CLI para tu arquitectura (x64, x64 *baseline* para procesadores antiguos, o ARM64), descomprímelo y añade la carpeta al `PATH`. También hay una aplicación de escritorio `.exe`.
2. **npm:** si tienes Node.js instalado, usa el comando `npm install -g @opencode/cli` de arriba.

### Comprobación

Cierra y abre la terminal. Entra en tu bóveda y ejecuta OpenCode:

```powershell
# PowerShell (Windows)
cd "$HOME\Documents\SegundoCerebro"
opencode
```

```bash
# Bash (macOS / Linux)
cd ~/Documents/SegundoCerebro
opencode
```

Debe abrirse la interfaz de OpenCode en la terminal.

## 3. Conectar un proveedor de modelos

Dentro de OpenCode escribe:

```text
/connect
```

Elige tu proveedor y sigue las instrucciones. Si el proveedor usa una API key, OpenCode la guarda en su propio almacenamiento de credenciales; **no la escribas en `opencode.json`**. Si necesitas referenciar una clave en la configuración, usa una variable de entorno con la sintaxis `"{env:NOMBRE_VARIABLE}"` (ver [12 — Seguridad](12-security-privacy.md#2-variables-de-entorno)).

## 4. Instalar la configuración de la bóveda

### Opción A — Script

Desde la carpeta de este repositorio:

```powershell
# PowerShell (Windows)
python scripts/install-agents.py --tool opencode --vault "$HOME\Documents\SegundoCerebro"
```

```bash
# Bash (macOS / Linux)
python3 scripts/install-agents.py --tool opencode --vault ~/Documents/SegundoCerebro
```

Añade `--dry-run` para ver qué copiaría sin copiar nada. El script **no sobrescribe** archivos existentes.

### Opción B — Copia manual

| Copia desde este repositorio | A tu bóveda |
| --- | --- |
| `opencode/opencode.example.json` | `opencode.json` |
| `opencode/agents/*.md` | `.opencode/agents/` |
| `opencode/commands/*.md` | `.opencode/commands/` |
| `opencode/instructions/*.md` | `.opencode/instructions/` |

`AGENTS.md` ya está en la bóveda (viene con la plantilla).

### Resultado

```text
SegundoCerebro/
├── AGENTS.md                      reglas compartidas (lectura nativa)
├── opencode.json                  permisos e instrucciones adicionales
└── .opencode/
    ├── agents/                    7 agentes especializados
    ├── commands/                  7 comandos /...
    └── instructions/              instrucciones específicas de OpenCode
```

## 5. Cómo funciona cada pieza

### 5.1 `AGENTS.md`

OpenCode lee automáticamente `AGENTS.md` en la raíz del proyecto. Contiene las reglas compartidas con cualquier otro agente. Si lo modificas, el cambio afecta a OpenCode y a Claude Code a la vez.

> OpenCode también tiene el comando `/init`, que genera o mejora un `AGENTS.md` analizando el proyecto. **No lo ejecutes sobre la bóveda de la plantilla**: está pensado para repositorios de código y reescribiría las reglas que ya tienes.

### 5.2 `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "99-SYSTEM/rules/*.md",
    ".opencode/instructions/*.md"
  ],
  "default_agent": "knowledge-manager",
  "permissions": [
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "read", "resource": "*05-PERSONAL/*", "effect": "ask" },
    { "action": "edit", "resource": "*", "effect": "ask" },
    { "action": "edit", "resource": "*05-PERSONAL/*", "effect": "deny" },
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "rm *", "effect": "deny" }
  ]
}
```

*(Extracto. El archivo completo está en [opencode/opencode.example.json](../opencode/opencode.example.json).)*

| Clave | Función |
| --- | --- |
| `$schema` | Permite que tu editor valide el archivo. |
| `instructions` | Archivos adicionales que se combinan con `AGENTS.md`. Acepta patrones como `*.md`. |
| `default_agent` | Agente principal al abrir una sesión. |
| `permissions` | Lista ordenada de reglas. Cada regla tiene `action`, `resource` y `effect` (`allow`, `ask` o `deny`). |

**Cómo se evalúan los permisos:**

1. **La última regla que coincide gana.** Por eso se escribe primero la regla general (`edit *` → `ask`) y después la excepción (`edit *05-PERSONAL/*` → `deny`).
2. `*` coincide con cualquier texto, **incluida la barra `/`**. Por eso `*05-PERSONAL/*` protege la carpeta tanto si la ruta llega como relativa como si llega como absoluta.
3. Una regla de `shell` que termina en ` *` también coincide con el comando sin argumentos: `git status *` permite `git status`.
4. Si ninguna regla coincide, OpenCode pregunta (`ask`).

**Acciones disponibles** (las más útiles para una bóveda): `read`, `edit`, `glob`, `grep`, `shell`, `webfetch`, `websearch`, `external_directory`, `subagent`, `skill`.

### 5.3 Agentes (`.opencode/agents/`)

Cada archivo `.md` define un agente. El nombre del archivo es su identificador; el cuerpo es su *system prompt*.

```markdown
---
description: "Recupera contexto: qué se decidió, qué se hizo y qué quedó pendiente..."
mode: all
permissions:
  - action: edit
    resource: "*"
    effect: deny
  - action: shell
    resource: "*"
    effect: deny
  - action: shell
    resource: "git log *"
    effect: allow
---

Eres el **Memory Assistant** de un segundo cerebro en Obsidian...
```

| Campo | Valores | Función |
| --- | --- | --- |
| `description` | texto | Explica al modelo cuándo usar el agente. Obligatorio en la práctica para subagentes. |
| `mode` | `primary`, `subagent`, `all` | `all` permite usarlo como agente principal o como subagente. |
| `permissions` | lista de reglas | Se **añaden después** de las globales; como gana la última coincidencia, pueden restringir más. |
| `model` | `proveedor/modelo` | Opcional. Si se omite, usa el modelo configurado. |

Los permisos del agente no sustituyen a los globales: se suman. Así, `memory-assistant` y `vault-auditor` quedan en solo lectura aunque la configuración global permita editar con confirmación.

### 5.4 Comandos (`.opencode/commands/`)

Cada archivo `.md` es un comando que se ejecuta escribiendo `/nombre-del-archivo`.

```markdown
---
description: "Recupera el contexto completo de un proyecto o tema..."
agent: memory-assistant
---

Recupera el contexto de: $ARGUMENTS
...
```

| Elemento | Función |
| --- | --- |
| `description` | Aparece en la lista de comandos. |
| `agent` | Agente que ejecuta el comando. |
| `$ARGUMENTS` | Todo lo que escribes después del comando. |
| `$1`, `$2`... | Argumentos por posición (las comillas agrupan palabras). |

Comandos incluidos:

| Comando | Agente | Qué hace |
| --- | --- | --- |
| `/capturar <texto>` | (por defecto) | Crea una captura en `00-INBOX/`. |
| `/procesar-inbox` | `note-processor` | Propone y aplica el procesamiento de la bandeja. |
| `/nuevo-proyecto <nombre> <descripción>` | `project-manager` | Crea un proyecto con la plantilla. |
| `/contexto-proyecto <proyecto>` | `memory-assistant` | Recupera contexto (solo lectura). |
| `/revision-semanal` | (por defecto) | Guía la revisión semanal. |
| `/auditar-boveda` | `vault-auditor` | Informe de auditoría (solo lectura). |
| `/sincronizar` | `knowledge-manager` | Mantenimiento completo por fases. |

## 6. Uso diario: ejemplos

```text
/capturar La técnica Feynman consiste en explicar un concepto con palabras simples para detectar lagunas.
```

```text
/contexto-proyecto Taller de Python
```

```text
¿Qué notas de 03-RESOURCES hablan de aprendizaje y no tienen enlaces? Solo lista, no cambies nada.
```

```text
Usa el agente research-assistant para documentar qué es la práctica espaciada con esta fuente: <pega aquí el texto>
```

Cuando OpenCode quiera editar un archivo o ejecutar un comando con efecto `ask`, te mostrará la acción y esperará tu aprobación.

## 7. Errores frecuentes

| Síntoma | Causa probable | Solución |
| --- | --- | --- |
| `opencode` no se reconoce. | La carpeta del binario no está en el `PATH`, o la terminal es antigua. | Abre una terminal nueva; revisa el `PATH`. |
| Los comandos `/...` no aparecen. | Carpeta mal nombrada o abierta fuera de la bóveda. | Debe ser `.opencode/commands/` (plural) y OpenCode debe abrirse en la raíz de la bóveda. |
| El agente edita sin preguntar. | Reglas en orden incorrecto. | La regla específica debe ir **después** de la general. |
| El agente no puede leer nada. | Una regla `deny` general al final de la lista. | Revisa el orden: la última coincidencia gana. |
| OpenCode ignora `permission` o `bash`. | Claves del formato antiguo (V1). | Usa `permissions` y `shell`. |
| El agente no conoce las convenciones. | `instructions` apunta a rutas inexistentes. | Comprueba que existe `99-SYSTEM/rules/` en la bóveda. |

## 8. Buenas prácticas

- Abre OpenCode siempre en la raíz de la bóveda.
- Mantén las reglas compartidas en `AGENTS.md`; usa `.opencode/instructions/` solo para lo específico de OpenCode.
- Antes de una sesión con muchos cambios, haz un commit (ver [09 — Git y GitHub](09-git-github.md)) para poder deshacerla.
- Prueba un permiso nuevo con una tarea pequeña antes de confiar en él.

## 9. Resultado esperado

- `opencode` se abre en la bóveda.
- `/contexto-proyecto` y `/auditar-boveda` responden sin intentar modificar archivos.
- Al pedir una edición, OpenCode solicita confirmación.
- Al pedir que edite algo en `05-PERSONAL/`, OpenCode lo rechaza.

---

Anterior: [06 — Integración con IA](06-ai-integration.md) | [Inicio](../README.md) | Siguiente: [08 — Claude Code](08-claude-code-setup.md)
