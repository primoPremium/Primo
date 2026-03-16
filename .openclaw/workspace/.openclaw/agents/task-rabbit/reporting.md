# Task-Rabbit Reporting Templates

## Progress Report Template
```markdown
# Task Progress Report
Date: {{date}}
Time: {{time}}
Task ID: {{task_id}}

## Status Summary
- Progress: {{progress_percentage}}%
- Status: {{status}}
- Time Elapsed: {{elapsed_time}}
- Time Remaining: {{estimated_remaining}}

## Task Details
- Assigned Agent: {{agent_name}}
- Priority Level: {{priority}}
- Dependencies: {{dependencies}}

## Recent Updates
{{updates_list}}

## Issues/Blockers
{{issues_list}}

## Next Steps
{{next_steps}}
```

## Completion Report Template
```markdown
# Task Completion Report
Date: {{date}}
Time: {{time}}
Task ID: {{task_id}}

## Summary
- Status: {{final_status}}
- Duration: {{total_duration}}
- Resources Used: {{resources}}

## Deliverables
{{deliverables_list}}

## Key Metrics
{{metrics_summary}}

## Recommendations
{{recommendations}}
```

## Alert Template
```markdown
🚨 **Task Alert**
Task ID: {{task_id}}
Alert Level: {{severity}}
Issue: {{issue_description}}
Impact: {{impact}}
Required Action: {{action_needed}}
```