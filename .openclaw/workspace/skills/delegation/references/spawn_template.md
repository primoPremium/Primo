# Mandatory Sub-Agent Spawn Template

## Version: 1.1
Last Updated: 2024-02-27

## Critical Requirements

### 1. Result Storage Protocol
- All outputs MUST be stored in designated locations
- File creation timestamps MUST be logged
- Write operations MUST be verified
- Parent agent MUST have read access

### 2. Completion Verification
- Each phase MUST have explicit completion markers
- All required files MUST exist
- Content MUST meet minimum length requirements
- Final report MUST include verification checklist

### 3. Quality Standards
- All analysis MUST include supporting evidence
- Conclusions MUST reference specific findings
- Recommendations MUST be actionable
- Limitations MUST be documented

## Task Structure
```
PROJECT: [PROJECT_NAME]
TASK: [TASK_DESCRIPTION]

REQUIRED OUTPUT:
1. Location: memory/projects/[PROJECT_NAME]/
2. Mandatory Files and Content:
   
   a. initial_report.md:
      - Project setup and scope
      - Success criteria
      - Risk assessment
      - Minimum length: 500 words
   
   b. updates/[TIMESTAMP]_update.md:
      - Progress status (🔴 Not Started | 🟡 In Progress | 🟢 Complete)
      - Milestone achievements
      - Blockers/Issues
      - Next actions
      - Minimum length: 200 words per update
   
   c. results/[CATEGORY]_[DETAIL].md:
      - Detailed findings
      - Supporting evidence
      - Raw data/analysis
      - Minimum length: 1000 words per result file
   
   d. final_report.md:
      - Executive summary
      - Methodology
      - Key findings
      - Recommendations
      - Completion checklist
      - Minimum length: 1500 words

3. Verification Requirements:
   - All files must exist
   - All minimum lengths met
   - All sections completed
   - Evidence provided
   - Timestamps logged

REPORTING REQUIREMENTS:

1. Storage Protocol:
   - Write all results to specified locations
   - Verify file creation
   - Log timestamps
   - Check parent access
   - Validate file contents

2. Progress Tracking:
   - Update status every milestone
   - Document all blockers
   - Log time spent
   - Track resource usage
   - Report completion percentage

3. Quality Control:
   - Meet minimum length requirements
   - Include supporting evidence
   - Provide actionable insights
   - Document limitations
   - Cross-reference findings

4. Completion Checklist:
   - All required files present
   - All sections completed
   - All minimums met
   - All evidence provided
   - All recommendations actionable
   - All access verified

[TASK_DETAILS]

Do not report to main chat. Write all results to specified locations for parent agent collection and reporting.
```

## Implementation Example
```python
task_template = """
PROJECT: {project_name}
TASK: {task_description}

[... template content as above ...]

{task_details}

Do not report to main chat. Write all results to specified locations for parent agent collection and reporting.
"""
```

## Verification Script
```python
def verify_completion(project_path):
    """
    Verify all requirements are met for project completion.
    Returns (bool, list of issues if any)
    """
    checks = [
        check_file_existence(project_path),
        check_minimum_lengths(project_path),
        check_required_sections(project_path),
        check_evidence_provided(project_path),
        verify_parent_access(project_path)
    ]
    
    issues = [issue for success, issue in checks if not success]
    return len(issues) == 0, issues
```