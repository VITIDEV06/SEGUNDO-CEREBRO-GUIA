# Relacionar conocimientos existentes

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Descubrir y crear conexiones entre notas que hoy están aisladas. |
| **Cuándo utilizarlo** | Tras crear notas nuevas, o cuando el grafo muestra muchas notas huérfanas. |
| **Resultado esperado** | Notas con enlaces explicados y menos huérfanas en el grafo. |

## Contexto necesario

- Una nota, un tema o una carpeta.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Encuentra conexiones para: [NOTA, TEMA O CARPETA]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Lee el contenido indicado.
2. Busca en la bóveda notas relacionadas por concepto (no solo por palabras iguales).
3. Clasifica cada relación como: amplía, ejemplifica, contradice, es requisito de, es aplicación de.
4. Presenta una tabla: | Nota A | Relación | Nota B | Frase explicativa |
5. Señala notas huérfanas del conjunto analizado.
6. Si el tema tiene más de 10 notas sin MOC, propón uno.
7. Tras mi aprobación, añade los enlaces en la sección "## Relaciones" de cada nota, con su frase explicativa, y actualiza la propiedad actualizado.
```

## Restricciones

- Cada enlace lleva una frase que explica la relación.
- No modifica el resto del contenido de las notas.

## Ejemplo de utilización

Tema: aprendizaje. Se proponen 9 enlaces, entre ellos: `Técnica Feynman` es aplicación de `La recuperación activa supera a la relectura`.

---

[Biblioteca de prompts](README.md)
