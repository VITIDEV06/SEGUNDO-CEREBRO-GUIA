# Crear notas permanentes

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Transformar material de lectura o estudio en notas atómicas, con palabras propias y enlazadas. |
| **Cuándo utilizarlo** | Al procesar resúmenes, notas de aprendizaje o capturas con ideas valiosas. |
| **Resultado esperado** | Notas permanentes nuevas en `03-RESOURCES/`, enlazadas a la fuente y a otras notas. |

## Contexto necesario

- Nota o notas de origen.
- `99-SYSTEM/rules/note-quality.md`.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Ayúdame a crear notas permanentes a partir de: [RUTA DE LA NOTA O NOTAS DE ORIGEN]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Lee 99-SYSTEM/rules/note-quality.md.
2. Identifica las ideas que merecen una nota permanente (una idea por nota).
3. Para cada una, propón: título como afirmación, explicación de 3 a 8 frases, por qué importa, 2 relaciones con notas existentes (con la frase que explica la relación) y fuente.
4. Antes de crear, busca si ya existe una nota permanente sobre esa idea; si existe, propón actualizarla en lugar de duplicarla.
5. Presenta las propuestas y espera mi aprobación. Puedo reescribir el texto para que use mis palabras.
6. Crea las aprobadas en 03-RESOURCES/ con la plantilla 10-TEMPLATES/permanent-note.md con estado: borrador hasta que yo las revise.
7. Añade en la nota de origen una sección "## Notas permanentes extraídas" con los enlaces.
```

## Restricciones

- Una idea por nota.
- No duplica notas existentes.
- Las notas quedan en `borrador` hasta tu revisión.

## Ejemplo de utilización

Desde un resumen sobre memoria se proponen 3 notas: `La práctica espaciada mejora la retención`, `La recuperación activa supera a la relectura` y `El olvido es parte del aprendizaje`.

---

[Biblioteca de prompts](README.md)
