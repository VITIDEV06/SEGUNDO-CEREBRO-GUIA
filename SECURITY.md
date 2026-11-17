# Política de seguridad

## Alcance

Este repositorio contiene documentación, plantillas de bóveda y archivos de configuración de ejemplo. No contiene un servicio en ejecución ni gestiona credenciales. Aun así, una configuración de ejemplo insegura puede provocar daños reales en la bóveda de quien la copie, por lo que tratamos esos casos como incidencias de seguridad.

Se consideran incidencias de seguridad:

- Un archivo de ejemplo que contenga una API key, token o credencial real.
- Una configuración de permisos (OpenCode o Claude Code) que permita a un agente borrar o modificar notas sensibles sin pedir autorización, contradiciendo lo que dice la documentación.
- Un script de `scripts/` que pueda sobrescribir o eliminar archivos del usuario.
- Una regla de `.gitignore` documentada como protectora que en realidad no excluye lo que promete.

## Versiones soportadas

Solo se mantiene la rama `main`.

## Cómo reportar una vulnerabilidad

1. **No abras un issue público** si el problema expone un secreto o permite daño inmediato.
2. Usa la función **Report a vulnerability** de la pestaña *Security* del repositorio en GitHub (GitHub Private Vulnerability Reporting).
3. Incluye: archivo afectado, pasos para reproducirlo y el impacto esperado.

Para problemas menores (por ejemplo, una regla de `.gitignore` mejorable) puedes abrir un issue normal.

## Si encontraste un secreto publicado

Si detectas una credencial real en el historial del repositorio, repórtala por el canal privado. La credencial debe considerarse comprometida y revocarse en el proveedor correspondiente; borrarla del repositorio no es suficiente porque permanece en el historial de Git y en posibles copias.

## Guía para usuarios

Las prácticas de seguridad para tu propia bóveda (variables de entorno, permisos de agentes, backups, separación pública/privada) están en [docs/12-security-privacy.md](docs/12-security-privacy.md).
