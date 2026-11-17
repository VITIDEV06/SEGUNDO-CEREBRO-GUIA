# Workflow B — Investigué un tema y quiero incorporarlo al cerebro

| | |
| --- | --- |
| **Paso del ciclo** | CAPTURE → PROCESS → CONNECT |
| **Tiempo** | 20 minutos |
| **Herramientas** | Cualquier agente |

## Objetivo

Convertir lo que leíste o investigaste en conocimiento propio: un resumen con fuentes, notas permanentes atómicas y enlaces con lo que ya sabías.

## Requisitos

- El material: textos, URL o tus apuntes.
- Datos de las fuentes (autor, título, fecha).

## Pasos

### 1. Punto de restauración

```bash
git add .
git commit -m "Antes de incorporar investigación sobre práctica espaciada"
```

### 2. Resumir y documentar

Abre el agente y envía:

```text
Usa el agente research-assistant para documentar este tema en mi segundo cerebro.

Tema: práctica espaciada en el aprendizaje
Fuentes (usa solo estas):
1. [AUTOR, TÍTULO, AÑO, URL] — [pega el texto o el extracto]
2. [AUTOR, TÍTULO, AÑO, URL] — [pega el texto o el extracto]

Crea la nota en 00-INBOX/ separando hallazgos con fuente, inferencias y preguntas abiertas.
Antes, dime qué sabe ya la bóveda sobre el tema.
```

### 3. Revisar la nota creada

Ábrela en Obsidian. Comprueba que cada hallazgo tenga fuente y que no haya afirmaciones que no estén en tus materiales.

### 4. Extraer notas permanentes

```text
A partir de 00-INBOX/Investigación - práctica espaciada.md, propón notas permanentes
(una idea por nota, título como afirmación). Busca antes si ya existen. Espera mi aprobación.
```

Revisa las propuestas y reescribe con tus palabras lo que haga falta antes de aprobar. Prompt completo: [04 — Crear notas permanentes](../prompts/04-crear-notas-permanentes.md).

### 5. Conectar

```text
Encuentra conexiones entre las notas permanentes que acabas de crear y el resto de la bóveda.
Presenta la tabla de relaciones y espera mi aprobación.
```

Prompt completo: [05 — Relacionar conocimientos](../prompts/05-relacionar-conocimientos.md).

### 6. Revisar y guardar

```bash
git diff
git add .
git commit -m "Incorporada investigación sobre práctica espaciada"
```

## Ejemplo de archivos resultantes

```text
00-INBOX/Investigación - práctica espaciada.md       (luego se mueve a 03-RESOURCES/)
03-RESOURCES/La práctica espaciada mejora la retención.md
03-RESOURCES/El olvido es parte del aprendizaje.md
```

`03-RESOURCES/La práctica espaciada mejora la retención.md`:

```markdown
---
tipo: permanente
estado: borrador
creado: 2026-11-16
actualizado: 2026-11-16
fuente: "[[Investigación - práctica espaciada]]"
tags:
  - tema/aprendizaje
---

# La práctica espaciada mejora la retención

Repartir el estudio de un tema en varias sesiones separadas en el tiempo produce
mejor recuerdo a largo plazo que concentrar el mismo tiempo en una sola sesión.

## Por qué importa
Planificar repasos cortos durante varias semanas es más eficaz que estudiar todo la víspera.

## Relaciones
- Se combina con [[La recuperación activa supera a la relectura]]: cada repaso espaciado
  debería ser un ejercicio de recuerdo, no una relectura.
```

## Errores frecuentes

| Error | Solución |
| --- | --- |
| Pedir "investiga X" sin fuentes ni permiso web. | Da las fuentes, o autoriza la búsqueda y revisa lo que trae. |
| Aprobar notas permanentes sin leerlas. | Son tu conocimiento: reescríbelas con tus palabras. |
| Guardar el resumen y no extraer nada. | Un resumen es material; las notas permanentes son aprendizaje. |

## Resultado esperado

Una nota de investigación con fuentes, entre 2 y 6 notas permanentes nuevas, y enlaces con notas que ya existían.

---

Anterior: [A](A-guardar-idea.md) | [Workflows](README.md) | Siguiente: [C — Contexto de un proyecto](C-contexto-de-proyecto.md)
