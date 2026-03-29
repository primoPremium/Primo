# GIF/Video Posting Method — Telegram
# Documented: 2026-03-19
# Status: ✅ VERIFIED WORKING

## The WORKING Method (use this EVERY time)

### Posting to DM (this chat session)
1. Copy media to workspace: `cp /source/file.mp4 /home/ubuntu/.openclaw/workspace/file.mp4`
2. Post with: `MEDIA:./file.mp4`
3. Use ONLY relative paths (./file.mp4) — absolute and ~ paths are blocked

### Posting to Group (Premium Meds Collective)
1. Copy media to workspace (if not already there)
2. Use Telegram Bot API with TELEGRAM_PAIRING_KEY:
```bash
source /home/ubuntu/.env && curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendAnimation" \
  -F "chat_id=-1003809781298" \
  -F "animation=@/home/ubuntu/.openclaw/workspace/filename.mp4"
```
3. For GIF with caption, add: `-F "caption=Your caption here"`
4. Confirm `"ok":true` in API response

### Key Details
- Bot: Primo (@Primo_premium_bot)
- Group chat_id: -1003809781298
- Credential: TELEGRAM_PAIRING_KEY (stored in /home/ubuntu/.env)
- NEVER use TELEGRAM_BOT_TOKEN — it doesn't exist; always use TELEGRAM_PAIRING_KEY
- Always `source /home/ubuntu/.env` before API calls
- Owner has authorized automatic token refresh — never block on credential issues

## GIF Library Assets (workspace copies)
- ./hot-hotdogs.mp4 — Owner's favorite (hot dog GIF) 🌭
- ./ateu.mp4 — A-Team "plan" GIF

## Trigger Rule: "plan"
- Keyword: exact word "plan" (case-insensitive)
- Targets: DM + Group
- Cadence: 1 GIF per minute max
- Rotation: round-robin through library
- No caption needed unless specified

## Lesson Learned
- MEDIA:./file.mp4 only works for the current session (DM)
- Group posting REQUIRES the Telegram Bot API with sendAnimation endpoint
- Always verify with `"ok":true` in response before reporting success
