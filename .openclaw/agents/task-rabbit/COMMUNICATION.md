# Task-Rabbit Communication Configuration

## Direct Communication Path
sessionKey: "agent:main:telegram:direct:8451594534"  # Marketing Director (Primo)

## Communication Methods
1. Direct Response:
```javascript
sessions_send({
    sessionKey: "agent:main:telegram:direct:8451594534",
    message: "[Status Report Content]"
})
```

2. Group Channel:
```javascript
message({
    action: "send",
    channel: "telegram",
    target: "-1003809781298",  // Premium Meds Collective group
    message: "[Report Content]"
})
```

## Required Headers
Every communication must include:
- Timestamp
- Source: "Task-Rabbit"
- Target: "Marketing Director"
- Priority Level
- Report ID

## Response Verification
- Confirm message delivery
- Check for acknowledgment
- Retry on failure
- Log all communication attempts

## Emergency Backup
If primary communication fails:
1. Retry direct session send
2. Attempt group message
3. Create persistent log file
4. Signal communication failure to main agent