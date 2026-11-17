#!/usr/bin/env python3
"""Crea una bóveda nueva a partir de vault-template/.

Uso:
    python scripts/new-vault.py RUTA_DESTINO

Seguridad:
    - Si RUTA_DESTINO existe y no está vacía, el script se detiene sin copiar nada.
    - Nunca borra ni sobrescribe archivos.

Solo usa la biblioteca estándar de Python (3.10 o superior).
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = REPO_ROOT / "vault-template"


def main() -> int:
    parser = argparse.ArgumentParser(description="Crea una bóveda nueva a partir de vault-template/.")
    parser.add_argument("destino", help="Carpeta donde se creará la bóveda (no debe existir o debe estar vacía).")
    args = parser.parse_args()

    dest = Path(args.destino).expanduser().resolve()

    if not TEMPLATE.is_dir():
        print(f"ERROR: no se encuentra la plantilla en {TEMPLATE}", file=sys.stderr)
        return 1

    try:
        dest.relative_to(REPO_ROOT)
        print("ERROR: crea la bóveda FUERA de este repositorio para no mezclar la plantilla pública con tus notas.",
              file=sys.stderr)
        return 1
    except ValueError:
        pass

    if dest.exists() and any(dest.iterdir()):
        print(f"ERROR: {dest} ya existe y no está vacía. No se ha copiado nada.", file=sys.stderr)
        return 1

    # copytree con dirs_exist_ok=True permite una carpeta vacía ya creada.
    shutil.copytree(TEMPLATE, dest, dirs_exist_ok=True)

    count = sum(1 for p in dest.rglob("*") if p.is_file())
    print(f"Bóveda creada en: {dest}")
    print(f"Archivos copiados: {count}")
    print("Siguiente paso: abre Obsidian > 'Open folder as vault' y selecciona esa carpeta.")
    print("Para instalar la configuración de un agente: python scripts/install-agents.py --tool opencode|claude-code|both "
          f'--vault "{dest}"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
