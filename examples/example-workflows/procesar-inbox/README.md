# Ejemplo: procesar la bandeja de entrada

Estado de dos capturas **antes** y **después** de ejecutar `/procesar-inbox` (OpenCode o Claude Code). Datos ficticios.

## Antes

```text
antes/00-INBOX/
├── feynman.md          captura de una idea de estudio, sin formato
└── reunion ana.md      apuntes rápidos de una reunión
```

## Propuesta del agente (paso 1, sin cambios todavía)

| Nota actual | Nuevo título | Tipo | Destino | Enlaces propuestos | Observaciones |
| --- | --- | --- | --- | --- | --- |
| `feynman.md` | Técnica Feynman | permanente | `03-RESOURCES/` | La recuperación activa supera a la relectura | Sin fuente: añadir tag `revisar/verificar-fuente`. |
| `reunion ana.md` | 2026-11-18 Planificación del taller | reunion | `07-MEETINGS/` | Taller de Python, Ana Pérez | Contiene una decisión y una tarea con responsable. |

## Respuesta de la persona

```text
Aprueba ambas filas.
```

## Después

```text
despues/
├── 03-RESOURCES/Técnica Feynman.md
└── 07-MEETINGS/2026-11-18 Planificación del taller.md
```

Observa en los archivos de `despues/`:

- Frontmatter completo según `conventions.md`.
- Título como afirmación o con el formato de reunión.
- Enlaces a notas existentes.
- El texto original conservado en `## Captura original`.

Los enlaces `[[...]]` apuntan a notas de la bóveda de ejemplo ([example-vault](../../example-vault/LEEME-ejemplo.md)).
