# Workflow A — Tengo una idea nueva y quiero guardarla

| | |
| --- | --- |
| **Paso del ciclo** | CAPTURE |
| **Tiempo** | 1 minuto |
| **Herramientas** | Obsidian, o cualquier agente |

## Objetivo

Que ninguna idea se pierda, sin interrumpir lo que estás haciendo y sin decidir todavía dónde va.

## Opción 1 — Sin IA, desde Obsidian (la más rápida)

1. En Obsidian pulsa `Ctrl+N` (`Cmd+N` en macOS). La nota se crea en `00-INBOX/` porque así está configurada la plantilla.
2. Escribe un título breve y la idea tal como la pensaste.
3. Cierra la nota. Ya está.

Alternativa: escríbela en la sección **Capturas** de la nota diaria.

## Opción 2 — Con el agente

Abre tu agente en la raíz de la bóveda y usa el comando:

```text
/capturar Hacer un bot que lea mis notas diarias del viernes y me sugiera qué llevar a la revisión semanal.
```

Funciona igual en OpenCode y en Claude Code. Si prefieres no usar comandos, el prompt completo está en [01 — Capturar una nueva idea](../prompts/01-capturar-idea.md).

## Ejemplo de archivo resultante

`00-INBOX/Bot que sugiere temas para la revisión semanal.md`

```markdown
---
tipo: captura
estado: borrador
creado: 2026-11-16
actualizado: 2026-11-16
---

Hacer un bot que lea mis notas diarias del viernes y me sugiera qué llevar a la revisión semanal.

## Posibles conexiones
- [[LEEME-diarias]]
- [[revision-semanal]]
```

## Qué pasa después

La captura se queda en `00-INBOX/` hasta el próximo procesamiento (`/procesar-inbox`) o la revisión semanal ([Workflow G](G-revision-semanal.md)). Allí se decidirá si es una idea (`08-IDEAS/`), parte de un proyecto o se descarta.

## Errores frecuentes

| Error | Solución |
| --- | --- |
| Pasar 10 minutos decidiendo la carpeta. | Capturar no exige decidir. Todo va a `00-INBOX/`. |
| Pedirle al agente que "mejore" la idea al capturarla. | Captura tal cual; la elaboración es otro paso. |
| Capturar en otra aplicación "porque estaba a mano". | Si lo haces, pásalo a `00-INBOX/` el mismo día. |

## Resultado esperado

Una nota nueva en `00-INBOX/` en menos de un minuto.

---

[Workflows](README.md) | Siguiente: [B — Incorporar una investigación](B-incorporar-investigacion.md)
