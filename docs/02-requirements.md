# 02 — Requisitos

> **Objetivo:** comprobar que tu equipo y tus cuentas cumplen lo necesario antes de instalar.
> **Tiempo estimado:** 10 minutos.

Anterior: [01 — Introducción](01-introduction.md) | [Inicio](../README.md) | Siguiente: [03 — Instalación](03-installation.md)

---

## 1. Resumen

| Componente | Obligatorio | Coste | Para qué |
| --- | --- | --- | --- |
| Obsidian | Sí | Gratuito para uso personal | Escribir y navegar la bóveda |
| Git | Sí | Gratuito | Historial de versiones y respaldo |
| Cuenta de GitHub | Recomendado | Gratuito (repositorios privados incluidos) | Copia de seguridad remota |
| OpenCode **o** Claude Code | Al menos uno | Depende del proveedor del modelo | Agente de IA |
| Python 3.10 o superior | Opcional | Gratuito | Scripts de validación e instalación |
| Editor de código (VS Code u otro) | Opcional | Gratuito | Editar archivos de configuración |

> **Solo necesitas un agente.** OpenCode y Claude Code son alternativas. Esta guía documenta ambos para que elijas.

## 2. Sistema operativo

La guía cubre **Windows 10/11**, **macOS** y **Linux**. Los requisitos mínimos publicados por Claude Code son macOS 13+, Windows 10 1809+, Ubuntu 20.04+ o Debian 10+, con 4 GB de RAM. OpenCode publica binarios para Windows (x64 y ARM64), macOS y Linux.

### Cómo saber qué terminal estás usando (Windows)

Muchos errores de principiante vienen de pegar un comando en la terminal equivocada.

| Lo que ves al inicio de la línea | Terminal |
| --- | --- |
| `PS C:\Users\TuNombre>` | PowerShell |
| `C:\Users\TuNombre>` (sin `PS`) | CMD (Símbolo del sistema) |
| `TuNombre@EQUIPO MINGW64 ~` | Git Bash |

En esta guía cada bloque de código indica para qué terminal es: `powershell`, `cmd` o `bash`. Los comandos de Git funcionan igual en las tres.

## 3. Cuentas y costes del agente de IA

### Claude Code

Requiere una de estas opciones:

- Una suscripción **Pro, Max, Ultra, Team o Enterprise** de Claude (el plan gratuito no incluye Claude Code).
- Una cuenta de **Claude Console** con facturación por uso de API.
- Un proveedor en la nube compatible (Amazon Bedrock, Google Cloud, Microsoft Foundry).

Fuente: [documentación oficial de instalación](https://code.claude.com/docs/en/setup).

### OpenCode

OpenCode es de código abierto y se conecta a distintos proveedores de modelos. Necesitas una cuenta en el proveedor que elijas (por ejemplo Anthropic, OpenAI u otros compatibles). El coste depende de ese proveedor. La conexión se hace con el comando `/connect` dentro de OpenCode.

Fuente: [documentación oficial de OpenCode](https://opencode.ai/docs/).

## 4. Conocimientos previos

No necesitas saber programar. Sí te ayudará:

- Saber abrir una terminal y pegar un comando.
- Saber crear y mover carpetas.

Si nunca usaste Markdown, la [guía 04](04-obsidian-setup.md) incluye lo básico.

## 5. Lista de comprobación

Marca cada punto antes de continuar:

- [ ] Sé qué sistema operativo y qué terminal uso.
- [ ] Tengo permisos para instalar programas en mi equipo.
- [ ] Decidí qué agente usaré primero: OpenCode o Claude Code.
- [ ] Tengo (o voy a crear) la cuenta necesaria para ese agente.
- [ ] Tengo una cuenta de GitHub, o la crearé en la [guía 09](09-git-github.md).

## 6. Errores frecuentes

| Error | Solución |
| --- | --- |
| Intentar usar Claude Code con el plan gratuito de Claude. | Necesitas Pro o superior, o una cuenta de Console. |
| Pegar un comando de PowerShell en CMD (o al revés). | Revisa la tabla de la sección 2. |
| Instalar los dos agentes "por si acaso" y no configurar ninguno. | Elige uno, configúralo bien, y añade el otro después si lo necesitas. |

## 7. Resultado esperado

Sabes qué vas a instalar, qué cuenta necesitas y en qué terminal ejecutarás los comandos.

---

Anterior: [01 — Introducción](01-introduction.md) | [Inicio](../README.md) | Siguiente: [03 — Instalación](03-installation.md)
