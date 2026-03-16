# WooCommerce API Error Codes

## Authentication Errors

- `401 Unauthorized`: Invalid API keys or incorrect authentication method
- `403 Forbidden`: Valid credentials but insufficient permissions

### Common Fixes
1. Verify WP_WOO_API_KEY and WP_WOO_API_SECRET are correct
2. Check API key permissions in WooCommerce settings
3. Ensure HTTPS is properly configured

## Rate Limiting

- `429 Too Many Requests`: API request limit exceeded
- Default: 25 requests per second

### Best Practices
1. Implement request throttling
2. Cache frequently accessed data
3. Use bulk operations where possible

## Common Operation Errors

### Products
- `400 Bad Request`: Invalid product data
- `404 Not Found`: Product ID doesn't exist
- `409 Conflict`: SKU already exists

### Orders
- `400 Bad Request`: Invalid order data
- `404 Not Found`: Order ID doesn't exist
- `409 Conflict`: Order number already exists

### Categories
- `400 Bad Request`: Invalid category data
- `404 Not Found`: Category ID doesn't exist

## Network Issues

- `Connection refused`: API endpoint unreachable
- `ETIMEDOUT`: Request timed out
- `ENOTFOUND`: DNS resolution failed

### Troubleshooting Steps
1. Verify API URL is correct
2. Check network connectivity
3. Validate SSL certificate
4. Check server firewall settings