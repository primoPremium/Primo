# Task-Rabbit Communication Protocol

## Primary Communication Chain
1. Task-Rabbit → Marketing Director (Primo)
   SessionKey: agent:main:telegram:direct:8451594534
   Channel: Premium Meds Collective Telegram Group (-1003809781298)
2. Marketing Director → Other Stakeholders

## Reporting Requirements

### 1. Regular Status Updates
- Frequency: Every 4 hours during active periods
- Channel: Premium Meds Collective Telegram Group
- Format: Structured markdown report
- Must include:
  - Agent status summary
  - Active tasks
  - Issues requiring attention
  - Performance metrics

### 2. Critical Updates
- Trigger: Any CRITICAL or EMERGENCY level alerts
- Channel: Direct to Marketing Director
- Response required: Within 15 minutes
- Must include:
  - Issue description
  - Impact assessment
  - Recommended actions
  - Timeline for resolution

### 3. Coordination Updates
- When: Any inter-agent task handoffs
- Format: JSON status update
- Must confirm:
  - Source agent readiness
  - Target agent availability
  - Task parameters
  - Expected completion time

## Communication Format

### Standard Report Template
```markdown
# Agent Status Report
Generated: [TIMESTAMP]
Report ID: [UUID]

## Active Agents Overview
| Agent | Status | Tasks | Issues |
|-------|--------|--------|--------|
| [NAME] | 🟢/🟡/🔴 | [COUNT] | [COUNT] |

## Current Tasks
### High Priority
- [ ] Task 1 (Owner: [AGENT])
- [ ] Task 2 (Owner: [AGENT])

### Standard Priority
- [ ] Task 3 (Owner: [AGENT])
- [ ] Task 4 (Owner: [AGENT])

## Issues Requiring Attention
- ⚠️ [ISSUE_DESCRIPTION] (Priority: [LEVEL])
- ⚠️ [ISSUE_DESCRIPTION] (Priority: [LEVEL])

## Performance Metrics
- Task Completion Rate: [PERCENTAGE]
- Response Time Avg: [TIME]
- Coordination Score: [SCORE]

## Recommendations
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

## Next Update
Scheduled: [TIMESTAMP]
```

### Critical Alert Template
```markdown
🚨 CRITICAL ALERT
Time: [TIMESTAMP]
Level: [CRITICAL/EMERGENCY]

Issue: [DESCRIPTION]

Impact:
- [IMPACT_1]
- [IMPACT_2]

Required Actions:
1. [ACTION_1]
2. [ACTION_2]

Timeline:
- Detection: [TIMESTAMP]
- Required Response: [TIMESTAMP]
- Resolution Target: [TIMESTAMP]

Escalation Contact:
- Primary: Marketing Director (Primo)
- Secondary: CEO Agent
```

## Response Requirements
1. All reports must be acknowledged
2. Critical alerts require explicit response
3. Recommendations need approval/rejection
4. Issues must be tracked until resolved

## Channels
1. Primary: Premium Meds Collective Telegram Group (-1003809781298)
2. Backup: Direct agent-to-agent communication
3. Emergency: Immediate escalation to Marketing Director

## Documentation
- All communications logged
- Regular reports archived
- Critical incidents documented
- Resolution steps recorded