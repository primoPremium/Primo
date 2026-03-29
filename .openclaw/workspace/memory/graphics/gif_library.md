# GIF Library — "plan" Trigger
# Updated: 2026-03-19
# Trigger: exact word "plan" (case-insensitive)
# Target: group + DM
# Cadence: max 1 per minute
# Rotation: round-robin

---

- id: gif1
  label: "Hot Hotdogs (owner favorite)"
  type: video/mp4
  local_path: /home/ubuntu/.openclaw/media/inbound/hot-hotdogs---53878874-d934-4c79-9035-dd143db9b7f2.mp4
  captions:
    - "I love it when a plan comes together 🌭"
    - "Now THAT'S a plan 🌭🔥"
  trigger: "plan"
  trigger_type: exact_word_case_insensitive
  frequency: 1_per_minute
  target: group_and_dm

- id: gif2
  label: "Hannibal - A-Team classic cigar"
  type: image/gif
  url: https://media.giphy.com/media/l3vR6aasfs0Ae3qdG/giphy.gif
  captions:
    - "I love it when a plan comes together 😎"
    - "Plan detected — Hannibal approves 🎯"
  trigger: "plan"
  trigger_type: exact_word_case_insensitive
  frequency: 1_per_minute
  target: group_and_dm

- id: gif3
  label: "A-Team plan celebration"
  type: image/gif
  url: https://media.giphy.com/media/7jCuFo0aPURJm/giphy.gif
  captions:
    - "A plan so good even the A-Team is impressed 💪"
    - "Plan activated — let's ride 🚐"
  trigger: "plan"
  trigger_type: exact_word_case_insensitive
  frequency: 1_per_minute
  target: group_and_dm

- id: gif4
  label: "Hannibal Liam Neeson plan"
  type: image/gif
  url: https://media.giphy.com/media/E8b8dWfw67rnq/giphy.gif
  captions:
    - "You call that a plan? THIS is a plan 🔥"
    - "Plan locked in — no turning back now 🎬"
  trigger: "plan"
  trigger_type: exact_word_case_insensitive
  frequency: 1_per_minute
  target: group_and_dm
