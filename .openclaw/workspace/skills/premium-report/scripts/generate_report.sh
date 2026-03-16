#!/bin/bash

# Default to summary report
REPORT_TYPE=${1:-summary}

# Set paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$BASE_DIR/templates"

# Select template based on report type
if [ "$REPORT_TYPE" = "full" ]; then
    TEMPLATE="$TEMPLATE_DIR/full_report.html"
else
    TEMPLATE="$TEMPLATE_DIR/summary_report.html"
fi

# Create temporary report file
TMP_REPORT=$(mktemp)
cp "$TEMPLATE" "$TMP_REPORT"

# Publish to here.now
cd ~/.agents/skills/here-now
./scripts/publish.sh "$TMP_REPORT"

# Cleanup
rm "$TMP_REPORT"