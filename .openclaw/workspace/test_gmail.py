from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import json
import base64
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import subprocess

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.modify']
TOKEN_PATH = Path('/home/ubuntu/.config/gogcli/token.json')

def browser_open(url):
    """Open URL in browser using OpenClaw's browser tool."""
    subprocess.run(['openclaw', 'browser', 'open', url])

def get_auth_code(auth_url):
    """Get authorization code using OpenClaw's browser tool."""
    # Open auth URL in browser
    browser_open(auth_url)
    print("Please complete the authorization in the browser...")
    
    # Wait for redirect to localhost
    while True:
        time.sleep(2)
        try:
            result = subprocess.run(
                ['openclaw', 'browser', 'status'], 
                capture_output=True, 
                text=True
            )
            if "localhost" in result.stdout:
                # Extract code from URL
                code = result.stdout.split("code=")[1].split("&")[0]
                return code
        except Exception as e:
            print(f"Error checking browser status: {e}")
            time.sleep(1)

def get_service():
    """Get an authorized Gmail API service instance."""
    try:
        # Load client configuration
        client_config = {
            "installed": {
                "client_id": os.getenv('GOOGLE_CLIENT_ID'),
                "client_secret": os.getenv('GOOGLE_CLIENT_SECRET'),
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["http://localhost"]
            }
        }
        
        creds = None
        # Load existing token if available
        if TOKEN_PATH.exists():
            creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
        
        # If no valid credentials available, run auth flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(
                    client_config,
                    SCOPES,
                    redirect_uri='http://localhost'
                )
                
                # Generate auth URL and get code using browser tool
                auth_url, _ = flow.authorization_url(access_type='offline', include_granted_scopes='true')
                code = get_auth_code(auth_url)
                
                # Exchange code for credentials
                flow.fetch_token(code=code)
                creds = flow.credentials
            
            # Save the credentials
            TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
            TOKEN_PATH.write_text(creds.to_json())
        
        return build('gmail', 'v1', credentials=creds)
    except Exception as e:
        print(f"Error setting up Gmail service: {e}")
        return None

def send_email(to_email, subject, body):
    """Send an email."""
    try:
        service = get_service()
        if not service:
            return "Failed to get Gmail service"
            
        message = MIMEMultipart()
        message['to'] = to_email
        message['from'] = 'premiummedscollective@gmail.com'
        message['subject'] = subject
        
        msg = MIMEText(body)
        message.attach(msg)
        
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        sent_message = service.users().messages().send(userId='me', 
                                                     body={'raw': raw}).execute()
        return f"Message sent successfully. Message ID: {sent_message['id']}"
    except Exception as e:
        return f"Error sending email: {str(e)}"

if __name__ == "__main__":
    result = send_email(
        'bweldy82@gmail.com',
        'Test Email from OpenClaw',
        'This is a test email sent via the Gmail API and OpenClaw automation.'
    )
    print(result)