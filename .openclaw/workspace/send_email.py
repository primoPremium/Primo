from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import json
import os.path

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Message Id: {message["id"]}')
        return True
    except Exception as e:
        print(f'An error occurred: {e}')
        return False

# Load credentials
creds = None
if os.path.exists('/home/ubuntu/.config/gogcli/token.json'):
    with open('/home/ubuntu/.config/gogcli/token.json', 'r') as token:
        creds = Credentials.from_authorized_user_file('/home/ubuntu/.config/gogcli/token.json', ['https://www.googleapis.com/auth/gmail.send'])

if not creds or not creds.valid:
    print("Invalid or missing credentials")
    exit(1)

try:
    # Create Gmail API service
    service = build('gmail', 'v1', credentials=creds)
    
    # Create and send email
    message = create_message(
        'me',
        'bweldy82@gmail.com',
        'TEST',
        'Testing automated email sending from Primo'
    )
    
    success = send_message(service, 'me', message)
    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send email")

except Exception as e:
    print(f"Error: {str(e)}")