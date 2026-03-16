---
name: woocommerce-api
description: WooCommerce REST API integration for e-commerce operations. Use when needing to: (1) Access product data, (2) Manage orders, (3) Handle customer information, (4) Generate sales reports, (5) Track inventory, or (6) Any other WooCommerce-specific operations. Includes analytics, logging, and error handling.
---

# WooCommerce API Skill

## Installation

1. Extract the skill:
```bash
cd ~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/skills/
tar xzf woocommerce-api.tar.gz
cd woocommerce-api
```

2. Run the installer:
```bash
chmod +x install.sh
./install.sh
```

This will:
- Create required directories
- Install Node.js dependencies
- Set up a sample .env if needed

## Configuration

1. Get your API credentials:
   - Go to WooCommerce > Settings > Advanced > REST API
   - Create a new key with read permissions
   - Copy the Consumer Key and Consumer Secret

2. Add to your .env:
```bash
WP_WOO_API_KEY=your_api_key
WP_WOO_API_SECRET=your_api_secret
```

## Quick Start

```javascript
const WooCommerceAPI = require('./scripts/wc-api-client.js');

// Initialize client
const api = new WooCommerceAPI({
    apiKey: process.env.WP_WOO_API_KEY,
    apiSecret: process.env.WP_WOO_API_SECRET
});

// Get products
const products = await api.getProducts();

// Get orders
const orders = await api.getOrders();
```

## Analytics Features

```javascript
const WooCommerceAnalytics = require('./scripts/wc-analytics.js');

const analytics = new WooCommerceAnalytics(api);

// Get top selling products
const topSellers = await analytics.getTopSellingProducts(12);

// Get sales trends by category
const trends = await analytics.getSalesTrendsByCategory(30);

// Get low stock alerts
const alerts = await analytics.getInventoryAlerts(5);
```

## Error Handling

All API requests include:
- Request logging (in ./logs)
- Error tracking
- Rate limiting protection
- Network error handling

See references/error-codes.md for common errors and solutions.

## Available Scripts

1. wc-api-client.js
   - Core API client with authentication
   - Basic CRUD operations
   - Request/response logging

2. wc-analytics.js
   - Sales analytics
   - Inventory tracking
   - Trend analysis

## References

- error-codes.md: Common errors and troubleshooting
- endpoints.md: Complete API endpoint reference

## Assets

- request-templates/: JSON templates for common operations
- postman/: Postman collection for testing

## Notes

1. Always check error-codes.md first when troubleshooting
2. Use analytics for regular reporting
3. Keep logs for debugging