# BOOTSTRAP.md

## Automatic Session Initialization
1. Agent Initialization
   - Email-Manager: Load email skill configuration
   - Task-Rabbit: Initialize coordination protocols
   - ICE: Load evaluation frameworks

## Email System Bootstrap
```bash
# Email system configuration
EMAIL_MANAGER_CONFIG="~/.openclaw/workspace/configs/email_manager.json"
EMAIL_SKILL_PATH="~/.openclaw/workspace/skills/email-suite/"

# Auto-load on session start
source $EMAIL_MANAGER_CONFIG
```

## Persistence Configuration
- Store configurations in workspace
- Auto-load required skills
- Maintain persistent agent states

## Required Skills
- email-suite
- delegation
- monitoring

Last Updated: 2026-03-05