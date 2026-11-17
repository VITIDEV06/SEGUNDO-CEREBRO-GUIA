# Ejemplo: recuperar contexto con trazabilidad

**Bóveda:** [examples/example-vault](../../examples/example-vault/LEEME-ejemplo.md)
**Comando:** `/contexto-proyecto Taller de Python` (OpenCode o Claude Code; usa `memory-assistant`)

## Petición

```text
/contexto-proyecto Taller de Python
```

## Respuesta esperada del agente

```markdown
## Contexto de Taller de Python
**Resumen:** Taller introductorio de Python de 4 sesiones para estudiantes de primer año,
con fecha límite 2027-03-15. El temario está cerrado; el aula está pendiente de confirmar.
Se decidió usar Jupyter Notebooks en un entorno en línea.

### Cronología
- 2026-11-16 — Proyecto creado (`01-PROJECTS/Taller de Python/Taller de Python.md`)
- 2026-11-18 — Reunión de planificación; temario aprobado (`07-MEETINGS/2026-11-18 Planificación del taller.md`)

### Decisiones
- Usar Jupyter Notebooks en línea — los estudiantes no instalan nada
  (`01-PROJECTS/Taller de Python/Taller de Python.md`, tabla de decisiones)

### Pendientes
- [ ] Confirmar aula, responsable Ana Pérez, antes del 2026-11-25 (`07-MEETINGS/2026-11-18 Planificación del taller.md`)
- [ ] Preparar el ejercicio de arranque de la sesión 1 (`01-PROJECTS/Taller de Python/Taller de Python.md`)

### Personas involucradas
- Ana Pérez — coordinación académica (`02-AREAS/Personas/Ana Pérez.md`)

### Lagunas
- No hay criterios de evaluación del taller.
- No consta el número de estudiantes previsto.
```

## Qué observar

| Comportamiento | Regla que lo provoca |
| --- | --- |
| Cada dato lleva su ruta. | Prompt del `memory-assistant` y regla "No inventes" de `AGENTS.md`. |
| Las lagunas se declaran, no se rellenan. | `agent-behavior.md`, sección "Cuando no sabes algo". |
| No modifica ningún archivo. | Permisos del agente: `edit * deny` (OpenCode) o `tools: Read, Glob, Grep` (Claude Code). |
| No lee `05-PERSONAL/`. | `privacy.md` y permisos globales. |

## Si la respuesta no cumple

Responde al agente:

```text
Indica la ruta de cada dato y separa lo que está en la bóveda de lo que infieres.
```
