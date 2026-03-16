import os
from woocommerce import API
import json
from collections import defaultdict
import sys

try:
    # Get credentials from environment variables
    consumer_key = os.getenv('WP_WOO_API_KEY')
    consumer_secret = os.getenv('WP_WOO_API_SECRET')
    
    if not consumer_key or not consumer_secret:
        print("Error: WooCommerce API credentials not found in environment variables")
        sys.exit(1)
        
    site_url = "https://premiummedscollective.com"

    # Initialize WooCommerce API with increased timeout
    wcapi = API(
        url=site_url,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        version="wc/v3",
        timeout=30
    )

    # Get all products with increased timeout
    response = wcapi.get("products", params={"per_page": 100})
    
    if response.status_code != 200:
        print(f"Error: API returned status code {response.status_code}")
        print(response.text)
        sys.exit(1)
        
    products = response.json()

    # Initialize counters
    active_count = 0
    category_counts = defaultdict(int)
    stock_status = {
        'instock': 0,
        'outofstock': 0,
        'onbackorder': 0
    }

    # Process products
    for product in products:
        if product['status'] == 'publish':
            active_count += 1
            
            # Count categories
            for category in product['categories']:
                category_counts[category['name']] += 1
                
            # Count stock status
            status = product['stock_status']
            stock_status[status] += 1

    # Prepare results
    results = {
        'total_active_products': active_count,
        'category_counts': dict(category_counts),
        'stock_status': stock_status
    }

    # Write results to file
    with open('woo_results.json', 'w') as f:
        json.dump(results, f, indent=2)
        
    print("Success! Results saved to woo_results.json")
    
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)