# Email-Manager Agent

## Overview
The Email-Manager agent handles all email communications for Premium Meds using Gmail integration.

## Required Environment Variables
The following environment variables must be set in ~/.openclaw/.env:

```bash
GMAIL_CLIENT_ID=your_client_id
GMAIL_CLIENT_SECRET=your_client_secret
GMAIL_REFRESH_TOKEN=your_refresh_token
GMAIL_ACCESS_TOKEN=your_access_token
```

## Usage by Other Agents
To request email services, other agents should:

1. Send a structured request to Email-Manager with:
   - recipient(s)
   - subject
   - body content
   - any attachments
   
2. Example request format:
```json
{
  "to": "customer@example.com",
  "subject": "Your Premium Meds Order",
  "body": "Thank you for your order...",
  "attachments": []
}
```

3. Wait for confirmation of email delivery

## Security & Compliance
- All emails are logged for compliance
- Authentication uses OAuth2 for enhanced security
- Rate limiting is enforced to prevent abuse

## Error Handling
- Failed deliveries are logged and retried
- Errors are reported back to requesting agent
- Maximum 3 retry attempts per email