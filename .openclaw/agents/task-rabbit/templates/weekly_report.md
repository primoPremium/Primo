# Weekly Progress Report
Week: {{week_number}} ({{date_range}})

## Executive Summary
{{summary}}

## Task Statistics
- Total Tasks: {{total_tasks}}
- Completed: {{completed_tasks}} ({{completion_rate}}%)
- New Tasks: {{new_tasks}}
- Carried Over: {{carried_over}}

## Agent Performance
{{#each agent_performance}}
### {{agent_name}}
- Tasks Handled: {{tasks_handled}}
- Success Rate: {{success_rate}}%
- Average Response Time: {{avg_response}}
- Notable Achievements: {{achievements}}
{{/each}}

## Key Accomplishments
{{#each accomplishments}}
1. {{title}}
   Impact: {{impact}}
   Status: {{status}}
{{/each}}

## Issues & Resolution
{{#each issues}}
### {{issue_title}}
- Status: {{status}}
- Impact: {{impact}}
- Resolution: {{resolution}}
- Prevention Measures: {{prevention}}
{{/each}}

## Resource Utilization
- System Load: {{system_load}}%
- Queue Efficiency: {{queue_efficiency}}%
- Response Times: {{response_times}}

## Next Week's Focus
{{#each next_week}}
1. {{priority}}: {{task}}
   Owner: {{owner}}
   Timeline: {{timeline}}
{{/each}}

## Recommendations
{{#each recommendations}}
- {{recommendation}}
{{/each}}

## Notes
{{notes}}