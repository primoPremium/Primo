# BOOTSTRAP.md

## Automatic Session Initialization (ALL sessions — DM + Group)

### Step 1: Global Startup Routine
- Load: memory/startup_routine_bradmin.md
- Load: MEMORY.md
- Apply startup context immediately to shape all tasks

### Step 2: Agent Initialization
- Email-Manager: Load email skill configuration
- Task-Rabbit: Initialize coordination protocols
- ICE: Load evaluation frameworks

### Step 3: Memory System Activation
- Sections in MEMORY.md: Voice, Process, People, Projects, Output, Tools
- On any correction or new learning → update MEMORY.md in place (replace, don't append)
- Changes visible to all sessions in real-time (shared workspace)

### Step 4: Startup Logging
- Append JSON-line to memory/global_startup_log.jsonl on every session start and every MEMORY.md update
- All timestamps in PST/PDT (America/Los_Angeles)
- Fields: timestamp, session_type, channel, action, session_id, note

### Step 5: Group Session Mirroring
- Group sessions follow the identical startup routine as DM sessions
- One routine for all — no separate initialization path

## Email System Bootstrap
```bash
EMAIL_MANAGER_CONFIG="~/.openclaw/workspace/configs/email_manager.json"
EMAIL_SKILL_PATH="~/.openclaw/workspace/skills/email-suite/"
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

Last Updated: 2026-03-18
