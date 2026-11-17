#!/usr/bin/env python3
"""Instala la configuración de OpenCode y/o Claude Code en una bóveda existente.

Uso:
    python scripts/install-agents.py --tool opencode    --vault RUTA_BOVEDA
    python scripts/install-agents.py --tool claude-code --vault RUTA_BOVEDA
    python scripts/install-agents.py --tool both        --vault RUTA_BOVEDA [--dry-run]

Qué copia:
    OpenCode     opencode/opencode.example.json  -> <bóveda>/opencode.json
                 opencode/agents/*.md            -> <bóveda>/.opencode/agents/
                 opencode/commands/*.md          -> <bóveda>/.opencode/commands/
                 opencode/instructions/*.md      -> <bóveda>/.opencode/instructions/
    Claude Code  claude-code/CLAUDE.md.example   -> <bóveda>/CLAUDE.md
                 claude-code/settings.example.json -> <bóveda>/.claude/settings.json
                 claude-code/agents/*.md         -> <bóveda>/.claude/agents/
                 claude-code/skills/*/SKILL.md   -> <bóveda>/.claude/skills/*/SKILL.md
                 claude-code/rules/*.md          -> <bóveda>/.claude/rules/

Seguridad:
    - Nunca sobrescribe: si un archivo de destino ya existe, lo omite y lo informa.
    - Nunca borra nada.
    - --dry-run muestra lo que haría sin copiar.

Solo usa la biblioteca estándar de Python (3.10 o superior).
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def plan_opencode(vault: Path) -> list[tuple[Path, Path]]:
    src = REPO_ROOT / "opencode"
    pairs = [(src / "opencode.example.json", vault / "opencode.json")]
    for sub in ("agents", "commands", "instructions"):
        for f in sorted((src / sub).glob("*.md")):
            pairs.append((f, vault / ".opencode" / sub / f.name))
    return pairs


def plan_claude(vault: Path) -> list[tuple[Path, Path]]:
    src = REPO_ROOT / "claude-code"
    pairs = [
        (src / "CLAUDE.md.example", vault / "CLAUDE.md"),
        (src / "settings.example.json", vault / ".claude" / "settings.json"),
    ]
    for f in sorted((src / "agents").glob("*.md")):
        pairs.append((f, vault / ".claude" / "agents" / f.name))
    for f in sorted((src / "skills").glob("*/SKILL.md")):
        pairs.append((f, vault / ".claude" / "skills" / f.parent.name / "SKILL.md"))
    for f in sorted((src / "rules").glob("*.md")):
        pairs.append((f, vault / ".claude" / "rules" / f.name))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description="Instala la configuración de agentes en una bóveda.")
    parser.add_argument("--tool", required=True, choices=["opencode", "claude-code", "both"])
    parser.add_argument("--vault", required=True, help="Ruta de la bóveda (debe contener AGENTS.md).")
    parser.add_argument("--dry-run", action="store_true", help="Muestra lo que se haría sin copiar.")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"ERROR: la carpeta {vault} no existe.", file=sys.stderr)
        return 1
    if not (vault / "AGENTS.md").is_file():
        print(f"ERROR: {vault} no contiene AGENTS.md. ¿Es una bóveda creada desde vault-template?", file=sys.stderr)
        return 1

    pairs: list[tuple[Path, Path]] = []
    if args.tool in ("opencode", "both"):
        pairs += plan_opencode(vault)
    if args.tool in ("claude-code", "both"):
        pairs += plan_claude(vault)

    copied, skipped = 0, 0
    for src, dst in pairs:
        rel = dst.relative_to(vault)
        if dst.exists():
            print(f"OMITIDO (ya existe): {rel}")
            skipped += 1
            continue
        if args.dry_run:
            print(f"Se copiaría: {rel}")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"Copiado: {rel}")
        copied += 1

    verb = "por copiar" if args.dry_run else "copiados"
    print(f"\nResumen: {copied} archivos {verb}, {skipped} omitidos.")
    if skipped:
        print("Los archivos omitidos no se tocaron. Compáralos a mano si quieres actualizarlos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
