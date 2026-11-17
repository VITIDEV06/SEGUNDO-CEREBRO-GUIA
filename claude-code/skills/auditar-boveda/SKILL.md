---
name: auditar-boveda
description: "Audita la bóveda: privacidad, estructura, propiedades, enlaces rotos, huérfanas, duplicados y mantenimiento. Entrega un informe sin modificar nada."
argument-hint: "[opcional: carpeta]"
disable-model-invocation: true
context: fork
agent: vault-auditor
---

Audita el segundo cerebro. Alcance: $ARGUMENTS (si está vacío, toda la bóveda excepto `05-PERSONAL/`).

Comprueba, en este orden de prioridad:
1. **Privacidad:** posibles credenciales, documentos de identidad, datos financieros o de salud fuera de `05-PERSONAL/`. Indica solo ruta y tipo de dato, nunca el dato.
2. **Estructura:** notas en carpetas que no corresponden a su `tipo`; archivos sueltos en la raíz.
3. **Propiedades:** falta `tipo`, `estado`, `creado` o `actualizado`; valores no válidos según `99-SYSTEM/rules/conventions.md`.
4. **Enlaces rotos:** `[[...]]` a notas inexistentes.
5. **Huérfanas:** notas sin enlaces entrantes ni salientes (excluye `99-SYSTEM/`, `10-TEMPLATES/` y `06-DAILY-NOTES/`).
6. **Duplicados:** títulos casi iguales o contenido repetido.
7. **Mantenimiento:** capturas con más de 7 días, proyectos activos sin cambios en 30 días, tags no registrados en `99-SYSTEM/tags.md`.

Formato: `# Auditoría — YYYY-MM-DD`, tabla resumen por severidad (crítico, importante, menor) y, por cada severidad, una tabla `Ruta | Problema | Corrección sugerida`. No modifiques ningún archivo.
