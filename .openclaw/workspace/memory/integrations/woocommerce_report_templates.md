# WooCommerce Report Templates

## Daily Sales Summary Template
```markdown
# Daily Sales Report - {DATE}

## Overview
- Total Orders: {COUNT}
- Total Revenue: ${AMOUNT}
- Average Order Value: ${AOV}
- Total Items Sold: {ITEMS}

## Performance Metrics
- Conversion Rate: {RATE}%
- Cart Abandonment: {ABANDON}%
- Peak Sales Hour: {HOUR}

## Top Products
1. {PRODUCT_1}: {QUANTITY} units (${REVENUE})
2. {PRODUCT_2}: {QUANTITY} units (${REVENUE})
3. {PRODUCT_3}: {QUANTITY} units (${REVENUE})

## Inventory Alerts
- Critical Stock: {LIST}
- Low Stock: {LIST}
```

## Product Ranking Template
```markdown
# Product Performance by Weight - {DATE}

## Top Sellers by Volume
1. {PRODUCT}: {WEIGHT}g sold
2. {PRODUCT}: {WEIGHT}g sold
3. {PRODUCT}: {WEIGHT}g sold

## Top Sellers by Revenue
1. {PRODUCT}: ${REVENUE}
2. {PRODUCT}: ${REVENUE}
3. {PRODUCT}: ${REVENUE}

## Stock Efficiency
- Best Stock/Sales Ratio: {PRODUCT}
- Needs Restock Soon: {LIST}
```

## Inventory Alert Template
```markdown
# Inventory Status Alert - {TIMESTAMP}

## Critical Alerts
- {PRODUCT}: {QUANTITY} remaining
- Expected stockout: {HOURS} hours
- Reorder quantity recommended: {UNITS}

## Warning Alerts
- {PRODUCT}: {QUANTITY} remaining
- Current sales velocity: {UNITS}/day
- Reorder window: {DAYS} days

## Action Required
[ ] Place reorder for {PRODUCTS}
[ ] Adjust stock levels
[ ] Review sales velocity
```

## Trend Analysis Template
```markdown
# Sales Trend Analysis - {PERIOD}

## Period Comparison
- Current Period: ${AMOUNT}
- Previous Period: ${AMOUNT}
- YoY Change: {PERCENT}%

## Product Category Trends
### Growing Categories
1. {CATEGORY}: +{PERCENT}%
2. {CATEGORY}: +{PERCENT}%

### Declining Categories
1. {CATEGORY}: -{PERCENT}%
2. {CATEGORY}: -{PERCENT}%

## Customer Insights
- New Customers: {COUNT}
- Repeat Purchase Rate: {RATE}%
- Average Items Per Order: {COUNT}

## Recommendations
1. {ACTION_ITEM}
2. {ACTION_ITEM}
3. {ACTION_ITEM}
```