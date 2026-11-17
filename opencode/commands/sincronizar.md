---
description: "Prompt maestro: sincroniza y mantiene el segundo cerebro (inbox, proyectos, índice, memoria de IA y auditoría) en una sesión guiada con aprobación por fases."
agent: knowledge-manager
---

Ejecuta una sesión de mantenimiento completa del segundo cerebro. Foco opcional: $ARGUMENTS

Reglas: sigue `AGENTS.md` y `99-SYSTEM/rules/`. No borres nada. No toques `05-PERSONAL/`. Cada fase termina con una propuesta y espera mi aprobación antes de modificar archivos.

Fase 1 — Estado (solo lectura): número de capturas en `00-INBOX/`, proyectos activos y su última actualización, notas modificadas en los últimos 7 días, problemas evidentes (enlaces rotos, propiedades faltantes).

Fase 2 — Bandeja: propuesta de procesamiento de `00-INBOX/` (tabla nota, título, tipo, destino, enlaces).

Fase 3 — Proyectos: para cada proyecto activo, propuesta de actualización (próximas acciones, estado, decisiones pendientes de registrar).

Fase 4 — Conexiones: notas recientes sin enlaces y temas con más de 10 notas sin MOC; propuesta de enlaces y MOC.

Fase 5 — Índice y memoria: propuesta de actualización de `99-SYSTEM/Indice.md`, `09-AI-MEMORY/contexto-activo.md` y `09-AI-MEMORY/decisiones.md`.

Fase 6 — Cierre: resumen de cambios con rutas, pendientes para la próxima sesión y propuesta de `09-AI-MEMORY/sesiones/YYYY-MM-DD-sincronizacion.md`.

Si una fase no tiene nada que hacer, dilo en una línea y pasa a la siguiente.
