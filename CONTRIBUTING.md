# Guía de contribución

Gracias por querer mejorar **Second Brain AI**. Este proyecto es educativo: cada contribución debe ayudar a que una persona sin experiencia previa pueda construir y mantener su segundo cerebro.

## Principios

1. **Verificable antes que llamativo.** No añadas comandos, opciones de configuración ni funciones que no hayas comprobado en la documentación oficial de la herramienta. Incluye el enlace a la fuente en la descripción del pull request.
2. **Sin datos personales reales.** Los ejemplos usan personas, empresas y proyectos ficticios.
3. **Sin secretos.** Nunca incluyas API keys, tokens ni contraseñas, ni siquiera "de prueba".
4. **Sin emojis.** La identidad visual usa iconos SVG y badges.
5. **Una sola fuente de verdad.** Si un contenido ya existe, enlázalo en lugar de copiarlo.
6. **Herramientas como alternativas.** OpenCode y Claude Code son opciones intercambiables; ningún flujo debe exigir ambas.

## Flujo de trabajo

```bash
# Bash, PowerShell o CMD: los comandos de Git son iguales en los tres
git clone https://github.com/<tu-usuario>/second-brain-ai.git
cd second-brain-ai
git switch -c mejora/descripcion-corta
```

Haz tus cambios y valida la estructura:

```bash
python scripts/validate-structure.py
```

El validador debe terminar con `0 errores`. Después:

```bash
git add .
git commit -m "docs: explica cómo usar Bases en proyectos"
git push -u origin mejora/descripcion-corta
```

Abre el pull request en GitHub y describe:

- Qué cambia y por qué.
- Cómo lo verificaste (versión de la herramienta, sistema operativo).
- Enlaces a la documentación oficial usada.

## Convenciones

| Elemento | Convención |
| --- | --- |
| Idioma | Español neutro. Términos técnicos en inglés cuando son el nombre real (por ejemplo, *frontmatter*, *commit*). |
| Mensajes de commit | `tipo: descripción` con tipos `docs`, `feat`, `fix`, `chore`, `refactor`. |
| Nombres de archivo | `kebab-case.md`, sin espacios ni tildes. |
| Comandos | Cada bloque indica el shell: `bash`, `powershell` o `cmd`. |
| Diagramas | Mermaid dentro del Markdown. |
| Plantillas | La fuente es `templates/`. Copia el cambio en `vault-template/10-TEMPLATES/`; el validador comprueba que coinciden. |

## Qué contribuciones son bienvenidas

- Correcciones de comandos o configuraciones que cambiaron en una versión nueva de una herramienta.
- Nuevos prompts en `ai/prompts/` siguiendo la estructura existente.
- Nuevos workflows en `ai/workflows/`.
- Traducciones (en una carpeta `i18n/<idioma>/`).
- Mejoras de claridad para principiantes.

## Código de conducta

Trata a todas las personas con respeto. Las críticas se dirigen al contenido, no a quien lo escribió.
