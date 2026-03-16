from typing import Dict, List, Optional
from datetime import datetime
from .utils import WooCommerceAPI, cache, logger

class OrderManager:
    def __init__(self):
        self.api = WooCommerceAPI()
        self.valid_statuses = [
            'pending', 'processing', 'on-hold', 'completed',
            'cancelled', 'refunded', 'failed'
        ]

    def list_orders(self, status: Optional[str] = None, 
                   page: int = 1, per_page: int = 10) -> List[Dict]:
        """List orders with filtering and pagination"""
        params = {'page': page, 'per_page': per_page}
        if status:
            if status not in self.valid_statuses:
                raise ValueError(f"Invalid status. Valid statuses: {self.valid_statuses}")
            params['status'] = status

        cache_key = f"orders_s{status}_p{page}_pp{per_page}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        orders = self.api._make_request('orders', params=params)
        cache.set(cache_key, orders)
        return orders

    def get_order(self, order_id: int) -> Dict:
        """Get detailed order information"""
        cache_key = f"order_{order_id}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        order = self.api._make_request(f'orders/{order_id}')
        cache.set(cache_key, order)
        return order

    def update_status(self, order_id: int, status: str) -> Dict:
        """Update order status"""
        if status not in self.valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses: {self.valid_statuses}")

        data = {'status': status}
        result = self.api._make_request(
            f'orders/{order_id}',
            method='PUT',
            data=data
        )
        cache.clear()  # Invalidate order cache
        
        # Log status change
        logger.info(
            f"Order {order_id} status updated to {status}"
        )
        
        return result

    def add_note(self, order_id: int, note: str, 
                 customer_note: bool = False) -> Dict:
        """Add note to order"""
        data = {
            'note': note,
            'customer_note': customer_note
        }
        
        return self.api._make_request(
            f'orders/{order_id}/notes',
            method='POST',
            data=data
        )

    def get_notes(self, order_id: int) -> List[Dict]:
        """Get order notes"""
        cache_key = f"order_notes_{order_id}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        notes = self.api._make_request(f'orders/{order_id}/notes')
        cache.set(cache_key, notes)
        return notes

    def process_refund(self, order_id: int, amount: float, 
                      reason: str = "") -> Dict:
        """Process order refund"""
        data = {
            'amount': str(amount),
            'reason': reason
        }
        
        result = self.api._make_request(
            f'orders/{order_id}/refunds',
            method='POST',
            data=data
        )
        cache.clear()
        
        logger.info(
            f"Refund processed for order {order_id}: "
            f"${amount} - {reason}"
        )
        
        return result

    def get_order_metrics(self, days: int = 30) -> Dict:
        """Get order metrics for specified period"""
        end_date = datetime.now().isoformat()
        start_date = (
            datetime.now()
            .replace(hour=0, minute=0, second=0, microsecond=0)
            .timestamp() - (days * 86400)
        )
        
        params = {
            'after': datetime.fromtimestamp(start_date).isoformat(),
            'before': end_date,
            'per_page': 100
        }
        
        orders = self.api._make_request('orders', params=params)
        
        metrics = {
            'total_orders': len(orders),
            'total_revenue': sum(float(o['total']) for o in orders),
            'status_breakdown': {},
            'daily_totals': {}
        }
        
        for order in orders:
            # Status breakdown
            status = order['status']
            metrics['status_breakdown'][status] = \
                metrics['status_breakdown'].get(status, 0) + 1
            
            # Daily totals
            date = order['date_created'].split('T')[0]
            metrics['daily_totals'][date] = \
                metrics['daily_totals'].get(date, 0) + float(order['total'])
        
        return metrics