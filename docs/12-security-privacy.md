# 12 — Seguridad y privacidad

> **Objetivo:** proteger tus datos, tus credenciales y tu bóveda frente a errores propios, errores de un agente y publicaciones accidentales.
> **Tiempo estimado:** 30 minutos. Léela antes de tu primer `git push`.

Anterior: [11 — Uso avanzado](11-advanced-usage.md) | [Inicio](../README.md) | Siguiente: [13 — Solución de problemas](13-troubleshooting.md)

---

## 1. Modelo de amenazas en una frase

Tus riesgos reales son tres: **publicar algo privado**, **filtrar una API key** y **que un agente modifique o borre notas** sin que lo notes. Cada sección de esta guía ataca uno de ellos.

## 2. Variables de entorno

Una **variable de entorno** es un valor que el sistema operativo entrega a los programas al ejecutarse. Es el lugar correcto para una API key: no vive en ningún archivo de la bóveda, así que no puede subirse a GitHub por error.

### Definir una variable para la sesión actual

```powershell
# PowerShell (solo esta ventana)
$env:ANTHROPIC_API_KEY = "pega-aquí-tu-clave"
```

```cmd
:: CMD (solo esta ventana)
set ANTHROPIC_API_KEY=pega-aquí-tu-clave
```

```bash
# Bash (solo esta terminal)
export ANTHROPIC_API_KEY="pega-aquí-tu-clave"
```

### Definirla de forma permanente

```powershell
# PowerShell: guarda la variable para tu usuario (abre una terminal nueva después)
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "pega-aquí-tu-clave", "User")
```

```bash
# Bash/Zsh: añade la línea a tu perfil (~/.bashrc o ~/.zshrc) y recárgalo
echo 'export ANTHROPIC_API_KEY="pega-aquí-tu-clave"' >> ~/.bashrc
source ~/.bashrc
```

> El historial de la terminal guarda lo que escribes. Si te preocupa, define la variable desde *Configuración del sistema → Variables de entorno* (Windows) o editando el archivo de perfil con un editor.

### Usar la variable en la configuración

| Herramienta | Cómo |
| --- | --- |
| OpenCode | `/connect` guarda la credencial fuera del proyecto. Si necesitas referenciarla en `opencode.json`, usa `"{env:ANTHROPIC_API_KEY}"`. |
| Claude Code | Con suscripción no necesitas clave. Con Console, define `ANTHROPIC_API_KEY` y Claude Code te preguntará si quieres usarla. |

### Archivo `.env`

Algunas herramientas leen un archivo `.env`. Este repositorio incluye [.env.example](../.env.example) (sin valores). Cópialo como `.env`, rellénalo solo en tu equipo, y comprueba que `.env` está en `.gitignore`. Ambos agentes tienen denegada la lectura de `.env`.

## 3. Qué nunca debe subirse a GitHub

| Elemento | Motivo | Protección en la plantilla |
| --- | --- | --- |
| API keys, tokens, contraseñas | Uso fraudulento inmediato. | `.env`, `*.pem`, `*.key` en `.gitignore`; lectura denegada a agentes. |
| `05-PERSONAL/` | Datos sensibles. | Excluida en el `.gitignore` de la bóveda. |
| `.obsidian/workspace*.json`, `cache` | Ruido y rutas locales. | Excluidos. |
| `.obsidian/plugins/*/data.json` | Algunos plugins guardan tokens de sincronización. | Excluido. |
| `.claude/settings.local.json`, `CLAUDE.local.md` | Preferencias personales. | Excluidos. |
| Tu bóveda completa en un repositorio **público** | Todo lo anterior a la vez. | Solo documentación: usa siempre repositorio privado. |

## 4. Permisos de los agentes

La plantilla aplica la misma política en ambas herramientas (detalle en [06 — Integración con IA](06-ai-integration.md#5-modelo-de-permisos-de-la-plantilla)):

| Nivel | Qué hace | Dónde |
| --- | --- | --- |
| Instrucciones | El agente *sabe* que no debe tocar `05-PERSONAL/`. | `AGENTS.md`, `99-SYSTEM/rules/privacy.md` |
| Permisos | La herramienta *impide* tocar `05-PERSONAL/`. | `opencode.json`, `.claude/settings.json` |
| Confirmación | Tú apruebas cada edición. | Efecto `ask` |
| Historial | Puedes deshacer cualquier cambio. | Git |

### Reglas para ajustar permisos sin perder seguridad

1. **Nunca** uses modos que omiten todas las confirmaciones (como `bypassPermissions` en Claude Code) en tu bóveda real.
2. Si una carpeta te pide demasiadas confirmaciones, permite la edición **solo en esa carpeta** (por ejemplo, `00-INBOX/`), no en toda la bóveda.
3. Mantén siempre en `deny`: borrar archivos, `git push`, `git reset --hard`, `git clean` y editar `05-PERSONAL/`.
4. Después de modificar permisos, pruébalos: pide al agente una acción que debería ser rechazada y comprueba que lo es.

Ejemplo — permitir editar en la bandeja sin preguntar:

```json
{ "action": "edit", "resource": "*00-INBOX/*", "effect": "allow" }
```

*(OpenCode: añádela **después** de `edit * ask` en la lista `permissions`.)*

```json
"allow": ["Edit(./00-INBOX/**)"]
```

*(Claude Code: añádela a la lista `allow`. Como `Edit` está en `ask`, y `ask` gana sobre `allow`, debes además quitar `Edit` de `ask` y poner reglas `ask` por carpeta. Por eso la plantilla mantiene `Edit` en `ask` global: es más simple y más seguro.)*

## 5. Evitar eliminaciones accidentales

- Los comandos de borrado están denegados en ambas configuraciones.
- Las reglas de la bóveda obligan a **archivar** (`04-ARCHIVE/`) en lugar de borrar.
- Obsidian guarda instantáneas locales con el plugin oficial **File recovery** (*Settings → File recovery*).
- Obsidian mueve los archivos eliminados a la papelera del sistema o a `.trash/` según *Settings → Files and links → Deleted files*.
- Git permite recuperar cualquier versión que hayas guardado en un commit.

> Las reglas de terminal se basan en el texto del comando. Un comando escrito de otra forma (por ejemplo, un script que borra archivos) podría no coincidir. Por eso la política por defecto para la terminal es **preguntar**, y por eso Git es tu red de seguridad final.

## 6. Backups: la regla 3-2-1

Mantén **3** copias, en **2** soportes distintos, con **1** fuera de tu casa.

| Copia | Ejemplo |
| --- | --- |
| 1. Original | Bóveda en tu disco. |
| 2. Remota versionada | Repositorio privado en GitHub. |
| 3. Independiente | Copia periódica en disco externo o servicio de copias de seguridad. |

Copia manual a un disco externo:

```powershell
# PowerShell o CMD (Windows): copia espejo; ajusta la letra de la unidad
robocopy "%USERPROFILE%\Documents\SegundoCerebro" "E:\Backups\SegundoCerebro" /MIR
```

> En PowerShell sustituye `%USERPROFILE%` por `$HOME`. **Cuidado con `/MIR`**: hace que el destino sea idéntico al origen, incluido eliminar en el destino lo que ya no exista en el origen. Comprueba bien el orden origen → destino.

```bash
# Bash (macOS / Linux): copia espejo; ajusta la ruta del disco
rsync -a --delete ~/Documents/SegundoCerebro/ /Volumes/Backup/SegundoCerebro/
```

Recuerda que `05-PERSONAL/` no está en GitHub: la copia independiente es la única copia remota de esa carpeta.

## 7. Separar bóveda pública y privada

Si quieres compartir parte de tu conocimiento (por ejemplo, apuntes de un curso):

1. **No hagas pública tu bóveda.** Crea una bóveda o repositorio aparte solo con lo publicable.
2. Copia ahí las notas seleccionadas, revisándolas una por una.
3. Revisa los enlaces `[[...]]`: pueden revelar títulos de notas privadas.
4. Revisa las propiedades: `fuente`, `asistentes` o `relacionado` pueden contener nombres.
5. Pide al agente *Vault Auditor* una auditoría de privacidad de esa carpeta antes de publicar.

## 8. Revisar cambios antes de cada commit

```bash
git status              # ¿qué archivos cambian? ¿hay alguno inesperado?
git diff                # ¿qué líneas cambian?
git add .
git diff --staged       # revisión final de lo que se va a guardar
git commit -m "Mensaje descriptivo"
```

Lista de comprobación antes de `git push`:

- [ ] El repositorio remoto es **privado** (`git remote -v` y comprobar en GitHub).
- [ ] `git status` no muestra archivos de `05-PERSONAL/`, `.env` ni claves.
- [ ] No hay API keys en el diff. Búsqueda rápida:

```bash
# Bash o Git Bash: busca patrones típicos de claves en lo que vas a subir
git diff --staged | grep -n -i -E "api[_-]?key|secret|token|password|sk-[a-z0-9]"
```

```powershell
# PowerShell: equivalente
git diff --staged | Select-String -Pattern "api[_-]?key|secret|token|password|sk-[a-z0-9]"
```

Si no aparece nada, puedes continuar. Si aparece algo, revísalo antes de hacer commit.

## 9. Si subiste un secreto o dato privado por error

1. **Revoca la credencial inmediatamente** en el proveedor (Anthropic Console, OpenAI, etc.) y genera una nueva. Asume que está comprometida: borrarla del repositorio no la protege, porque sigue en el historial y puede haber sido copiada.
2. Borra el archivo del repositorio y añádelo a `.gitignore`.
3. Si el dato debe desaparecer del historial, sigue la guía oficial de GitHub [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
4. Activa **Secret scanning** y **Push protection** en *Settings → Code security* de tu repositorio si están disponibles para tu cuenta.

## 10. Resultado esperado

- Ninguna credencial vive dentro de la bóveda.
- Los agentes no pueden editar `05-PERSONAL/` ni ejecutar comandos destructivos.
- Tienes tres copias de tu bóveda.
- Revisas `git diff --staged` antes de cada commit importante.

---

Anterior: [11 — Uso avanzado](11-advanced-usage.md) | [Inicio](../README.md) | Siguiente: [13 — Solución de problemas](13-troubleshooting.md)
