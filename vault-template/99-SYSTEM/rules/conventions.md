---
tipo: sistema
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
---

# Convenciones de la bóveda

Reglas de nombres, propiedades y enlaces. Las siguen las personas y los agentes de IA.

## Nombres de archivo

| Tipo | Formato | Ejemplo |
| --- | --- | --- |
| Nota permanente | Afirmación o concepto en lenguaje natural | `La práctica espaciada mejora la retención.md` |
| Proyecto | `01-PROJECTS/<Nombre>/<Nombre>.md` | `01-PROJECTS/Taller de Python/Taller de Python.md` |
| Nota diaria | `YYYY-MM-DD.md` | `2026-11-16.md` |
| Reunión | `YYYY-MM-DD Tema.md` | `2026-11-16 Planificación del taller.md` |
| Persona | `02-AREAS/Personas/Nombre Apellido.md` | `02-AREAS/Personas/Ana Pérez.md` |
| Mapa de contenido | `MOC - Tema.md` | `MOC - Aprendizaje.md` |
| Sesión de IA | `09-AI-MEMORY/sesiones/YYYY-MM-DD-tema.md` | `2026-11-16-revision-semanal.md` |

- Prohibidos: `\ / : * ? " < > |` `#` `^` `[` `]`.
- Los nombres son únicos en toda la bóveda.
- Mayúscula inicial; el resto en minúsculas salvo nombres propios.

## Propiedades (frontmatter YAML)

```yaml
---
tipo: permanente          # diaria | proyecto | area | reunion | persona | permanente | aprendizaje | idea | captura | moc | sistema
estado: borrador          # borrador | activo | en-pausa | completado | archivado | procesada
creado: 2026-11-16
actualizado: 2026-11-16
tags:
  - tema/aprendizaje
fuente: ""                # URL, libro, conversación, etc.
relacionado:
  - "[[Otra nota]]"
---
```

| Propiedad | Obligatoria en | Notas |
| --- | --- | --- |
| `tipo`, `estado`, `creado`, `actualizado` | Todas salvo capturas rápidas | Fechas en `YYYY-MM-DD`. |
| `area` | Proyectos | Enlace entre comillas: `"[[Docencia]]"`. |
| `proyecto` | Reuniones | Enlace entre comillas. |
| `fecha_limite` | Proyectos con plazo | `YYYY-MM-DD`. |
| `fuente` | Recursos, aprendizaje, investigación | Obligatoria si el contenido viene de fuera. |
| `asistentes` | Reuniones | Lista de enlaces a personas. |

## Enlaces

- Enlaces internos con wikilinks: `[[Nombre de nota]]`.
- Cada nota nueva enlaza al menos a una nota existente (su proyecto, área o MOC).
- Al enlazar notas permanentes, explica la relación en una frase.
- Enlaces dentro de propiedades: siempre entre comillas.

## Ubicación de notas nuevas

| Si la nota es... | Va en |
| --- | --- |
| Captura sin procesar | `00-INBOX/` |
| Parte de un proyecto activo | `01-PROJECTS/<Proyecto>/` |
| Sobre una responsabilidad continua | `02-AREAS/` |
| Conocimiento de referencia o permanente | `03-RESOURCES/` |
| Una idea sin ejecutar | `08-IDEAS/` |
| Un acta de reunión | `07-MEETINGS/` |
