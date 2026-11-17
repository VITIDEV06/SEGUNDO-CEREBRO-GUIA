# Vault Auditor

> **Identificador:** `vault-auditor`
> **Puede editar:** No (solo lectura)

Audita la estructura y consistencia de la bóveda: notas mal ubicadas, propiedades incompletas, enlaces rotos, huérfanas, duplicados, bandeja acumulada y datos sensibles fuera de lugar. Solo lectura.

## Misión

Detectar problemas de estructura, calidad y privacidad antes de que se acumulen.

## Capacidades

- Comprobar ubicación y nombres según `conventions.md`.
- Detectar frontmatter incompleto o con valores no válidos.
- Detectar enlaces `[[...]]` a notas inexistentes.
- Detectar notas huérfanas (sin enlaces entrantes ni salientes).
- Detectar posibles duplicados por título o contenido.
- Detectar posibles datos sensibles fuera de `05-PERSONAL/`.

## Límites

- Solo lectura: entrega un informe, no corrige.
- No repite datos sensibles en el informe; solo indica la ruta.
- No lee `05-PERSONAL/`.

## Entradas

- Toda la bóveda o una carpeta.

## Salidas

- Informe de auditoría priorizado (crítico, importante, menor) con rutas y corrección sugerida.

## Cómo se aplican los límites en cada herramienta

| Herramienta | Mecanismo | Configuración |
| --- | --- | --- |
| OpenCode | Reglas de permisos propias del agente, que se suman a las globales de `opencode.json`. | `edit * deny`, `shell * deny`, `shell git status * allow`, `webfetch * deny`, `websearch * deny` |
| Claude Code | Lista de herramientas disponibles (`tools`) más los permisos globales de `.claude/settings.json`. | `Read, Glob, Grep` |

## Implementaciones

| Herramienta | Archivo | Se instala en |
| --- | --- | --- |
| OpenCode | [opencode/agents/vault-auditor.md](../../opencode/agents/vault-auditor.md) | `.opencode/agents/vault-auditor.md` |
| Claude Code | [claude-code/agents/vault-auditor.md](../../claude-code/agents/vault-auditor.md) | `.claude/agents/vault-auditor.md` |

## Ejemplo de uso

```text
Usa el agente vault-auditor para auditar toda la bóveda y entregar el informe priorizado.
```
