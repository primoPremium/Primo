# Agent Delegation System Configuration Requirements
Last Updated: 2024-03-06

## Current Status
- Main agent lacks delegation capabilities
- Task-Rabbit agent inaccessible
- Agent spawning limited to main agent only

## Required Configuration Changes

### 1. Agent Access Configuration
Required entries in `.openclaw/agents/`:
```
/.openclaw/agents/
  ├── task-rabbit/
  │   ├── AGENT.md          # Task-Rabbit core configuration
  │   ├── protocols.md      # Delegation protocols
  │   └── reporting.md      # Progress reporting templates
  └── config/
      └── delegation.json   # Agent delegation permissions
```

### 2. Permission Structure
```json
{
  "main": {
    "can_delegate": true,
    "allowed_agents": [
      "task-rabbit",
      "marketing",
      "seo",
      "analytics",
      "web-posting",
      "email-manager",
      "security",
      "research",
      "ice"
    ]
  },
  "task-rabbit": {
    "can_monitor": true,
    "can_coordinate": true,
    "reporting_channel": "telegram:-1003809781298"
  }
}
```

### 3. Required Environment Variables
```
TASK_RABBIT_API_KEY=<key>
AGENT_DELEGATION_ENABLED=true
PROGRESS_MONITORING_ENABLED=true
```

### 4. Implementation Steps
1. Create Task-Rabbit agent configuration directory
2. Configure agent delegation permissions
3. Set up required environment variables
4. Verify Task-Rabbit agent access
5. Test delegation protocols
6. Validate monitoring capabilities

### 5. Delegation Protocol Updates
All task monitoring and coordination should flow through Task-Rabbit:
```
Main Agent → Task-Rabbit → Specialized Agents
                       ↳ Progress Monitoring
                       ↳ Status Reporting
                       ↳ Agent Coordination
```

## Priority Tasks
1. Configure Task-Rabbit agent access
2. Implement delegation permissions
3. Update environment configuration
4. Test complete delegation flow

## Impact on Current Operations
- Temporary manual monitoring required until configuration complete
- Need to document all delegated tasks for retroactive monitoring
- May require brief system downtime during implementation

## Next Steps
1. Review and approve configuration requirements
2. Schedule implementation window
3. Prepare backup monitoring procedures
4. Execute configuration updates
5. Verify system functionality

## Notes
- All configuration changes must maintain existing security protocols
- Implementation should be done during low-activity period
- Full system backup recommended before changes
- Post-implementation testing required for all agent interactions