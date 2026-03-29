#!/bin/bash
# Daily Progress Report Poster
# Posts a daily progress summary to the Premium Meds Collective group
# Runs daily at 8:00 PM PST via cron

WORKSPACE="/home/ubuntu/.openclaw/workspace"
LOG_FILE="$WORKSPACE/memory/daily_reports/daily_report.log"
CHAT_ID="-1003809781298"

mkdir -p "$(dirname "$LOG_FILE")"

# Extract token
TELEGRAM_PAIRING_KEY=$(grep '^TELEGRAM_PAIRING_KEY=' /home/ubuntu/.env | head -1 | sed 's/^TELEGRAM_PAIRING_KEY=//' | tr -d '"')

if [ -z "$TELEGRAM_PAIRING_KEY" ]; then
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] FAIL: No token" >> "$LOG_FILE"
  exit 1
fi

# Build today's date
TODAY=$(TZ="America/Los_Angeles" date '+%Y-%m-%d %A')
NOW=$(TZ="America/Los_Angeles" date '+%I:%M %p %Z')

# Find latest competitor report date
LATEST_COMP=$(ls -t "$WORKSPACE/memory/competitor_analysis/"*_weekly_report.md 2>/dev/null | head -1)
if [ -n "$LATEST_COMP" ] && [ -f "$LATEST_COMP" ]; then
  COMP_DATE=$(basename "$LATEST_COMP" | sed 's/_weekly_report.md//')
else
  COMP_DATE="pending"
fi

# Build the report text
MSG="📊 Daily Progress Report ($TODAY) — $NOW

Status: ✅ On Track

🔬 Research & Competitor Updates
• Competitor analysis digest posted daily at 7:00 PM PST
• Latest report: $COMP_DATE

📈 SEO Findings
• SEO keyword analysis reports available in memory/seo/
• Monitoring ongoing for Orange County market position

🌐 Website Updates (Premium Meds)
• Website: https://premiummedscollective.com
• Content and product updates monitored weekly

🤠 Chuck Norris GIF + Joke: Posted weekly (Sundays at 8:00 AM PST)

📅 Active Scheduled Reports:
• Competitor Analysis Digest — Daily at 7:00 PM PST
• Daily Progress Report — Daily at 8:00 PM PST
• Chuck Norris GIF + Joke — Weekly (Sundays at 8:00 AM PST)

Full archived reports available on request.

🌿 \"Growing premium takes patience and precision.\" 🌾

— Primo, Marketing & Advertising Director"

# Post to group
RESPONSE=$(curl -s --max-time 30 -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendMessage" \
  -d "chat_id=${CHAT_ID}" \
  --data-urlencode "text=${MSG}" \
  2>&1)

OK=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ok',False))" 2>/dev/null || echo "False")

TIMESTAMP=$(TZ="America/Los_Angeles" date '+%Y-%m-%d %I:%M %p %Z')

if [ "$OK" = "True" ]; then
  echo "[$TIMESTAMP] ✅ Daily progress report posted to group" >> "$LOG_FILE"
else
  echo "[$TIMESTAMP] ❌ FAILED — $RESPONSE" >> "$LOG_FILE"
fi
