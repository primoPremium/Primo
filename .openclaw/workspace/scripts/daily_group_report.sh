#!/usr/bin/env bash
# Daily Progress Report — Posts to Premium Meds Collective group at scheduled time
# Cron: 10:30 AM Pacific daily

set -eo pipefail

# Load only the vars we need (avoid unbound variable errors from other entries)
BOT_TOKEN=$(grep '^TELEGRAM_PAIRING_KEY=' /home/ubuntu/.env | head -1 | sed 's/^TELEGRAM_PAIRING_KEY=//;s/^"//;s/"$//')

CHAT_ID="-1003809781298"
DATE=$(TZ="America/Los_Angeles" date +"%Y-%m-%d")
TIME=$(TZ="America/Los_Angeles" date +"%I:%M %p %Z")
REPORT_DIR="/home/ubuntu/.openclaw/workspace/memory/competitor_analysis"
LATEST_REPORT="${REPORT_DIR}/${DATE}_weekly_report.md"
HERE_NOW_LINK="https://robust-mango-yzdq.here.now/"
LOG_FILE="/home/ubuntu/.openclaw/workspace/memory/logs/daily_report_posts.log"

mkdir -p "$(dirname "$LOG_FILE")"

MESSAGE="📊 Daily Progress Report (${DATE}) — ${TIME}

🔗 Live Report: ${HERE_NOW_LINK}

Status: ✅ On Track
Highlights:
• Top performers and their recent moves
• Pricing, promos, and product positioning shifts
• Content and channel strategies gaining traction
• Potential risks and opportunities for Premium Meds

Full archived report available on request.

🌿 \"Growing premium takes patience and precision.\" 🌾

— Primo, Marketing"

# Post to group
RESPONSE=$(curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg chat_id "$CHAT_ID" --arg text "$MESSAGE" '{chat_id: $chat_id, text: $text, link_preview_options: {is_disabled: true}}')")

# Log result
echo "[${DATE} ${TIME}] Response: ${RESPONSE}" >> "$LOG_FILE"

# Check success
if echo "$RESPONSE" | jq -e '.ok == true' > /dev/null 2>&1; then
  MSG_ID=$(echo "$RESPONSE" | jq -r '.result.message_id')
  echo "[${DATE} ${TIME}] SUCCESS — message_id: ${MSG_ID}" >> "$LOG_FILE"
else
  echo "[${DATE} ${TIME}] FAILED — ${RESPONSE}" >> "$LOG_FILE"
fi
