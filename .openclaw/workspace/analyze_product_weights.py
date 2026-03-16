import os
import requests
from collections import defaultdict
from datetime import datetime

# Get credentials from environment
api_key = os.getenv('WP_WOO_API_KEY')
api_secret = os.getenv('WP_WOO_API_SECRET')
base_url = 'https://premiummedscollective.com/wp-json/wc/v3'

# Initialize session with authentication
session = requests.Session()
session.auth = (api_key, api_secret)

def fetch_all_orders():
    page = 1
    orders = []
    while True:
        response = session.get(f"{base_url}/orders", params={
            'page': page,
            'per_page': 100,
            'status': 'completed'
        })
        if not response.json():
            break
        orders.extend(response.json())
        page += 1
    return orders

def analyze_products():
    orders = fetch_all_orders()
    product_stats = defaultdict(lambda: {
        'name': '',
        'total_weight': 0,
        'order_count': 0,
        'total_orders': 0
    })
    
    total_weight = 0
    
    for order in orders:
        for item in order.get('line_items', []):
            product_id = item['product_id']
            quantity = item['quantity']
            
            # Get product weight
            product_response = session.get(f"{base_url}/products/{product_id}")
            product = product_response.json()
            weight = float(product.get('weight', 0))
            
            product_stats[product_id]['name'] = item['name']
            product_stats[product_id]['total_weight'] += weight * quantity
            product_stats[product_id]['order_count'] += 1
            product_stats[product_id]['total_orders'] += quantity
            total_weight += weight * quantity

    # Convert to list and sort by total weight
    products_list = [
        {
            'name': stats['name'],
            'total_weight': stats['total_weight'],
            'percentage': (stats['total_weight'] / total_weight * 100) if total_weight > 0 else 0,
            'order_count': stats['order_count'],
            'avg_order_size': stats['total_weight'] / stats['order_count'] if stats['order_count'] > 0 else 0
        }
        for product_id, stats in product_stats.items()
    ]
    
    return sorted(products_list, key=lambda x: x['total_weight'], reverse=True)[:10]

def generate_report():
    products = analyze_products()
    report = "🏆 *TOP 10 PRODUCTS BY WEIGHT REPORT*\n"
    report += f"Generated on: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n\n"
    
    for i, product in enumerate(products, 1):
        report += f"*{i}. {product['name']}*\n"
        report += f"• Total Weight: {product['total_weight']:.2f} kg\n"
        report += f"• Sales Volume: {product['percentage']:.1f}%\n"
        report += f"• Orders: {product['order_count']}\n"
        report += f"• Avg Order: {product['avg_order_size']:.2f} kg\n\n"
    
    return report

if __name__ == '__main__':
    print(generate_report())