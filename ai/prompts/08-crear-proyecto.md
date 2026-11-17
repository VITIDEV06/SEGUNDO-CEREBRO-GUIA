# Crear un nuevo proyecto

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Iniciar un proyecto con estructura completa, enlazado a su área y recursos, sin duplicar proyectos existentes. |
| **Cuándo utilizarlo** | Al empezar cualquier trabajo con objetivo y fecha de fin. |
| **Resultado esperado** | Un proyecto nuevo con nota principal estructurada y enlazada. |

## Contexto necesario

- Nombre, objetivo y, si existen, fecha límite y área.
- Plantilla `10-TEMPLATES/project.md`.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Crea un nuevo proyecto en mi segundo cerebro.

Nombre: [NOMBRE]
Objetivo: [QUÉ EXISTIRÁ CUANDO TERMINE]
Fecha límite: [AAAA-MM-DD o "sin fecha"]
Área: [ÁREA RELACIONADA o "no sé"]
Contexto adicional: [OPCIONAL]

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Busca en 01-PROJECTS/, 08-IDEAS/ y 04-ARCHIVE/ proyectos o ideas similares. Si hay coincidencias, muéstralas y pregunta antes de continuar.
2. Crea 01-PROJECTS/<Nombre>/<Nombre>.md con la estructura de 10-TEMPLATES/project.md, sustituyendo las variables {{...}} por valores reales.
3. Completa solo con la información dada. Lo que falte, déjalo vacío.
4. Propón enlaces a un área de 02-AREAS/ y a recursos de 03-RESOURCES/.
5. Responde con la ruta creada, los campos vacíos y 3 preguntas para precisar el objetivo o el alcance.
```

## Restricciones

- No inventa tareas, fechas ni responsables.
- Comprueba duplicados antes de crear.

## Ejemplo de utilización

Nombre: Taller de Python. Objetivo: impartir 4 sesiones introductorias. Resultado: `01-PROJECTS/Taller de Python/Taller de Python.md` y preguntas sobre audiencia, aula y materiales.

---

[Biblioteca de prompts](README.md)
