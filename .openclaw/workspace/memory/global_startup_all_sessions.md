Global Startup Routine for All Sessions (including group sessions)

Objective
- Ensure the startup routine (startup_routine_bradmin.md) is applied universally to every new session, including group chats, and in all channels.

Scope
- Applies to: all user sessions, DMs, and group sessions where Primo/Bradmin Bot collaborates.

Startup Behavior
1. Load foundational context files:
   - Read memory/startup_routine_bradmin.md
   - Read MEMORY.md
2. Enforce uniform memory augmentation:
   - When corrections are issued by user, update the relevant sections in MEMORY.md
   - Maintain sections: Voice, Process, People, Projects, Output, Tools
3. Session-wide consistency:
   - Apply the same startup routine content to any new session
   - If a group session is created, initialize with the startup routine notes and ensure updates are mirrored
4. Delegation and coordination:
   - Route tasks through Task-Rabbit; do not execute tasks directly
   - Log startup routine application to memory/global_startup_log.md

Operational Notes
- Update branding and preferences in MEMORY.md as the startup routine evolves
- Ensure all agents and sub-agents recognize the global startup routine on session creation

Last Updated: 2026-03-18