# Procesar notas desorganizadas

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Convertir capturas o notas importadas en notas bien formadas, con título, propiedades, destino y enlaces. |
| **Cuándo utilizarlo** | Cuando `00-INBOX/` acumula notas, o al importar notas de otra aplicación. |
| **Resultado esperado** | Bandeja vacía o reducida, notas en su carpeta con propiedades y enlaces, e informe final. |

## Contexto necesario

- Carpeta o lista de notas a procesar.
- Plantillas en `10-TEMPLATES/`.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Procesa estas notas de mi segundo cerebro: [CARPETA O LISTA DE NOTAS; por defecto 00-INBOX/]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Paso 1 — Sin modificar nada, presenta esta tabla:
| Nota actual | Nuevo título | Tipo | Destino | Enlaces propuestos | Observaciones |
En Observaciones indica: posibles duplicados (con ruta), notas que deberían dividirse, datos sensibles (solo la ruta, sin repetir el dato) y capturas sin valor.

Paso 2 — Espera mi aprobación (puedo aprobar todas, algunas filas o pedir cambios).

Paso 3 — Para cada fila aprobada:
- Añade el frontmatter según el tipo (99-SYSTEM/rules/conventions.md).
- Aplica la estructura de la plantilla de 10-TEMPLATES/ que corresponda.
- Si reescribes mucho, conserva el original en "## Captura original".
- Mueve el archivo al destino y añade los enlaces.

Paso 4 — Informa: notas procesadas con su ruta final, pendientes y dudas.
```

## Restricciones

- Nada se mueve sin aprobación.
- Nada se descarta sin aprobación explícita.
- Conserva el texto original.

## Ejemplo de utilización

Con 6 capturas, el agente propone: 2 notas permanentes en `03-RESOURCES/`, 1 idea en `08-IDEAS/`, 1 nota de proyecto, 1 duplicado a fusionar y 1 captura descartable. Apruebas las filas 1 a 5.

---

[Biblioteca de prompts](README.md)
