#!/usr/bin/env python3

import os
import sys
import json
import time
from datetime import datetime

def create_project_structure(project_name):
    base_path = f"memory/projects/{project_name}"
    os.makedirs(f"{base_path}/updates", exist_ok=True)
    os.makedirs(f"{base_path}/results", exist_ok=True)
    return base_path

def write_report(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def create_initial_report(project_name, data):
    template = """INITIAL PROJECT REPORT
Date: {timestamp}
Project: {project_name}

1. PROJECT SCOPE
{scope}

2. CURRENT STATUS
{status}

3. RESOURCES ALLOCATED
{resources}

4. TIMELINE
{timeline}

5. SUCCESS METRICS
{metrics}

6. RISK ASSESSMENT
{risks}

7. NEXT ACTIONS
{actions}
"""
    report = template.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        project_name=project_name,
        scope=data.get('scope', 'N/A'),
        status=data.get('status', 'N/A'),
        resources=data.get('resources', 'N/A'),
        timeline=data.get('timeline', 'N/A'),
        metrics=data.get('metrics', 'N/A'),
        risks=data.get('risks', 'N/A'),
        actions=data.get('actions', 'N/A')
    )
    return report

def create_update_report(project_name, data):
    template = """UPDATE: {project_name}
Time: {timestamp}
Status: {status}

- Progress: {progress}
- Findings: {findings}
- Blockers: {blockers}
- Next: {next_steps}
"""
    report = template.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        project_name=project_name,
        status=data.get('status', 'IN_PROGRESS'),
        progress=data.get('progress', 'N/A'),
        findings=data.get('findings', 'N/A'),
        blockers=data.get('blockers', 'None'),
        next_steps=data.get('next_steps', 'N/A')
    )
    return report

def create_final_report(project_name, data):
    template = """FINAL PROJECT REPORT
Date: {timestamp}
Project: {project_name}

1. EXECUTIVE SUMMARY
{summary}

2. DETAILED FINDINGS
{findings}

3. LESSONS LEARNED
{lessons}

4. RECOMMENDATIONS
{recommendations}

5. NEXT STEPS
{next_steps}
"""
    report = template.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        project_name=project_name,
        summary=data.get('summary', 'N/A'),
        findings=data.get('findings', 'N/A'),
        lessons=data.get('lessons', 'N/A'),
        recommendations=data.get('recommendations', 'N/A'),
        next_steps=data.get('next_steps', 'N/A')
    )
    return report

def main():
    if len(sys.argv) != 4:
        print("Usage: create_report.py <project_name> <report_type> <data_json>")
        sys.exit(1)

    project_name = sys.argv[1]
    report_type = sys.argv[2]
    data = json.loads(sys.argv[3])

    base_path = create_project_structure(project_name)

    if report_type == 'initial':
        report = create_initial_report(project_name, data)
        write_report(f"{base_path}/initial_report.md", report)
    elif report_type == 'update':
        report = create_update_report(project_name, data)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        write_report(f"{base_path}/updates/{timestamp}_update.md", report)
    elif report_type == 'final':
        report = create_final_report(project_name, data)
        write_report(f"{base_path}/final_report.md", report)
    else:
        print(f"Unknown report type: {report_type}")
        sys.exit(1)

if __name__ == "__main__":
    main()