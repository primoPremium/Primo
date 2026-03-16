# Successful Configurations

## Browser Settings
```json
{
    "profile": "chrome",
    "viewport": {
        "width": 1920,
        "height": 1080
    },
    "wait_for_network": true,
    "wait_time_ms": 2000
}
```

## Email Settings
```json
{
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 587,
    "use_tls": true,
    "retry_attempts": 3,
    "retry_delay_ms": 1000
}
```

## Template Variables
- {page_title}
- {url}
- {timestamp}
- {sender_name}
- {viewport}
- {notes}

## Known Working Combinations
1. Chrome 120+ with default viewport
2. Gmail API with OAuth2
3. PNG format for screenshots