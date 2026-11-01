#!/usr/bin/env bash
# Muestra las reglas del clasificador del modo automático. Solo lee: no ejecuta critique ni reset.
set -euo pipefail
command -v claude > /dev/null || { echo "Falta claude: instala Claude Code primero" >&2; exit 1; }
claude --version

echo "== Reglas de fábrica (claude auto-mode defaults) =="
claude auto-mode defaults

echo "== Una regla concreta: Git Destructive =="
claude auto-mode defaults --label 'Git Destructive'

echo "== Lo que usa el clasificador: tus ajustes + los de fábrica (claude auto-mode config) =="
claude auto-mode config
