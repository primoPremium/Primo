#!/usr/bin/env python3
import os
import json
from pathlib import Path
from google.oauth2.credentials import Credentials

# Define paths
CONFIG_DIR = Path('/home/ubuntu/.config/gogcli')
TOKEN_PATH = CONFIG_DIR / 'token.json'

def setup_initial_token():
    """Set up initial token using environment variables."""
    # Create initial token with environment variables
    token_data = {
        'client_id': os.getenv('GOOGLE_CLIENT_ID'),
        'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
        'scopes': [
            'https://www.googleapis.com/auth/gmail.send',
            'https://www.googleapis.com/auth/gmail.modify'
        ],
        'token': None,  # Will be obtained through OAuth flow
        'refresh_token': None,  # Will be obtained through OAuth flow
        'token_uri': 'https://oauth2.googleapis.com/token'
    }
    
    # Ensure config directory exists
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    # Write token file
    TOKEN_PATH.write_text(json.dumps(token_data))
    print(f"Initial token configuration written to {TOKEN_PATH}")

if __name__ == "__main__":
    # Check environment variables
    required_vars = ['GOOGLE_CLIENT_ID', 'GOOGLE_CLIENT_SECRET']
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        exit(1)
    
    setup_initial_token()
    print("Token setup complete. Please run test_email.py to verify the setup.")