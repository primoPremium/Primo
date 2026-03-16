---
name: gmail
description: Gmail integration using exec for reliable cross-chat access. Manages Premium Meds Collective email (premiummedscollective@gmail.com) with support for reading, sending, and managing emails. Use for: (1) Checking emails, (2) Reading specific messages, (3) Sending emails with templates, (4) Managing labels and organization.
---

# Gmail Integration

Access Gmail through reliable exec commands. Pre-configured for Premium Meds Collective email management.

## Quick Commands

All operations use exec to ensure consistent access across all chats:

### Check Messages
```bash
# List unread messages
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py check --labels "UNREAD"

# Check specific label
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py check --labels "INBOX"

# Search messages
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py check --labels "INBOX" --query "from:example@email.com"
```

### Read Messages
```bash
# Read specific message
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py read --message-id MESSAGE_ID
```

### Send Messages
```bash
# Send using template
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py send --to "recipient@email.com" --template "template_name" --vars '{"key":"value"}'
```

### Manage Labels
```bash
# Apply label
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py label --label "Support" --message-id MESSAGE_ID
```

## Available Templates

Templates are stored in `templates/` and support variable substitution:

- `progress_report.txt` - Marketing progress reports
- `campaign_update.txt` - Campaign status updates
- `analytics_report.txt` - Marketing analytics summaries
- `delivery_status.txt` - Delivery tracking notifications

## Template Usage

1. All templates support variables in {braces}
2. Send with --vars as JSON string
3. Example:
```bash
exec cd ~/.openclaw/workspace/skills/gmail && ./scripts/gmail.py send \
  --to "recipient@email.com" \
  --template "progress_report" \
  --vars '{"project":"Q1 Marketing","date":"2024-03-01"}'
```

## Authentication

OAuth2 credentials are pre-configured for premiummedscollective@gmail.com in service-account.json.

## Error Handling

Common issues and solutions:
1. Authentication errors: Check service-account.json permissions
2. Template errors: Verify template exists and variables match
3. API limits: Space out requests if hitting Gmail API limits

## Security Notes

1. Credentials stored securely in service-account.json
2. Access restricted to premiummedscollective@gmail.com
3. Templates validated before sending
4. Rate limiting enforced

For implementation details, see [references/api.md](references/api.md).