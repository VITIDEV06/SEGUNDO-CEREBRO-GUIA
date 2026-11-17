# Crear un mapa de conocimientos

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Construir un mapa de contenido (MOC) que organice todo lo que sabes de un tema y muestre lagunas. |
| **Cuándo utilizarlo** | Cuando un tema supera unas 10 notas o quieres una visión de conjunto. |
| **Resultado esperado** | Un MOC navegable con lagunas identificadas. |

## Contexto necesario

- Tema.
- Notas existentes del tema.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Crea un mapa de conocimientos sobre: [TEMA]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Reúne todas las notas del tema (por tags, enlaces, títulos y contenido).
2. Agrúpalas en 3 a 6 secciones lógicas (fundamentos, técnicas, aplicaciones, debates, etc.).
3. Propón la nota 03-RESOURCES/MOC - <Tema>.md con frontmatter tipo: moc, y en cada sección una lista de [[enlaces]] con una frase que explique qué aporta cada nota.
4. Añade "## Lagunas": subtemas que faltan o están poco desarrollados.
5. Añade "## Preguntas abiertas".
6. Incluye un diagrama Mermaid (flowchart) con las relaciones principales, si aporta claridad.
7. Espera mi aprobación antes de crear la nota. Después, propón añadir un enlace al MOC en 99-SYSTEM/Indice.md.
```

## Restricciones

- Solo enlaza notas que existen.
- Las lagunas no se rellenan con contenido inventado.

## Ejemplo de utilización

Tema: aprendizaje. Resultado: `MOC - Aprendizaje` con 4 secciones, 14 notas enlazadas y 3 lagunas.

---

[Biblioteca de prompts](README.md)
