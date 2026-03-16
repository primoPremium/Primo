# Email Review Agent Configuration

## Overview
Weekly email review agent for monitoring bweldy82@gmail.com using the Gmail skill.

## Schedule
- Day: Wednesday
- Time: 6:00 AM PT
- Frequency: Weekly

## Configuration
- Target Email: bweldy82@gmail.com
- Review Period: Past 7 days
- Output Directory: /home/ubuntu/.openclaw/workspace/memory/email_reports/

## Tasks
1. Connect to Gmail using authenticated client
2. Fetch emails from the past week
3. Analyze:
   - New message threads
   - Important updates
   - Action items
   - Engagement metrics
4. Generate weekly report
5. Post summary to Premium Meds Collective Telegram group

## Report Format
```markdown
# Email Activity Report
Date: YYYY-MM-DD

## Overview
- Total messages: [count]
- New threads: [count]
- Action items: [count]
- Priority updates: [count]

## Important Updates
[List of important messages with snippets]

## Action Items
[List of tasks/follow-ups needed]

## Engagement Metrics
- Response rate: [%]
- Average response time: [duration]
- Peak activity times: [times]

## Detailed Message Log
[Chronological list of significant messages]

## Notes
[Any additional observations or recommendations]
```

## Dependencies
- Gmail Skill (/home/ubuntu/.openclaw/workspace/skills/gmail/)
- OAuth2 credentials
- Secure token storage

## Error Handling
1. Authentication failures
   - Retry with token refresh
   - Alert if persistent
2. API rate limits
   - Implement exponential backoff
   - Continue from last successful point
3. Missing messages
   - Log gaps in coverage
   - Include in report summary