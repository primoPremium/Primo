#!/usr/bin/env bash
# post_to_group.sh — Lightweight Telegram group posting module
# AUTHORIZED CALLER: Cathy Agent ONLY
# TR and ICE have awareness-only access (emergency use untested)
#
# Usage: ./post_to_group.sh "Your message here" [chat_id]
#
# Env vars required (from ~/.env):
#   TELEGRAM_PAIRING_KEY   — Bot token
#   TELEGRAM_GROUP_CHAT_ID — Group chat ID (without -100 prefix; script adds it)
#
# Returns: delivery confirmation with message_id and timestamp on success.

set -euo pipefail

# Load env if not already set
if [ -z "${TELEGRAM_PAIRING_KEY:-}" ]; then
  if [ -f "$HOME/.env" ]; then
    set -a; source "$HOME/.env"; set +a
  else
    echo "❌ TELEGRAM_PAIRING_KEY not set and ~/.env not found"; exit 1
  fi
fi

MESSAGE="${1:?Usage: post_to_group.sh \"message\" [chat_id]}"
RAW_CHAT_ID="${2:-${TELEGRAM_GROUP_CHAT_ID:?TELEGRAM_GROUP_CHAT_ID not set}}"
TOKEN="${TELEGRAM_PAIRING_KEY}"

# Ensure -100 prefix for supergroup IDs
if [[ "$RAW_CHAT_ID" =~ ^[0-9]+$ ]]; then
  CHAT_ID="-100${RAW_CHAT_ID}"
elif [[ "$RAW_CHAT_ID" =~ ^-100[0-9]+$ ]]; then
  CHAT_ID="$RAW_CHAT_ID"
else
  CHAT_ID="$RAW_CHAT_ID"
fi

RESPONSE=$(curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendMessage" \
  -d "chat_id=${CHAT_ID}" \
  -d "text=${MESSAGE}" \
  -d "parse_mode=HTML")

if echo "$RESPONSE" | grep -q '"ok":true'; then
  MSG_ID=$(echo "$RESPONSE" | grep -oP '"message_id":\K[0-9]+' || echo "unknown")
  DATE=$(echo "$RESPONSE" | grep -oP '"date":\K[0-9]+' || echo "unknown")
  echo "✅ Posted | msg_id=${MSG_ID} | ts=${DATE}"
  exit 0
else
  DESC=$(echo "$RESPONSE" | grep -oP '"description":"\K[^"]+' || echo "unknown error")
  echo "❌ Failed: ${DESC}"
  echo "$RESPONSE"
  exit 1
fi
