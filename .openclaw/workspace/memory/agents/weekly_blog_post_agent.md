# Weekly Blog Post Agent — Configuration

## Purpose
Publish one original blog post per week to premiummedscollective.com, inspired by a competitor's recent blog post. Each post is our own take — never a copy.

## Cadence
- **Frequency:** Weekly
- **Day:** Every Monday
- **Draft ready by:** 10:00 AM PT Monday
- **Publish by:** 12:00 PM PT Monday
- **Group digest posted:** Immediately after publish

## Process (each week)
1. **Scout** — Search competitor blogs (Eaze, Hyperwolf, Grassdoor, Amuse, Weedmaps, Leafly, local OC dispensaries) for a recent, high-quality blog post worth modeling.
2. **Select** — Pick one post that aligns with Premium Meds' audience (OC cannabis consumers, productivity, wellness, education, product guides, seasonal topics).
3. **Draft** — Write a 1800–2500 word original blog post modeled after the competitor's structure, tone, and depth. Tailor to Premium Meds brand voice (professional, warm, knowledgeable, not salesy). Include:
   - H2 section headers
   - Terpene/product education where relevant
   - Responsible use messaging with credible sources
   - Internal links to /shop/, city delivery pages (/delivery-mission-viejo/, /delivery-irvine/, etc.)
   - FAQ section (5-6 questions)
   - Soft CTA at the end
   - Orange County / South OC woven in naturally
4. **SEO** — Before publishing:
   - Write a meta description (~160 chars)
   - Assign relevant category and tags
   - Fetch and upload a fresh hero image
   - Set featured image on the post
5. **Publish** — Push as published via WP REST API
6. **Announce** — Post a digest to Premium Meds Collective Telegram group (-1003809781298) with:
   - Title and summary bullets
   - Live post URL
   - Shop CTA
   - Primo signature
7. **Log** — Record in memory/blog_drafts/publish_log.md:
   - Date, title, competitor source post URL, our post URL, tags, group message ID

## Competitor Blog Sources (rotation)
- https://www.eaze.com/blog (or /article/)
- https://www.hyperwolf.com/blog
- https://www.grassdoor.com/blog
- https://weedmaps.com/learn
- https://www.leafly.com/news
- Local OC dispensary blogs as discovered

## Brand Voice
- Professional but approachable — like talking to a smart friend
- Knowledgeable with honest caveats (especially around health/science claims)
- OC-local flavor throughout
- Never copy competitor text — always original

## WordPress Details
- API: WP REST API v2
- Credentials: WP_REST_API_USER / WP_REST_API_PASS in ~/.env
- Default category: 41 (Delivery — or create topic-specific)
- Author: Primo PremiumMedsCollective (user 150)
- Post format: HTML content, published status
- Slug convention: lowercase-hyphenated-topic-keywords

## Tags Created So Far
- 42: focus
- 43: productivity
- 44: cannabis
- 45: orange county
- 46: deep work
- 47: microdosing

## First Post (reference)
- Title: Focus Mode: How to Choose Cannabis for Productivity and Deep Work
- Competitor source: https://www.eaze.com/article/focus-mode-terpenes-formats-deep-work
- Our URL: https://premiummedscollective.com/news/focus-mode-cannabis-productivity-deep-work/
- Post ID: 14076
- Published: 2026-03-29

## Created
2026-03-29 by Primo
