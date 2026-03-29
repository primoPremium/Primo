#!/bin/bash
# Hourly Chuck Norris Content Poster Clone
# This script is an exact clone of the working Chuck Norris GIF poster functionality,
# designed to run independently as a separate hourly task.

set -euo pipefail

WORKSPACE="/home/ubuntu/.openclaw/workspace"
# Using dedicated paths for this cloned task to ensure isolation
LOG_FILE="$WORKSPACE/memory/hourly_posts/clone_poster_log.txt"
INDEX_FILE="$WORKSPACE/memory/hourly_posts/clone_current_index.txt"
USED_FILE="$WORKSPACE/memory/hourly_posts/clone_used_indices.txt"
CHAT_ID="-1003809781298" # Premium Meds Collective Group

# Ensure directories for logs and index files exist
mkdir -p "$(dirname "$LOG_FILE")"
mkdir -p "$(dirname "$INDEX_FILE")"
mkdir -p "$(dirname "$USED_FILE")"

# Source Telegram bot token
TELEGRAM_PAIRING_KEY=$(grep '^TELEGRAM_PAIRING_KEY=' /home/ubuntu/.env | head -1 | sed 's/^TELEGRAM_PAIRING_KEY=//' | tr -d '"')

if [ -z "$TELEGRAM_PAIRING_KEY" ]; then
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] ❌ TELEGRAM_PAIRING_KEY not found" >> "$LOG_FILE"
  exit 1
fi

# Function to escape MarkdownV2 special characters for Telegram
escape_markdownv2() {
    local text="$1" # Use local variable
    echo "$text" | sed \
        -e 's/\\/\\\\/g' \
        -e 's/"/\\"/g' \
        -e 's/\$/\\$/g' \
        -e 's/#/\\#/g' \
        -e 's/\* /\\* /g' \
        -e 's/\- /\\- /g' \
        -e 's/\./\\./g' \
        -e 's/!/\\!/g' \
        -e 's/\[/\\\[/g' \
        -e 's/\]/\\]/g' \
        -e 's/(/\\(/g' \
        -e 's/)/\\)/g' \
        -e 's/~/\~/g' \
        -e 's/`/\\`/g' \
        -e 's/>/\\>/g'
}

# --- Content Data (Mimicking Chuck Norris Poster) ---
# Exactly replicating the GIF links and joke API structure from the working script.
GIF_LINKS=(
  "https://media.giphy.com/media/BIuuwHRNKs15C/giphy.gif"
  "https://media.giphy.com/media/pHHEGxLBh8wFy/giphy.gif"
  "https://media.giphy.com/media/3o6Mbm6G6X9Xl8Wp5m/giphy.gif"
  "https://media.giphy.com/media/vaWd6xDKtLL5S/giphy.gif"
  "https://media.giphy.com/media/l1J3nY7N7LBrBobVm/giphy.gif"
  "https://media.giphy.com/media/WNuF3KK9NaQ8w/giphy.gif"
  "https://media.giphy.com/media/4Z3DdOZRTcXPa/giphy.gif"
  "https://media.giphy.com/media/UvdC8pXudeEak/giphy.gif"
  "https://media.giphy.com/media/l1J3G5lf06vi58EIE/giphy.gif"
  "https://media.giphy.com/media/13fR00PIYwb7Gg/giphy.gif"
  "https://media.giphy.com/media/T9sIxZs1X3LhK/giphy.gif"
  "https://media.giphy.com/media/6Od5syJe53FaqJtxFn/giphy.gif"
)
TOTAL=${#GIF_LINKS[@]}

# --- Index Management ---
# Read current index, initialize if missing.
if [ ! -f "$INDEX_FILE" ]; then echo "0" > "$INDEX_FILE"; fi
IDX=$(cat "$INDEX_FILE" | tr -d '[:space:]')

# Validate index, reset if out of bounds.
if ! [[ "$IDX" =~ ^[0-9]+$ ]] || [ "$IDX" -ge "$TOTAL" ]; then
  IDX=0
fi

GIF_URL="${GIF_LINKS[$IDX]}"

# --- Content Fetching ---
# Fetch a random Chuck Norris joke from the API, with a fallback.
JOKE=$(curl -sf --max-time 10 "https://api.chucknorris.io/jokes/random" | python3 -c "import sys,json; print(json.load(sys.stdin)['value'])" 2>/dev/null)
if [ -z "$JOKE" ]; then JOKE="Chuck Norris counted to infinity. Twice."; fi

CAPTION="🤠 $JOKE"

# --- Send Content to Telegram ---
RESPONSE=$(curl -s --max-time 30 -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendAnimation" \
  --data-urlencode "chat_id=${CHAT_ID}" \
  --data-urlencode "animation=${GIF_URL}" \
  --data-urlencode "caption=${CAPTION}" \
  2>&1)

OK=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ok',False))" 2>/dev/null || echo "False")

NOW=$(TZ="America/Los_Angeles" date '+%Y-%m-%d %I:%M %p %Z')

if [ "$OK" = "True" ]; then
  echo "[$NOW] ✅ Posted content ${RND_IDX} — $GIF_URL" >> "$LOG_FILE"
  # Mark as used (this logic pertains to random selection; for hourly, it might be less critical if always cycling)
  echo "$RND_IDX" >> "$USED_FILE"
else
  echo "[$NOW] ❌ FAILED content ${RND_IDX} — $RESPONSE" >> "$LOG_FILE"
fi

# --- Advance Index ---
# Advance index, wrapping around for the next run.
NEXT_IDX=$(( (IDX + 1) % TOTAL ))
echo "$NEXT_IDX" > "$INDEX_FILE"
