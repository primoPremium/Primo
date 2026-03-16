# Standard Delegation Workflow

## Core Process Structure
1. Primo delegates task needs to Task-Rabbit Agent (TR/Teddy)
2. Task-Rabbit Agent maintains oversight while delegating execution to Worker Agent after communicating requirements and credentials needed with ICE
3. Task-Rabbit monitors progress and coordinates
4. Worker Agent conducts the actual task
5. ICE Agent verifies connections and successful payloads
6. Task-Rabbit communicates to Primo and messages telegram the update
7. Finally, Primo reviews the verified results

## Role Clarification

### Task-Rabbit (TR/Teddy)
- Primary responsibility for delegation
- Task management
- Progress monitoring
- Reporting and communication
- Template management oversight

### ICE (Integrations and Customs Enforcement)
- API/skill/tool integration verification
- Rules and guidelines enforcement
- Cultural alignment enforcement
- Security and credentials management
- Acts as secrets vault
- Enforcement of compliance standards

### Worker Agents (Research, Marketing, SEO, etc.)
- Execute assigned tasks within their domain
- Maintain and improve domain-specific templates
- Report progress to Task-Rabbit
- Follow ICE-enforced guidelines

## Implementation Notes
- Steps #2 (executing agent) and #4 (agent identity) are interchangeable with any worker agent
- All agents maintain and improve their templates over time
- ICE acts as local government/law enforcement for rules and culture
- Task-Rabbit is the central coordinator for all delegation flows

## Communication Flow
- All task updates flow through Task-Rabbit
- ICE maintains oversight of security and compliance
- Worker agents do not communicate directly with Primo
- Telegram updates are managed by Task-Rabbit