from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
from .utils import WooCommerceAPI, logger
from .orders import OrderManager
from .inventory import InventoryManager
from .products import ProductManager

class ReportGenerator:
    def __init__(self):
        self.api = WooCommerceAPI()
        self.orders = OrderManager()
        self.inventory = InventoryManager()
        self.products = ProductManager()

    def generate_sales_report(self, period: str = 'week') -> Dict:
        """Generate sales report for specified period"""
        periods = {
            'day': 1,
            'week': 7,
            'month': 30,
            'quarter': 90
        }
        
        if period not in periods:
            raise ValueError(f"Invalid period. Valid periods: {list(periods.keys())}")

        metrics = self.orders.get_order_metrics(days=periods[period])
        
        report = {
            'period': period,
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_orders': metrics['total_orders'],
                'total_revenue': round(metrics['total_revenue'], 2),
                'average_order_value': round(
                    metrics['total_revenue'] / metrics['total_orders']
                    if metrics['total_orders'] > 0 else 0,
                    2
                )
            },
            'status_distribution': metrics['status_breakdown'],
            'daily_revenue': metrics['daily_totals']
        }
        
        # Save report
        self._save_report('sales', report)
        return report

    def generate_inventory_report(self) -> Dict:
        """Generate inventory status report"""
        stock_status = self.inventory.get_stock_status()
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_products': len(stock_status),
                'out_of_stock': len([
                    p for p in stock_status 
                    if p['stock_status'] == 'outofstock'
                ]),
                'low_stock': len([
                    p for p in stock_status
                    if p['stock_quantity'] is not None
                    and p['stock_quantity'] <= 5
                    and p['stock_quantity'] > 0
                ])
            },
            'stock_levels': {
                p['name']: {
                    'quantity': p['stock_quantity'],
                    'status': p['stock_status']
                }
                for p in stock_status
            }
        }
        
        # Save report
        self._save_report('inventory', report)
        return report

    def generate_alert_report(self) -> Dict:
        """Generate current alerts report"""
        stock_status = self.inventory.get_stock_status()
        order_metrics = self.orders.get_order_metrics(days=1)
        
        alerts = {
            'generated_at': datetime.now().isoformat(),
            'inventory_alerts': [
                {
                    'product_name': p['name'],
                    'current_stock': p['stock_quantity'],
                    'status': p['stock_status']
                }
                for p in stock_status
                if p['stock_quantity'] is not None 
                and p['stock_quantity'] <= 5
            ],
            'order_alerts': [
                {
                    'status': status,
                    'count': count
                }
                for status, count in order_metrics['status_breakdown'].items()
                if status in ['failed', 'cancelled']
            ]
        }
        
        # Save report
        self._save_report('alerts', alerts)
        return alerts

    def _save_report(self, report_type: str, data: Dict):
        """Save report to file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"../assets/reports/{report_type}_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Report saved: {filename}")
        except Exception as e:
            logger.error(f"Failed to save report: {str(e)}")

    def get_performance_metrics(self) -> Dict:
        """Get overall store performance metrics"""
        orders_30d = self.orders.get_order_metrics(days=30)
        orders_7d = self.orders.get_order_metrics(days=7)
        stock_status = self.inventory.get_stock_status()
        
        return {
            'generated_at': datetime.now().isoformat(),
            'monthly_metrics': {
                'revenue': round(orders_30d['total_revenue'], 2),
                'orders': orders_30d['total_orders'],
                'avg_order_value': round(
                    orders_30d['total_revenue'] / orders_30d['total_orders']
                    if orders_30d['total_orders'] > 0 else 0,
                    2
                )
            },
            'weekly_metrics': {
                'revenue': round(orders_7d['total_revenue'], 2),
                'orders': orders_7d['total_orders']
            },
            'inventory_health': {
                'total_products': len(stock_status),
                'out_of_stock': len([
                    p for p in stock_status 
                    if p['stock_status'] == 'outofstock'
                ]),
                'low_stock': len([
                    p for p in stock_status
                    if p['stock_quantity'] is not None
                    and p['stock_quantity'] <= 5
                ])
            }
        }