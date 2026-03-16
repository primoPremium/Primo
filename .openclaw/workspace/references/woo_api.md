# WooCommerce API Reference

## Authentication
```env
WOOCOMMERCE_CONSUMER_KEY=your_consumer_key
WOOCOMMERCE_CONSUMER_SECRET=your_consumer_secret
WORDPRESS_API_URL=https://premiummedscollective.com/wp-json
```

## Endpoints

### Products
- `GET /wp-json/wc/v3/products` - List products
- `GET /wp-json/wc/v3/products/<id>` - Get single product
- `POST /wp-json/wc/v3/products` - Create product
- `PUT /wp-json/wc/v3/products/<id>` - Update product
- `DELETE /wp-json/wc/v3/products/<id>` - Delete product
- `POST /wp-json/wc/v3/products/batch` - Batch update products

### Orders
- `GET /wp-json/wc/v3/orders` - List orders
- `GET /wp-json/wc/v3/orders/<id>` - Get single order
- `PUT /wp-json/wc/v3/orders/<id>` - Update order
- `GET /wp-json/wc/v3/orders/<id>/notes` - Get order notes
- `POST /wp-json/wc/v3/orders/<id>/notes` - Create order note
- `POST /wp-json/wc/v3/orders/<id>/refunds` - Create refund

## Common Parameters

### Product Parameters
```json
{
    "name": "Product Name",
    "regular_price": "29.99",
    "description": "Product description",
    "stock_quantity": 100,
    "manage_stock": true,
    "stock_status": "instock"
}
```

### Order Parameters
```json
{
    "status": "processing",
    "customer_note": "Customer provided note",
    "meta_data": [
        {
            "key": "custom_field",
            "value": "custom value"
        }
    ]
}
```

## Status Codes
- 200: Success
- 201: Created
- 400: Bad request
- 401: Unauthorized
- 404: Not found
- 500: Server error

## Rate Limiting
- Default: 25 requests per second
- Batch operations recommended for bulk updates
- Use caching when possible

## Error Handling
```json
{
    "code": "woocommerce_rest_invalid_id",
    "message": "Invalid ID.",
    "data": {
        "status": 404
    }
}
```

## Best Practices
1. Always use HTTPS
2. Implement error handling
3. Use batch operations for bulk updates
4. Cache responses when possible
5. Handle rate limiting
6. Validate input data
7. Log API interactions