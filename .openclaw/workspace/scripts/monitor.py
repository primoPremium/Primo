#!/usr/bin/env python3
"""
WooCommerce Monitoring Script
Handles system monitoring, alerts, and reporting
"""

import os
import json
import time
from datetime import datetime
from woocommerce import API

def check_system_status():
    """Check WooCommerce system status"""
    wcapi = get_api_connection()
    return wcapi.get("system_status").json()

def monitor_inventory():
    """Monitor inventory levels and trigger alerts"""
    wcapi = get_api_connection()
    products = wcapi.get("products").json()
    
    alerts = []
    for product in products:
        if int(product.get('stock_quantity', 0)) < get_threshold(product['id']):
            alerts.append({
                'product_id': product['id'],
                'name': product['name'],
                'current_stock': product['stock_quantity'],
                'threshold': get_threshold(product['id'])
            })
    
    return alerts

def generate_report(report_type='daily'):
    """Generate monitoring report"""
    data = {
        'timestamp': datetime.now().isoformat(),
        'type': report_type,
        'system_status': check_system_status(),
        'inventory_alerts': monitor_inventory()
    }
    
    # Save report to file
    filename = f"reports/{report_type}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    return filename

def main():
    """Main monitoring loop"""
    while True:
        try:
            alerts = monitor_inventory()
            if alerts:
                send_alerts(alerts)
            time.sleep(300)  # Check every 5 minutes
        except Exception as e:
            log_error(e)

if __name__ == "__main__":
    main()