# WooCommerce REST API Integration Documentation

## API Endpoint Structure
Base URL: `https://premiummedscollective.com/wp-json/wc/v3/`

## Authentication
- Authentication Method: OAuth 1.0a or Consumer Key/Secret
- Required Headers:
  - `Authorization`: OAuth credentials
  - `Content-Type`: application/json

### API Keys Setup
1. Generate API keys in WooCommerce → Settings → Advanced → REST API
2. Store credentials securely in environment variables:
  - `WC_CONSUMER_KEY`
  - `WC_CONSUMER_SECRET`

## Key Endpoints

### Products
- List Products: `GET /products`
- Single Product: `GET /products/<id>`
- Product Variations: `GET /products/<id>/variations`
- Product Categories: `GET /products/categories`

### Orders
- List Orders: `GET /orders`
- Single Order: `GET /orders/<id>`
- Create Order: `POST /orders`
- Update Order: `PUT /orders/<id>`

### Inventory
- Stock Levels: `GET /products/<id>` (includes stock_quantity)
- Batch Update: `POST /products/batch`

## Data Refresh Intervals
- Inventory Status: Every 5 minutes
- Order Status: Real-time
- Product Updates: Every 15 minutes
- Analytics Data: Hourly

## Error Handling Procedures

### Common HTTP Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 429: Too Many Requests
- 500: Server Error

### Error Handling Strategy
1. Implement exponential backoff for rate limits
2. Cache valid responses
3. Log all API errors with:
   - Timestamp
   - Endpoint
   - Error code
   - Response body
   - Request parameters

### Rate Limiting
- Default: 25 requests per second
- Batch operations recommended for bulk updates
- Monitor X-RateLimit headers

### Recovery Procedures
1. Network Errors: Retry with exponential backoff
2. Authentication Errors: Refresh credentials
3. Rate Limits: Queue requests and process within limits
4. Data Validation: Log and alert for manual review

## Response Format
```json
{
  "id": 123,
  "name": "Sample Product",
  "type": "simple",
  "status": "publish",
  "price": "19.99",
  "regular_price": "24.99",
  "stock_quantity": 15,
  "stock_status": "instock"
}
```