from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import os.path
import json

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    # Load the OAuth 2.0 credentials from the config file
    client_secrets_file = os.path.expanduser('~/.config/gogcli/google_oauth_client.json')
    
    # Create a flow instance with offline access
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file,
        scopes=SCOPES,
        redirect_uri='http://localhost'
    )

    # Generate the authorization URL
    auth_url, _ = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    
    print(f'\nPlease go to this URL to authorize the application:\n{auth_url}\n')
    auth_code = input('Enter the authorization code: ')
    
    # Exchange the authorization code for credentials
    flow.fetch_token(code=auth_code)
    credentials = flow.credentials

    # Build and return the Gmail service
    return build('gmail', 'v1', credentials=credentials)

def send_test_email():
    try:
        # Get the Gmail service
        service = get_gmail_service()
        
        # Create the email message
        message = MIMEText('testing automated email sending')
        message['to'] = 'bweldy82@gmail.com'
        message['subject'] = 'TEST'
        
        # Encode the message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        
        # Send the email
        sent_message = service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        
        print(f'Message Id: {sent_message["id"]}')
        return True
        
    except Exception as e:
        print(f'An error occurred: {e}')
        return False

if __name__ == '__main__':
    success = send_test_email()
    print(f'Email sent successfully: {success}')