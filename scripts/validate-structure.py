#!/usr/bin/env python3
"""Valida la estructura y la calidad del repositorio Second Brain AI.

Uso:
    python scripts/validate-structure.py

Código de salida: 0 si no hay errores, 1 si los hay.
Solo usa la biblioteca estándar de Python (3.10 o superior).
"""
from __future__ import annotations

import filecmp
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md", ".gitignore", ".env.example",
    "assets/banner.jpg", "assets/architecture", "assets/diagrams",
    *[f"docs/{n}" for n in [
        "01-introduction.md", "02-requirements.md", "03-installation.md", "04-obsidian-setup.md",
        "05-vault-architecture.md", "06-ai-integration.md", "07-opencode-setup.md",
        "08-claude-code-setup.md", "09-git-github.md", "10-workflows.md", "11-advanced-usage.md",
        "12-security-privacy.md", "13-troubleshooting.md"]],
    *[f"vault-template/{d}" for d in [
        "00-INBOX", "01-PROJECTS", "02-AREAS", "03-RESOURCES", "04-ARCHIVE", "05-PERSONAL",
        "06-DAILY-NOTES", "07-MEETINGS", "08-IDEAS", "09-AI-MEMORY", "10-TEMPLATES", "99-SYSTEM",
        "AGENTS.md", ".gitignore", ".obsidian/app.json"]],
    "ai/README.md", "ai/prompts/README.md", "ai/agents/README.md", "ai/workflows/README.md",
    "ai/rules/README.md", "ai/examples/README.md",
    "opencode/README.md", "opencode/opencode.example.json", "opencode/agents", "opencode/commands",
    "opencode/instructions",
    "claude-code/README.md", "claude-code/CLAUDE.md.example", "claude-code/settings.example.json",
    "claude-code/agents", "claude-code/skills", "claude-code/rules",
    *[f"templates/{n}.md" for n in [
        "daily-note", "project", "meeting", "person", "permanent-note", "learning-note", "idea"]],
    "examples/example-vault", "examples/example-projects", "examples/example-workflows",
    "scripts/README.md", "scripts/validate-structure.py", "scripts/new-vault.py", "scripts/install-agents.py",
]

AGENT_IDS = ["knowledge-manager", "research-assistant", "project-manager", "note-processor",
             "learning-assistant", "memory-assistant", "vault-auditor"]
COMMAND_IDS = ["capturar", "procesar-inbox", "nuevo-proyecto", "contexto-proyecto",
               "revision-semanal", "auditar-boveda", "sincronizar"]

MERMAID_TYPES = ("flowchart", "graph", "sequenceDiagram", "stateDiagram", "stateDiagram-v2",
                 "classDiagram", "erDiagram", "gantt", "pie", "mindmap", "timeline", "journey")

SECRET_PATTERNS = [
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{32,}"),
    re.compile(r"ghp_[A-Za-z0-9]{36}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{40,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]

EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F900-\U0001F9FF\U00002B50\U00002B55\uFE0F]")

TEXT_EXT = {".md", ".json", ".py", ".base", ".example", ".txt", ".gitignore"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}

errors: list[str] = []
warnings: list[str] = []


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def iter_files(ext: set[str] | None = None):
    for p in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        if p.is_file() and (ext is None or p.suffix in ext or p.name in ext):
            yield p


def strip_code(text: str) -> str:
    """Elimina bloques de código cercados, código en línea y comentarios HTML."""
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def github_slug(heading: str) -> str:
    h = heading.strip().lower()
    h = h.replace("`", "")
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)  # enlaces en encabezados
    out = []
    for ch in h:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in ("L", "N"):
            out.append(ch)
    return "".join(out).replace(" ", "-")


def anchors_of(md: Path) -> set[str]:
    text = re.sub(r"^```.*?^```", "", md.read_text(encoding="utf-8"), flags=re.S | re.M)
    seen: dict[str, int] = {}
    result = set()
    for m in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, flags=re.M):
        s = github_slug(m.group(1))
        if s in seen:
            seen[s] += 1
            s = f"{s}-{seen[s]}"
        else:
            seen[s] = 0
        result.add(s)
    return result


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, flags=re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            data[km.group(1)] = km.group(2).strip().strip('"')
    return data


# ---------------------------------------------------------------------------
def check_required():
    for r in REQUIRED:
        if not (ROOT / r).exists():
            errors.append(f"[estructura] Falta: {r}")
    for d in ["assets/architecture", "assets/diagrams"]:
        p = ROOT / d
        if p.is_dir() and not any(p.iterdir()):
            errors.append(f"[estructura] Carpeta vacía (Git no la versionará): {d}")
    for a in AGENT_IDS:
        for base in ("ai/agents", "opencode/agents", "claude-code/agents"):
            if not (ROOT / base / f"{a}.md").is_file():
                errors.append(f"[estructura] Falta agente {base}/{a}.md")
    for c in COMMAND_IDS:
        if not (ROOT / "opencode/commands" / f"{c}.md").is_file():
            errors.append(f"[estructura] Falta comando opencode/commands/{c}.md")
        if not (ROOT / "claude-code/skills" / c / "SKILL.md").is_file():
            errors.append(f"[estructura] Falta skill claude-code/skills/{c}/SKILL.md")
    prompts = sorted((ROOT / "ai/prompts").glob("[0-9][0-9]-*.md"))
    if len(prompts) < 17:
        errors.append(f"[estructura] Se esperaban 17 prompts en ai/prompts, hay {len(prompts)}")
    workflows = sorted((ROOT / "ai/workflows").glob("[A-H]-*.md"))
    if len(workflows) != 8:
        errors.append(f"[estructura] Se esperaban 8 workflows (A-H), hay {len(workflows)}")


def check_markdown_links():
    link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]]*\]\(([^)\s]+)\)")
    html_re = re.compile(r"""(?:src|href)=["']([^"']+)["']""")
    count = 0
    for md in iter_files({".md"}):
        raw = md.read_text(encoding="utf-8")
        text = strip_code(raw)
        targets = [a or b for a, b in link_re.findall(text)] + html_re.findall(text)
        for t in targets:
            if re.match(r"^(https?:|mailto:|tel:)", t):
                continue
            count += 1
            path_part, _, anchor = t.partition("#")
            target = md if not path_part else (md.parent / unquote(path_part)).resolve()
            if not target.exists():
                errors.append(f"[enlace] {rel(md)} -> {t} (no existe)")
                continue
            if anchor and target.is_file() and target.suffix == ".md":
                if unquote(anchor) not in anchors_of(target):
                    errors.append(f"[ancla] {rel(md)} -> {t} (no existe el encabezado)")
    return count


def check_wikilinks():
    vaults = [ROOT / "vault-template", ROOT / "examples/example-vault"]
    total = 0
    for v in vaults:
        names = set()
        for p in v.rglob("*"):
            if p.is_file():
                names.add(p.stem)
                names.add(p.name)
        for md in v.rglob("*.md"):
            if "10-TEMPLATES" in md.parts:
                continue
            text = strip_code(md.read_text(encoding="utf-8"))
            for m in re.finditer(r"\[\[([^\]|#]*)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", text):
                name = m.group(1).strip()
                total += 1
                if not name:
                    errors.append(f"[wikilink] {rel(md)}: enlace vacío [[]]")
                elif name not in names and Path(name).name not in names:
                    errors.append(f"[wikilink] {rel(md)} -> [[{name}]] (nota inexistente)")
    return total


def check_templates_sync():
    a, b = ROOT / "templates", ROOT / "vault-template/10-TEMPLATES"
    for f in sorted(a.glob("*.md")):
        g = b / f.name
        if not g.exists():
            errors.append(f"[plantillas] Falta en vault-template/10-TEMPLATES: {f.name}")
        elif not filecmp.cmp(f, g, shallow=False):
            errors.append(f"[plantillas] Difiere de templates/: vault-template/10-TEMPLATES/{f.name}")


def check_json():
    n = 0
    for p in iter_files({".json"}):
        n += 1
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"[json] {rel(p)}: {e}")
    # Coherencia básica de las configuraciones de agentes
    oc = json.loads((ROOT / "opencode/opencode.example.json").read_text(encoding="utf-8"))
    for i, rule in enumerate(oc.get("permissions", [])):
        if set(rule) != {"action", "resource", "effect"} or rule["effect"] not in ("allow", "ask", "deny"):
            errors.append(f"[opencode] Regla de permiso {i} mal formada: {rule}")
    cc = json.loads((ROOT / "claude-code/settings.example.json").read_text(encoding="utf-8"))
    perms = cc.get("permissions", {})
    for key in perms:
        if key not in ("allow", "ask", "deny", "defaultMode", "additionalDirectories"):
            errors.append(f"[claude-code] Clave de permisos desconocida: {key}")
    return n


def check_frontmatter():
    for a in AGENT_IDS:
        p = ROOT / "opencode/agents" / f"{a}.md"
        fm = frontmatter(p.read_text(encoding="utf-8")) if p.exists() else None
        if fm is None or "description" not in fm or fm.get("mode") not in ("primary", "subagent", "all"):
            errors.append(f"[frontmatter] {rel(p)}: requiere description y mode válido")
        p = ROOT / "claude-code/agents" / f"{a}.md"
        fm = frontmatter(p.read_text(encoding="utf-8")) if p.exists() else None
        if fm is None or fm.get("name") != a or not fm.get("description"):
            errors.append(f"[frontmatter] {rel(p)}: requiere name == '{a}' y description")
    for c in COMMAND_IDS:
        p = ROOT / "opencode/commands" / f"{c}.md"
        fm = frontmatter(p.read_text(encoding="utf-8")) if p.exists() else None
        if fm is None or not fm.get("description"):
            errors.append(f"[frontmatter] {rel(p)}: requiere description")
        if fm and "template" in fm:
            errors.append(f"[frontmatter] {rel(p)}: 'template' no se permite en el frontmatter")
        if fm and fm.get("agent") and fm["agent"] not in AGENT_IDS:
            errors.append(f"[frontmatter] {rel(p)}: agente desconocido {fm['agent']}")
        p = ROOT / "claude-code/skills" / c / "SKILL.md"
        fm = frontmatter(p.read_text(encoding="utf-8")) if p.exists() else None
        if fm is None or fm.get("name") != c or not fm.get("description"):
            errors.append(f"[frontmatter] {rel(p)}: requiere name == '{c}' y description")
        if fm and fm.get("agent") and fm["agent"] not in AGENT_IDS:
            errors.append(f"[frontmatter] {rel(p)}: agente desconocido {fm['agent']}")
    for p in (ROOT / "templates").glob("*.md"):
        fm = frontmatter(p.read_text(encoding="utf-8"))
        if fm is None or "tipo" not in fm:
            errors.append(f"[frontmatter] {rel(p)}: la plantilla requiere la propiedad tipo")


def check_mermaid():
    n = 0
    for md in iter_files({".md"}):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"^```mermaid\s*\n(.*?)^```", text, flags=re.S | re.M):
            n += 1
            body = m.group(1)
            lines = [ln.strip() for ln in body.splitlines() if ln.strip() and not ln.strip().startswith("%%")]
            if not lines or not lines[0].split()[0] in MERMAID_TYPES:
                errors.append(f"[mermaid] {rel(md)}: tipo de diagrama desconocido: {lines[0] if lines else '(vacío)'}")
                continue
            opens = sum(1 for ln in lines if re.match(r"^(subgraph|alt|opt|loop|par|critical)\b", ln))
            ends = sum(1 for ln in lines if ln == "end")
            if opens != ends:
                errors.append(f"[mermaid] {rel(md)}: bloques abiertos ({opens}) y 'end' ({ends}) no coinciden")
            if re.search(r"\]\s*\[", body):
                warnings.append(f"[mermaid] {rel(md)}: posible nodo con corchetes consecutivos")
    return n


def check_secrets_and_emojis():
    for p in iter_files():
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".ico", ".pdf"}:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                errors.append(f"[secreto] {rel(p)}: coincide con el patrón {pat.pattern}")
        for i, line in enumerate(text.splitlines(), 1):
            if EMOJI_RE.search(line):
                errors.append(f"[emoji] {rel(p)}:{i}")
                break
        if p.name == ".env":
            errors.append(f"[secreto] Archivo .env presente en el repositorio: {rel(p)}")


def check_bases():
    for p in ROOT.rglob("*.base"):
        text = p.read_text(encoding="utf-8")
        if "views:" not in text:
            errors.append(f"[bases] {rel(p)}: falta 'views:'")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    check_required()
    nlinks = check_markdown_links()
    nwiki = check_wikilinks()
    check_templates_sync()
    njson = check_json()
    check_frontmatter()
    nmer = check_mermaid()
    check_secrets_and_emojis()
    check_bases()

    print("Second Brain AI — validación de estructura")
    print(f"  Enlaces Markdown comprobados: {nlinks}")
    print(f"  Wikilinks comprobados:        {nwiki}")
    print(f"  Archivos JSON comprobados:    {njson}")
    print(f"  Diagramas Mermaid:            {nmer}")
    for w in warnings:
        print(f"AVISO  {w}")
    for e in errors:
        print(f"ERROR  {e}")
    print(f"\nResultado: {len(errors)} errores, {len(warnings)} avisos.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
