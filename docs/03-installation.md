# 03 — Instalación

> **Objetivo:** instalar Obsidian, Git y Python, descargar este repositorio y crear tu bóveda a partir de la plantilla.
> **Tiempo estimado:** 20–30 minutos.
> **Los agentes de IA** se instalan en guías propias: [07 — OpenCode](07-opencode-setup.md) y [08 — Claude Code](08-claude-code-setup.md).

Anterior: [02 — Requisitos](02-requirements.md) | [Inicio](../README.md) | Siguiente: [04 — Configuración de Obsidian](04-obsidian-setup.md)

---

## 1. Qué vamos a instalar y por qué

| Programa | Qué es | Por qué lo necesitamos |
| --- | --- | --- |
| Obsidian | Aplicación para escribir y enlazar notas Markdown. | Es la interfaz humana de la bóveda. |
| Git | Sistema de control de versiones. | Guarda el historial y permite deshacer cambios de la IA. |
| Python | Lenguaje de programación. | Ejecuta los scripts `new-vault.py`, `install-agents.py` y `validate-structure.py`. |

## 2. Instalar Obsidian

**Opción A — Instalador oficial (todas las plataformas):** descarga el instalador desde [obsidian.md/download](https://obsidian.md/download) y ejecútalo.

**Opción B — Gestor de paquetes:**

```powershell
# PowerShell (Windows)
winget install Obsidian.Obsidian
```

```bash
# Bash (macOS con Homebrew)
brew install --cask obsidian
```

En Linux, la página de descargas ofrece AppImage, `.deb`, Snap y Flatpak.

**Comprobación:** abre Obsidian. Debe aparecer la pantalla de bienvenida con las opciones *Create new vault* y *Open folder as vault*. Todavía no crees ninguna bóveda.

## 3. Instalar Git

```powershell
# PowerShell (Windows). Instala Git y Git Bash.
winget install --id Git.Git -e
```

```bash
# Bash (macOS con Homebrew)
brew install git
```

```bash
# Bash (Ubuntu / Debian)
sudo apt update && sudo apt install git
```

También puedes descargar el instalador de Windows desde [git-scm.com](https://git-scm.com/downloads/win). Acepta las opciones por defecto.

**Cierra y vuelve a abrir la terminal** y comprueba:

```bash
git --version
```

Debe mostrar algo como `git version 2.x.x`. Configura tu identidad (se usa en el historial de cambios):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"
```

> **Privacidad:** el correo aparece en cada commit. GitHub ofrece una dirección `noreply` en *Settings → Emails* si no quieres exponer tu correo real. Lo explicamos en [09 — Git y GitHub](09-git-github.md).

## 4. Instalar Python (opcional, recomendado)

```powershell
# PowerShell (Windows)
winget install --id Python.Python.3.12 -e
```

```bash
# Bash (macOS con Homebrew)
brew install python
```

En Ubuntu/Debian Python 3 ya viene instalado. Comprueba:

```powershell
# PowerShell o CMD (Windows)
python --version
```

```bash
# Bash (macOS / Linux)
python3 --version
```

> En macOS y Linux usa `python3` donde esta guía escribe `python`.

## 5. Descargar este repositorio

```bash
# Funciona igual en PowerShell, CMD y Bash
git clone https://github.com/<usuario>/second-brain-ai.git
cd second-brain-ai
```

Sustituye `<usuario>` por la cuenta donde está publicado el repositorio. Si prefieres no usar Git todavía, en GitHub pulsa **Code → Download ZIP** y descomprime el archivo.

## 6. Crear tu bóveda a partir de la plantilla

La carpeta `vault-template/` es una bóveda vacía y organizada. **No escribas tus notas dentro de este repositorio**: cópiala a otra ubicación. Así separas la plantilla pública de tu información privada.

**Opción A — Script (recomendado):**

```powershell
# PowerShell (Windows), desde la carpeta second-brain-ai
python scripts/new-vault.py "$HOME\Documents\SegundoCerebro"
```

```bash
# Bash (macOS / Linux), desde la carpeta second-brain-ai
python3 scripts/new-vault.py ~/Documents/SegundoCerebro
```

El script copia la plantilla, incluida la carpeta oculta `.obsidian/`, y **se detiene sin tocar nada** si la carpeta de destino ya existe y no está vacía.

**Opción B — Copia manual:**

```powershell
# PowerShell o CMD (Windows). /E copia subcarpetas, incluidas las ocultas.
robocopy vault-template "%USERPROFILE%\Documents\SegundoCerebro" /E
```

> En PowerShell sustituye `%USERPROFILE%` por `$HOME`. Robocopy devuelve el código `1` cuando copia archivos correctamente; no es un error.

```bash
# Bash (macOS / Linux)
cp -R vault-template ~/Documents/SegundoCerebro
```

## 7. Abrir la bóveda en Obsidian

1. Abre Obsidian.
2. Pulsa **Open folder as vault**.
3. Selecciona la carpeta `SegundoCerebro` que acabas de crear.
4. Si Obsidian pregunta si confías en el autor de la bóveda, elige **Trust author and enable plugins**: la plantilla solo activa plugins oficiales (*core plugins*), no plugins de la comunidad.

Debes ver en la barra lateral las carpetas `00-INBOX` a `99-SYSTEM` y la nota `AGENTS.md`.

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
| --- | --- | --- |
| `git` o `python` "no se reconoce como comando". | La terminal se abrió antes de instalar. | Cierra la terminal y abre una nueva. |
| `python` abre la Microsoft Store. | Alias de Windows. | Instala Python con winget o desactiva el alias en *Configuración → Aplicaciones → Alias de ejecución*. |
| La bóveda no tiene plantillas configuradas. | Se copió sin la carpeta oculta `.obsidian/`. | Usa el script o `robocopy /E`. |
| `new-vault.py` dice que el destino no está vacío. | Protección contra sobrescritura. | Elige otra carpeta o vacíala tú manualmente. |

## 9. Resultado esperado

- Obsidian, Git y (opcionalmente) Python instalados y verificados.
- Este repositorio descargado.
- Una bóveda nueva fuera del repositorio, abierta en Obsidian, con la estructura de carpetas visible.

---

Anterior: [02 — Requisitos](02-requirements.md) | [Inicio](../README.md) | Siguiente: [04 — Configuración de Obsidian](04-obsidian-setup.md)
