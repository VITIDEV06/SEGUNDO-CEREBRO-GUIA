---
tipo: sistema
estado: activo
creado: 2026-11-16
actualizado: 2026-11-16
---

# Privacidad

## Qué se considera sensible

- Salud, finanzas, situación legal, datos familiares.
- Documentos de identidad, números de cuenta, direcciones, teléfonos.
- Contraseñas, API keys, tokens, códigos de recuperación (estos **no** deben estar en la bóveda: usa un gestor de contraseñas).
- Opiniones personales sobre terceros.
- Información confidencial de empleadores o clientes.

## Dónde va

- Todo lo sensible va en `05-PERSONAL/`.
- `05-PERSONAL/` no se sube a repositorios públicos y está excluida en `.gitignore` de los repositorios de plantilla.

## Reglas para agentes de IA

1. No leer `05-PERSONAL/` salvo petición explícita en el chat. Los permisos de la configuración lo exigen además de esta regla.
2. No modificar ni mover nada en `05-PERSONAL/`. La configuración lo deniega.
3. No copiar información sensible a otras carpetas, a `09-AI-MEMORY/` ni a resúmenes.
4. Si detectas información sensible fuera de `05-PERSONAL/`, avisa con la ruta exacta y **no la repitas** en la respuesta.
5. No leer archivos `.env` ni archivos con credenciales.
6. Notas de personas (`02-AREAS/Personas/`): solo contexto profesional (rol, proyectos compartidos, acuerdos). Nada de datos personales.

## Antes de publicar o hacer `git push`

- Ejecutar `git status` y `git diff --staged` y revisar cada archivo.
- Confirmar que el repositorio remoto es **privado** si contiene notas reales.
