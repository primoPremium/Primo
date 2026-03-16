# Agent Prerequisites

## Core Requirements
All agents must verify browser status before operations:

1. Browser Initialization
   ```
   Required: OpenClaw browser must be started
   Check: browser tool status
   Action: Start if not running
   ```

2. Order of Operations:
   - Check browser status first
   - Start browser if needed
   - Then proceed with assigned tasks

## Email-Manager Specific
1. Pre-flight Checklist:
   - ✓ Verify browser is running
   - ✓ Check email interface accessibility
   - ✓ Confirm credentials loaded

## ICE Agent Specific
1. System Checks:
   - ✓ Verify browser status
   - ✓ Confirm access to required interfaces
   - ✓ Validate information sources

## Task-Rabbit Coordination
1. Verification Steps:
   - Confirm agent prerequisites met
   - Check browser status before delegation
   - Monitor agent readiness

Last Updated: 2026-03-05