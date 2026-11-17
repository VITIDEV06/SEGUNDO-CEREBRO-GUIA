# Recuperar contexto de proyectos anteriores

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Retomar un proyecto (o reutilizar lo aprendido en uno antiguo) sin depender de tu memoria. |
| **Cuándo utilizarlo** | Al volver a un proyecto tras semanas sin tocarlo, o al empezar uno parecido a otro ya terminado. |
| **Resultado esperado** | Contexto completo y trazable para retomar o reutilizar un proyecto. |

## Contexto necesario

- Nombre del proyecto o tema.
- Proyectos en `01-PROJECTS/` y `04-ARCHIVE/`.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Recupera el contexto de: [PROYECTO O TEMA]
Motivo: [RETOMARLO / REUTILIZARLO EN UN PROYECTO NUEVO LLAMADO ...]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.
- Tarea de solo lectura.

Busca en este orden: 09-AI-MEMORY/contexto-activo.md, 09-AI-MEMORY/decisiones.md, la nota principal en 01-PROJECTS/ o 04-ARCHIVE/, reuniones en 07-MEETINGS/, notas diarias en 06-DAILY-NOTES/, sesiones en 09-AI-MEMORY/sesiones/ y notas relacionadas en 03-RESOURCES/ y 08-IDEAS/.

Entrega:
## Resumen (3-5 frases)
## Cronología (fecha — hecho — ruta)
## Decisiones y motivos
## Pendientes que quedaron abiertos
## Lecciones aprendidas (solo si están escritas en la bóveda)
## Qué reutilizar (plantillas, recursos, contactos profesionales)
## Lagunas (lo que no está documentado)

Cada dato con su ruta entre comillas invertidas.
```

## Restricciones

- Solo lectura.
- No completa lagunas con suposiciones.

## Ejemplo de utilización

Proyecto archivado: Taller de Excel 2025. Resultado: cronología de 8 hitos, 3 decisiones, 2 lecciones y la lista de materiales reutilizables.

---

[Biblioteca de prompts](README.md)
