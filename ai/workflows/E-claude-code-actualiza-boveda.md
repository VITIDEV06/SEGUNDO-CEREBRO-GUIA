# Workflow E — Quiero que Claude Code actualice mi bóveda

| | |
| --- | --- |
| **Paso del ciclo** | ORGANIZE → CONNECT |
| **Tiempo** | 15 minutos |
| **Herramientas** | Claude Code (configurado según [08 — Claude Code](../../docs/08-claude-code-setup.md)) |

## Objetivo

Dejar que Claude Code haga cambios en varias notas (procesar, enlazar, actualizar propiedades) manteniendo el control: ves cada cambio, lo apruebas y puedes deshacerlo.

## Requisitos

- Configuración instalada: `CLAUDE.md`, `.claude/settings.json`, `.claude/agents/`, `.claude/skills/`.
- La bóveda es un repositorio Git ([09 — Git y GitHub](../../docs/09-git-github.md)).

## Pasos

### 1. Punto de restauración

```bash
git status
git add .
git commit -m "Antes de sesión con Claude Code"
```

### 2. Abrir Claude Code y comprobar la configuración

```bash
claude
```

Dentro de Claude Code:

```text
/permissions
```

Comprueba que `Edit(./05-PERSONAL/**)` aparece en las reglas de denegación.

### 3. Pedir la actualización (plan primero)

Ejemplo: normalizar propiedades de las notas de `03-RESOURCES/`.

```text
Revisa las notas de 03-RESOURCES/ y detecta las que no cumplen el esquema de propiedades
de 99-SYSTEM/rules/conventions.md (faltan tipo, estado, creado o actualizado, o tienen
valores no válidos). No modifiques nada todavía: presenta una tabla con nota, problema
y corrección propuesta.
```

### 4. Aprobar por partes

```text
Aplica las correcciones de las filas 1 a 10. Las demás, déjalas para después.
```

Claude Code pedirá confirmación para cada edición (`Edit` está en `ask`). Lee el diff que muestra antes de aceptar.

### 5. Revisar el resultado en Git

```bash
git diff --stat
git diff
```

- Si todo está bien: `git add .` y `git commit -m "Normalizadas propiedades de 03-RESOURCES"`.
- Si algo no te gusta: `git restore "ruta/nota.md"` para un archivo, o `git restore .` para todo.

### 6. Registrar la sesión (opcional)

```text
Propón un resumen de esta sesión para 09-AI-MEMORY/sesiones/ con objetivo, cambios (rutas),
decisiones y pendientes.
```

## Otras actualizaciones habituales

| Tarea | Cómo pedirla |
| --- | --- |
| Procesar la bandeja | `/procesar-inbox` |
| Añadir enlaces entre notas de un tema | Prompt [05 — Relacionar conocimientos](../prompts/05-relacionar-conocimientos.md) |
| Fusionar duplicados | Prompt [10 — Detectar duplicados](../prompts/10-detectar-duplicados.md) |
| Mantenimiento completo | `/sincronizar` |
| Auditoría previa | `/auditar-boveda` (se ejecuta en el subagente `vault-auditor`, solo lectura) |

## Errores frecuentes

| Error | Solución |
| --- | --- |
| Aceptar todas las ediciones sin leerlas. | Si son muchas, aprueba por bloques y revisa con `git diff`. |
| Usar un modo que omite confirmaciones para ir más rápido. | No en tu bóveda real. Reduce el alcance de la tarea en su lugar. |
| Claude mueve notas y rompe enlaces. | Pídele explícitamente que actualice los enlaces entrantes (la regla está en `agent-behavior.md`). |

## Resultado esperado

Cambios aplicados solo donde los aprobaste, revisados con `git diff` y guardados en un commit con mensaje descriptivo.

---

Anterior: [D](D-incorporar-conversacion-ia.md) | [Workflows](README.md) | Siguiente: [F — OpenCode consulta proyectos](F-opencode-consulta-proyectos.md)
