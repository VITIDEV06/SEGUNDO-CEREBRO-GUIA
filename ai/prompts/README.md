# Biblioteca de prompts

Diecisiete prompts profesionales para trabajar con tu segundo cerebro. Funcionan igual en **OpenCode** y en **Claude Code**: abre el agente en la raíz de tu bóveda, copia el bloque *Instrucciones*, sustituye los textos entre corchetes `[ ]` y envíalo.

## Estructura de cada prompt

| Sección | Contenido |
| --- | --- |
| Nombre | Título del prompt. |
| Objetivo | Qué consigue. |
| Cuándo utilizarlo | Situación en la que aplica. |
| Contexto necesario | Qué debe existir en la bóveda o qué debes aportar. |
| Instrucciones | El prompt listo para copiar. Incluye las reglas generales, así que funciona de forma independiente. |
| Restricciones | Límites que el prompt impone al agente. |
| Resultado esperado | Qué debes obtener. |
| Ejemplo de utilización | Caso concreto con datos ficticios. |

## Índice

| N.º | Prompt | Cuándo |
| --- | --- | --- |
| 00 | [Prompt maestro: sincronizar y mantener el segundo cerebro](00-prompt-maestro-sincronizacion.md) | Una vez por semana o tras un periodo sin mantenimiento. |
| 01 | [Capturar una nueva idea](01-capturar-idea.md) | En cuanto surge una idea. |
| 02 | [Procesar notas desorganizadas](02-procesar-notas-desorganizadas.md) | Cuando `00-INBOX/` acumula notas o al importar notas. |
| 03 | [Resumir documentos](03-resumir-documento.md) | Después de leer algo que quieres conservar. |
| 04 | [Crear notas permanentes](04-crear-notas-permanentes.md) | Al procesar resúmenes o notas de estudio. |
| 05 | [Relacionar conocimientos existentes](05-relacionar-conocimientos.md) | Tras crear notas nuevas o con muchas huérfanas. |
| 06 | [Investigar un tema](06-investigar-tema.md) | Antes de estudiar, enseñar o decidir. |
| 07 | [Analizar un proyecto](07-analizar-proyecto.md) | Seguimiento o proyecto estancado. |
| 08 | [Crear un nuevo proyecto](08-crear-proyecto.md) | Al empezar un trabajo con objetivo y fecha. |
| 09 | [Actualizar información existente](09-actualizar-informacion.md) | Cuando algo cambió. |
| 10 | [Detectar información duplicada](10-detectar-duplicados.md) | Mensualmente. |
| 11 | [Realizar revisión semanal](11-revision-semanal.md) | Cada semana. |
| 12 | [Preparar una sesión de estudio](12-preparar-sesion-estudio.md) | Antes de estudiar un tema con notas. |
| 13 | [Crear un mapa de conocimientos](13-mapa-de-conocimientos.md) | Cuando un tema supera unas 10 notas. |
| 14 | [Actualizar el índice de la bóveda](14-actualizar-indice.md) | Tras crear o archivar proyectos y MOC. |
| 15 | [Generar un informe de actividad](15-informe-actividad.md) | Fin de mes o trimestre. |
| 16 | [Recuperar contexto de proyectos anteriores](16-recuperar-contexto-proyecto.md) | Al retomar o reutilizar un proyecto. |

## Prompts y comandos

Algunos prompts tienen un comando equivalente ya instalado (más corto de invocar):

| Prompt | OpenCode | Claude Code |
| --- | --- | --- |
| 00 Prompt maestro | `/sincronizar` | `/sincronizar` |
| 01 Capturar | `/capturar` | `/capturar` |
| 02 Procesar | `/procesar-inbox` | `/procesar-inbox` |
| 08 Crear proyecto | `/nuevo-proyecto` | `/nuevo-proyecto` |
| 11 Revisión semanal | `/revision-semanal` | `/revision-semanal` |
| 16 Recuperar contexto | `/contexto-proyecto` | `/contexto-proyecto` |

Para convertir cualquier otro prompt en comando, consulta [11 — Uso avanzado](../../docs/11-advanced-usage.md#2-crear-tu-propio-comando).

## Buenas prácticas

- Haz un commit antes de usar prompts que modifican archivos.
- Si un prompt devuelve algo inventado, recuérdale la regla: "Solo con información de la bóveda; indica la ruta de cada dato".
- Adapta los prompts a tu bóveda, pero conserva las restricciones.
