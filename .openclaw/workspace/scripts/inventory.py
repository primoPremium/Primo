from typing import Dict, List, Optional
from .utils import WooCommerceAPI, cache, logger

class InventoryManager:
    def __init__(self):
        self.api = WooCommerceAPI()
        self.alert_thresholds = {}

    def get_stock_status(self, product_id: Optional[int] = None) -> Dict:
        """Get stock status for one or all products"""
        if product_id:
            cache_key = f"stock_{product_id}"
            cached = cache.get(cache_key)
            if cached:
                return cached

            product = self.api._make_request(f'products/{product_id}')
            stock_info = {
                'product_id': product_id,
                'name': product['name'],
                'stock_quantity': product.get('stock_quantity', 0),
                'stock_status': product['stock_status']
            }
            cache.set(cache_key, stock_info)
            return stock_info
        else:
            # Get all products with stock info
            products = self.api._make_request(
                'products',
                params={'status': 'publish', 'per_page': 100}
            )
            return [{
                'product_id': p['id'],
                'name': p['name'],
                'stock_quantity': p.get('stock_quantity', 0),
                'stock_status': p['stock_status']
            } for p in products]

    def update_stock(self, product_id: int, quantity: int) -> Dict:
        """Update product stock quantity"""
        data = {
            'stock_quantity': quantity,
            'stock_status': 'instock' if quantity > 0 else 'outofstock'
        }
        
        result = self.api._make_request(
            f'products/{product_id}',
            method='PUT',
            data=data
        )
        cache.clear()  # Invalidate stock cache
        
        # Check alert threshold
        self.check_alert_threshold(product_id, quantity)
        
        return result

    def set_alert_threshold(self, product_id: int, threshold: int):
        """Set low stock alert threshold"""
        self.alert_thresholds[product_id] = threshold
        current_stock = self.get_stock_status(product_id)
        self.check_alert_threshold(
            product_id, 
            current_stock['stock_quantity']
        )

    def check_alert_threshold(self, product_id: int, quantity: int):
        """Check if stock is below threshold and log alert"""
        if product_id in self.alert_thresholds:
            threshold = self.alert_thresholds[product_id]
            if quantity <= threshold:
                product = self.api._make_request(f'products/{product_id}')
                logger.warning(
                    f"Low stock alert: {product['name']} "
                    f"(ID: {product_id}) - "
                    f"Current stock: {quantity}, "
                    f"Threshold: {threshold}"
                )

    def batch_update_stock(self, updates: List[Dict[str, int]]) -> Dict:
        """Batch update stock quantities"""
        batch_data = {
            'update': [
                {
                    'id': item['product_id'],
                    'stock_quantity': item['quantity']
                }
                for item in updates
            ]
        }
        
        result = self.api._make_request(
            'products/batch',
            method='POST',
            data=batch_data
        )
        cache.clear()
        
        # Check thresholds after update
        for item in updates:
            self.check_alert_threshold(
                item['product_id'],
                item['quantity']
            )
        
        return result