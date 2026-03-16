"""
WordPress management utility combining REST API and CLI functionality.
"""
import os
from typing import Dict, Any, Optional
from .wp_api import WordPressAPI
from .wp_cli import WordPressCLI

class WordPressManager:
    def __init__(self):
        self.api = WordPressAPI()
        self.cli = WordPressCLI()

    def create_post_with_image(self, title: str, content: str, 
                             image_path: str, 
                             status: str = 'draft') -> Dict[str, Any]:
        """
        Create a post with featured image using both API and CLI.
        """
        # Upload featured image
        media = self.api.upload_media(image_path, {
            'title': f'Featured image for {title}'
        })
        
        # Create post
        post = self.api.create_post({
            'title': title,
            'content': content,
            'status': status,
            'featured_media': media['id']
        })
        
        # Optimize images using CLI
        self.cli.execute(['media', 'regenerate', str(media['id'])])
        
        return post

    def backup_and_update(self) -> None:
        """
        Perform full backup and update WordPress core, plugins, and themes.
        """
        # Create backup directory if not exists
        backup_dir = os.path.join(self.cli.wp_path, 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        
        # Export database
        db_backup = os.path.join(backup_dir, 'pre_update_backup.sql')
        self.cli.db_export(db_backup)
        
        try:
            # Perform updates
            self.cli.update_core()
            self.cli.update_plugins()
            self.cli.update_themes()
            
            # Flush caches
            self.cli.cache_flush()
            self.cli.rewrite_flush()
            
        except Exception as e:
            # If update fails, restore database
            self.cli.db_import(db_backup)
            raise Exception(f"Update failed, database restored: {str(e)}")

    def create_draft_post(self, title: str, content: str) -> Dict[str, Any]:
        """
        Create a draft post and validate it exists via CLI.
        """
        # Create draft via API
        post = self.api.create_post({
            'title': title,
            'content': content,
            'status': 'draft'
        })
        
        # Verify via CLI
        result = self.cli.execute([
            'post', 'get', str(post['id']),
            '--field=status'
        ])
        
        if result.strip() != 'draft':
            raise Exception(f"Post status verification failed: {result}")
            
        return post

    def publish_post(self, post_id: int) -> Dict[str, Any]:
        """
        Publish a draft post and verify via both API and CLI.
        """
        # Update via API
        post = self.api.update_post(post_id, {'status': 'publish'})
        
        # Verify via CLI
        status = self.cli.execute([
            'post', 'get', str(post_id),
            '--field=status'
        ]).strip()
        
        if status != 'publish':
            raise Exception(f"Post not published. Status: {status}")
            
        return post