---
name: delegation
description: Standardized framework for sub-agent delegation, monitoring, and result reporting. Use when spawning sub-agents to ensure consistent reporting, result storage, and accountability. Provides structured templates for initial reports, progress updates, and final reports.
---

# Delegation Framework Skill

## Core Components

1. Report Templates
2. Result Storage
3. Progress Monitoring
4. Accountability Chain

## Templates

### Initial Report (Verbose)
```markdown
INITIAL PROJECT REPORT
Date: [TIMESTAMP]
Project: [PROJECT_NAME]

1. PROJECT SCOPE
   - Objectives
   - Deliverables
   - Constraints

2. CURRENT STATUS
   - Setup details
   - Agent IDs
   - Initial phase

3. RESOURCES ALLOCATED
   - Agent count
   - Credentials/Access
   - Tools required

4. TIMELINE
   - Start time
   - Expected duration
   - Update schedule
   - Completion target

5. SUCCESS METRICS
   - Key indicators
   - Validation points
   - Quality criteria

6. RISK ASSESSMENT
   - Potential issues
   - Mitigation plans
   - Dependencies

7. NEXT ACTIONS
   - Immediate steps
   - Monitoring plan
   - Decision points
```

### Progress Update (Concise)
```markdown
UPDATE: [PROJECT_NAME]
Time: [TIMESTAMP]
Status: [IN_PROGRESS/BLOCKED/COMPLETE]

- Progress: [KEY_MILESTONE]
- Findings: [BRIEF_SUMMARY]
- Blockers: [IF_ANY]
- Next: [UPCOMING_STEP]
```

### Final Report (Verbose)
```markdown
FINAL PROJECT REPORT
Date: [TIMESTAMP]
Project: [PROJECT_NAME]

1. EXECUTIVE SUMMARY
   - Duration
   - Status
   - Resource usage
   - Key outcomes

2. DETAILED FINDINGS
   - Results analysis
   - Data collected
   - Metrics achieved

3. LESSONS LEARNED
   - Successes
   - Challenges
   - Process improvements

4. RECOMMENDATIONS
   - Immediate actions
   - Long-term improvements
   - Risk mitigations

5. NEXT STEPS
   - Follow-up tasks
   - Maintenance needs
   - Future considerations
```

## Result Storage

### Directory Structure
```
memory/
├── projects/
│   └── [PROJECT_NAME]/
│       ├── initial_report.md
│       ├── updates/
│       │   └── [TIMESTAMP]_update.md
│       ├── results/
│       │   └── [RESULT_FILES]
│       └── final_report.md
```

### Storage Protocol
1. Create project directory
2. Store initial report
3. Log updates chronologically
4. Save result artifacts
5. Store final report

## Mandatory Usage

1. Sub-Agent Spawn Requirements
- MUST include output location specification
- MUST include report format requirements
- MUST specify result storage instructions
- MUST use standard template (see references/spawn_template.md)

2. Initial Setup
```python
# Create project directory
mkdir -p memory/projects/[PROJECT_NAME]

# Store initial report
write_report("memory/projects/[PROJECT_NAME]/initial_report.md", initial_report)

# Spawn sub-agent with mandatory template
spawn_agent(
    project_name="example_project",
    task_description="Sample task",
    task_details="Specific instructions",
    output_location="memory/projects/example_project/"
)
```

2. Progress Updates
```python
# Log update
update_path = f"memory/projects/[PROJECT_NAME]/updates/{timestamp}_update.md"
write_report(update_path, update_content)
```

3. Result Storage
```python
# Store results
result_path = f"memory/projects/[PROJECT_NAME]/results/{filename}"
write_file(result_path, result_data)
```

4. Final Report
```python
# Store final report
write_report("memory/projects/[PROJECT_NAME]/final_report.md", final_report)
```

## Monitoring Protocol

1. Check agent status every 2-5 minutes
2. Log significant changes
3. Report blockers immediately
4. Verify result storage
5. Validate completion criteria

## Accountability

1. Parent agent responsible for:
   - Project setup
   - Regular monitoring
   - Result verification
   - Report compilation
   - Final delivery

2. Sub-agents responsible for:
   - Task execution
   - Progress updates
   - Result generation
   - Result storage
   - Result reporting
   - Error reporting

## Best Practices

1. Always create project directory first
2. Use consistent naming conventions
3. Include timestamps in all reports
4. Verify result storage
5. Maintain clear ownership chain
6. Document any deviations
