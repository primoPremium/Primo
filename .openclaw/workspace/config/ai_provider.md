# AI Provider Configuration

## Primary Configuration
- Provider: OpenRouter
- Model: claude-3.5-sonnet
- Path: openrouter/anthropic/claude-3.5-sonnet

## Agent Settings
All agents should use these settings by default:
- Provider: OpenRouter
- Model: claude-3.5-sonnet
- Timeout: 30 minutes for standard tasks
- Extended timeout: 60 minutes for complex analysis

## Connection Requirements
- Gateway must be running
- OpenRouter authentication configured
- Default model set to openrouter/anthropic/claude-3.5-sonnet

## Usage Guidelines
1. All spawned agents should inherit these settings
2. Verify gateway connection before spawning agents
3. Include timeout settings appropriate to task complexity
4. Monitor performance and adjust as needed

## Error Handling
1. Check gateway status on connection failures
2. Verify OpenRouter service status
3. Confirm model availability
4. Report any persistent issues to system administrator

Last Updated: 2024-03-19