#!/usr/bin/env bash
set -euo pipefail

# Chatty-Cathy startup placeholder
# NOTE: OpenClaw agent runtimes differ by deployment; this script is intended
# to standardize local initialization steps (logs/paths/last_id tracking).

AGENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE="/home/ubuntu/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory/chatty-cathy"
STATE_DIR="$MEMORY_DIR/state"

mkdir -p "$MEMORY_DIR" "$STATE_DIR"
touch "$MEMORY_DIR/activity_log.md" "$MEMORY_DIR/escalations.md"

# last processed group message id (idempotency)
LAST_ID_FILE="$STATE_DIR/last_group_message_id.txt"
if [[ ! -f "$LAST_ID_FILE" ]]; then
  echo "0" > "$LAST_ID_FILE"
fi

echo "[Cathy] Initialized. AgentDir=$AGENT_DIR MemoryDir=$MEMORY_DIR LastId=$(cat "$LAST_ID_FILE")"