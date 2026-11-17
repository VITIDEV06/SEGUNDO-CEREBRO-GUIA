# Capturar una nueva idea

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Guardar una idea en la bandeja de entrada en segundos, sin perderla y sin interrumpir lo que estás haciendo. |
| **Cuándo utilizarlo** | En cuanto surge una idea, una frase o un dato que quieres conservar. |
| **Resultado esperado** | Un archivo nuevo en `00-INBOX/` y una respuesta de dos o tres líneas. |

## Contexto necesario

- El texto de la idea, tal como se te ocurrió.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Guarda esta idea como captura en mi segundo cerebro:

[PEGA AQUÍ LA IDEA]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Crea un archivo en 00-INBOX/ con un título breve y descriptivo (sin los caracteres \ / : * ? " < > | # ^ [ ]).
2. Añade frontmatter con: tipo: captura, estado: borrador, creado y actualizado con la fecha de hoy.
3. Copia la idea tal cual, sin reinterpretarla ni ampliarla.
4. Añade una sección "## Posibles conexiones" con hasta 3 notas existentes relacionadas. Si no hay, escribe "Ninguna encontrada".
5. No la clasifiques ni la proceses.
6. Responde solo con la ruta creada y las conexiones.
```

## Restricciones

- Solo crea un archivo en `00-INBOX/`.
- No modifica el texto de la idea.

## Ejemplo de utilización

Idea: "Usar Bases para ver todas las reuniones de un proyecto". Resultado: `00-INBOX/Bases para reuniones por proyecto.md` con conexión sugerida a `[[LEEME-reuniones]]`.

---

[Biblioteca de prompts](README.md)
