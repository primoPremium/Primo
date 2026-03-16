# OpenClaw Token Limits Investigation

## Issue Summary
Date: 2026-02-27
Impact: Initially observed gateway communication degradation after token limit increase

## Investigation Timeline

### Phase 1: Initial Problem
- Gateway token limits set to 4096 tokens
- Observed immediate degradation
- Reverted to 160 tokens as emergency fix

### Phase 2: Working Configuration (160 tokens)
- Gateway token limits: 160 tokens
- Location: `/home/ubuntu/.config/systemd/user/openclaw-gateway.service.d/limits.conf`
- Status: Functioning normally with complete responses
- All token limits aligned at 160

### Phase 3: Successful Optimization
Reference: https://claude.ai/share/2bbeb0de-fff0-4517-bd1a-14ffdad76020
New working configuration:
```
[Service]
# Enough for coherent responses, won't bankrupt you
Environment="OPENCLAW_MAX_TOKENS=2048"
Environment="OPENCLAW_MAX_OUTPUT_TOKENS=1024"
Environment="OPENCLAW_AGENT_MAX_TOKENS=2048"
Environment="OPENCLAW_AGENT_MAX_OUTPUT_TOKENS=1024"
Environment="OPENCLAW_EMBEDDED_MAX_TOKENS=1024"
Environment="OPENCLAW_EMBEDDED_MAX_OUTPUT_TOKENS=512"
Environment="OPENCLAW_OPENROUTER_MAX_TOKENS=1024"
# Re-enable compaction - this is what keeps your 58k input tokens from exploding
Environment="OPENCLAW_COMPACTION_ENABLED=1"
```

## Configuration Analysis
1. Model Settings (openclaw.json)
   - Claude 3.5 Sonnet: maxTokens=2048
   - OpenRouter Free: maxTokens=512

2. Key Changes That Worked:
   - Aligned MAX_TOKENS with model capability (2048)
   - Set reasonable output limits (1024)
   - Re-enabled compaction for large input handling
   - Maintained tiered token limits for different operations

## Root Cause Analysis
Initial theory about smaller tokens being better was incomplete:
1. Token limits need to align with model capabilities
2. Compaction is crucial for handling large inputs
3. Tiered token limits provide better resource management

## Key Insights
1. Compaction plays a vital role in managing input tokens
2. Token limits should be balanced across components
3. Alignment with model capabilities is more important than arbitrary limits

## Current Status
- System functioning normally with higher token limits
- Improved response capability while maintaining stability
- Compaction handling large inputs effectively

## Recommendations
1. Keep current optimized configuration
2. Monitor system performance with new limits
3. Consider similar balanced approaches for future optimizations

## Supporting Evidence
1. Initial logs showed issues with 4096 tokens
2. System stable with 160-token emergency configuration
3. Currently operating efficiently with balanced higher limits
4. Compaction managing large inputs successfully

## Related Files
- `/home/ubuntu/.config/systemd/user/openclaw-gateway.service.d/limits.conf`
- `/home/ubuntu/.openclaw/openclaw.json`