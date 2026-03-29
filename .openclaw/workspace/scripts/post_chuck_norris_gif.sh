#!/bin/bash
# Chuck Norris Hourly GIF + Joke Poster (mixed GIFs)
# Posts a rotating GIF with a random Chuck Norris joke to Premium Meds Collective group

WORKSPACE="/home/ubuntu/.openclaw/workspace"
INDEX_FILE="/home/ubuntu/.openclaw/workspace/memory/chuck-norris/current_index.txt"
LOG_FILE="/home/ubuntu/.openclaw/workspace/memory/chuck-norris/post_log.txt"
USED_FILE="/home/ubuntu/.openclaw/workspace/memory/chuck-norris/used_indices.txt"
CHAT_ID="-1003809781298"

# Extract only the token we need (avoid sourcing the full .env which has problematic vars)
TELEGRAM_PAIRING_KEY=$(grep '^TELEGRAM_PAIRING_KEY=' /home/ubuntu/.env | head -1 | sed 's/^TELEGRAM_PAIRING_KEY=//' | tr -d '"')

if [ -z "$TELEGRAM_PAIRING_KEY" ]; then
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] ❌ TELEGRAM_PAIRING_KEY not found" >> "$LOG_FILE"
  exit 1
fi

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

# Initialize index files if missing
if [ ! -f "$INDEX_FILE" ]; then echo "0" > "$INDEX_FILE"; fi
if [ ! -f "$USED_FILE" ]; then touch "$USED_FILE"; fi

# Build a list of used indices
USED_COUNT=$(wc -l < "$USED_FILE" 2>/dev/null || echo 0)

# Determine a random unused index
UNUSED=()
for i in $(seq 0 $((TOTAL-1))); do
  if ! grep -qx "$i" "$USED_FILE"; then UNUSED+=($i); fi
done

if [ ${#UNUSED[@]} -eq 0 ]; then
  # Reset used list and choose a fresh random index
  > "$USED_FILE"
  for i in $(seq 0 $((TOTAL-1))); do
    UNUSED+=($i)
  done
fi

# Pick a random unused index
RND_IDX=${UNUSED[$RANDOM % ${#UNUSED[@]}]}
GIF_URL="${GIF_LINKS[$RND_IDX]}"

# Fetch a random Chuck Norris joke
JOKE=$(curl -sf --max-time 10 "https://api.chucknorris.io/jokes/random" | python3 -c "import sys,json; print(json.load(sys.stdin)['value'])" 2>/dev/null)
if [ -z "$JOKE" ]; then JOKE="Chuck Norris counted to infinity. Twice."; fi

CAPTION="🤠 $JOKE"

# Send GIF + joke to the group via sendAnimation
RESPONSE=$(curl -s --max-time 30 -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendAnimation" \
  --data-urlencode "chat_id=${CHAT_ID}" \
  --data-urlencode "animation=${GIF_URL}" \
  --data-urlencode "caption=${CAPTION}" \
  2>&1)

OK=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ok',False))" 2>/dev/null || echo "False")

NOW=$(TZ="America/Los_Angeles" date '+%Y-%m-%d %I:%M %p %Z')

if [ "$OK" = "True" ]; then
  echo "[$NOW] ✅ Posted GIF ${RND_IDX} — $GIF_URL" >> "$LOG_FILE"
  # mark as used
  echo "$RND_IDX" >> "$USED_FILE"
else
  echo "[$NOW] ❌ FAILED GIF ${RND_IDX} — $RESPONSE" >> "$LOG_FILE"
fi

# Update index file for reference (optional)
NEXT_IDX=$(( (RND_IDX + 1) % TOTAL ))
echo "$NEXT_IDX" > "$INDEX_FILE" 
