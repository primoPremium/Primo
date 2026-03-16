# Sub-Agent Requirements

## Mandatory Reporting Configuration
Every spawned sub-agent must include these reporting requirements:

1. Direct Chat Communication
   - Use message tool to report back to main chat
   - Report regardless of success/failure
   - Include timestamp in PST (12hr format)

2. Standard Report Format
   ```
   [Task Name] Report
   Timestamp: [PST timestamp]
   Status: [Success/Failed]
   
   Details:
   - [Key details specific to task]
   - [Results or findings]
   - [Any errors or issues]
   
   API/Task Status: [Connected/Error/Completed/etc]
   ```

3. Delivery Requirements
   - Use message tool with action=send
   - Ensure delivery confirmation
   - No silent completions allowed

## Implementation
- Add these requirements to EVERY sessions_spawn task description
- Include reporting format in task specifications
- Require acknowledgment of receipt
- Follow up if no report received

## Verification
- Monitor sub-agent completion
- Verify report delivery
- Track communication success rate

Added: 2026-02-27 at 1:58 PM PST