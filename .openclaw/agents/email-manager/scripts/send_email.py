from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_credentials():
    creds = None
    token_path = os.path.expanduser('~/.config/gogcli/token.json')
    creds_path = os.path.expanduser('~/.config/gogcli/google_oauth_client.json')
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    return creds

def create_message_with_attachment(sender, to, subject, message_text, file_path=None):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    if file_path:
        with open(file_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='md')
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
            message.attach(attachment)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return {'raw': raw_message}

def send_email(to, subject, body, attachment_path=None):
    try:
        creds = get_credentials()
        service = build('gmail', 'v1', credentials=creds)
        
        sender = 'premiummedscollective@gmail.com'
        message = create_message_with_attachment(sender, to, subject, body, attachment_path)
        
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        return f"Message Id: {sent_message['id']}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print("Usage: python send_email.py <recipient> <subject> <body> [attachment_path]")
        sys.exit(1)
    
    to = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    attachment_path = sys.argv[4] if len(sys.argv) > 4 else None
    
    result = send_email(to, subject, body, attachment_path)
    print(result)