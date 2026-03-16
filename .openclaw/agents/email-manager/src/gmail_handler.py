"""
Gmail handler using browser-based authentication.
"""
import subprocess
import time

def browser_open(url):
    """Open URL in browser using OpenClaw's browser tool."""
    try:
        # Start browser if needed
        subprocess.run(
            ['openclaw', 'browser', 'start', '--profile', 'openclaw'],
            capture_output=True,
            text=True
        )
        
        # Wait for browser to be ready
        if not wait_for_browser():
            raise Exception("Browser failed to start and connect")
            
        # Open URL
        result = subprocess.run(
            ['openclaw', 'browser', 'open', '--url', url],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"Browser command failed: {result.stderr}")
        return result.stdout
    except Exception as e:
        print(f"Browser error: {e}")
        return None

def wait_for_browser():
    """Wait for browser to be ready."""
    attempts = 0
    while attempts < 10:
        result = subprocess.run(
            ['openclaw', 'browser', 'status'],
            capture_output=True,
            text=True
        )
        if 'running' in result.stdout:
            return True
        time.sleep(1)
        attempts += 1
    return False

def send_email(to_email, subject, body):
    """Send an email using Gmail web interface."""
    try:
        # Navigate to Gmail
        browser_open('https://mail.google.com')
        return "Browser navigation initiated"
    except Exception as e:
        return f"Error: {str(e)}"