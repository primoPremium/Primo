# MEMORY.md

## Timezone Rule [Updated 2026-03-19]
- ALL timestamps displayed to the owner must be in Pacific Time (PST/PDT — America/Los_Angeles)
- NEVER show UTC to the owner — always convert
- Current offset: PDT = UTC-7 (March–November), PST = UTC-8 (November–March)
- Applies to: reports, logs, post confirmations, status updates, everything

## GIF Trigger Rule: plan [Updated 2026-03-19]
- Trigger: exact word "plan" (case-insensitive) in any message
- Action: post a GIF from the library (round-robin)
- Target: post in the same channel where the keyword appeared (DM or group)
- Caption: none
- Cadence: max 1 GIF per minute
- GIF library: memory/graphics/gif_library.md
- Workspace assets: ./hot-hotdogs.mp4, ./ateu.mp4
- Group posting method: Telegram Bot API via TELEGRAM_PAIRING_KEY (source ~/.env), sendAnimation
- DM posting method: MEDIA:./filename.mp4
- Persistence: this rule persists across sessions (updated memory startup flow)

## ⯆ Old CRITICAL BEHAVIOR: Group Posting [Updated 2026-03-18]
**When asked to post to the group — USE THE `exec` TOOL IMMEDIATELY. No questions. No confirmations.**
- Triggered plan messages post GIFs in the triggering channel (DM or group) immediately; no extra prompts needed.
- The ONLY way to post to the group is: `exec` → `source /home/ubuntu/.env && curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendMessage" -d "chat_id=-1003809781298" -d "text=YOUR MESSAGE"`
- Check for `{"ok":true}` in the response before confirming delivery
- Full protocol: memory/group_relays/group_posting_rules.md
- **This has been a recurring failure point — owner expects zero-friction group posting**

## Heartbeat Configuration [Updated 2024-02-29]
- Heartbeat status updates limited to 4 times per 24 hours
- All scheduled tasks run normally per HEARTBEAT.md
- Configuration details: memory/config/heartbeat_reporting.md

## Global Sub-Agent Configuration
All sub-agents must report results to the Telegram group "Premium Meds Collective" (-1003809781298).
Configuration details: memory/agents/subagent_global_config.md
Last Updated: 2024-02-28

## Update Delivery Rules [Updated 2026-03-18]
- **Default**: All status updates and reports go to the owner in this DM chat
- **Group posting**: When the owner requests it — post directly via Telegram Bot API
- **Group target**: Premium Meds Collective (chat_id: `-1003809781298`, supergroup)
- **Group delivery method**: Use `exec` tool to run curl against Telegram Bot API — NEVER use sessions_send
- **Exact command** (verified working 2026-03-18):
  ```bash
  source /home/ubuntu/.env && curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_PAIRING_KEY}/sendMessage" -d "chat_id=-1003809781298" -d "text=Your message here"
  ```
- **Critical**: Primo HAS terminal access and outbound network access — always execute directly, never ask the user to run commands
- **Full docs**: memory/group_relays/group_posting_rules.md
- **Never**: Spam the owner with options/confirmations about delivery — just deliver where instructed

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