# Task-Rabbit Configuration

## System Configuration
```json
{
  "update_frequency": {
    "critical": "real-time",
    "standard": 3600,
    "routine": 14400
  },
  "alert_thresholds": {
    "response_time": 300,
    "completion_delay": 3600,
    "queue_length": 10
  },
  "reporting": {
    "daily_summary": "21:00",
    "weekly_report": "Monday 09:00",
    "status_interval": 3600
  }
}
```

## Agent Monitoring Rules
```json
{
  "default": {
    "heartbeat_interval": 900,
    "max_silence": 3600,
    "grace_period": 300
  },
  "critical_agents": {
    "heartbeat_interval": 300,
    "max_silence": 900,
    "grace_period": 120
  }
}
```

## Task Priority Levels
1. URGENT (immediate action)
2. HIGH (within 1 hour)
3. MEDIUM (within 4 hours)
4. LOW (within 24 hours)
5. ROUTINE (scheduled)

## Communication Channels
- Primary: Direct agent messaging
- Secondary: Status updates to main agent
- Emergency: Immediate alerts to main agent and CEO agent

## Performance Thresholds
```json
{
  "task_completion": {
    "optimal": "< 100% of estimated time",
    "acceptable": "< 120% of estimated time",
    "warning": "> 120% of estimated time",
    "critical": "> 150% of estimated time"
  },
  "response_times": {
    "urgent": "< 5 minutes",
    "high": "< 15 minutes",
    "medium": "< 30 minutes",
    "low": "< 2 hours"
  },
  "coordination_efficiency": {
    "optimal": "< 5 minute handoff",
    "acceptable": "< 15 minute handoff",
    "warning": "> 15 minute handoff",
    "critical": "> 30 minute handoff"
  }
}
```

## Monitoring Scope
### Core Agents
- CEO Agent
- ICE Agent
- Research Agent
- Marketing Agent
- SEO Agent
- Analytics Agent

### Support Agents
- Email-Manager Agent
- Security Agent
- Web-Posting Agent

## Task Queue Management
```json
{
  "queue_limits": {
    "per_agent": 5,
    "total_system": 20
  },
  "scheduling": {
    "max_concurrent": 3,
    "min_interval": 300
  },
  "load_balancing": {
    "threshold": 0.8,
    "redistribution_delay": 900
  }
}
```

## Reporting Templates
Located in ~/.openclaw/agents/task-rabbit/templates/
- daily_summary.md
- weekly_report.md
- status_update.md
- alert_template.md