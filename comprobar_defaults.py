#!/usr/bin/env python3
"""Avisa si un bloque autoMode sustituye las reglas de fábrica por olvidar "$defaults".

Uso: python3 comprobar_defaults.py [ruta/settings.json]   (por defecto ~/.claude/settings.json)
Sale con 1 si alguna lista de autoMode no lleva "$defaults". Solo lee el archivo.
"""
import json
import os
import sys

LISTAS = ("environment", "allow", "soft_deny", "hard_deny")


def problemas(settings):
    """Lista de avisos para un settings.json ya cargado."""
    auto = settings.get("autoMode") or {}
    return [f'autoMode.{k} no incluye "$defaults": sustituye TODA la lista de fábrica'
            for k in LISTAS if isinstance(auto.get(k), list) and "$defaults" not in auto[k]]


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/.claude/settings.json")
    try:
        with open(ruta, encoding="utf-8") as f:
            settings = json.load(f)
    except FileNotFoundError:
        print(f"No existe {ruta}: no hay autoMode que revisar.")
        return 0
    except json.JSONDecodeError as err:
        print(f"{ruta} no es JSON válido: {err}", file=sys.stderr)
        return 2
    avisos = problemas(settings)
    for a in avisos:
        print(f"AVISO: {a}")
    if not avisos:
        print(f'OK: {ruta} no sustituye ninguna lista de fábrica (o no tiene autoMode).')
    # El clasificador ignora autoMode en los settings del proyecto
    if "autoMode" in settings and os.path.normpath(ruta).replace("\\", "/").endswith((".claude/settings.json", ".claude/settings.local.json")) \
            and os.path.dirname(os.path.abspath(ruta)) != os.path.expanduser("~/.claude"):
        print("AVISO: autoMode en los settings de un proyecto se ignora; ponlo en ~/.claude/settings.json.")
    return 1 if avisos else 0


if __name__ == "__main__":
    sys.exit(main())
