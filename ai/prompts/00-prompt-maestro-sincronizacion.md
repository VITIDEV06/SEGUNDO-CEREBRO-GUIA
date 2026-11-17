# Prompt maestro: sincronizar y mantener el segundo cerebro

| Campo | Descripción |
| --- | --- |
| **Objetivo** | Ejecutar una sesión de mantenimiento integral que deja la bóveda al día: bandeja procesada, proyectos actualizados, conexiones nuevas, índice y memoria de IA sincronizados. |
| **Cuándo utilizarlo** | Una vez por semana (puede sustituir a la revisión semanal) o después de un periodo sin mantener la bóveda. |
| **Resultado esperado** | Bóveda al día, con un registro de sesión en `09-AI-MEMORY/sesiones/` y `contexto-activo.md` actualizado. |

## Contexto necesario

- Bóveda con `AGENTS.md` y `99-SYSTEM/rules/`.
- Recomendado: un commit de Git justo antes.
- Equivale a los comandos `/sincronizar` de OpenCode y Claude Code.

## Instrucciones (prompt para copiar)

Sustituye los textos entre corchetes `[ ]` y pega el bloque completo en OpenCode o Claude Code, abiertos en la raíz de la bóveda.

```text
Actúa como gestor de mi segundo cerebro en Obsidian y ejecuta una sesión de sincronización completa.

Reglas generales:
- Sigue AGENTS.md y 99-SYSTEM/rules/ de la bóveda.
- No inventes información: si algo no está en la bóveda o en el material proporcionado, dilo.
- No leas ni modifiques 05-PERSONAL/.
- No elimines archivos.
- Trabaja por fases. Cada fase termina con una propuesta y espera mi aprobación antes de modificar archivos.
- Si una fase no requiere cambios, dilo en una línea y pasa a la siguiente.

Fase 1 — Estado (solo lectura)
Informa: número de notas en 00-INBOX/ y cuántas tienen más de 7 días; proyectos activos con su fecha de última actualización; notas modificadas en los últimos 7 días; problemas evidentes (enlaces rotos, propiedades obligatorias que faltan).

Fase 2 — Bandeja de entrada
Para cada nota de 00-INBOX/ propón: nuevo título, tipo, carpeta de destino, enlaces y observaciones (duplicados, dividir, datos sensibles). Presenta una tabla.

Fase 3 — Proyectos
Para cada proyecto con estado activo: próximas acciones vigentes, decisiones sin registrar, si está bloqueado o inactivo más de 30 días. Propón actualizaciones.

Fase 4 — Conexiones
Notas creadas o modificadas esta semana sin enlaces; temas con más de 10 notas sin MOC. Propón enlaces (con la frase que explica cada relación) y MOC nuevos.

Fase 5 — Índice y memoria
Propón cambios para 99-SYSTEM/Indice.md, 09-AI-MEMORY/contexto-activo.md y 09-AI-MEMORY/decisiones.md.

Fase 6 — Cierre
Resume todos los cambios con rutas, lista pendientes para la próxima sesión y propón el archivo 09-AI-MEMORY/sesiones/AAAA-MM-DD-sincronizacion.md.

Foco opcional de esta sesión: [ESCRIBE AQUÍ UN FOCO O DÉJALO VACÍO]
```

## Restricciones

- Aprobación obligatoria antes de cada fase de cambios.
- No elimina; archiva en `04-ARCHIVE/` si se aprueba.
- No toca `05-PERSONAL/`.

## Ejemplo de utilización

Foco opcional: "proyectos de docencia". El agente presenta la Fase 1 (12 capturas, 3 proyectos activos, 2 enlaces rotos) y espera. Apruebas la Fase 2 parcialmente ("aplica las filas 1 a 8"), y así sucesivamente.

---

[Biblioteca de prompts](README.md)
