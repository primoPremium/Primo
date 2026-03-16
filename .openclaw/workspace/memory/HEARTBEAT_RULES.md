# HEARTBEAT RULES AND REQUIREMENTS

## MANDATORY FORMATTING
All heartbeat responses MUST use the Premium Meds standard format without exception:

```
📊 PREMIUM MEDS HEARTBEAT CHECK
══════════════════════════════
🕒 Timestamp: [TIME] PT

🎯 TASK STATUS
──────────────
#️⃣ [TASK NAME]
   ⏰ Due: [NEXT DUE DATE/TIME]
   📊 Status: [✅ COMPLETED|⏳ PENDING|🟦 SCHEDULED|⚠️ OVERDUE]
   📝 Note: [RELEVANT DETAILS]

⚠️ ALERTS: [IF ANY]
📈 SYSTEM STATUS: [OPERATIONAL STATUS]
🔄 NEXT CHECK: [NEXT SCHEDULED CHECK]
```

## CRITICAL RULES
1. This format is MANDATORY for ALL heartbeat responses
2. No exceptions or deviations allowed
3. No plain text status updates
4. Format must be applied immediately without user prompting
5. This applies to both routine checks and alerts

## IMPLEMENTATION
- Check this file on every heartbeat request
- Never skip formatting
- Never wait for user reminders
- Format must be applied before sending ANY heartbeat response

## VERIFICATION
- Self-verify format before sending
- Include all required sections
- Use exact emojis and formatting
- Maintain consistent spacing and borders

## ENFORCEMENT
If any heartbeat response is sent without this format:
1. Immediately correct the format
2. Review this rules file
3. Strengthen format monitoring