# Detectar información duplicada

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Encontrar notas repetidas o solapadas y proponer cómo consolidarlas. |
| **Cuándo utilizarlo** | Mensualmente, o cuando sospechas que escribiste lo mismo dos veces. |
| **Resultado esperado** | Lista priorizada de duplicados y, tras aprobación, notas consolidadas. |

## Contexto necesario

- Carpeta o tema a revisar (o toda la bóveda).

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Busca información duplicada en: [CARPETA, TEMA o "toda la bóveda"]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.
- Fase de análisis de solo lectura.

Instrucciones:
1. Compara títulos (similares, sinónimos, singular/plural) y contenido (párrafos o ideas repetidas).
2. Presenta grupos de posibles duplicados:
   | Grupo | Notas | Tipo de solapamiento (idéntico / parcial / mismo tema) | Propuesta |
3. Para cada grupo propón: nota a conservar, contenido a fusionar, y qué hacer con las demás (convertir en enlace o mover a 04-ARCHIVE/).
4. Indica cuántos enlaces entrantes tiene cada nota (los que habría que redirigir).
5. Espera mi aprobación antes de fusionar o mover nada.
```

## Restricciones

- No elimina: archiva.
- Redirige enlaces entrantes al fusionar.

## Ejemplo de utilización

Se detectan `Pomodoro.md` y `Técnica Pomodoro.md` (solapamiento parcial). Propuesta: conservar la segunda, fusionar 2 párrafos y redirigir 3 enlaces.

---

[Biblioteca de prompts](README.md)
