# Gmail Integration for ICE Agent

## Overview
This document describes how ICE (Information Collection and Evaluation) agent interacts with Gmail services through the Email-Manager agent.

## Email Data Collection
ICE can collect and process:
- Customer inquiries
- Order confirmations
- Delivery notifications
- Support requests

## Integration Points
1. Monitoring inbox via Email-Manager
2. Processing email content for data extraction
3. Forwarding relevant information to other agents

## Usage Instructions
1. Email Monitoring:
```json
{
  "action": "monitor",
  "folder": "INBOX",
  "filters": {
    "from": "customer@example.com",
    "subject": "Order *"
  }
}
```

2. Data Extraction:
- Order details
- Customer information
- Delivery preferences
- Support tickets

3. Information Routing:
- Orders → Task-Rabbit for processing
- Support → Support team
- Inquiries → Marketing team

## Security Requirements
- OAuth2 authentication required
- Access limited to business-related emails
- Data encryption in transit and at rest