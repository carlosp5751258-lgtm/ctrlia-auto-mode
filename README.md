# Modo automático de Claude Code: clasificador y reglas

[Read in English](README.en.md)

Ajustes listos para copiar para el modo automático (auto mode) de Claude Code: enseñarle tu entorno, endurecer las reglas sin perder las de fábrica, pedir confirmación antes de cada push, empezar en Manual o quitarlo. Más un script que lista las reglas del clasificador y un comprobador que avisa si olvidaste `"$defaults"`.

La referencia completa (cómo decide cada acción, qué bloquea por defecto, `/auto-mode-setup`, límites de 3 y 20 bloqueos, coste) está en:

- Español: https://ctrlia.dev/recetas/auto-mode.html
- English: https://ctrlia.dev/en/recetas/auto-mode.html

## Qué incluye

| Archivo | Para qué | Dónde va |
| --- | --- | --- |
| `settings/entorno-y-reglas.json` | `autoMode.environment`, `soft_deny` y `hard_deny` conservando las reglas de fábrica con `"$defaults"` | `~/.claude/settings.json` |
| `settings/preguntar-antes-de-push.json` | Reglas ask para `git push` y `gh pr create`, sin salir de auto para lo demás | Cualquier settings |
| `settings/empezar-en-manual.json` | Empezar siempre en Manual (Shift+Tab sigue llevando a auto) | `~/.claude/settings.json` |
| `settings/desactivar-auto-mode.json` | Quitar el modo automático del todo | Configuración gestionada (organizaciones) |
| `settings/revisar-todo-shell.json` | Que el clasificador revise todo comando de shell y apagar `/auto-mode-setup` | `~/.claude/settings.json` |
| `inspeccionar.sh` | Lista las reglas de fábrica, la regla «Git Destructive» y lo que usa el clasificador. Solo lee | — |
| `comprobar_defaults.py` | Avisa (y sale con 1) si una lista de `autoMode` no lleva `"$defaults"` o si está en los settings de un proyecto | — |

## Cómo usarlo

```bash
git clone https://github.com/carlosp5751258-lgtm/ctrlia-auto-mode.git
cd ctrlia-auto-mode
./inspeccionar.sh | less
python3 comprobar_defaults.py            # revisa tu ~/.claude/settings.json
```

Para aplicar un ajuste, **mezcla** su bloque en tu `~/.claude/settings.json` (no sustituyas el archivo) y cambia `mi-org` y `mi-empresa.com` por los tuyos. Después, `claude auto-mode config` para comprobar que tus entradas están dentro.

Importante: `autoMode` y `"defaultMode": "auto"` se ignoran en `.claude/settings.json` y `.claude/settings.local.json` del proyecto. Y si escribes una lista sin `"$defaults"`, sustituyes toda la lista de fábrica (por ejemplo, un `hard_deny` sin `$defaults` elimina la regla de exfiltración de datos).

## Qué se probó

Con Claude Code **2.1.316** en Linux, con `CLAUDE_CONFIG_DIR` temporal: `inspeccionar.sh` lista 16 allow, 72 soft_deny, 1 hard_deny y 21 entradas de entorno. `comprobar_defaults.py` tiene tests (`python3 -m unittest test_comprobar_defaults`) y se probó con todos los JSON de `settings/` (todos OK), con un `soft_deny` sin `$defaults` en un settings de proyecto (dos avisos, salida 1), con JSON roto (salida 2) y sin archivo (salida 0). No se ejecutaron `/auto-mode-setup`, `claude auto-mode critique` ni `reset`, porque escriben en la configuración o consumen el plan.

## Licencia

MIT. Ver [LICENSE](LICENSE).

---
Parte de **[Ctrl+IA](https://ctrlia.dev/)**: programa con Claude Code como un pro, en español. Hecho por Carlos P.
