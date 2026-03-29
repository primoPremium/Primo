Startup Hooks: Automatic loading and propagation rules

1) Session creation hook
- On every new session (DM or group), automatically load:
  - memory/startup_routine_bradmin.md
  - MEMORY.md
- Context should reflect startup notes immediately.

2) Memory propagation hook
- When MEMORY.md is updated in any session, propagate changes to all other active sessions (conflicts resolved by last-write-wins per section).

3) Group-session mirroring
- For every new group session, initialize with startup notes from startup_routine_bradmin.md and ensure updates are mirrored across all group sessions.

4) Startup log
- Append an entry to memory/global_startup_log.md for every load/propagation event with timestamp, session_id, action.

5) Safety and coordination
- All actions routed through Task-Rabbit; no direct execution by main agent.
- Log all startup actions for audit.
