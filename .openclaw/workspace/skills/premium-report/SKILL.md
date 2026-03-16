# Premium Meds Automated Report Generator

## Overview
Generates and publishes Premium Meds progress reports using here.now integration.

## Features
- Creates visually enhanced HTML reports
- Publishes via here.now for permanent hosting
- Generates both quick summaries and detailed reports
- Integrates with heartbeat system

## Templates
- Full Report: templates/full_report.html
- Summary Report: templates/summary_report.html

## Configuration
- API Key: Uses HERE_DOT_NOW_KEY from .env
- Output Format: Responsive HTML with Premium Meds branding
- Auto-publish: Integrated with heartbeat system

## Usage
```bash
./scripts/generate_report.sh [--type full|summary]
```