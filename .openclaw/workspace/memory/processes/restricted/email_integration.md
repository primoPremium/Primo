# Restricted: Email Integration Documentation
For Email-Manager, ICE, and Task-Rabbit only

## Component Access
1. Email-Manager Agent
   - Primary handler for email operations
   - Direct access to gmail_handler.py
   - Template management
   - Execution of email tasks

2. ICE Agent
   - Security and credential management
   - OAuth2 authentication oversight
   - Environment variable maintenance
   - Access control enforcement

3. Task-Rabbit Agent
   - Request coordination
   - Progress monitoring
   - Status reporting to requesters
   - No direct handler access

## Core Integration
- Location: /home/ubuntu/.openclaw/agents/email-manager/src/gmail_handler.py
- Credentials: Managed by ICE
- Access: Restricted to Email-Manager execution

## Process Flow
1. Other agents submit requests to Task-Rabbit
2. Task-Rabbit coordinates with Email-Manager
3. ICE verifies security compliance
4. Email-Manager executes using handler

## Security Notes
- Handler location and details restricted
- Credentials managed solely by ICE
- Access limited to authorized agents
- No direct handler access by other agents

## Last Updated: 2026-03-13