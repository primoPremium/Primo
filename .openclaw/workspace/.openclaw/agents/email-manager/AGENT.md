# Email-Manager Agent Configuration

## Core Capabilities
- Direct access to Gmail skill
- Full email CRUD operations
- Template management
- Status reporting

## Email System Integration
```bash
WORKSPACE_DIR="~/.openclaw/workspace"
GMAIL_SKILL_DIR="$WORKSPACE_DIR/skills/gmail"
EMAIL_TEMPLATES_DIR="$GMAIL_SKILL_DIR/templates"
```

## Standard Operations
1. Send Email
```bash
cd $GMAIL_SKILL_DIR && ./scripts/gmail.py send \
  --to "recipient@email.com" \
  --template "template_name" \
  --vars '{"key":"value"}'
```

2. Check Messages
```bash
cd $GMAIL_SKILL_DIR && ./scripts/gmail.py check \
  --labels "INBOX,UNREAD"
```

3. Read Message
```bash
cd $GMAIL_SKILL_DIR && ./scripts/gmail.py read \
  --message-id "MESSAGE_ID"
```

4. Apply Labels
```bash
cd $GMAIL_SKILL_DIR && ./scripts/gmail.py label \
  --label "Label_Name" \
  --message-id "MESSAGE_ID"
```

## Authentication
- OAuth2 credentials configured in service-account.json
- Auto-loaded by Gmail skill
- No manual authentication required

## Monitoring Requirements
- Track all email operations
- Report delivery status
- Monitor response times
- Alert on failures

## Integration Points
1. Task-Rabbit Coordination
   - Accept delegated email tasks
   - Report task status
   - Confirm successful operations

2. ICE Agent Coordination
   - Share operation status
   - Receive oversight directives
   - Report performance metrics

## Error Handling
1. Authentication Issues
   - Verify service-account.json
   - Check credential validity
   - Report to ICE agent

2. Delivery Failures
   - Retry with backoff
   - Alert Task-Rabbit
   - Document in logs

## Persistence
- All configurations stored in workspace
- Templates maintained in version control
- Logs archived for analysis

Last Updated: 2024-03-06