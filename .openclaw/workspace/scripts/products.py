from typing import Dict, List, Optional
from .utils import WooCommerceAPI, cache, logger

class ProductManager:
    def __init__(self):
        self.api = WooCommerceAPI()

    def list_products(self, page: int = 1, per_page: int = 10) -> List[Dict]:
        """List products with pagination"""
        cache_key = f"products_p{page}_pp{per_page}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        products = self.api._make_request(
            'products',
            params={'page': page, 'per_page': per_page}
        )
        cache.set(cache_key, products)
        return products

    def add_product(self, name: str, price: float, description: str = "") -> Dict:
        """Add new product"""
        data = {
            "name": name,
            "regular_price": str(price),
            "description": description,
            "status": "draft"  # Default to draft for safety
        }
        
        result = self.api._make_request(
            'products',
            method='POST',
            data=data
        )
        cache.clear()  # Invalidate product cache
        return result

    def update_product(self, product_id: int, field: str, value: str) -> Dict:
        """Update product field"""
        allowed_fields = ['name', 'regular_price', 'description', 'status']
        if field not in allowed_fields:
            raise ValueError(f"Invalid field. Allowed fields: {allowed_fields}")

        data = {field: value}
        result = self.api._make_request(
            f'products/{product_id}',
            method='PUT',
            data=data
        )
        cache.clear()
        return result

    def delete_product(self, product_id: int, force: bool = False) -> Dict:
        """Delete product"""
        result = self.api._make_request(
            f'products/{product_id}',
            method='DELETE',
            params={'force': force}
        )
        cache.clear()
        return result

    def get_product(self, product_id: int) -> Dict:
        """Get single product details"""
        cache_key = f"product_{product_id}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        product = self.api._make_request(f'products/{product_id}')
        cache.set(cache_key, product)
        return product

    def search_products(self, query: str) -> List[Dict]:
        """Search products by name/sku"""
        return self.api._make_request(
            'products',
            params={'search': query}
        )