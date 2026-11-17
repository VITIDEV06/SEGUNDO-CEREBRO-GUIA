# Workflow F — Quiero utilizar OpenCode para consultar mis proyectos

| | |
| --- | --- |
| **Paso del ciclo** | REVIEW |
| **Tiempo** | 5 minutos |
| **Herramientas** | OpenCode (configurado según [07 — OpenCode](../../docs/07-opencode-setup.md)) |

## Objetivo

Hacer preguntas sobre tus proyectos y obtener respuestas basadas en la bóveda, con la ruta de cada dato, **sin riesgo de modificar nada**.

## Por qué es seguro

El comando `/contexto-proyecto` usa el agente `memory-assistant`, que tiene estas reglas propias en `.opencode/agents/memory-assistant.md`:

```yaml
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
```

Como las reglas del agente se aplican después de las globales y gana la última coincidencia, no puede editar ni ejecutar comandos salvo `git log`.

## Pasos

### 1. Abrir OpenCode en la bóveda

```bash
cd <ruta-de-tu-bóveda>
opencode
```

### 2. Consultas habituales

Contexto completo de un proyecto:

```text
/contexto-proyecto Taller de Python
```

Vista general de todos los proyectos:

```text
Lista los proyectos de 01-PROJECTS/ con estado, fecha de última actualización, próxima
acción y fecha límite. Ordena por fecha límite. Solo lectura; indica la ruta de cada proyecto.
```

Proyectos que necesitan atención:

```text
¿Qué proyectos activos no tienen próximas acciones o llevan más de 30 días sin
actualizarse? Solo lectura.
```

Reutilizar un proyecto antiguo:

```text
Busca en 04-ARCHIVE/ proyectos parecidos a "Taller de Python" y dime qué materiales,
decisiones y lecciones podría reutilizar. Cita rutas. Solo lectura.
```

Historial con Git (si la bóveda está versionada):

```text
Usa git log para decirme qué cambió en 01-PROJECTS/Taller de Python/ en las últimas dos semanas.
```

### 3. Guardar una respuesta útil (opcional)

Si la respuesta te sirve para una reunión, pide al agente principal (no al `memory-assistant`) que la guarde:

```text
Guarda el último resumen como nota en 00-INBOX/ titulada "Estado Taller de Python 2026-11-16".
```

## Ejemplo de respuesta esperada

```markdown
## Contexto de Taller de Python
**Resumen:** Taller de 4 sesiones para primer año, con fecha límite 2027-03-15.
Temario de las sesiones 1 y 2 cerrado; aula pendiente de confirmar.

### Cronología
- 2026-11-16 — Proyecto creado (`01-PROJECTS/Taller de Python/Taller de Python.md`)
- 2026-11-18 — Reunión de planificación (`07-MEETINGS/2026-11-18 Planificación del taller.md`)

### Decisiones
- Usar Jupyter Notebooks — los estudiantes no instalan nada (`09-AI-MEMORY/decisiones.md`)

### Pendientes
- [ ] Confirmar aula (`07-MEETINGS/2026-11-18 Planificación del taller.md`)

### Lagunas
- No hay evaluación definida para el taller.
```

## Errores frecuentes

| Error | Solución |
| --- | --- |
| La respuesta no cita rutas. | Recuérdalo: "Indica la ruta de cada dato". |
| El agente dice que no encuentra el proyecto. | Revisa el nombre exacto de la carpeta en `01-PROJECTS/` o `04-ARCHIVE/`. |
| Intenta editar y se rechaza. | Correcto: `memory-assistant` es de solo lectura. Usa otro agente para editar. |

## Resultado esperado

Respuestas trazables sobre tus proyectos en segundos, sin cambios en la bóveda.

---

Anterior: [E](E-claude-code-actualiza-boveda.md) | [Workflows](README.md) | Siguiente: [G — Revisión semanal](G-revision-semanal.md)
