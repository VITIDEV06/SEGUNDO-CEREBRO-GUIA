---
tipo: sistema
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
---

# Calidad de las notas

## Nota permanente

Una nota permanente cumple estas condiciones:

1. **Atómica:** contiene una sola idea. Si necesitas "y además", probablemente son dos notas.
2. **Con palabras propias:** explica la idea como se la contarías a otra persona. Las citas textuales van entre comillas y con fuente.
3. **Título como afirmación:** `La práctica espaciada mejora la retención` es mejor que `Práctica espaciada`.
4. **Autónoma:** se entiende sin abrir otras notas.
5. **Conectada:** enlaza al menos a otra nota y explica por qué.
6. **Con fuente:** indica de dónde viene la idea (`fuente`).

## Estructura recomendada

```markdown
# Título como afirmación

Explicación en 3 a 8 frases.

## Por qué importa
Aplicación práctica o consecuencia.

## Relaciones
- Amplía [[Otra nota]] porque...
- Contradice parcialmente [[Otra nota]] cuando...

## Fuente
Autor, obra o URL.
```

## Señales de una nota de baja calidad

| Señal | Corrección |
| --- | --- |
| Más de 500 palabras sobre varios temas | Dividir en varias notas permanentes. |
| Sin enlaces | Buscar notas relacionadas y enlazar. |
| Copia literal de una fuente | Reescribir con palabras propias. |
| Sin propiedad `tipo` o `estado` | Completar el frontmatter. |
| Título genérico ("Notas", "Varios") | Renombrar con el tema real. |

## Resúmenes generados por IA

- Indican al final: `Resumen generado con asistencia de IA a partir de: <fuente>`.
- No añaden datos que no estén en la fuente.
- Marcan las inferencias como `(inferencia)`.
