# Alert: {{alert_level}}
Time: {{timestamp}}

## Alert Details
Type: {{alert_type}}
Source: {{source}}
Priority: {{priority}}

## Description
{{description}}

## Impact
{{impact}}

## Required Action
{{action_required}}

## Timeline
Response Required By: {{response_deadline}}

## Current Status
{{current_status}}

## Resolution Steps
{{#each resolution_steps}}
1. {{step}}
{{/each}}

## Escalation Path
{{#each escalation_path}}
{{level}}: {{contact}}
{{/each}}

## Notes
{{notes}}