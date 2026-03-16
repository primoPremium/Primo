# OpenClaw Telegram Fix Notes
Date: 2026-02-22

## Problem
- Gateway crash-looping due to invalid config keys
- Telegram showing "Context overflow" on every message
- Auto-compaction failing with 402 (insufficient OpenRouter credits)

## Root Causes
1. `agents.defaults.agent` - unrecognized key in v2026.2.19-2, crashes gateway
2. `agents.defaults.compaction` - invalid schema in new version, crashes gateway
3. OpenRouter key had only ~184 tokens of credit, but compaction requested 8192
4. Old session file accumulated overflow/error history, poisoning future runs

## Fix Applied

### 1. Config keys removed
```json
del(.agents.defaults.agent)
del(.agents.defaults.compaction)
```

### 2. Model switched to free tier
```json
agents.defaults.model.primary = "openrouter/openrouter/free"
```

### 3. Session cleared
```bash
rm -f ~/.openclaw/agents/main/sessions/*.jsonl
```
Then sent /new in Telegram.

## If It Breaks Again
```bash
# Clear sessions and restart
rm -f ~/.openclaw/agents/main/sessions/*.jsonl
systemctl --user restart openclaw-gateway.service
# Then send /new in Telegram
```

## To Switch Back to Claude (when OpenRouter credits are topped up)
Edit ~/.openclaw/openclaw.json:
- agents.defaults.model.primary = "openrouter/anthropic/claude-3.5-sonnet"
- Update models.providers.openrouter.models accordingly

## Working Config (agents.defaults)
```json
{
  "model": { "primary": "openrouter/openrouter/free" },
  "workspace": "~/.openclaw/workspace",
  "models": {
    "openrouter/openrouter/free": {
      "params": { "maxTokens": 512 }
    }
  },
  "skipBootstrap": true,
  "bootstrapMaxChars": 2000
}
```
