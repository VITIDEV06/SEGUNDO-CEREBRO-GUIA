# Investigar un tema

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Preparar una nota de investigación con fuentes, separando hechos, inferencias y preguntas abiertas. |
| **Cuándo utilizarlo** | Antes de estudiar un tema nuevo, preparar una clase o tomar una decisión informada. |
| **Resultado esperado** | Una nota de investigación verificable en `00-INBOX/`. |

## Contexto necesario

- Pregunta de investigación.
- Fuentes proporcionadas o permiso para buscar en la web.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Investiga este tema para mi segundo cerebro: [PREGUNTA O TEMA]

Fuentes que debes usar: [LISTA DE URL O TEXTOS; o escribe "puedes buscar en la web con mi confirmación"]
Profundidad: [BÁSICA / INTERMEDIA / AVANZADA]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Primero resume lo que la bóveda ya sabe del tema, con enlaces.
2. Si necesitas buscar en la web, dime qué vas a buscar y espera confirmación.
3. Crea una nota en 00-INBOX/ "Investigación - <tema>" con tipo: captura y fuente con todas las fuentes, y estas secciones:
   ## Pregunta
   ## Lo que ya sabía la bóveda
   ## Hallazgos (cada uno con su fuente)
   ## Inferencias (marcadas como tales)
   ## Contradicciones con notas existentes
   ## Preguntas abiertas
   ## Notas permanentes candidatas
4. Lo que no tenga fuente lleva el tag revisar/verificar-fuente.
```

## Restricciones

- Cada hallazgo con fuente.
- Acceso web solo con confirmación.
- Solo crea en `00-INBOX/`.

## Ejemplo de utilización

Tema: "¿Qué es la práctica espaciada?" con dos fuentes aportadas. Resultado: 5 hallazgos con fuente, 1 inferencia marcada, 2 preguntas abiertas.

---

[Biblioteca de prompts](README.md)
