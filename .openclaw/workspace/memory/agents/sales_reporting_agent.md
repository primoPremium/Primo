# Sales Reporting Agent Configuration

## Purpose
Generate daily sales analysis reports for Premium Meds, focusing on inventory movement, pricing effectiveness, and actionable insights.

## Schedule
- Runs daily at 6:00 AM UTC
- Report delivery by 6:30 AM UTC
- Data cutoff: Previous day 11:59 PM UTC

## Data Collection Points

### 1. Sales Metrics
- Daily sales volume
- Revenue by category
- Units sold by product
- Average order value
- Conversion rates

### 2. Inventory Status
- Current stock levels
- Low stock alerts (< 20 units)
- Days of inventory remaining
- Reorder recommendations

### 3. Pricing Analysis
- Regular price performance
- Promotional effectiveness
- Margin analysis
- Competitive positioning

### 4. Product Performance
- Top 10 by units
- Top 10 by revenue
- Top 10 by weight/volume
- New product performance

### 5. Category Analysis
- Category share of sales
- Growth rates
- Margin contribution
- Inventory turns

## Report Structure

### Daily Sales Snapshot
```markdown
# Daily Sales Report
Date: [YYYY-MM-DD]
Report Generated: [TIMESTAMP]

## 📊 Sales Performance
- Total Sales: $XXX
- Units Sold: XXX
- Average Order Value: $XXX
- Top Selling Product: [PRODUCT_NAME]

## 🏆 Top Performers
1. [PRODUCT] - [UNITS] units, $[REVENUE]
2. [PRODUCT] - [UNITS] units, $[REVENUE]
3. [PRODUCT] - [UNITS] units, $[REVENUE]

## 📦 Inventory Alerts
- Low Stock: [PRODUCTS]
- Out of Stock: [PRODUCTS]
- Reorder Needed: [PRODUCTS]

## 💰 Promotion Performance
- Active Promos: [COUNT]
- Best Performing: [PROMO]
- Revenue Impact: $[AMOUNT]

## 🎯 Recommendations
1. [ACTION_ITEM]
2. [ACTION_ITEM]
3. [ACTION_ITEM]
```

## Monitoring Metrics

### Key Performance Indicators
1. Sales Growth
   - Daily % change
   - Week-over-week
   - Month-over-month

2. Inventory Health
   - Stock turnover
   - Days of inventory
   - Dead stock alerts

3. Pricing Effectiveness
   - Margin achievement
   - Promotion ROI
   - Price elasticity

4. Category Performance
   - Category mix
   - Growth rates
   - Profitability

## Alert Thresholds

### Inventory Alerts
- Low Stock: < 20 units
- Critical: < 10 units
- Overstock: > 90 days supply

### Performance Alerts
- Sales Decline: > 20% day-over-day
- Margin Drop: > 5% below target
- Zero Sales: 3+ consecutive days

## Report Delivery
1. Generated to memory/sales_analysis/YYYY-MM-DD_daily_report.md
2. Critical alerts highlighted at top
3. Actionable recommendations included
4. Previous day comparison included

## Data Sources
- WooCommerce sales data
- Inventory management system
- Pricing database
- Historical sales records

## AI Provider Settings
- Provider: OpenRouter
- Model: openrouter/anthropic/claude-3.5-sonnet
- Timeout: 30 minutes
- Error handling: Retry once on connection failure

## Security & Compliance
- No customer PII included
- Revenue rounded to nearest dollar
- Sensitive data excluded
- Access restricted to management

## Continuous Improvement
- Track report usage
- Monitor recommendation implementation
- Gather feedback
- Update metrics as needed

## Template Example
```markdown
# Daily Sales Analysis
Date: [DATE]

## Executive Summary
Brief overview of key metrics and changes

## Sales Performance
Detailed breakdown of sales metrics

## Product Analysis
Top performers and concerns

## Inventory Status
Current stock levels and alerts

## Recommendations
Actionable items for today

## Historical Comparison
Previous day and week comparison
```

## Success Metrics
- Report delivered by 6:30 AM UTC
- All critical data points included
- Actionable recommendations provided
- No missing data points
- Accurate calculations

---
Last Updated: February 27, 2026
Review Frequency: Monthly