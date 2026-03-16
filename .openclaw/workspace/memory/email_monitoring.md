# Email Monitoring Rules

## Priority Senders
- bweldy82@gmail.com
  - Action: Alert chat immediately
  - Include: Email summary when possible
  - Priority: High
  - Added: 2026-02-27

## Monitoring Process
1. Check Gmail API for new messages
2. Filter for priority senders
3. Generate summary if content is accessible
4. Alert chat immediately with findings

## Action Reporting Requirements
ALL Gmail actions must be reported to chat, including:
- Reading emails (include summary)
- Sending emails (include confirmation)
- Deleting emails (include what was deleted)
- Moving/organizing emails (include from/to locations)
- Label changes (include what changed)
- Any other Gmail API interactions

Each report must include:
- Action taken
- Status (success/failure)
- Relevant details (IDs, subjects, etc)
- Timestamp (PST in 12hr format)

## Technical Implementation
- Using Gmail API configuration
- Token location: /home/ubuntu/.config/gogcli/token.json
- Monitor via heartbeat checks
- Immediate reporting for all actions
- No silent operations allowed