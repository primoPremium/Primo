# WordPress Agent Configuration

## 🔐 Site Access
### WordPress Admin
- Site URL: https://premiummedscollective.com/wp-admin
- Admin Path: /wp-admin
- Required Credentials:
  - Username: [CONFIGURED IN ENV]
  - Password: [CONFIGURED IN ENV]
  - Role: Administrator

### Database Access
- Host: localhost
- Database: u934417329_premium
- Username: [CONFIGURED IN ENV]
- Password: [CONFIGURED IN ENV]
- Port: 3306

## 🛠️ WP-CLI Configuration
### Environment Setup
```bash
# Load credentials from .env
source ~/.env

# Site path (to be confirmed)
WP_SITE_PATH="/var/www/html/premiummedscollective.com"

# Base command with authentication
WP_BASE_CMD="wp --allow-root --path=$WP_SITE_PATH --url=https://premiummedscollective.com --user=$WP_CLI_USER --password=$WP_CLI_PASS"
```

### Common Commands
```bash
# List all products
$WP_BASE_CMD wc product list

# Get product sales
$WP_BASE_CMD wc product list --fields=name,total_sales,regular_price,weight --orderby=total_sales --order=DESC

# Get specific product data
$WP_BASE_CMD wc product get <id> --format=json

# Update product
$WP_BASE_CMD wc product update <id> --field=<field> --value=<value>
```

## 📊 Data Collection Methods
### WooCommerce API
```php
// API Credentials loaded from environment
define('WC_API_KEY', getenv('WP_CLI_USER'));
define('WC_API_SECRET', getenv('WP_CLI_PASS'));

// API Endpoints
$WC_PRODUCTS_ENDPOINT = '/wp-json/wc/v3/products';
$WC_ORDERS_ENDPOINT = '/wp-json/wc/v3/orders';
$WC_REPORTS_ENDPOINT = '/wp-json/wc/v3/reports';
```

### Product Data Queries
```sql
-- Top Products by Units Sold
SELECT 
    p.post_title,
    SUM(order_item_meta__qty.meta_value) as quantity,
    SUM(order_item_meta__line_total.meta_value) as total_sales
FROM 
    wp_posts as p
    INNER JOIN wp_woocommerce_order_items as order_items ON p.ID = order_items.order_item_id
    INNER JOIN wp_woocommerce_order_itemmeta as order_item_meta__qty ON order_items.order_item_id = order_item_meta__qty.order_item_id
    INNER JOIN wp_woocommerce_order_itemmeta as order_item_meta__line_total ON order_items.order_item_id = order_item_meta__line_total.order_item_id
WHERE 
    p.post_type = 'product'
GROUP BY 
    p.ID
ORDER BY 
    quantity DESC
LIMIT 10;
```

## 📈 Metrics to Track
1. Sales Metrics
   - Units sold
   - Revenue
   - Weight/volume sold
   - Average order value

2. Product Performance
   - Best sellers by category
   - Sales velocity
   - Stock turnover
   - Price point performance

3. Customer Behavior
   - Popular combinations
   - Time of purchase
   - Category preferences
   - Repeat purchases

## 🔄 Update Procedures
### Daily Tasks
- Update sales metrics
- Check inventory levels
- Monitor product performance
- Update stock status

### Weekly Tasks
- Generate sales reports
- Update top products list
- Review product performance
- Check for low stock

### Monthly Tasks
- Full sales analysis
- Category performance review
- Update product rankings
- Trend analysis

## 🔒 Security Notes
- Credentials stored in ~/.env
- Never commit credentials to repo
- Use environment variables for sensitive data
- Regular credential rotation recommended

## 📝 Logging
### Log Locations
- WordPress Logs: /var/log/wordpress/
- WooCommerce Logs: /var/www/html/premiummedscollective.com/wp-content/uploads/wc-logs/
- Access Logs: /var/log/apache2/

### Log Rotation
- Frequency: Daily
- Retention: 30 days
- Compression: Yes

---
Last Updated: February 27, 2026
Next Review: March 27, 2026