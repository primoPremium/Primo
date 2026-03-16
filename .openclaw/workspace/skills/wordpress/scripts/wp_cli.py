"""
WordPress CLI command execution wrapper.
"""
import os
import subprocess
from typing import Optional, List, Union
from dotenv import load_dotenv

class WordPressCLI:
    def __init__(self):
        load_dotenv()
        self.wp_path = os.getenv('WP_CLI_PATH')
        self.wp_user = os.getenv('WP_CLI_USER')
        self.wp_ssh = os.getenv('WP_CLI_SSH')
        
        if not self.wp_path:
            raise ValueError("WP_CLI_PATH environment variable is required")

    def execute(self, command: Union[str, List[str]], capture_output: bool = True) -> str:
        """
        Execute a WP-CLI command.
        
        Args:
            command: Command string or list of arguments
            capture_output: Whether to capture and return command output
            
        Returns:
            Command output as string if capture_output is True
        """
        if isinstance(command, str):
            command = command.split()
            
        base_cmd = []
        if self.wp_ssh:
            # Remote execution via SSH
            base_cmd = ['ssh', self.wp_ssh]
            
        wp_cmd = ['wp'] + command
        
        if self.wp_user:
            wp_cmd += ['--user=' + self.wp_user]
            
        full_cmd = base_cmd + wp_cmd
        
        # Execute in WordPress directory
        result = subprocess.run(
            full_cmd,
            cwd=self.wp_path,
            capture_output=capture_output,
            text=True,
            check=True
        )
        
        return result.stdout if capture_output else ''

    def plugin_install(self, plugin_name: str) -> str:
        """Install a WordPress plugin."""
        return self.execute(['plugin', 'install', plugin_name])

    def plugin_activate(self, plugin_name: str) -> str:
        """Activate a WordPress plugin."""
        return self.execute(['plugin', 'activate', plugin_name])

    def theme_install(self, theme_name: str) -> str:
        """Install a WordPress theme."""
        return self.execute(['theme', 'install', theme_name])

    def theme_activate(self, theme_name: str) -> str:
        """Activate a WordPress theme."""
        return self.execute(['theme', 'activate', theme_name])

    def update_core(self) -> str:
        """Update WordPress core."""
        return self.execute(['core', 'update'])

    def update_plugins(self) -> str:
        """Update all plugins."""
        return self.execute(['plugin', 'update', '--all'])

    def update_themes(self) -> str:
        """Update all themes."""
        return self.execute(['theme', 'update', '--all'])

    def db_export(self, file_path: str) -> str:
        """Export database to SQL file."""
        return self.execute(['db', 'export', file_path])

    def db_import(self, file_path: str) -> str:
        """Import database from SQL file."""
        return self.execute(['db', 'import', file_path])

    def cache_flush(self) -> str:
        """Flush the WordPress object cache."""
        return self.execute(['cache', 'flush'])

    def rewrite_flush(self) -> str:
        """Flush rewrite rules."""
        return self.execute(['rewrite', 'flush'])