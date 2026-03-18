#!/usr/bin/env python3
"""Chatty-Cathy watchdog — lightweight watcher cycle for group monitoring."""

import os, time, datetime

LOGDIR = "/home/ubuntu/.openclaw/workspace/memory/chatty-cathy"
STATE_DIR = os.path.join(LOGDIR, "state")
ACT_LOG = os.path.join(LOGDIR, "activity_log.md")
ESC_LOG = os.path.join(LOGDIR, "escalations.md")
LAST_ID = os.path.join(STATE_DIR, "last_group_message_id.txt")
EVENTS_FILE = os.path.join(LOGDIR, "mock_events.txt")  # for testing only

os.makedirs(STATE_DIR, exist_ok=True)


def now_pst():
    # Approximate PST (UTC-8); in production use pytz or zoneinfo
    utc = datetime.datetime.utcnow()
    pst = utc - datetime.timedelta(hours=8)
    return pst.strftime("%Y-%m-%d %H:%M PST")


def read_last_id():
    if os.path.exists(LAST_ID):
        with open(LAST_ID) as f:
            val = f.read().strip()
            return int(val) if val.isdigit() else 0
    return 0


def write_last_id(n):
    with open(LAST_ID, "w") as f:
        f.write(str(n))


def append_activity(entry):
    with open(ACT_LOG, "a") as f:
        f.write(entry + "\n")


def append_escalation(entry):
    with open(ESC_LOG, "a") as f:
        f.write(entry + "\n")


def process_event(event_line, msg_id):
    ts = now_pst()
    lower = event_line.lower()

    # Trigger word: plan
    if "plan" in lower:
        action = "trigger-response"
        response = "📋🔥 (emoji posted in group)"
        escalated = False
    else:
        # Default: escalate to owner
        action = "escalated"
        response = "On it 👍 (hold message posted in group)"
        escalated = True

    log_entry = (
        f"\n### {ts}\n"
        f"- **From**: [group member]\n"
        f"- **Message**: {event_line[:120]}\n"
        f"- **Action**: {action}\n"
        f"- **Response**: {response}\n"
        f"- **Escalation**: {'yes' if escalated else 'no'}\n"
        f"- **Message ID**: {msg_id}\n"
    )
    append_activity(log_entry)

    if escalated:
        esc_entry = (
            f"\n### {ts}\n"
            f"- **Trigger**: {event_line[:120]}\n"
            f"- **Escalated to**: Bradmin Bot (DM)\n"
            f"- **Owner response**: pending\n"
            f"- **Resolution**: awaiting owner\n"
        )
        append_escalation(esc_entry)

    return action


def main():
    last_id = read_last_id()
    ts = now_pst()
    append_activity(f"\n### {ts}\n- **Watcher cycle started** (last_id={last_id})\n")

    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE) as f:
            lines = [l.strip() for l in f if l.strip()]
        processed = 0
        for line in lines:
            last_id += 1
            action = process_event(line, last_id)
            processed += 1
            print(f"[Cathy] msg_id={last_id} action={action} event={line[:60]}")
        # Clear events after processing
        os.remove(EVENTS_FILE)
        print(f"[Cathy] Processed {processed} events. last_id now {last_id}")
    else:
        print("[Cathy] No new events. Idle cycle.")

    write_last_id(last_id)
    append_activity(f"\n### {ts}\n- **Watcher cycle complete** (last_id={last_id})\n")
    print(f"[Cathy] Cycle complete. last_id={last_id}")


if __name__ == "__main__":
    main()
