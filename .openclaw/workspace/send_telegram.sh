#!/bin/bash
source /home/ubuntu/.env
MSG="🌿 Weekly Report — March 30, 2026

Here's your Monday full report:
https://dusky-sycam-ndes.here.now/

— Primo 🤖"

curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendMessage" \
  -d "chat_id=-1003809781298" \
  --data-urlencode "text=${MSG}"
