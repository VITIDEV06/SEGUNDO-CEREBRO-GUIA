---
tipo: sistema
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
---

# Proyectos

Un proyecto tiene **un objetivo concreto y una fecha de fin**. Ejemplos: "Preparar el taller de Python", "Publicar la guía en GitHub".

## Estructura
```text
01-PROJECTS/
└── Nombre del proyecto/
    ├── Nombre del proyecto.md   Nota principal (plantilla: project)
    └── ...                       Notas de trabajo del proyecto
```

## Reglas
- La nota principal tiene `tipo: proyecto` y `estado: activo | en-pausa | completado`.
- Las reuniones del proyecto viven en `07-MEETINGS/` y enlazan aquí con la propiedad `proyecto`.
- Al terminar, mueve la carpeta completa a `04-ARCHIVE/`.

Vista: [[proyectos.base]]
