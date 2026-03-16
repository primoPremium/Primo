from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import os.path
import json
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_credentials():
    creds = None
    token_path = os.path.expanduser('~/.config/gmail-cli/token.pickle')
    credentials_path = os.path.expanduser('~/.config/gogcli/google_oauth_client.json')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use the modern localhost flow
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, 
                SCOPES,
                redirect_uri='http://127.0.0.1:8080'
            )
            creds = flow.run_local_server(port=8080)

        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def send_test_email():
    try:
        # Get credentials and build service
        creds = get_credentials()
        service = build('gmail', 'v1', credentials=creds)

        # Create message
        message = MIMEText('testing automated email sending')
        message['to'] = 'bweldy82@gmail.com'
        message['subject'] = 'TEST'

        # Encode the message
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        message_body = {'raw': raw}

        # Send the email
        sent_message = service.users().messages().send(userId='me', body=message_body).execute()
        print(f'Message Id: {sent_message["id"]}')
        return True

    except Exception as e:
        print(f'An error occurred: {e}')
        return False

if __name__ == '__main__':
    success = send_test_email()
    print(f'Email sent successfully: {success}')