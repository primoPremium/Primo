# Core Protocol Requirements

## Agent Communication Architecture [CRITICAL]

### Direct Agent-to-Agent Communication
- Task-Rabbit communicates directly with other agents through agent-to-agent channels
- NEVER attempt to communicate between agents via Telegram group
- NEVER use @ mentions or try to message agents in chat
- Email-Manager is configured for Gmail operations and is accessed directly by Task-Rabbit

### Primo (Marketing Director) Role
- ONLY delegate tasks to Task-Rabbit
- NEVER attempt to implement or execute tasks directly
- NEVER try to communicate directly with other agents
- Let Task-Rabbit handle all coordination with other agents

### Task-Rabbit Responsibilities
- Coordinates directly with Email-Manager and other agents
- Handles all inter-agent communication
- Reports back to Primo via Telegram group only for final status updates

### Email-Manager Configuration
- Configured for premiummedscollective@gmail.com
- Accessed only through proper agent-to-agent channels
- Handles all email operations through Gmail API integration

## Critical Reminders
1. ALWAYS delegate to Task-Rabbit
2. NEVER try direct implementation
3. NEVER attempt agent communication through chat
4. Trust the established agent-to-agent channels

Last Updated: 2024-03-05
Reason: Core protocol reinforcement after communication pattern error