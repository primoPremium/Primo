# Daily Progress Summary
Date: {{date}}

## Task Overview
- Total Active Tasks: {{total_tasks}}
- Completed Today: {{completed_tasks}}
- In Progress: {{in_progress_tasks}}
- Blocked: {{blocked_tasks}}

## Agent Status
{{#each agent_status}}
### {{agent_name}}
- Active Tasks: {{active_tasks}}
- Completion Rate: {{completion_rate}}%
- Current Status: {{status}}
{{/each}}

## Critical Updates
{{#each critical_updates}}
- [{{timestamp}}] {{message}}
{{/each}}

## Issues Requiring Attention
{{#each issues}}
- Priority: {{priority}}
  Description: {{description}}
  Action Required: {{action}}
{{/each}}

## Tomorrow's Priority Tasks
{{#each priority_tasks}}
1. {{task_name}} ({{assigned_to}})
   Est. Completion: {{eta}}
{{/each}}

## Performance Metrics
- System Health: {{system_health}}%
- Average Response Time: {{avg_response_time}}s
- Task Success Rate: {{success_rate}}%

## Notes
{{notes}}