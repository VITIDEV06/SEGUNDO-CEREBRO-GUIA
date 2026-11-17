# Generar un informe de actividad

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Resumir qué se hizo en un periodo: notas creadas, proyectos avanzados, aprendizajes y decisiones. |
| **Cuándo utilizarlo** | Al final de un mes o trimestre, antes de una evaluación o para un informe de avance. |
| **Resultado esperado** | Un informe de actividad basado en datos de la bóveda. |

## Contexto necesario

- Periodo.
- Opcional: historial de Git si la bóveda está versionada.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Genera un informe de actividad de mi segundo cerebro.

Periodo: [AAAA-MM-DD a AAAA-MM-DD]
Audiencia: [SOLO YO / MI EQUIPO / MI SUPERVISOR]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.
- Tarea de solo lectura, salvo que te pida guardar el informe.

Instrucciones:
1. Identifica notas creadas o modificadas en el periodo (propiedades creado y actualizado; si la bóveda usa Git, puedes usar git log --since y --until, que es solo lectura).
2. Entrega:
   ## Resumen ejecutivo (5 líneas)
   ## Proyectos: avance por proyecto con evidencias (rutas)
   ## Conocimiento: notas permanentes y MOC nuevos
   ## Reuniones y decisiones
   ## Métricas: notas creadas por carpeta, capturas procesadas, proyectos completados
   ## Pendientes que pasan al siguiente periodo
3. Si la audiencia no soy solo yo, excluye cualquier contenido personal y avísame de qué excluiste.
4. Pregunta si quiero guardarlo en 00-INBOX/.
```

## Restricciones

- Solo lectura por defecto.
- Datos con evidencia (ruta).

## Ejemplo de utilización

Periodo: octubre. Resultado: 34 notas nuevas, 2 proyectos completados, 6 decisiones registradas.

---

[Biblioteca de prompts](README.md)
