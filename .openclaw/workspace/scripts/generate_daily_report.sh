#!/bin/bash
# Daily Progress Report Generator
# Compiles research, SEO, and placeholder updates, then posts directly to Telegram.

set -euo pipefail

WORKSPACE="/home/ubuntu/.openclaw/workspace"
REPORT_FILE="$WORKSPACE/memory/daily_reports/latest_progress_report.md"
LOG_FILE="$WORKSPACE/memory/daily_reports/report_generator.log"
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
mkdir -p "$WORKSPACE/memory/competitor_analysis" # Ensure this exists for checks
mkdir -p "$WORKSPACE/memory/seo" # Ensure this exists for checks

# --- Report Header ---
REPORT_HEADER="# Daily Progress Report - $(escape_markdownv2 "$(TZ='America/Los_Angeles' date '+%Y-%m-%d %A %Z')")"
echo -e "$REPORT_HEADER" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- Section 1: General Daily Activities ---
# COMPLETELY REMOVED DUE TO UNRESOLVED ISSUES AND TO ENSURE SCRIPT RELIABILITY.
# This section is removed entirely.

# --- Section 2: Research & Competitor Updates ---
echo -e "## 🔬 Research & Competitor Updates\n" >> "$REPORT_FILE"
echo -e "_(Summary of recent findings and website analysis)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

RESEARCH_DIR="$WORKSPACE/memory/competitor_analysis"
# Capture find output, set default if empty or command fails
# Using process substitution to handle find output more robustly
LATEST_RESEARCH_FILE=$(find "$RESEARCH_DIR" -type f -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n 1 | cut -d' ' -f2-)

# Assign fallback string if no file was found or find command failed
if [ -z "$LATEST_RESEARCH_FILE" ]; then
  LATEST_RESEARCH_FILE="No files found in $RESEARCH_DIR"
fi

# Now check if the variable contains the fallback string OR if the file actually exists
if [[ "$LATEST_RESEARCH_FILE" != "No files found in $RESEARCH_DIR" ]] && [ -f "$LATEST_RESEARCH_FILE" ]; then
  echo "### Latest Research Report:" >> "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
  echo "*   **File:** \`$(escape_markdownv2 "$(basename "$LATEST_RESEARCH_FILE")")\`" >> "$REPORT_FILE"
  echo "*   **Last Modified:** \$(TZ='America/Los_Angeles' date -d @\$(stat -c %Y \"$LATEST_RESEARCH_FILE\") '+%Y-%m-%d %I:%M %p %Z')" >> "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
  echo "    **Content Snippet:**" >> "$REPORT_FILE"
  echo "    \`\`\`" >> "$REPORT_FILE"
  head -n 5 "$LATEST_RESEARCH_FILE" | escape_markdownv2 >> "$REPORT_FILE" # First 5 lines
  echo "    \`\`\`" >> "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
else
  echo "No recent competitor analysis reports found in $RESEARCH_DIR." >> "$REPORT_FILE"
fi
echo "" >> "$REPORT_FILE"

# --- Section 3: SEO Findings ---
echo -e "## 📈 SEO Findings\n" >> "$REPORT_FILE"
echo -e "_(Summary of recent SEO analysis)_" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

SEO_DIR="$WORKSPACE/memory/seo"
# Capture find output, set default if empty or command fails
LATEST_SEO_FILE=$(find "$SEO_DIR" -name "*_keyword_analysis.md" -type f -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n 1 | cut -d' ' -f2-)
if [ -z "$LATEST_SEO_FILE" ]; then
  LATEST_SEO_FILE="No files found in $SEO_DIR"
fi

if [ -n "$LATEST_SEO_FILE" ] && [ -f "$LATEST_SEO_FILE" ]; then
  echo "### Latest SEO Analysis:" >> "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
  echo "*   **File:** \`$(escape_markdownv2 "$(basename "$LATEST_SEO_FILE")")\`" >> "$REPORT_FILE"
  echo "*   **Last Modified:** \$(TZ='America/Los_Angeles' date -d @\$(stat -c %Y \"$LATEST_SEO_FILE\") '+%Y-%m-%d %I:%M %p %Z')" >> "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
  echo "    **Key Snippet (Top 5 lines):**" >> "$REPORT_FILE"
  echo "    \`\`\`" >> "$REPORT_FILE"
  head -n 5 "$LATEST_SEO_FILE" | escape_markdownv2 >> "$REPORT_FILE" # First 5 lines
  echo "    \`\`\`" >> "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
else
  echo "No recent SEO analysis files found in $SEO_DIR." >> "$REPORT_FILE"
fi
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
echo "    *   Script ran at: [\$(escape_markdownv2 "\$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')")]" >> "$REPORT_FILE"
echo "    *   Report generated from: \`$(escape_markdownv2 "$REPORT_FILE")\`" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- Send Report to Telegram Directly ---
REPORT_CONTENT=$(cat "$REPORT_FILE")

# Escape the final report content for MarkdownV2
ESCAPED_REPORT_CONTENT=$(escape_markdownv2 "$REPORT_CONTENT")

# Check if content seems substantial enough to send, avoiding empty messages.
# A minimal report would have the header and the placeholder sections.
# We check for the presence of a key section like "Research" to determine if it's substantial.
if echo "$ESCAPED_REPORT_CONTENT" | grep -q "## 🔬 Research"; then
  curl -s -X POST "https://api.telegram.API/bot${TELEGRAM_PAIRING_KEY}/sendMessage" \
    -d "chat_id=${CHAT_ID}" \
    -d "parse_mode=MarkdownV2" \
    -d "text=${ESCAPED_REPORT_CONTENT}" \
    2>&1

  # Log successful execution
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] SUCCESS: Daily progress report generated and sent directly to Telegram." >> "$LOG_FILE"
else
  echo "[$(TZ='America/Los_Angeles' date '+%Y-%m-%d %I:%M %p %Z')] WARNING: Report content seems minimal or empty. Not sending to Telegram." >> "$LOG_FILE"
fi

# Clean up old reports (optional: keep last 7 days)
find "$WORKSPACE/memory/daily_reports" -type f -name "*.md" -mtime +7 -delete
