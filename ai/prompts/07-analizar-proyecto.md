# Analizar un proyecto

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Obtener un diagnóstico del estado de un proyecto: avance, riesgos, bloqueos y próximos pasos. |
| **Cuándo utilizarlo** | Antes de una reunión de seguimiento, cuando un proyecto parece estancado o en la revisión semanal. |
| **Resultado esperado** | Un diagnóstico del proyecto que puedes usar en una reunión o para decidir prioridades. |

## Contexto necesario

- Nota principal del proyecto en `01-PROJECTS/`.
- Reuniones y notas diarias relacionadas.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Analiza el proyecto: [NOMBRE DEL PROYECTO]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.
- Esta tarea es de solo lectura: no modifiques archivos.

Instrucciones:
1. Lee la nota principal, sus notas de trabajo, las reuniones que la enlazan y las notas diarias que la mencionan.
2. Entrega:
   ## Objetivo y criterios de finalización (según la nota)
   ## Avance (qué criterios están cumplidos, con evidencia y ruta)
   ## Próximas acciones vigentes
   ## Bloqueos y riesgos
   ## Decisiones tomadas y decisiones pendientes
   ## Inconsistencias (fechas pasadas, tareas sin responsable, objetivo ambiguo)
   ## Recomendación: 3 próximos pasos concretos
3. Cita la ruta de cada dato.
```

## Restricciones

- Solo lectura.
- Cada afirmación con su ruta.

## Ejemplo de utilización

Proyecto: Taller de Python. Resultado: 2 de 4 criterios cumplidos, 1 bloqueo (aula sin confirmar) y 3 pasos recomendados.

---

[Biblioteca de prompts](README.md)
