# 04 — Configuración de Obsidian

> **Objetivo:** dejar Obsidian listo para trabajar con la plantilla: Markdown básico, plugins oficiales, plantillas, notas diarias, propiedades, Bases, búsqueda y grafo.
> **Tiempo estimado:** 30 minutos.

Anterior: [03 — Instalación](03-installation.md) | [Inicio](../README.md) | Siguiente: [05 — Arquitectura de la bóveda](05-vault-architecture.md)

---

## 1. Qué es Obsidian y qué no es

**Obsidian** es una aplicación que muestra y edita una carpeta de archivos Markdown (`.md`). A esa carpeta la llama *vault* (bóveda). Todo lo que ves en Obsidian es un archivo normal en tu disco: puedes abrirlo con el Bloc de notas, con VS Code o con un agente de IA.

Obsidian **no** es una base de datos en la nube ni guarda tus notas en un formato propio. Esa es la razón por la que funciona tan bien con agentes de IA: el agente edita los mismos archivos que tú ves.

## 2. Markdown en cinco minutos

| Escribes | Obtienes |
| --- | --- |
| `# Título` | Encabezado de nivel 1 (`##` nivel 2, etc.) |
| `**negrita**` | **negrita** |
| `*cursiva*` | *cursiva* |
| `- elemento` | Lista con viñetas |
| `1. elemento` | Lista numerada |
| `- [ ] tarea` | Casilla de tarea |
| `` `código` `` | `código` en línea |
| `[texto](https://ejemplo.com)` | Enlace externo |
| `[[Nombre de nota]]` | Enlace interno de Obsidian |
| `![[imagen.png]]` | Incrustar una imagen o nota |
| `> cita` | Bloque de cita |

## 3. Configuración recomendada

Abre **Settings** (icono de engranaje, abajo a la izquierda). La plantilla ya incluye estos valores en `.obsidian/app.json`, `.obsidian/templates.json` y `.obsidian/daily-notes.json`; comprueba que se aplicaron.

### 3.1 Files and links

| Opción | Valor | Motivo |
| --- | --- | --- |
| Default location for new notes | *In the folder specified below* → `00-INBOX` | Todo lo nuevo entra por la bandeja de entrada. |
| Default location for new attachments | `03-RESOURCES/_adjuntos` | Las imágenes y PDF no ensucian las demás carpetas. |
| Automatically update internal links | Activado | Si renombras una nota, los enlaces no se rompen. |
| Use [[Wikilinks]] | Activado | Sintaxis `[[nota]]`, la más cómoda para enlazar. |

### 3.2 Core plugins (plugins oficiales)

En **Settings → Core plugins** activa:

| Plugin | Para qué |
| --- | --- |
| Templates | Insertar plantillas en notas. |
| Daily notes | Crear la nota del día con un clic. |
| Backlinks | Ver qué notas enlazan a la actual. |
| Outgoing links | Ver a qué notas enlaza la actual. |
| Graph view | Visualizar la red de notas. |
| Search | Búsqueda avanzada. |
| Properties view | Ver y editar propiedades YAML. |
| Bases | Vistas tipo base de datos sobre tus notas. |
| Tags view | Panel con todos los tags. |
| File recovery | Instantáneas locales para recuperar versiones. |

> Esta guía **no requiere plugins de la comunidad**. Puedes añadirlos más adelante, pero cada uno es código de terceros con acceso a tu bóveda.

### 3.3 Templates

1. **Settings → Templates → Template folder location**: `10-TEMPLATES`.
2. Formato de fecha: `YYYY-MM-DD`.

Para usar una plantilla: crea una nota vacía, abre la paleta de comandos (`Ctrl+P` en Windows/Linux, `Cmd+P` en macOS) y ejecuta **Templates: Insert template**.

Variables disponibles en el plugin oficial: `{{title}}` (título de la nota), `{{date}}` y `{{time}}`, con formato opcional, por ejemplo `{{date:YYYY-MM-DD}}`.

### 3.4 Daily notes

**Settings → Daily notes**:

| Opción | Valor |
| --- | --- |
| Date format | `YYYY-MM-DD` |
| New file location | `06-DAILY-NOTES` |
| Template file location | `10-TEMPLATES/daily-note` |

Ahora el icono de calendario de la barra lateral (o el comando **Daily notes: Open today's daily note**) crea la nota `2026-11-16.md` con la plantilla aplicada.

## 4. Enlaces, backlinks y tags

**Enlaces internos.** Escribe `[[` y Obsidian sugiere notas existentes. Si enlazas a una nota que no existe, el enlace queda pendiente y puedes crearla con un clic. Variantes útiles:

```markdown
[[Interrogación activa]]                    enlace simple
[[Interrogación activa|esta técnica]]       texto alternativo
[[Interrogación activa#Cómo aplicarla]]     enlace a un encabezado
![[Interrogación activa]]                   incrusta la nota
```

**Backlinks.** El panel *Backlinks* muestra todas las notas que enlazan a la actual. Es la forma de descubrir conexiones que no recordabas.

**Tags.** Se escriben como `#tema/aprendizaje` en el texto o en la propiedad `tags`. Úsalos para **temas transversales**, no para el estado de una nota (para eso están las propiedades). La taxonomía de la plantilla está en `99-SYSTEM/tags.md`.

## 5. Propiedades (YAML frontmatter)

Las propiedades son metadatos al inicio de la nota, entre dos líneas `---`:

```yaml
---
tipo: proyecto
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
area: "[[Formación]]"
tags:
  - tema/docencia
---
```

Obsidian las muestra como un formulario editable. Los agentes de IA y las Bases las usan para filtrar. El esquema completo de propiedades está en [05 — Arquitectura de la bóveda](05-vault-architecture.md#6-propiedades-estándar).

## 6. Bases

**Bases** es un plugin oficial que convierte un conjunto de notas en una tabla filtrable, usando sus propiedades. Las vistas se guardan en archivos `.base` (YAML).

La plantilla incluye tres en `99-SYSTEM/bases/`:

| Archivo | Muestra |
| --- | --- |
| `proyectos.base` | Proyectos agrupados por estado. |
| `inbox.base` | Notas pendientes de procesar en `00-INBOX`. |
| `notas-permanentes.base` | Notas permanentes ordenadas por fecha de actualización. |

Ejemplo (`proyectos.base`):

```yaml
filters:
  and:
    - file.inFolder("01-PROJECTS")
    - 'tipo == "proyecto"'
views:
  - type: table
    name: Proyectos por estado
    groupBy:
      property: note.estado
      direction: ASC
    order:
      - file.name
      - note.estado
      - note.fecha_limite
```

Sintaxis oficial: [obsidian.md/help/bases/syntax](https://obsidian.md/help/bases/syntax).

## 7. Búsqueda

`Ctrl+Shift+F` (`Cmd+Shift+F` en macOS) abre la búsqueda. Operadores útiles:

| Búsqueda | Encuentra |
| --- | --- |
| `path:01-PROJECTS estado` | La palabra *estado* solo dentro de proyectos. |
| `tag:#tema/python` | Notas con ese tag. |
| `[estado:activo]` | Notas con la propiedad `estado` igual a `activo`. |
| `"frase exacta"` | Coincidencia literal. |
| `task-todo:` | Tareas sin completar. |

## 8. Graph View

El grafo muestra cada nota como un punto y cada enlace como una línea. Úsalo para:

- Detectar **notas huérfanas** (puntos sin conexiones): candidatas a enlazar o archivar.
- Ver **centros de conocimiento** (puntos con muchas líneas): candidatos a convertirse en mapas de contenido (MOC).

En los filtros del grafo excluye `path:99-SYSTEM` y `path:10-TEMPLATES` para que no distorsionen la vista.

## 9. Errores frecuentes

| Problema | Solución |
| --- | --- |
| "Insert template" no muestra plantillas. | Revisa que el plugin Templates esté activo y la carpeta sea `10-TEMPLATES`. |
| La nota diaria se crea en la raíz. | Revisa *Daily notes → New file location*. |
| Las propiedades aparecen como texto. | El bloque `---` debe ser lo primero del archivo, sin líneas antes. |
| Una Base aparece vacía. | Las notas no tienen la propiedad exacta (`tipo: proyecto`), o la carpeta del filtro es otra. |
| Enlaces rotos tras mover archivos fuera de Obsidian. | Mueve y renombra notas **dentro** de Obsidian para que actualice los enlaces. |

## 10. Buenas prácticas

- Mueve y renombra notas desde Obsidian, no desde el explorador de archivos.
- Usa propiedades para el estado y tags para el tema.
- No crees carpetas nuevas sin actualizar `AGENTS.md`: los agentes dependen de esa descripción.

## 11. Resultado esperado

- Plugins oficiales activados.
- La nota diaria de hoy creada en `06-DAILY-NOTES` con la plantilla aplicada.
- La Base `99-SYSTEM/bases/proyectos.base` abre sin errores (aunque esté vacía).

---

Anterior: [03 — Instalación](03-installation.md) | [Inicio](../README.md) | Siguiente: [05 — Arquitectura de la bóveda](05-vault-architecture.md)
