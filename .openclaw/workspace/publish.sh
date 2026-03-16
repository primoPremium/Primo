#!/bin/bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <file>" >&2
    exit 1
fi

FILE="$1"
TOKEN="${HERE_DOT_NOW_KEY:-}"

if [[ ! -f "$FILE" ]]; then
    echo "Error: File not found: $FILE" >&2
    exit 1
fi

RESPONSE=$(curl -s -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: $(file --mime-type -b "$FILE")" \
    --data-binary "@$FILE" \
    "https://api.here.now/v1/files")

if [[ $? -ne 0 ]]; then
    echo "Error: Upload failed" >&2
    exit 1
fi

echo "$RESPONSE" | jq -r '.url'