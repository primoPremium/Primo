from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import json
import base64
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from email.mime.text import MIMEText

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def browser_tool(action, **kwargs):
    """Execute browser tool actions directly"""
    try:
        from openclaw.tools import browser
        result = browser.call(action, **kwargs)
        print(f"Browser {action} result:", result)
        return result
    except Exception as e:
        print(f"Browser {action} error:", e)
        return None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.server.oauth_response = self.path
        self.wfile.write(b"Authentication successful! You can close this window.")
    
    def log_message(self, format, *args):
        pass

def start_local_server(port):
    """Start local server for OAuth callback"""
    server = HTTPServer(('localhost', port), OAuthCallbackHandler)
    server.oauth_response = None
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    return server

def ensure_browser_ready():
    """Ensure browser is running with correct profile"""
    print("Ensuring browser is ready...")
    
    # Stop any existing instance
    print("Stopping existing browser...")
    browser_tool('stop')
    time.sleep(1)
    
    # Start with openclaw profile
    print("Starting browser with openclaw profile...")
    result = browser_tool('start', profile='openclaw')
    
    if not result:
        raise Exception("Failed to start browser (no result)")
    if not result.get('running'):
        raise Exception(f"Browser not running after start: {result}")
    
    # Allow browser to initialize
    time.sleep(2)
    
    # Verify browser status
    status = browser_tool('status')
    if not status or not status.get('running'):
        raise Exception(f"Browser not responding after start: {status}")
    
    print("Browser is ready")
    return True

def run_oauth_flow(flow):
    """Run OAuth flow with browser integration"""
    port = 8080
    server = start_local_server(port)
    
    try:
        # Ensure browser is ready
        ensure_browser_ready()
        
        # Get authorization URL
        auth_url, _ = flow.authorization_url(prompt='consent')
        print(f"Opening auth URL: {auth_url}")
        
        # Navigate to auth URL
        result = browser_tool('navigate', url=auth_url)
        if not result:
            raise Exception(f"Failed to navigate to auth URL")
        
        # Wait for callback
        timeout = 300  # 5 minutes
        start_time = time.time()
        print("Waiting for OAuth callback...")
        
        while time.time() - start_time < timeout:
            if server.oauth_response:
                try:
                    print("Got OAuth callback, exchanging code...")
                    flow.fetch_token(
                        authorization_response=f"http://localhost:{port}{server.oauth_response}"
                    )
                    print("Successfully exchanged code for token")
                    return flow.credentials
                except Exception as e:
                    raise Exception(f"Failed to exchange auth code: {e}")
            time.sleep(1)
        
        raise Exception("Authorization flow timed out")
    
    finally:
        print("Cleaning up OAuth flow...")
        server.shutdown()
        server.server_close()
        browser_tool('stop')

def get_credentials():
    """Get Gmail API credentials"""
    creds = None
    token_path = os.path.expanduser('~/.config/gogcli/token.json')
    creds_path = os.path.expanduser('~/.config/gogcli/google_oauth_client.json')
    
    # Check for credentials file
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"OAuth credentials not found at {creds_path}")
    
    # Try loading existing token
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
            
            # Valid credentials
            if creds and creds.valid:
                print("Using existing valid credentials")
                return creds
                
            # Expired but refreshable
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing expired credentials...")
                creds.refresh(Request())
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
                print("Successfully refreshed credentials")
                return creds
                
        except Exception as e:
            print(f"Error with existing credentials: {e}")
    
    # Need new OAuth flow
    try:
        print("Starting new OAuth flow...")
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = run_oauth_flow(flow)
        
        # Save credentials
        print("Saving new credentials...")
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
        print("Successfully saved credentials")    
        
        return creds
        
    except Exception as e:
        raise Exception(f"OAuth flow failed: {e}")

def send_test_email(service, to):
    """Send test email with error handling"""
    try:
        message = MIMEText("Test email via OpenClaw Gmail integration")
        message['to'] = to
        message['subject'] = "OpenClaw Gmail Test"
        
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        service.users().messages().send(userId='me', body={'raw': raw}).execute()
        return "Test email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

def main():
    """Main function with error handling"""
    try:
        # Get credentials
        print("Getting credentials...")
        creds = get_credentials()
        
        # Build Gmail service
        print("Building Gmail service...")
        service = build('gmail', 'v1', credentials=creds)
        
        # Send test email
        print("Sending test email...")
        result = send_test_email(service, 'test@example.com')  # Replace with actual test email
        print(result)
        
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()