# Email Task Delegation Protocol

## Core Process
1. All email tasks MUST be routed through:
   Task-Rabbit → Email-Manager Agent

2. Critical Email Requirements:
   - ALWAYS CC premiummedsoc@gmail.com on official reports
   - Priority should be marked as High for management communications
   - Include all relevant attachments and links

2. Standard Email Flow:
   - Primo (main) delegates to Task-Rabbit
   - Task-Rabbit coordinates with Email-Manager
   - Email-Manager handles all email operations
   - Task-Rabbit monitors and reports back

3. Required Components:
   - Sender: premiummedscollective@gmail.com
   - Monitoring: Task-Rabbit status tracking
   - Reporting: Completion confirmation

## Implementation
```bash
# Example delegation flow
1. Primo → Task-Rabbit
   "Please coordinate email delivery task"

2. Task-Rabbit → Email-Manager
   "Send email with following parameters:
    - To: [recipient]
    - Subject: [subject]
    - Content: [content]"

3. Email-Manager → Task-Rabbit
   "Email delivery status"

4. Task-Rabbit → Primo
   "Task completion report"
```

## Error Recovery
If email task fails:
1. Task-Rabbit notifies Primo
2. Email-Manager provides error details
3. Implement correction through proper chain

Last Updated: 2026-03-05