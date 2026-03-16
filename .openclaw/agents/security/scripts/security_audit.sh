#!/usr/bin/env bash

# Security audit script
# Run comprehensive security checks and log results

# Set variables
LOG_DIR="$HOME/.openclaw/workspace/memory/security/logs/system"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_security_audit.log"

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Start logging
echo "Security Audit - $DATE" > "$LOG_FILE"
echo "======================" >> "$LOG_FILE"

# System update check
echo "Checking system updates..." >> "$LOG_FILE"
apt list --upgradable 2>/dev/null >> "$LOG_FILE"

# OpenClaw status
echo -e "\nChecking OpenClaw status..." >> "$LOG_FILE"
openclaw gateway status >> "$LOG_FILE"

# Check running processes
echo -e "\nChecking running processes..." >> "$LOG_FILE"
ps aux | grep openclaw >> "$LOG_FILE"

# Check open ports
echo -e "\nChecking open ports..." >> "$LOG_FILE"
netstat -tulpn 2>/dev/null >> "$LOG_FILE"

# Check disk usage
echo -e "\nChecking disk usage..." >> "$LOG_FILE"
df -h >> "$LOG_FILE"

# Check memory usage
echo -e "\nChecking memory usage..." >> "$LOG_FILE"
free -h >> "$LOG_FILE"

echo -e "\nSecurity audit completed at $(date)" >> "$LOG_FILE"