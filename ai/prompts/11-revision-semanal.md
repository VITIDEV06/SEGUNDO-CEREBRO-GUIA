# Realizar revisión semanal

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Cerrar la semana con la bóveda ordenada, los proyectos revisados y las prioridades claras. |
| **Cuándo utilizarlo** | Una vez por semana, siempre el mismo día. |
| **Resultado esperado** | Informe semanal, contexto activo actualizado y registro de la sesión. |

## Contexto necesario

- Notas diarias de la semana.
- Proyectos activos.
- `09-AI-MEMORY/contexto-activo.md`.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Guíame en mi revisión semanal. Semana: [AAAA-MM-DD a AAAA-MM-DD, o "últimos 7 días"]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Fase 1 — Diagnóstico (solo lectura):
1. Bandeja: cuántas notas hay en 00-INBOX/ y cuántas tienen más de 7 días.
2. Notas diarias de la semana: tareas sin completar, capturas sin procesar y elementos con tags revisar/...
3. Proyectos activos: última actualización, próximas acciones, bloqueos.
4. Ideas en 08-IDEAS/ listas para decidir.
5. Tareas de reuniones de la semana no reflejadas en su proyecto.

Fase 2 — Informe:
## Logros de la semana
## Pendientes
## Proyectos que requieren atención
## Propuestas de cambios (tabla: archivo, cambio, motivo)
## Tres prioridades para la próxima semana

Fase 3 — Tras mi aprobación: aplica los cambios, actualiza 09-AI-MEMORY/contexto-activo.md y propón 09-AI-MEMORY/sesiones/AAAA-MM-DD-revision-semanal.md.
```

## Restricciones

- Diagnóstico sin cambios.
- Cambios solo tras aprobación.

## Ejemplo de utilización

Resultado: 9 capturas pendientes, 2 proyectos sin actividad, 3 prioridades definidas y `contexto-activo.md` actualizado.

---

[Biblioteca de prompts](README.md)
