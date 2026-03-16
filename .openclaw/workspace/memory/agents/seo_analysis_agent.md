# SEO Analysis Agent Configuration

## Purpose
Automated SEO analysis and reporting for cannabis delivery services in Orange County, with focus on competitive positioning and market opportunities.

## Analysis Parameters
### Target Keywords
- Primary focus: Cannabis delivery in Orange County
- Related terms: marijuana delivery, weed delivery, cannabis dispensary
- Geographic scope: Orange County, CA and surrounding areas
- Local service areas and neighborhoods

### Analysis Components
1. Competitor Ranking Analysis
   - Track top 10 competitors' positions
   - Monitor ranking changes
   - Identify ranking patterns

2. Local Market Position
   - Geographic coverage analysis
   - Service area optimization
   - Local pack rankings

3. Opportunity Identification
   - Keyword gaps
   - Featured snippet opportunities
   - Local SEO optimization potential

## Reporting Configuration
### Output Specifications
- File Path: memory/seo/YYYY-MM-DD_keyword_analysis.md
- Format: Markdown
- Frequency: Every 2 days
- Runtime Limit: 45 minutes

### Report Structure
1. Executive Summary
   - Overall ranking health
   - Key changes since last report
   - Priority action items

2. Detailed Rankings Table
   - Keyword positions
   - Position changes
   - Search volume
   - Competition metrics

3. Competitor Analysis
   - Top competitor movements
   - Strategy insights
   - Market share analysis

4. Recommendations
   - Prioritized action items
   - Quick wins
   - Strategic opportunities

### Distribution
- Auto-post to Telegram group: -1003809781298
- Format: Markdown-formatted message
- Include key metrics and changes

## Technical Implementation
### Execution Schedule
- Frequency: Every 2 days
- Preferred execution time: 02:00 UTC
- Maximum runtime: 45 minutes

### Error Handling
1. Search Failure Recovery
   - Maximum retry attempts: 3
   - Retry delay: 5 minutes
   - Exponential backoff: 1.5x

2. Alert System
   - Trigger conditions:
     * 3 consecutive failed runs
     * Data anomaly detection
     * Runtime exceeding 80% of limit
   - Alert destination: Same Telegram group

3. Data Validation
   - Required data points check
   - Historical data consistency
   - Competitor data presence
   - Geographic coverage verification

### Data Storage
- Base Directory: memory/seo/
- Naming Convention: YYYY-MM-DD_keyword_analysis.md
- Archive Policy: Retain 90 days

## Recovery Procedures
1. Failed Run Recovery
   - Log failure reason
   - Attempt targeted rerun of failed components
   - Fall back to partial report if necessary

2. Data Validation Failures
   - Log invalid data points
   - Use last known good data where appropriate
   - Flag unreliable metrics in report

3. Timeout Handling
   - Save partial results
   - Prioritize essential metrics
   - Include completion status in report