# Scripts

Tres scripts en Python 3.10+ que solo usan la biblioteca estándar (no hay que instalar dependencias). En macOS y Linux escribe `python3` donde aquí aparece `python`.

| Script | Para qué |
| --- | --- |
| [new-vault.py](new-vault.py) | Crear una bóveda nueva a partir de `vault-template/`. |
| [install-agents.py](install-agents.py) | Copiar la configuración de OpenCode y/o Claude Code a una bóveda. |
| [validate-structure.py](validate-structure.py) | Comprobar la calidad de este repositorio antes de publicarlo. |

Ninguno borra ni sobrescribe archivos.

## new-vault.py

```bash
python scripts/new-vault.py "<ruta-de-la-nueva-bóveda>"
```

- Copia toda la plantilla, incluidas las carpetas ocultas (`.obsidian/`) y `.gitignore`.
- Se detiene si el destino existe y no está vacío.
- Se niega a crear la bóveda dentro de este repositorio.

## install-agents.py

```bash
python scripts/install-agents.py --tool opencode    --vault "<ruta-de-tu-bóveda>"
python scripts/install-agents.py --tool claude-code --vault "<ruta-de-tu-bóveda>"
python scripts/install-agents.py --tool both        --vault "<ruta-de-tu-bóveda>" --dry-run
```

- Exige que la bóveda contenga `AGENTS.md`.
- Si un archivo de destino existe, lo omite y lo informa (`OMITIDO (ya existe)`).
- `--dry-run` muestra lo que haría sin copiar nada.

## validate-structure.py

```bash
python scripts/validate-structure.py
```

Comprueba:

| Comprobación | Detalle |
| --- | --- |
| Estructura | Existen todos los archivos y carpetas que documenta el README. |
| Enlaces Markdown | Cada enlace relativo `[texto](ruta)` apunta a un archivo existente, y cada `#ancla` a un encabezado existente. |
| Wikilinks | Los `[[enlaces]]` de `vault-template/` y `examples/example-vault/` apuntan a notas existentes. |
| Plantillas | `templates/` y `vault-template/10-TEMPLATES/` son idénticas. |
| JSON | Todos los `.json` son válidos. |
| Frontmatter | Agentes, comandos y skills tienen los campos obligatorios de su herramienta. |
| Mermaid | Cada bloque empieza con un tipo de diagrama conocido y tiene los `end` de sus `subgraph`. |
| Secretos | No hay patrones de API keys o tokens. |
| Emojis | No hay emojis (requisito de estilo del proyecto). |
| Bases | Los `.base` contienen `views`. |

Termina con código `0` si no hay errores y `1` si los hay, por lo que puede usarse en integración continua (por ejemplo, GitHub Actions).

> La comprobación de Mermaid es estructural: detecta errores comunes, pero no sustituye a renderizar el diagrama. GitHub muestra un error visible en la página si un diagrama no se puede renderizar.
