# ICE: Email Integration Security
RESTRICTED - ICE Agent Only

## Core Responsibilities
- Maintain Gmail OAuth2 credentials
- Monitor authentication status
- Enforce access restrictions
- Audit email operations

## Critical Variables
- GOOGLE_CLIENT_ID (required for Gmail API)
- GOOGLE_CLIENT_SECRET (required for Gmail API)
- GOOGLE_CLIENT_WEB_ID (available but not used by handler)
- GOOGLE_CLIENT_WEB_SECRET (available but not used by handler)

## Security Protocols
1. Credential Management
   - Store in secure environment
   - Regular rotation schedule
   - Access logging

2. Authentication Oversight
   - Monitor OAuth2 status
   - Handle reauthorization
   - Track access patterns

3. Access Control
   - Restrict handler access
   - Monitor usage attempts
   - Log unauthorized access

## Integration Points
- Email-Manager: Execution only
- Task-Rabbit: Coordination only
- All others: No direct access

## Last Updated: 2026-03-13