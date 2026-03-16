# Gmail Skill Integration

## Overview
Integration between Email-Manager Agent and OpenClaw Gmail Skill for reliable email operations.

## Skill Location
```
~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/gmail/
```

## Core Components
1. Gmail Script: ./scripts/gmail.py
2. Templates: ./templates/*.txt
3. Authentication: service-account.json (pre-configured)

## Usage Examples

### Send Email
```bash
cd ~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/gmail && ./scripts/gmail.py send \
  --to "recipient@email.com" \
  --template "template_name"
```

### Check Messages
```bash
cd ~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/gmail && ./scripts/gmail.py check \
  --labels "UNREAD"
```

### Read Specific Message
```bash
cd ~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/gmail && ./scripts/gmail.py read \
  --message-id MESSAGE_ID
```

## Template Management
- Location: ~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/gmail/templates/
- Format: Plain text with variable substitution {var_name}
- Naming: descriptive_name.txt

## Authentication
- Using pre-configured OAuth2 for premiummedscollective@gmail.com
- Credentials in service-account.json
- No additional setup needed

## Integration Testing
Verified working on:
- Date: 2024-03-04
- Test: Successfully sent agent list to both premiummedscollective@gmail.com and bweldy82@gmail.com
- Message IDs: 19cb793e86ea767d, 19cb796230347d6a