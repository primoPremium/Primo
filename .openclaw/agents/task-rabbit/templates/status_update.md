# Status Update
Time: {{timestamp}}

## Task Status
ID: {{task_id}}
Agent: {{agent_name}}
Status: {{status}}

## Progress
- Current Stage: {{stage}}
- Completion: {{completion_percentage}}%
- ETA: {{eta}}

## Details
{{details}}

## Next Steps
{{next_steps}}

## Issues/Blockers
{{#if issues}}
{{#each issues}}
- {{issue}}
{{/each}}
{{else}}
No current issues
{{/if}}

## Resources
{{#each resources}}
- {{name}}: {{status}}
{{/each}}

## Notes
{{notes}}