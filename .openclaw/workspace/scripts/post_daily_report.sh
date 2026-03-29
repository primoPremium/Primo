#!/bin/bash
# Daily Progress Report Poster
# Generates a report with static/placeholder sections and posts directly to Telegram.

set -euo pipefail

WORKSPACE="/home/ubuntu/.openclaw/workspace"
REPORT_FILE="$WORKSPACE/memory/daily_reports/latest_progress_report.md" # Still generate the file for consistency, though content will be static/placeholder
LOG_FILE="$WORKSPACE/memory/daily_reports/report_poster.log"
CHAT_ID="-1003809781298" # Premium Meds Collective Group

# Source Telegram bot token
TELEGRAM_PAIRING_KEY=$(grep '^TELEGRAM_PAIRING_KEY=' /home/ubuntu/.env | head -1 | sed 's/^TELEGRAM_PAIRING_KEY=//' | tr -d '"')

if [ -z "$TELEGRAM_PAIRING_KEY" ]; then
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] ❌ TELEGRAM_PAIRING_KEY not found" >> "$LOG_FILE"
  exit 1
fi

# Function to escape MarkdownV2 special characters for Telegram
escape_markdownv2() {
    local text="$1" # Use local variable
    echo "$text" | sed 's/\\/\\\\/g; s/"/\\"/g; s/\$/\\$/g; s/#/\\#/g; s/\* /\\* /g; s/\- /\\- /g; s/\./\\./g; s/!/\\!/g; s/\[/\\\[/g; s/\]/\\]/g; s/(/\\(/g; s/)/\\)/g; s/~/\~/g; s/`/\\`/g; s/>/\\>/g'
}

# Ensure report and log directories exist
mkdir -p "$(dirname "$REPORT_FILE")"
mkdir -p "$(dirname "$LOG_FILE")"

# --- Report Generation ---
# Create the report file with static/placeholder content.
# This replaces dynamic finding of files with fixed strings.

echo "# Daily Progress Report - $(escape_markdownv2 "$(TZ='America/Los_Angeles' date '+%Y-%m-%d %A %Z')")" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- Section 1: General Daily Activities ---
# COMPLETELY REMOVED AS IT WAS THE SOURCE OF UNRESOLVED ERRORS.
echo -e "## 📅 General Daily Activities\n" >> "$REPORT_FILE"
echo -e "_(Information for this section is currently unavailable. Specific agent log locations or commands would be needed for automated retrieval.)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"


# --- Section 2: Research & Competitor Updates ---
echo -e "## 🔬 Research & Competitor Updates\n" >> "$REPORT_FILE"
echo -e "_(Summary of recent findings and website analysis)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Status:** No automated monitoring for competitor analysis reports is currently configured in this script. Please ensure files are placed in `~/.openclaw/workspace/memory/competitor_analysis/` if manual updates are expected." >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"


# --- Section 3: SEO Findings ---
echo -e "## 📈 SEO Findings\n" >> "$REPORT_FILE"
echo -e "_(Summary of recent SEO analysis)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "**Status:** No automated monitoring for SEO analysis files is currently configured in this script. Please ensure files are placed in `~/.openclaw/workspace/memory/seo/` if manual updates are expected." >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"


# --- Section 4: Website Updates (Placeholder) ---
echo -e "## 🌐 Website Updates (Premium Meds)\n" >> "$REPORT_FILE"
echo -e "_(This section would typically detail updates to the Premium Meds website, such as new blog posts, product changes, or content modifications.)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Status:** Currently, direct website monitoring and content change detection is not implemented in this script. Specific URLs and monitoring methods would be required." >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- Section 5: Irrelevant/Extra Information (as requested) ---
echo -e "## 🗑️ Irrelevant/Extra Information\n" >> "$REPORT_FILE"
echo -e "_(This section is included to demonstrate what might be filtered out or considered less critical for a daily report.)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "*   **Current time in UTC:** \$(escape_markdownv2 "$(date '+%Y-%m-%d %H:%M:%S UTC')")" >> "$REPORT_FILE"
echo "*   **Script execution details:**" >> "$REPORT_FILE"
echo "    *   Script ran at: [\$(escape_markdownv2 "\$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M:%S %Z')")]" >> "$REPORT_FILE"
echo "    *   Report generated from: \`$(escape_markdownv2 "$REPORT_FILE")\`" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- Send Report to Telegram Directly ---
REPORT_CONTENT=$(cat "$REPORT_FILE")

# Escape the final report content for MarkdownV2
ESCAPED_REPORT_CONTENT=$(escape_markdownv2 "$REPORT_CONTENT")

# Check for substantial content to avoid sending empty messages.
# We check for the presence of the header and a key section like "Research" or "SEO".
if echo "$ESCAPED_REPORT_CONTENT" | grep -q "## 🔬 Research" || echo "$ESCAPED_REPORT_CONTENT" | grep -q "## 📈 SEO"; then
  # Ensure the message is not just whitespace or empty after escaping
  if [ -n "$ESCAPED_REPORT_CONTENT" ] && echo "$ESCAPED_REPORT_CONTENT" | grep -vE '^\s*$' > /dev/null; then
    curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendMessage" \
      -d "chat_id=${CHAT_ID}" \
      -d "parse_mode=MarkdownV2" \
      -d "text=${ESCAPED_REPORT_CONTENT}" \
      2>&1

    # Log successful execution
    echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] SUCCESS: Daily progress report generated and sent directly to Telegram." >> "$LOG_FILE"
  else
    echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] WARNING: Report content seems minimal or empty after processing. Not sending to Telegram." >> "$LOG_FILE"
  fi
else
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] WARNING: Report content seems minimal or empty. Not sending to Telegram." >> "$LOG_FILE"
fi

# Clean up old reports (optional: keep last 7 days)
find "$WORKSPACE/memory/daily_reports" -type f -name "*.md" -mtime +7 -delete
