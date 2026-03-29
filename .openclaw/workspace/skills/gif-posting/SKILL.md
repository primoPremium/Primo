# GIF Posting Skill

## Purpose
Post GIFs/animations from the media library to Telegram DMs or groups without requiring FFmpeg or any conversion tools.

## Key Insight
Telegram natively renders `.mp4` files as GIFs/animations. No conversion to `.gif` format is needed. Simply post the `.mp4` file using the `MEDIA:` directive and Telegram handles the rest.

## How It Works

### DM Posting (Current Chat)
Use the `MEDIA:` inline directive with a **relative path** from the workspace:
```
MEDIA:./hot-hotdogs.mp4
```
- Path must be relative to `/home/ubuntu/.openclaw/workspace/`
- Do NOT use absolute paths or `~` paths — they are blocked
- Telegram auto-plays `.mp4` files as looping animations (GIF behavior)

### Group Posting (Telegram Bot API)
Use the `exec` tool to call the Telegram Bot API `sendAnimation` endpoint:
```bash
source /home/ubuntu/.env && curl -s -X POST \
  "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendAnimation" \
  -F "chat_id=-1003809781298" \
  -F "animation=@/home/ubuntu/.openclaw/workspace/hot-hotdogs.mp4" \
  -F "caption=Your caption here"
```
- Use `sendAnimation` (not `sendVideo` or `sendDocument`) for GIF behavior
- Check response for `{"ok":true}` before confirming delivery
- Omit `-F "caption=..."` for no caption

## GIF Library
All available GIFs are cataloged in:
```
memory/graphics/gif_library.md
```
Each entry includes:
- `id`: unique identifier
- `label`: human-readable name
- `type`: mime type (video/mp4 or image/gif)
- `local_path`: path to the file on disk
- `url`: remote URL (for image/gif types)
- `captions`: array of caption options
- `trigger`: keyword trigger (if any)

## Workspace Assets
Pre-staged mp4 files ready for immediate posting:
- `./hot-hotdogs.mp4` — Hot hotdogs animation (owner favorite)
- `./ateu.mp4` — ATEU animation

## Rules
- Max 1 GIF per minute (rate limit)
- Round-robin rotation when triggered by keywords
- No FFmpeg or conversion tools required
- `.mp4` files ARE the GIFs — Telegram handles rendering

## For Agents: Cathy & ICE
1. Read the GIF library at `memory/graphics/gif_library.md`
2. To post in DM: `MEDIA:./filename.mp4` with optional caption text
3. To post in group: use `exec` with `sendAnimation` API call (see above)
4. Always check that the file exists in workspace before posting
5. For URL-based GIFs (image/gif type), use `MEDIA:https://url` for DMs or pass the URL to the API

## Troubleshooting
- **"File not found"**: Check the file exists at the expected workspace path
- **"FFmpeg not found"**: You don't need FFmpeg. Post the .mp4 directly.
- **"Blocked path"**: Use relative paths (`./file.mp4`), never absolute or `~` paths
- **API returns `{"ok":false}`**: Verify TELEGRAM_PAIRING_KEY is set in ~/.env and chat_id is correct
