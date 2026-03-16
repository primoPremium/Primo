import os
import logging
from typing import Dict, Any, Optional
import requests
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('woocommerce.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WooCommerceAPI:
    def __init__(self):
        self.api_url = os.environ.get('WORDPRESS_API_URL')
        self.consumer_key = os.environ.get('WOOCOMMERCE_CONSUMER_KEY')
        self.consumer_secret = os.environ.get('WOOCOMMERCE_CONSUMER_SECRET')
        
        if not all([self.api_url, self.consumer_key, self.consumer_secret]):
            raise ValueError("Missing required environment variables")

    def _make_request(self, endpoint: str, method: str = 'GET', 
                     params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make authenticated request to WooCommerce API"""
        url = f"{self.api_url}/wc/v3/{endpoint}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=(self.consumer_key, self.consumer_secret),
                params=params,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise

    def test_connection(self) -> bool:
        """Test API connection"""
        try:
            self._make_request('system_status')
            return True
        except:
            return False

class Cache:
    def __init__(self):
        self.cache = {}
        self.timestamps = {}
        self.max_age = 300  # 5 minutes default

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache if not expired"""
        if key in self.cache:
            if (datetime.now() - self.timestamps[key]).seconds < self.max_age:
                return self.cache[key]
            else:
                del self.cache[key]
                del self.timestamps[key]
        return None

    def set(self, key: str, value: Any):
        """Set value in cache"""
        self.cache[key] = value
        self.timestamps[key] = datetime.now()

    def clear(self):
        """Clear all cache entries"""
        self.cache.clear()
        self.timestamps.clear()

# Global cache instance
cache = Cache()