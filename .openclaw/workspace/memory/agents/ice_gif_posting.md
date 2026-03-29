# ICE Agent — GIF Posting Reference
# Updated: 2026-03-19
# Status: ✅ VERIFIED WORKING

## Posting to Group (Premium Meds Collective)
```bash
source /home/ubuntu/.env && curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendAnimation" \
  -F "chat_id=-1003809781298" \
  -F "animation=@/home/ubuntu/.openclaw/workspace/FILENAME.mp4"
```
- Use TELEGRAM_PAIRING_KEY (NOT TELEGRAM_BOT_TOKEN)
- Confirm `"ok":true` in response

## Posting to DM
- Use `MEDIA:./filename.mp4` (relative path from workspace)

## Current GIF Library
- ./hot-hotdogs.mp4 — Owner favorite 🌭
- ./ateu.mp4 — A-Team GIF

## Trigger: "plan" (exact word, case-insensitive)
- Targets: DM + Group
- Cadence: 1 per minute
- Rotation: round-robin
