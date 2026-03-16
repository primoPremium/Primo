from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os.path
import json

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar.readonly',
    # Add other scopes as needed
]

def save_credentials(creds, token_path='token.json'):
    """Save credentials to file"""
    creds_data = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }
    with open(token_path, 'w') as token:
        json.dump(creds_data, token)

def load_credentials(token_path='token.json'):
    """Load credentials from file"""
    if not os.path.exists(token_path):
        return None
    with open(token_path, 'r') as token:
        creds_data = json.load(token)
    return Credentials.from_authorized_user_info(creds_data)

def get_credentials(client_secrets_file='credentials.json', token_path='token.json'):
    """Get valid credentials, refreshing or running auth flow if necessary"""
    creds = load_credentials(token_path)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh credentials if we have a refresh token
            creds.refresh(Request())
        else:
            # Run the OAuth flow
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials
        save_credentials(creds, token_path)

    return creds

if __name__ == '__main__':
    # Example usage
    try:
        creds = get_credentials()
        print("Successfully authenticated!")
        print(f"Access token: {creds.token[:15]}...")  # Only show beginning of token
    except Exception as e:
        print(f"Error during authentication: {e}")