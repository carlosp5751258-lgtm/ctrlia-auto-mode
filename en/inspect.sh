#!/usr/bin/env bash
# Shows the auto mode classifier rules. Read-only: does not run critique or reset.
set -euo pipefail
command -v claude > /dev/null || { echo "claude is missing: install Claude Code first" >&2; exit 1; }
claude --version

echo "== Built-in rules (claude auto-mode defaults) =="
claude auto-mode defaults

echo "== One specific rule: Git Destructive =="
claude auto-mode defaults --label 'Git Destructive'

echo "== What the classifier uses: your settings + the built-in ones (claude auto-mode config) =="
claude auto-mode config
