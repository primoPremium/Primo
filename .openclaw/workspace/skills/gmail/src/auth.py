import os
from cryptography.fernet import Fernet
from pathlib import Path
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

class GmailAuth:
    def __init__(self):
        self.token_dir = Path.home() / ".openclaw" / "secure" / "gmail"
        self.token_dir.mkdir(parents=True, exist_ok=True)
        self.token_path = self.token_dir / "token.enc"
        self.key_path = self.token_dir / "key.secret"
        self.pickle_path = self.token_dir / "token.pickle"
        
        if not self.key_path.exists():
            self._generate_encryption_key()
            
    def _generate_encryption_key(self):
        """Generate and save a new encryption key."""
        key = Fernet.generate_key()
        with open(self.key_path, 'wb') as f:
            f.write(key)
            
    def _get_encryption_key(self):
        """Retrieve the encryption key."""
        with open(self.key_path, 'rb') as f:
            return f.read()
            
    def _encrypt_token(self, token_data):
        """Encrypt token data."""
        f = Fernet(self._get_encryption_key())
        return f.encrypt(json.dumps(token_data).encode())
        
    def _decrypt_token(self, encrypted_data):
        """Decrypt token data."""
        f = Fernet(self._get_encryption_key())
        return json.loads(f.decrypt(encrypted_data).decode())
        
    def get_credentials(self):
        """Get Gmail API credentials."""
        creds = None
        
        # Try to load from pickle first (for existing tokens)
        if self.pickle_path.exists():
            with open(self.pickle_path, 'rb') as token:
                creds = pickle.load(token)
        
        # If no pickle, try encrypted token
        if not creds and self.token_path.exists():
            with open(self.token_path, 'rb') as token:
                token_data = self._decrypt_token(token.read())
                creds = Credentials.from_authorized_user_info(token_data)
                
        # If no valid credentials available, use service account
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # Use stored credentials from environment
                creds = Credentials.from_authorized_user_info({
                    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                    "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                    "refresh_token": os.getenv("GOOGLE_REFRESH_TOKEN"),
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "scopes": ['https://www.googleapis.com/auth/gmail.modify']
                })
            
            # Save the credentials
            with open(self.pickle_path, 'wb') as token:
                pickle.dump(creds, token)
                
            token_data = {
                'token': creds.token,
                'refresh_token': creds.refresh_token,
                'token_uri': creds.token_uri,
                'client_id': creds.client_id,
                'client_secret': creds.client_secret,
                'scopes': creds.scopes
            }
            with open(self.token_path, 'wb') as token:
                token.write(self._encrypt_token(token_data))
                
        return creds