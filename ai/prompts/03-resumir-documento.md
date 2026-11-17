# Resumir documentos

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Obtener un resumen fiel y útil de un documento, conectado con lo que ya sabes. |
| **Cuándo utilizarlo** | Después de leer un artículo, capítulo, informe o transcripción que quieres conservar. |
| **Resultado esperado** | Una nota de resumen en `00-INBOX/` lista para procesar, con candidatas a notas permanentes. |

## Contexto necesario

- El documento (texto pegado o ruta del archivo).
- Datos de la fuente: autor, título, fecha, URL.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Resume este documento para mi segundo cerebro.

Fuente: [AUTOR, TÍTULO, FECHA, URL]
Documento: [PEGA EL TEXTO O INDICA LA RUTA DEL ARCHIVO]
Para qué lo quiero: [OBJETIVO DE LECTURA]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Crea una nota en 00-INBOX/ titulada "Resumen - <título del documento>" con tipo: aprendizaje, estado: borrador y fuente completa.
2. Estructura:
   - ## Idea principal (2-3 frases)
   - ## Puntos clave (máximo 7, cada uno con la sección o página de origen si existe)
   - ## Citas textuales relevantes (entre comillas, máximo 3, con ubicación)
   - ## Relación con mis notas (busca notas relacionadas y explica cada relación)
   - ## Notas permanentes candidatas (títulos como afirmaciones)
   - ## Preguntas abiertas
3. Termina con: "Resumen generado con asistencia de IA a partir de: <fuente>".
4. Lo que no esté en el documento no va en el resumen; si añades una interpretación, márcala como (inferencia).
```

## Restricciones

- Fidelidad a la fuente.
- Las citas son textuales y van entre comillas.

## Ejemplo de utilización

Fuente: un artículo sobre técnicas de estudio. Resultado: 6 puntos clave, 2 citas, relación con `[[MOC - Aprendizaje]]` y 3 notas permanentes candidatas.

---

[Biblioteca de prompts](README.md)
