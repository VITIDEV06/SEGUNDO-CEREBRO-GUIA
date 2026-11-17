# Actualizar información existente

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Incorporar información nueva a notas existentes sin perder la anterior ni crear duplicados. |
| **Cuándo utilizarlo** | Cuando algo cambió (una decisión, un dato, una versión de software) o aprendiste algo que corrige una nota. |
| **Resultado esperado** | Notas actualizadas con trazabilidad del cambio. |

## Contexto necesario

- Información nueva y su fuente.
- Nota o notas a actualizar (o el tema).

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Actualiza mi segundo cerebro con esta información nueva:

Información: [PEGA LA INFORMACIÓN]
Fuente: [DE DÓNDE VIENE]
Notas afectadas: [RUTAS, o "búscalas tú"]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Localiza las notas afectadas.
2. Para cada una, muestra un antes/después de las líneas que cambiarían.
3. Si la información nueva contradice la anterior, no la borres: añade una sección o línea "Actualización AAAA-MM-DD:" explicando el cambio y su fuente.
4. Espera mi aprobación.
5. Aplica los cambios aprobados y actualiza la propiedad actualizado.
6. Si el cambio es una decisión, propón añadirla a 09-AI-MEMORY/decisiones.md.
```

## Restricciones

- La información anterior no se borra cuando hay contradicción: se documenta.
- Cambios solo tras aprobación.

## Ejemplo de utilización

Información: "El taller pasa de 4 a 3 sesiones". Se actualiza el proyecto con una línea fechada y se propone registrar la decisión.

---

[Biblioteca de prompts](README.md)
