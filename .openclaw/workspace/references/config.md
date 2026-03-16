# Configuration Guide

## Environment Setup

### Required Environment Variables
```env
# WooCommerce API Credentials
WOOCOMMERCE_CONSUMER_KEY=your_consumer_key
WOOCOMMERCE_CONSUMER_SECRET=your_consumer_secret
WORDPRESS_API_URL=https://premiummedscollective.com/wp-json

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=/path/to/woocommerce.log

# Cache Settings
CACHE_DURATION=300  # 5 minutes in seconds
```

### Directory Structure
```
├── SKILL.md               # Main skill documentation
├── scripts/              # Python automation scripts
│   ├── utils.py         # Utility functions
│   ├── products.py      # Product management
│   ├── inventory.py     # Inventory tracking
│   ├── orders.py        # Order processing
│   └── reports.py       # Reporting functions
├── references/          # Documentation
│   ├── woo_api.md      # API reference
│   ├── config.md       # This configuration guide
│   └── troubleshooting.md
├── assets/             # Templates and resources
│   ├── templates/
│   │   ├── reports/
│   │   ├── emails/
│   │   └── alerts/
│   └── reports/        # Generated reports
```

## Security Configuration

### API Key Management
1. Generate API keys in WooCommerce:
   - WooCommerce > Settings > Advanced > REST API
   - Create new key with appropriate permissions
2. Store keys securely following credential_handling.md
3. Regular key rotation recommended

### Permission Levels
- READ: View products, orders, reports
- WRITE: Update products, process orders
- DELETE: Remove products, cancel orders

## Monitoring Configuration

### Alert Thresholds
```python
# Inventory alerts
LOW_STOCK_THRESHOLD = 5
CRITICAL_STOCK_THRESHOLD = 2

# Order alerts
FAILED_ORDER_THRESHOLD = 3  # Alerts if > 3 failed orders/day
PROCESSING_TIME_THRESHOLD = 48  # Hours before alert
```

### Logging Configuration
```python
# logging.conf
{
    "version": 1,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "woocommerce.log",
            "formatter": "detailed"
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple"
        }
    },
    "formatters": {
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "simple": {
            "format": "%(levelname)s - %(message)s"
        }
    }
}
```

## Performance Optimization

### Caching
- Default cache duration: 5 minutes
- Adjustable per endpoint:
  - Products: 5 minutes
  - Orders: 2 minutes
  - Reports: 15 minutes

### Batch Operations
- Use batch endpoints for bulk updates
- Maximum 100 items per batch
- Implement retry logic for failures

## Report Configuration

### Report Types
1. Sales Reports
   - Daily, Weekly, Monthly
   - Revenue, Orders, Average Order Value
2. Inventory Reports
   - Stock levels
   - Low stock alerts
   - Product performance
3. Alert Reports
   - Stock alerts
   - Order processing issues
   - System health

### Report Storage
- Format: JSON
- Location: assets/reports/
- Naming: {report_type}_{timestamp}.json
- Retention: 90 days