# Claude Code auto mode: the classifier and its rules

[Leer en español](README.md)

The Spanish version is in the repository root and in [README.md](README.md); the English files are in `en/`.

Ready-to-copy settings for Claude Code's auto mode: teach it your environment, tighten the rules without losing the built-in ones, ask before every push, start in Manual or remove it. Plus a script that lists the classifier's rules and a checker that warns if you forgot `"$defaults"`.

The full reference (how it decides each action, what it blocks by default, `/auto-mode-setup`, the 3 and 20 block limits, cost) is at:

- English: https://ctrlia.dev/en/recetas/auto-mode.html
- Español: https://ctrlia.dev/recetas/auto-mode.html

## What's included

| File | What for | Where it goes |
| --- | --- | --- |
| `en/settings/environment-and-rules.json` | `autoMode.environment`, `soft_deny` and `hard_deny`, keeping the built-in rules with `"$defaults"` | `~/.claude/settings.json` |
| `en/settings/ask-before-push.json` | Ask rules for `git push` and `gh pr create`, staying in auto for everything else | Any settings file |
| `en/settings/start-in-manual.json` | Always start in Manual (Shift+Tab still takes you to auto) | `~/.claude/settings.json` |
| `en/settings/disable-auto-mode.json` | Remove auto mode entirely | Managed settings (organizations) |
| `en/settings/review-all-shell.json` | Have the classifier review every shell command and turn off `/auto-mode-setup` | `~/.claude/settings.json` |
| `en/inspect.sh` | Lists the built-in rules, the "Git Destructive" rule and what the classifier uses. Read-only | — |
| `en/check_defaults.py` | Warns (and exits with 1) if an `autoMode` list lacks `"$defaults"` or sits in a project's settings | — |

## How to use it

```bash
git clone https://github.com/carlosp5751258-lgtm/ctrlia-auto-mode.git
cd ctrlia-auto-mode/en
./inspect.sh | less
python3 check_defaults.py                 # checks your ~/.claude/settings.json
```

To apply a setting, **merge** its block into your `~/.claude/settings.json` (don't replace the file) and change `my-org` and `my-company.com` to yours. Then run `claude auto-mode config` to check your entries are in.

Important: `autoMode` and `"defaultMode": "auto"` are ignored in the project's `.claude/settings.json` and `.claude/settings.local.json`. And if you write a list without `"$defaults"`, you replace the whole built-in list (for example, a `hard_deny` without `$defaults` removes the data exfiltration rule).

## What was tested

With Claude Code **2.1.316** on Linux, with a temporary `CLAUDE_CONFIG_DIR`: `en/inspect.sh` lists 16 allow, 72 soft_deny, 1 hard_deny and 21 environment entries. `en/check_defaults.py` has tests (`cd en && python3 -m unittest test_check_defaults`) and was run against every JSON in `en/settings/` (all OK), a `soft_deny` without `$defaults` in a project settings file (two warnings, exit 1), broken JSON (exit 2) and a missing file (exit 0). `/auto-mode-setup`, `claude auto-mode critique` and `reset` weren't run, because they write to the settings or use your plan.

## License

MIT. See [LICENSE](LICENSE).

---
Part of **[Ctrl+IA](https://ctrlia.dev/)**: code with Claude Code like a pro. Made by Carlos P.
