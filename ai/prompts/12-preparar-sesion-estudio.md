# Preparar una sesión de estudio

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Planificar una sesión de estudio eficaz usando tus propias notas, con recuperación activa y repaso. |
| **Cuándo utilizarlo** | Antes de estudiar un tema que ya tiene notas en la bóveda. |
| **Resultado esperado** | Plan de sesión con tiempos, preguntas de repaso y notas prioritarias. |

## Contexto necesario

- Tema.
- Tiempo disponible.
- Notas de aprendizaje y permanentes del tema.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Prepara una sesión de estudio.

Tema: [TEMA]
Tiempo disponible: [MINUTOS]
Objetivo: [QUÉ QUIERO SER CAPAZ DE HACER O EXPLICAR AL TERMINAR]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.
- Basa todo en mis notas. Si añades conocimiento externo, márcalo como (conocimiento externo, verificar).

Instrucciones:
1. Reúne las notas del tema (aprendizaje, permanentes, MOC) y resume qué sé y qué falta.
2. Propón un plan por bloques con minutos: repaso de lo anterior, material nuevo, práctica de recuperación y cierre.
3. Genera 8 preguntas de recuperación activa (abiertas, no de sí/no), indicando la nota que contiene cada respuesta. No muestres las respuestas.
4. Indica qué notas repasar primero (las menos actualizadas o con dudas abiertas).
5. Pregunta si quiero guardar el plan en la nota de aprendizaje del tema, en la sección "## Repaso".
```

## Restricciones

- Preguntas basadas en las notas.
- Respuestas ocultas hasta que las pidas.

## Ejemplo de utilización

Tema: técnicas de aprendizaje, 45 minutos. Plan: 10 min repaso, 15 min material nuevo, 15 min preguntas, 5 min cierre.

---

[Biblioteca de prompts](README.md)
