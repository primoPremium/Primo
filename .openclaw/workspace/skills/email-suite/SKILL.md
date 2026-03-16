# Premium Meds Email Operations Skill

## Description
Authenticated access and operations for Premium Meds' premiummedscollective@gmail.com account.

## Authentication
1. Load credentials from ~/.env:
   ```
   GOOGLE_CLIENT_ID="<from ~/.env>"
   GOOGLE_CLIENT_SECRET="<from ~/.env>"
   ```
2. Email account: premiummedscollective@gmail.com (from WP_CRED_USER)
3. Verify authentication before operations
4. Report authentication status to chat

## Core Email Operations
1. Read Operations
   - Check inbox/folders
   - Search emails
   - Read message content
   - Download attachments

2. Write Operations
   - Draft new emails
   - Reply to messages
   - Forward emails
   - Send with attachments

3. Preview & Review
   - Draft previews
   - Offer review
   - Template application
   - Format checking

## Technical Configuration

### Gmail Authentication
- Account: premiummedscollective@gmail.com
- Credentials: ~/.env
- Required scopes:
  - gmail.modify
  - gmail.send
  - gmail.readonly

### Attachment Handling
- Screenshot capture (via browser skill)
- File attachments
- Size optimization
- Format validation

### Templates Location
./templates/
- business_correspondence.md
- marketing_preview.md
- offer_template.md

## Usage Examples

### Read Email
```bash
# Check inbox
email_ops read inbox --latest 5

# Search specific emails
email_ops search --query "subject:order confirmation"
```

### Send Email with Attachment
```bash
# Send with screenshot
email_ops send \
  --to "recipient@example.com" \
  --subject "Product Preview" \
  --template "marketing_preview" \
  --attach_screenshot "product_page.png"
```

### Draft Preview
```bash
# Create draft for review
email_ops draft \
  --template "offer_template" \
  --values "product:Vape,price:60.00" \
  --preview_mode
```

## Integration Notes
- ALWAYS load credentials from ~/.env
- Use WP_CRED_USER for email address
- Report all actions to chat
- Maintain template consistency

## Error Handling
1. Check ~/.env first
2. Report missing credentials to chat
3. Request configuration if missing
4. Log all authentication attempts

## Required Environment
- Gmail API credentials (from ~/.env)
- OpenClaw browser skill (for screenshots)
- Template access
- Chat reporting enabled