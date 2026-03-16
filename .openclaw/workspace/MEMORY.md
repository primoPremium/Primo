# MEMORY.md

## Heartbeat Configuration [Updated 2024-02-29]
- Heartbeat status updates limited to 4 times per 24 hours
- All scheduled tasks run normally per HEARTBEAT.md
- Configuration details: memory/config/heartbeat_reporting.md

## Global Sub-Agent Configuration
All sub-agents must report results to the Telegram group "Premium Meds Collective" (-1003809781298).
Configuration details: memory/agents/subagent_global_config.md
Last Updated: 2024-02-28

## Core Integrations

### Here.now Integration [COMPLETE - 2024-02-29]
- Purpose: Automated progress reporting and permanent web publishing
- Key: HERE_DOT_NOW_KEY (stored in .env)
- Status: ✅ Fully operational
- Usage: Integrated with heartbeat system for automated reporting
- Latest URL Format: {slug}.here.now
- Documentation: ~/.agents/skills/here-now/SKILL.md

### Gmail Integration [COMPLETE - 2024-02-28]
- Account: premiummedscollective@gmail.com
- Status: ✅ Fully operational
- Setup: Using OpenClaw Gmail skill with our OAuth2 credentials
- Purpose: Email monitoring and management for Premium Meds
- Usage: Simply request email tasks like "check emails" or "send a report"
- Documentation: memory/systems/email_integration.md [Added 2024-03-05]

### WooCommerce Integration

#### Overview
Premium Meds WooCommerce integration established on 2026-02-28 to provide automated monitoring and reporting of e-commerce operations.

#### Credentials Status
- Last Verified: 2026-03-02
- Location: ~/.env
- API Integration: ✅ Functional
- Components:
  - API Key: Present
  - API Secret: Present
  - WordPress User Credentials: Present
  - DB Credentials: Present

#### Recent Activity
- 2026-03-02: Successfully used API credentials to initiate blog post draft creation

[Rest of the content remains the same...]