# Workflow H — Quiero respaldar mi bóveda en GitHub sin publicar información privada

| | |
| --- | --- |
| **Paso del ciclo** | Transversal |
| **Tiempo** | 15 minutos la primera vez; 1 minuto después |
| **Herramientas** | Git, GitHub |

## Objetivo

Tener una copia remota y versionada de tu bóveda, en un repositorio **privado**, que no incluya datos sensibles ni credenciales.

## Pasos (primera vez)

### 1. Revisar el `.gitignore` de la bóveda

La plantilla incluye `.gitignore` en la raíz de la bóveda. Ábrelo y confirma que excluye, al menos:

```gitignore
05-PERSONAL/*
!05-PERSONAL/LEEME-personal.md
.env
.env.*
.obsidian/workspace.json
.obsidian/plugins/*/data.json
.claude/settings.local.json
```

Explicación de cada regla: [12 — Seguridad y privacidad](../../docs/12-security-privacy.md#3-qué-nunca-debe-subirse-a-github).

### 2. Buscar datos sensibles fuera de `05-PERSONAL/`

```text
/auditar-boveda
```

Revisa la sección **Crítico** del informe. Mueve tú mismo a `05-PERSONAL/` cualquier nota sensible que aparezca (los agentes no pueden escribir en esa carpeta).

### 3. Inicializar y revisar

```bash
cd <ruta-de-tu-bóveda>
git init
git add .
git status
```

Lee la lista completa. **No debe aparecer** ningún archivo de `05-PERSONAL/` (salvo el `LEEME`), ningún `.env` ni ninguna clave.

Comprobación de patrones de secretos:

```bash
# Bash o Git Bash
git diff --staged | grep -n -i -E "api[_-]?key|secret|token|password|sk-[a-z0-9]"
```

```powershell
# PowerShell
git diff --staged | Select-String -Pattern "api[_-]?key|secret|token|password|sk-[a-z0-9]"
```

Sin resultados → continúa.

### 4. Primer commit

```bash
git commit -m "Bóveda inicial"
```

### 5. Crear el repositorio privado y subir

En [github.com/new](https://github.com/new): nombre `SegundoCerebro`, visibilidad **Private**, sin README ni `.gitignore`. Luego:

```bash
git branch -M main
git remote add origin https://github.com/<tu-usuario>/SegundoCerebro.git
git push -u origin main
```

O con GitHub CLI:

```bash
gh repo create SegundoCerebro --private --source=. --remote=origin --push
```

### 6. Verificar en GitHub

- Aparece el indicador **Private**.
- La carpeta `05-PERSONAL` solo contiene `LEEME-personal.md`.
- No hay archivos `.env`.

## Pasos (cada semana)

```bash
git status
git diff --stat
git add .
git diff --staged
git commit -m "Revisión semanal AAAA-MM-DD"
git push
```

## ¿Y `05-PERSONAL/`?

No está en GitHub. Respáldala con la copia independiente de la regla 3-2-1 (disco externo o servicio de copias de seguridad cifrado). Ver [12 — Seguridad, sección 6](../../docs/12-security-privacy.md#6-backups-la-regla-3-2-1).

## Errores frecuentes

| Error | Solución |
| --- | --- |
| Crear el repositorio como público. | *Settings → General → Danger Zone → Change visibility* → Private. Si ya hubo datos expuestos, ver [12 — Seguridad, sección 9](../../docs/12-security-privacy.md#9-si-subiste-un-secreto-o-dato-privado-por-error). |
| `05-PERSONAL/` aparece en `git status` tras haberla versionado antes. | `git rm -r --cached 05-PERSONAL` y commit (no borra tus archivos locales). |
| Pedirle al agente que haga `git push`. | Está denegado a propósito: publicar es decisión tuya. |

## Resultado esperado

Un repositorio privado en GitHub con el historial de tu bóveda, sin datos sensibles ni credenciales, actualizado al menos una vez por semana.

---

Anterior: [G](G-revision-semanal.md) | [Workflows](README.md)
