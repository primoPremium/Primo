# here.now Publishing Workflow (All Agents)

> Last updated: 2026-03-18
> Status: VERIFIED WORKING

## Purpose
Generate permanent, live web URLs for status reports, progress updates, and any content that needs to be shared with the board (Premium Meds Collective group).

## How to Publish (Step-by-Step)

### 1. Create content
Write your HTML/file to a directory:
```bash
mkdir -p /tmp/my-report
# Write index.html or place files in the directory
```

### 2. Run the publish script
```bash
bash ~/.agents/skills/here-now/scripts/publish.sh /tmp/my-report
```

### 3. Read the output
The script outputs a live URL like:
```
https://robust-mango-yzdq.here.now/
publish_result.site_url=https://robust-mango-yzdq.here.now/
publish_result.auth_mode=authenticated
publish_result.persistence=permanent
```

### 4. Use the URL from the script output
- **ALWAYS use the URL returned by the publish script** — never invent or guess a slug
- The slug is randomly generated (e.g., `robust-mango-yzdq`)
- If `auth_mode=authenticated` and `persistence=permanent`, the link is permanent
- If `auth_mode=anonymous`, the link expires in 24 hours

## What NOT to Do
- ❌ NEVER make up a here.now URL (e.g., `daily-report-2026-03-18.here.now`) — this will 404
- ❌ NEVER assume a slug format — always run the publish script first
- ❌ NEVER post a link to the group before verifying it was returned by the script

## API Key
- Stored at `~/.herenow/credentials` (already configured)
- Auth mode: authenticated (permanent publishes)

## Updating an Existing Publish
```bash
bash ~/.agents/skills/here-now/scripts/publish.sh /tmp/my-report --slug {existing-slug}
```

## Integration with Daily Reports
- **ALL status reports** posted to the Premium Meds Collective group MUST include a working here.now link
- Generate the report HTML → publish via script → post the returned URL to the group
- This is non-negotiable for all agents (ICE, TR, SEO, Analytics, etc.)

## Skill Documentation
- Full skill docs: `~/.agents/skills/here-now/SKILL.md`
- Publish script: `~/.agents/skills/here-now/scripts/publish.sh`
