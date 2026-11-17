# Actualizar el índice de la bóveda

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Mantener `99-SYSTEM/Indice.md` como punto de entrada fiable a proyectos, áreas y mapas de contenido. |
| **Cuándo utilizarlo** | Tras crear o archivar proyectos, áreas o MOC; como parte de la revisión semanal. |
| **Resultado esperado** | Índice sincronizado con el estado real de la bóveda. |

## Contexto necesario

- `99-SYSTEM/Indice.md`.
- Carpetas `01-PROJECTS/`, `02-AREAS/`, `03-RESOURCES/`.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Actualiza el índice de mi segundo cerebro (99-SYSTEM/Indice.md).

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.

Instrucciones:
1. Lista los proyectos con estado activo o en-pausa (nota principal de cada carpeta de 01-PROJECTS/), con una línea de estado.
2. Lista las notas de área de 02-AREAS/ (excluye LEEME y Personas/).
3. Lista los MOC de 03-RESOURCES/ (notas con tipo: moc).
4. Compara con el índice actual: qué entradas faltan, cuáles sobran (proyectos archivados) y cuáles tienen enlaces rotos.
5. Muestra el nuevo contenido de las secciones "Proyectos activos", "Áreas" y "Mapas de contenido (MOC)" y espera mi aprobación.
6. No modifiques las secciones Paneles, Sistema ni Memoria de IA.
```

## Restricciones

- Solo modifica las tres secciones indicadas.
- Solo enlaza notas existentes.

## Ejemplo de utilización

Se añaden 2 proyectos nuevos, se retira 1 archivado y se añade `MOC - Aprendizaje`.

---

[Biblioteca de prompts](README.md)
