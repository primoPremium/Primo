"""
WordPress REST API client implementation.
"""
import os
import requests
from typing import Dict, Any, Optional
from dotenv import load_dotenv

class WordPressAPI:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('WP_CRED_URL')
        self.username = os.getenv('WP_CRED_USERNAME')
        self.password = os.getenv('WP_CRED_PASSWORD')
        
        if not all([self.base_url, self.username, self.password]):
            raise ValueError("Missing required WordPress credentials")
            
        self.api_base = f"{self.base_url.rstrip('/')}/wp-json/wp/v2"
        self.auth = (self.username, self.password)

    def create_post(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new post."""
        endpoint = f"{self.api_base}/posts"
        response = requests.post(endpoint, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def update_post(self, post_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing post."""
        endpoint = f"{self.api_base}/posts/{post_id}"
        response = requests.post(endpoint, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def get_post(self, post_id: int) -> Dict[str, Any]:
        """Retrieve a post by ID."""
        endpoint = f"{self.api_base}/posts/{post_id}"
        response = requests.get(endpoint, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def delete_post(self, post_id: int, force: bool = False) -> Dict[str, Any]:
        """Delete a post."""
        endpoint = f"{self.api_base}/posts/{post_id}"
        params = {'force': force}
        response = requests.delete(endpoint, params=params, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def upload_media(self, file_path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Upload media file to WordPress."""
        endpoint = f"{self.api_base}/media"
        files = {'file': open(file_path, 'rb')}
        response = requests.post(endpoint, files=files, data=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def get_users(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get WordPress users."""
        endpoint = f"{self.api_base}/users"
        response = requests.get(endpoint, params=params, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def create_user(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new WordPress user."""
        endpoint = f"{self.api_base}/users"
        response = requests.post(endpoint, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def update_settings(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update WordPress settings."""
        endpoint = f"{self.base_url.rstrip('/')}/wp-json/settings"
        response = requests.post(endpoint, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()