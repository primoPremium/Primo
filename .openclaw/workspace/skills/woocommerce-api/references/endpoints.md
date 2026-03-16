# WooCommerce REST API Endpoints

## Products

### List Products
GET /wp-json/wc/v3/products
- Query parameters:
  - per_page (default: 10, max: 100)
  - page
  - search
  - after, before (ISO8601 Date)
  - order (asc/desc)
  - orderby (date, id, title, slug)

### Get Product
GET /wp-json/wc/v3/products/{id}

### Create Product
POST /wp-json/wc/v3/products
```json
{
    "name": "Product Name",
    "type": "simple",
    "regular_price": "29.99",
    "description": "Product description",
    "short_description": "Short description",
    "categories": [
        {"id": category_id}
    ]
}
```

## Orders

### List Orders
GET /wp-json/wc/v3/orders
- Query parameters:
  - status
  - customer
  - after, before
  - per_page, page

### Get Order
GET /wp-json/wc/v3/orders/{id}

### Create Order
POST /wp-json/wc/v3/orders

## Customers

### List Customers
GET /wp-json/wc/v3/customers

### Get Customer
GET /wp-json/wc/v3/customers/{id}

## Reports

### Sales Report
GET /wp-json/wc/v3/reports/sales
- Parameters:
  - date_min
  - date_max
  - period (week, month, year)

### Top Sellers
GET /wp-json/wc/v3/reports/top_sellers
- Parameters:
  - period
  - limit

## Categories

### List Categories
GET /wp-json/wc/v3/products/categories

### Get Category
GET /wp-json/wc/v3/products/categories/{id}