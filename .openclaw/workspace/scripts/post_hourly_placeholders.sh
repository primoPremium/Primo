#!/bin/bash
# Hourly Placeholder Content Poster
# Posts rotating content from a predefined list with dynamic fetching and direct Telegram posting.
# This script is a direct replica of the working Chuck Norris GIF poster functionality.

set -euo pipefail

WORKSPACE="/home/ubuntu/.openclaw/workspace"
LOG_FILE="$WORKSPACE/memory/hourly_posts/poster_log.txt"
CHAT_ID="-1003809781298" # Premium Meds Collective Group
INDEX_FILE="$WORKSPACE/memory/hourly_posts/current_index.txt"
GIF_LIST_FILE="$WORKSPACE/memory/hourly_posts/content_items.txt" # To store placeholders if needed, or use inline

# Ensure log and index directories exist
mkdir -p "$(dirname "$LOG_FILE")"
mkdir -p "$(dirname "$INDEX_FILE")"
mkdir -p "$(dirname "$GIF_LIST_FILE")"

# --- Configuration for Content ---
# NOTE: This section conceptually replaces the Chuck Norris specific data.
# For a direct clone of functionality posting Chuck Norris GIFs and jokes,
# we would use the actual Chuck Norris URLs and joke API.
# If the intent is to post *different* content, this part would change.
# Per instructions: "posts a Chuck Norris gif and joke every hour on the hour."
# So, we are replicating that functionality exactly.

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
# Using the exact same GIF links and joke API structure for replication.
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
# Read current index (default 0), initialize if missing.
if [ ! -f "$INDEX_FILE" ]; then
  echo "0" > "$INDEX_FILE"
fi
IDX=$(cat "$INDEX_FILE" | tr -d '[:space:]')

# Validate index, reset if out of bounds.
if ! [[ "$IDX" =~ ^[0-9]+$ ]] || [ "$IDX" -ge "$TOTAL" ]; then
  IDX=0
fi

GIF_URL="${GIF_LINKS[$IDX]}"

# --- Content Fetching ---
# Fetch a random Chuck Norris joke from the API, with a fallback.
JOKE=$(curl -sf --max-time 10 "https://api.chucknorris.io/jokes/random" | python3 -c "import sys,json; print(json.load(sys.stdin)['value'])" 2>/dev/null)
if [ -z "$JOKE" ]; then
  JOKE="Chuck Norris counted to infinity. Twice."
fi

# --- Prepare Message ---
CAPTION="🤠 $JOKE" # Using the same caption structure

# --- Send Content to Telegram ---
RESPONSE=$(curl -s --max-i timeout 30 -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendAnimation" \
  --data-urlencode "chat_id=${CHAT_ID}" \
  --data-urlencode "animation=${GIF_URL}" \
  --data-urlencode "caption=${CAPTION}" \
  2>&1)

OK=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ok',False))" 2>/dev/null || echo "False")

NOW=$(TZ="America/Los_Angeles" date '+%Y-%m-%d %I:%M %p %Z')

if [ "$OK" = "True" ]; then
  echo "[$NOW] ✅ Posted content #$IDX — $GIF_URL" >> "$LOG_FILE"
else
  echo "[$NOW] ❌ FAILED content #$IDX — $RESPONSE" >> "$LOG_FILE"
fi

# --- Advance Index ---
# Advance index (wrap around) for the next run.
NEXT_IDX=$(( (IDX + 1) % TOTAL ))
echo "$NEXT_IDX" > "$INDEX_FILE"

# --- Cleanup (optional) ---
# No explicit cleanup needed for this simple script beyond log rotation if implemented elsewhere.
