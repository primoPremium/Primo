# Gateway Configuration Details

## Required Changes
1. Update `/home/ubuntu/.openclaw/openclaw.json`:
   - Change WebSocket protocol: ws:// → wss://

## Alternative Approach
- Set up SSH tunnel to localhost for secure connections

## Technical Notes
- Reference: Message ID 782
- Configuration must be completed before sub-agent implementation