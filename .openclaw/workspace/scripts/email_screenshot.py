#!/usr/bin/env python3

import json
import os
import time
from datetime import datetime
from typing import Optional, Dict, Any

class EmailScreenshotter:
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.browser_session = None
        self.last_screenshot = None

    def _load_config(self, config_path: Optional[str] = None) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        default_config = {
            "browser": {
                "profile": "chrome",
                "viewport": {"width": 1920, "height": 1080},
                "wait_time_ms": 2000
            },
            "templates_path": "configs/email_templates.md",
            "success_config_path": "memory/successful_configs.md"
        }
        
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return {**default_config, **json.load(f)}
        return default_config

    def capture_screenshot(self, url: str) -> str:
        """Capture screenshot using browser tool"""
        # Initialize browser session
        result = self._browser_command("start", profile="chrome")
        self.browser_session = result.get("sessionId")

        # Navigate and capture
        self._browser_command("navigate", url=url)
        time.sleep(self.config["browser"]["wait_time_ms"] / 1000)
        
        screenshot = self._browser_command("screenshot", 
                                         fullPage=True,
                                         type="png")
        
        self.last_screenshot = screenshot
        return screenshot

    def send_email(self, to: str, template: str = "default", 
                   variables: Optional[Dict[str, str]] = None) -> bool:
        """Send email with screenshot using template"""
        if not self.last_screenshot:
            raise ValueError("No screenshot captured yet")

        template_content = self._load_template(template)
        variables = variables or {}
        
        # Format template
        formatted_content = self._format_template(template_content, variables)
        
        # Send via message tool
        self._send_message(to, formatted_content, self.last_screenshot)
        return True

    def capture_and_send(self, url: str, email_to: str, 
                        template: str = "default", 
                        variables: Optional[Dict[str, str]] = None) -> bool:
        """Capture screenshot and send email in one operation"""
        self.capture_screenshot(url)
        return self.send_email(email_to, template, variables)

    def _browser_command(self, action: str, **kwargs) -> Dict[str, Any]:
        """Execute browser tool command"""
        # This would interface with the OpenClaw browser tool
        # Implementation depends on the actual tool interface
        pass

    def _load_template(self, template_name: str) -> str:
        """Load email template from templates file"""
        # Implementation to load template from configs/email_templates.md
        pass

    def _format_template(self, template: str, variables: Dict[str, str]) -> str:
        """Format template with variables"""
        variables.setdefault("timestamp", datetime.utcnow().isoformat())
        return template.format(**variables)

    def _send_message(self, to: str, content: str, attachment: str) -> bool:
        """Send email using message tool"""
        # This would interface with the OpenClaw message tool
        # Implementation depends on the actual tool interface
        pass

    def cleanup(self) -> None:
        """Cleanup resources"""
        if self.browser_session:
            self._browser_command("stop")
            self.browser_session = None