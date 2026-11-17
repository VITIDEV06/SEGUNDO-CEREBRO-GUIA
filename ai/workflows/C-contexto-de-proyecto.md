# Workflow C — Comencé un proyecto y quiero mantener su contexto

| | |
| --- | --- |
| **Paso del ciclo** | ORGANIZE → CREATE |
| **Tiempo** | 15 minutos al inicio, 5 minutos por actualización |
| **Herramientas** | Cualquier agente |

## Objetivo

Que el proyecto tenga, desde el primer día, una nota principal con objetivo, alcance, próximas acciones y decisiones, y que se mantenga actualizada para que tú (o un agente) podáis retomarlo en cualquier momento.

## Pasos

### 1. Crear el proyecto

```text
/nuevo-proyecto "Taller de Python" Impartir un taller introductorio de 4 sesiones para estudiantes de primer año antes del 2027-03-15. Área: Docencia.
```

Responde a las 3 preguntas que te hará el agente para precisar el objetivo.

### 2. Registrar cada reunión

Después de cada reunión, pega tus apuntes:

```text
Usa el agente project-manager. Crea el acta de esta reunión en 07-MEETINGS/ enlazada al
proyecto "Taller de Python", y añade al proyecto las decisiones y las tareas que tengan responsable.

Fecha: 2026-11-18
Asistentes: Ana Pérez, Luis Gómez (personas ficticias)
Apuntes:
[PEGA TUS APUNTES]
```

### 3. Registrar decisiones importantes

```text
Añade esta decisión al proyecto "Taller de Python" y a 09-AI-MEMORY/decisiones.md:
Decisión: usaremos Jupyter Notebooks en lugar de un IDE.
Motivo: los estudiantes no tienen que instalar nada si usan un entorno en línea.
```

### 4. Actualizar el contexto activo

Si el proyecto es prioritario, inclúyelo en `09-AI-MEMORY/contexto-activo.md` (lo hace la revisión semanal, [Workflow G](G-revision-semanal.md)).

### 5. Diagnóstico periódico

```text
Analiza el proyecto Taller de Python. Solo lectura.
```

Prompt completo: [07 — Analizar un proyecto](../prompts/07-analizar-proyecto.md).

## Ejemplo de estructura resultante

```text
01-PROJECTS/
└── Taller de Python/
    ├── Taller de Python.md            nota principal
    └── Temario por sesión.md          nota de trabajo
07-MEETINGS/
└── 2026-11-18 Planificación del taller.md   proyecto: "[[Taller de Python]]"
```

Ejemplo completo con contenido: [examples/example-projects/](../../examples/example-projects/README.md).

## Errores frecuentes

| Error | Solución |
| --- | --- |
| Proyecto sin criterios de finalización. | Sin ellos nunca sabrás si terminó. Define 2 a 5. |
| Decisiones solo en el acta de la reunión. | Cópialas a la tabla de decisiones del proyecto. |
| Tareas sin responsable. | El agente no las añade como próximas acciones; asígnalas. |
| Copiar recursos dentro del proyecto. | Enlaza a `03-RESOURCES/`. |

## Resultado esperado

Un proyecto con nota principal completa, reuniones enlazadas y un registro de decisiones que permite retomarlo meses después con [Workflow F](F-opencode-consulta-proyectos.md) o el prompt [16 — Recuperar contexto](../prompts/16-recuperar-contexto-proyecto.md).

---

Anterior: [B](B-incorporar-investigacion.md) | [Workflows](README.md) | Siguiente: [D — Incorporar una conversación con otra IA](D-incorporar-conversacion-ia.md)
