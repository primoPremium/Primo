# Email Manager Configuration

## Gmail Integration (Updated 2024-03-04)

### OpenClaw Gmail Skill
```json
{
  "skill_path": "~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/gmail/",
  "documentation": "docs/GMAIL_INTEGRATION.md",
  "authentication": "service-account.json (pre-configured)",
  "templates_dir": "templates/"
}
```

### API Settings
```json
{
  "service": "gmail",
  "version": "v1",
  "user_id": "premiummedscollective@gmail.com",
  "quota_limits": {
    "daily_send": 2000,
    "batch_size": 100,
    "rate_limit": 250
  }
}
```

## Email Processing

### Queue Configuration
```json
{
  "max_queue_size": 1000,
  "processing_interval": 60,
  "batch_size": 100,
  "retry_config": {
    "max_attempts": 3,
    "initial_delay": 1000,
    "max_delay": 8000,
    "backoff_multiplier": 2
  }
}
```

### Template Settings
```json
{
  "template_dir": "templates/",
  "default_encoding": "utf-8",
  "max_size": 10485760,
  "allowed_mime_types": [
    "text/plain",
    "text/html",
    "multipart/alternative"
  ]
}
```

## Monitoring Configuration

### Performance Monitoring
```json
{
  "metrics": {
    "delivery_rate": true,
    "open_rate": true,
    "click_rate": true,
    "bounce_rate": true,
    "response_time": true
  },
  "thresholds": {
    "delivery_rate_min": 0.98,
    "bounce_rate_max": 0.02,
    "response_time_max": 2000
  }
}
```

### Alert Configuration
```json
{
  "critical": {
    "notification": "immediate",
    "channels": ["main_agent", "task_rabbit"],
    "retry": true
  },
  "warning": {
    "notification": "batch",
    "interval": 3600,
    "channels": ["task_rabbit"]
  },
  "info": {
    "notification": "daily",
    "channels": ["task_rabbit"]
  }
}
```

## Reporting Configuration

### Standard Reports
```json
{
  "daily_summary": {
    "schedule": "0 9 * * *",
    "metrics": [
      "total_sent",
      "delivery_rate",
      "bounce_rate",
      "error_count"
    ]
  },
  "weekly_report": {
    "schedule": "0 10 * * 1",
    "metrics": [
      "weekly_stats",
      "performance_trends",
      "issue_summary"
    ]
  }
}
```

### Performance Metrics
```json
{
  "collection_interval": 300,
  "retention_period": 2592000,
  "aggregation_rules": {
    "hourly": {
      "window": 3600,
      "metrics": ["delivery_rate", "error_rate"]
    },
    "daily": {
      "window": 86400,
      "metrics": ["all"]
    }
  }
}
```

## Security Configuration

### Access Control
```json
{
  "roles": {
    "admin": {
      "permissions": ["send", "read", "delete", "configure"]
    },
    "sender": {
      "permissions": ["send", "read"]
    },
    "monitor": {
      "permissions": ["read"]
    }
  }
}
```

### Compliance Settings
```json
{
  "require_unsubscribe": true,
  "max_retry_attempts": 3,
  "log_retention_days": 90,
  "sensitive_content_scan": true
}
```