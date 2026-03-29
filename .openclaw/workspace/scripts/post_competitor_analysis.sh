#!/bin/bash
# Daily Competitor Analysis Digest Poster
# Finds the latest competitor analysis report, builds a digest + summary, and posts to the group
# Runs daily at 7:00 PM PST via cron

WORKSPACE="/home/ubuntu/.openclaw/workspace"
LOG_FILE="$WORKSPACE/memory/competitor_analysis/post_log.txt"
CHAT_ID="-1003809781298"
REPORT_DIR="$WORKSPACE/memory/competitor_analysis"

mkdir -p "$(dirname "$LOG_FILE")"

# Extract token
TELEGRAM_PAIRING_KEY=$(grep '^TELEGRAM_PAIRING_KEY=' /home/ubuntu/.env | head -1 | sed 's/^TELEGRAM_PAIRING_KEY=//' | tr -d '"')

if [ -z "$TELEGRAM_PAIRING_KEY" ]; then
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] FAIL: No token" >> "$LOG_FILE"
  exit 1
fi

# Find the latest report file
LATEST_REPORT=$(ls -t "$REPORT_DIR"/*_weekly_report.md 2>/dev/null | head -1)

if [ -z "$LATEST_REPORT" ]; then
  LATEST_REPORT="none"
fi

# Build the message
TODAY=$(TZ="America/Los_Angeles" date '+%Y-%m-%d')

if [ "$LATEST_REPORT" != "none" ] && [ -f "$LATEST_REPORT" ]; then
  REPORT_DATE=$(basename "$LATEST_REPORT" | sed 's/_weekly_report.md//')
  REPORT_REF="memory/competitor_analysis/$(basename "$LATEST_REPORT")"

  # Extract summary line (first non-header, non-blank line after Scope/Executive)
  SUMMARY=$(grep -A2 "Executive Summary\|Scope:" "$LATEST_REPORT" | grep "^- \|^[A-Z]" | head -1)
  if [ -z "$SUMMARY" ]; then
    SUMMARY="OC delivery competitors reviewed. See full report for details."
  fi

  # Extract bullet highlights
  HIGHLIGHTS=$(grep "^- " "$LATEST_REPORT" | head -6 | sed 's/^- /• /')
  if [ -z "$HIGHLIGHTS" ]; then
    HIGHLIGHTS="• Report available — see full file for details"
  fi

  # Extract recommended actions
  ACTIONS=""
  IN_ACTIONS=false
  while IFS= read -r line; do
    if echo "$line" | grep -qi "Recommended Actions"; then
      IN_ACTIONS=true
      continue
    fi
    if [ "$IN_ACTIONS" = true ]; then
      if echo "$line" | grep -q "^- "; then
        ACTIONS="$ACTIONS
$(echo "$line" | sed 's/^- /• /')"
      elif echo "$line" | grep -q "^#\|^$" && [ -n "$ACTIONS" ]; then
        break
      fi
    fi
  done < "$LATEST_REPORT"

  if [ -z "$ACTIONS" ]; then
    ACTIONS="• See full report for recommended actions"
  fi

  MSG="📊 Competitor Analysis Report — OC Cannabis Market ($REPORT_DATE)

$SUMMARY

Key findings:
$HIGHLIGHTS

Recommended actions for Premium Meds:
$ACTIONS

Full report: $REPORT_REF

🌿 \"Know thy competitor, grow thy harvest.\" 🌾

— Primo, Marketing & Advertising Director"

else
  MSG="📊 Competitor Analysis Report — $TODAY

No new competitor analysis report found for today. Latest data may be pending.

Full report available on request.

🌿 \"Know thy competitor, grow thy harvest.\" 🌾

— Primo, Marketing & Advertising Director"
fi

# Post to group
RESPONSE=$(curl -s --max-time 30 -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendMessage" \
  --data-urlencode "chat_id=${CHAT_ID}" \
  --data-urlencode "text=${MSG}" \
  2>&1)

OK=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ok',False))" 2>/dev/null || echo "False")

TIMESTAMP=$(TZ="America/Los_Angeles" date '+%Y-%m-%d %I:%M %p %Z')

if [ "$OK" = "True" ]; then
  echo "[$TIMESTAMP] ✅ Competitor analysis digest posted to group" >> "$LOG_FILE"
else
  echo "[$TIMESTAMP] ❌ FAILED — $RESPONSE" >> "$LOG_FILE"
fi
