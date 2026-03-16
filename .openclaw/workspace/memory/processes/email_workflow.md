# Email Integration Workflow

## Overview
Custom Gmail integration using our gmail_handler.py for all Premium Meds email operations.

## Core Components
1. Custom Gmail Handler
   - Location: /home/ubuntu/.openclaw/agents/email-manager/src/gmail_handler.py
   - Features:
     - Gmail API integration
     - Built-in OAuth2 flow
     - OpenClaw browser integration
     - Attachment support
     - Environment-based configuration

2. Required Environment Variables
   - GOOGLE_CLIENT_ID
   - GOOGLE_CLIENT_SECRET

## Standard Process Flow
1. Agent needs to send email:
   - Task-Rabbit coordinates the request
   - ICE verifies credential access
   - Email-Manager handles execution using gmail_handler.py

2. Email Request Protocol
   - All email requests go through Task-Rabbit
   - Task-Rabbit coordinates with Email-Manager
   - Email-Manager uses gmail_handler.py
   - ICE maintains security oversight

3. Authentication Flow
   - Credentials managed through environment variables
   - OAuth flow handled by gmail_handler.py
   - Browser integration for auth completion

## Agent Responsibilities

### Task-Rabbit
- Receive and coordinate email requests
- Route requests to Email-Manager
- Monitor task completion
- Report results back to requesting agent

### ICE
- Maintain security of credentials
- Monitor authentication status
- Ensure proper access controls
- Verify integration compliance

### Email-Manager
- Execute email operations via gmail_handler.py
- Maintain email templates
- Handle attachments when needed
- Report sending status

### Other Agents
- Route all email requests through Task-Rabbit
- Never attempt direct email sending
- Include required email parameters:
  - Recipient(s)
  - Subject
  - Body content
  - Attachments (if any)

## Template Usage
Email templates are stored and managed by Email-Manager agent:
- Location: /home/ubuntu/.openclaw/agents/email-manager/templates/
- Standard templates for common communications
- Custom template creation as needed

## Error Handling
1. Authentication Issues
   - ICE verifies credentials
   - Task-Rabbit coordinates resolution
   - Email-Manager attempts reauth if needed

2. Sending Failures
   - Email-Manager reports to Task-Rabbit
   - Task-Rabbit coordinates retry strategy
   - ICE verifies no security implications

## Monitoring
- Task-Rabbit tracks all email operations
- ICE monitors security aspects
- Email-Manager maintains sending logs

## Last Updated: 2026-03-13