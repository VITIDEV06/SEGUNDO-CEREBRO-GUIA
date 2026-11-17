---
tipo: sistema
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
---

# Comportamiento de los agentes

## Flujo de aprobación

```text
1. Entender la petición  -> si es ambigua, preguntar antes de actuar.
2. Leer el contexto      -> 09-AI-MEMORY y notas relacionadas.
3. Proponer              -> lista de notas a crear, modificar o mover.
4. Esperar aprobación    -> obligatorio si hay más de 5 notas o cualquier movimiento.
5. Ejecutar              -> aplicar solo lo aprobado.
6. Informar              -> rutas de todo lo creado, modificado o movido.
```

## Límites

| Acción | Permitido |
| --- | --- |
| Leer y buscar notas (excepto `05-PERSONAL/`) | Sí |
| Crear notas en `00-INBOX/` | Sí, informando |
| Crear o editar notas en otras carpetas | Sí, tras confirmación |
| Mover notas | Sí, tras confirmación y verificando enlaces |
| Mover a `04-ARCHIVE/` | Sí, tras confirmación |
| Eliminar notas | Solo con autorización explícita, nota por nota |
| Editar `05-PERSONAL/`, `.obsidian/`, `10-TEMPLATES/` | No (las plantillas solo si se pide explícitamente) |
| `git push`, `git reset --hard`, `git clean` | No |
| Acceder a internet | Solo si la tarea lo requiere y tras confirmación |

## Al mover o renombrar una nota

1. Buscar todas las notas que enlazan a ella (`[[Nombre]]`).
2. Actualizar esos enlaces en la misma operación.
3. Informar de las notas cuyos enlaces se actualizaron.

## Registro de sesiones

Al final de una sesión con cambios importantes, proponer un resumen en `09-AI-MEMORY/sesiones/YYYY-MM-DD-tema.md` con:

- Objetivo de la sesión.
- Cambios realizados (rutas).
- Decisiones tomadas.
- Pendientes.

## Cuando no sabes algo

Di "No encuentro esa información en la bóveda" y propón dónde podría buscarse. No completes huecos con suposiciones.
