# AI agents

Pytdbot ships a skill and a local docs CLI so coding agents use bound methods, helpers, and TDLib types correctly.

1. Install Pytdbot
2. Point the agent at the skill:
    - In this repo: [`pytdbot/ai/SKILL.md`](https://github.com/pytdbot/client/blob/main/pytdbot/ai/SKILL.md)
    - Or: `curl -O "https://raw.githubusercontent.com/pytdbot/client/refs/heads/main/pytdbot/ai/SKILL.md"`
3. Register it the way your tool expects (project skill, agent rule, or “read this file first”)

## CLI

```bash
python -m pytdbot.docs search "send photo"
python -m pytdbot.docs function sendMessage getChat
python -m pytdbot.docs type message
python -m pytdbot.docs helper reply_text reply_photo
python -m pytdbot.docs stats
```

Same commands as `pytdbot-docs` after install. `--json` for machine-readable output.
