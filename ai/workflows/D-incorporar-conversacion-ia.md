# Workflow D — Hablé con otra IA y quiero incorporar los resultados

| | |
| --- | --- |
| **Paso del ciclo** | CAPTURE → PROCESS |
| **Tiempo** | 10 minutos |
| **Herramientas** | Cualquier agente |

## Objetivo

Aprovechar una conversación útil con un chat de IA (Claude, ChatGPT, Gemini u otro) sin contaminar tu bóveda con información no verificada.

> **Principio:** lo que dice otra IA es una **fuente no verificada**, no un hecho. Se etiqueta como tal y se verifica antes de convertirse en nota permanente.

## Pasos

### 1. Exportar la conversación

Copia la conversación (o la parte útil) a un archivo de texto o directamente al portapapeles. No incluyas datos personales que hayas compartido con ese chat.

### 2. Capturar y destilar

Abre tu agente en la bóveda y envía:

```text
Incorpora a mi segundo cerebro los resultados de esta conversación con otra IA.

Herramienta y fecha: [NOMBRE DEL CHAT, AAAA-MM-DD]
Objetivo de la conversación: [QUÉ BUSCABA]
Conversación:
[PEGA AQUÍ LA CONVERSACIÓN]

Instrucciones:
- Sigue AGENTS.md. No leas ni modifiques 05-PERSONAL/.
- Crea una nota en 00-INBOX/ titulada "Conversación IA - <tema>" con tipo: captura,
  fuente: "<herramienta>, <fecha>", y el tag formato/conversacion-ia.
- Estructura: ## Pregunta original, ## Conclusiones útiles, ## Afirmaciones que requieren
  verificación (con el tag revisar/verificar-fuente), ## Ideas o tareas accionables,
  ## Relación con notas existentes.
- No copies la conversación entera: destila. Conserva textual solo lo imprescindible, entre comillas.
- No añadas información que no esté en la conversación.
- Indica la ruta creada y qué afirmaciones conviene verificar primero.
```

### 3. Verificar

Para cada afirmación marcada, contrasta con una fuente fiable. Si la verificas, añade la fuente y quita el tag `revisar/verificar-fuente`.

### 4. Procesar

En el siguiente `/procesar-inbox`, las conclusiones verificadas pueden convertirse en notas permanentes, y las tareas en próximas acciones de un proyecto.

## Ejemplo de archivo resultante

`00-INBOX/Conversación IA - estructura de un taller introductorio.md`

```markdown
---
tipo: captura
estado: borrador
creado: 2026-11-16
actualizado: 2026-11-16
fuente: "Chat de IA, 2026-11-16"
tags:
  - formato/conversacion-ia
---

## Pregunta original
Cómo estructurar un taller introductorio de programación de 4 sesiones.

## Conclusiones útiles
- Empezar cada sesión con un ejercicio que dé un resultado visible en 10 minutos.

## Afirmaciones que requieren verificación
- "Las sesiones de más de 90 minutos reducen la retención." #revisar/verificar-fuente

## Ideas o tareas accionables
- [ ] Preparar un ejercicio de arranque por sesión.

## Relación con notas existentes
- Aplica a [[Taller de Python]].
```

## Errores frecuentes

| Error | Solución |
| --- | --- |
| Pegar la conversación completa como nota. | Destila: conclusiones, dudas y acciones. |
| Tratar las respuestas de la IA como hechos. | Etiqueta, verifica y cita fuentes reales. |
| Pegar en el agente datos personales que estaban en la conversación. | Elimínalos antes de pegar. |

## Resultado esperado

Una nota de captura breve, trazable y marcada como no verificada, lista para procesar.

---

Anterior: [C](C-contexto-de-proyecto.md) | [Workflows](README.md) | Siguiente: [E — Claude Code actualiza la bóveda](E-claude-code-actualiza-boveda.md)
