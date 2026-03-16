#!/usr/bin/env python3

import os
import json
import base64
import pickle
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Dict, Optional, Union
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GmailClient:
    """Gmail client for OpenClaw skill integration with proper security and error handling."""
    
    # Gmail API scopes
    SCOPES = ['https://www.googleapis.com/auth/gmail.modify',
              'https://www.googleapis.com/auth/gmail.compose',
              'https://www.googleapis.com/auth/gmail.readonly']
    
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, token_path: str):
        """Initialize Gmail client with OAuth2 credentials.
        
        Args:
            client_id: OAuth2 client ID
            client_secret: OAuth2 client secret
            redirect_uri: OAuth2 redirect URI
            token_path: Path to store/load OAuth2 tokens
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_path = Path(token_path)
        self.credentials = None
        self.service = None
        
    def authenticate(self) -> None:
        """Handle OAuth2 authentication flow with secure token management."""
        try:
            if self.token_path.exists():
                with open(self.token_path, 'rb') as token:
                    self.credentials = pickle.load(token)

            if not self.credentials or not self.credentials.valid:
                if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                    self.credentials.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_config(
                        {
                            "web": {
                                "client_id": self.client_id,
                                "client_secret": self.client_secret,
                                "redirect_uris": [self.redirect_uri],
                                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                "token_uri": "https://oauth2.googleapis.com/token"
                            }
                        },
                        self.SCOPES
                    )
                    self.credentials = flow.run_local_server(port=0)

                # Save the credentials securely
                with open(self.token_path, 'wb') as token:
                    pickle.dump(self.credentials, token)

            self.service = build('gmail', 'v1', credentials=self.credentials)
            
        except Exception as e:
            raise RuntimeError(f"Authentication failed: {str(e)}")

    def list_messages(self, max_results: int = 10, query: str = "") -> List[Dict]:
        """List email messages with optional query.
        
        Args:
            max_results: Maximum number of messages to return
            query: Gmail search query string
            
        Returns:
            List of message dictionaries
        """
        try:
            results = self.service.users().messages().list(
                userId='me',
                maxResults=max_results,
                q=query
            ).execute()
            
            messages = []
            if 'messages' in results:
                for msg in results['messages']:
                    message = self.service.users().messages().get(
                        userId='me',
                        id=msg['id']
                    ).execute()
                    messages.append(message)
            
            return messages
            
        except HttpError as error:
            raise RuntimeError(f"Failed to list messages: {str(error)}")

    def get_message(self, message_id: str) -> Dict:
        """Get a specific email message by ID.
        
        Args:
            message_id: Gmail message ID
            
        Returns:
            Message dictionary with full details
        """
        try:
            return self.service.users().messages().get(
                userId='me',
                id=message_id
            ).execute()
            
        except HttpError as error:
            raise RuntimeError(f"Failed to get message {message_id}: {str(error)}")

    def send_message(self, to: str, subject: str, body: str,
                    attachments: Optional[List[str]] = None) -> Dict:
        """Send an email message with optional attachments.
        
        Args:
            to: Recipient email address
            subject: Email subject
            body: Email body text
            attachments: Optional list of attachment file paths
            
        Returns:
            Sent message details
        """
        try:
            message = MIMEMultipart()
            message['to'] = to
            message['subject'] = subject

            message.attach(MIMEText(body, 'plain'))

            if attachments:
                for attachment_path in attachments:
                    with open(attachment_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename="{os.path.basename(attachment_path)}"'
                        )
                        message.attach(part)

            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
            
            return self.service.users().messages().send(
                userId='me',
                body={'raw': raw_message}
            ).execute()
            
        except (HttpError, IOError) as error:
            raise RuntimeError(f"Failed to send message: {str(error)}")

    def create_label(self, name: str) -> Dict:
        """Create a new Gmail label.
        
        Args:
            name: Label name
            
        Returns:
            Created label details
        """
        try:
            return self.service.users().labels().create(
                userId='me',
                body={'name': name}
            ).execute()
            
        except HttpError as error:
            raise RuntimeError(f"Failed to create label {name}: {str(error)}")

    def list_labels(self) -> List[Dict]:
        """List all Gmail labels.
        
        Returns:
            List of label dictionaries
        """
        try:
            results = self.service.users().labels().list(userId='me').execute()
            return results.get('labels', [])
            
        except HttpError as error:
            raise RuntimeError(f"Failed to list labels: {str(error)}")

    def modify_message(self, message_id: str, add_labels: List[str] = None,
                      remove_labels: List[str] = None) -> Dict:
        """Modify message labels.
        
        Args:
            message_id: Gmail message ID
            add_labels: Labels to add
            remove_labels: Labels to remove
            
        Returns:
            Modified message details
        """
        try:
            return self.service.users().messages().modify(
                userId='me',
                id=message_id,
                body={
                    'addLabelIds': add_labels or [],
                    'removeLabelIds': remove_labels or []
                }
            ).execute()
            
        except HttpError as error:
            raise RuntimeError(f"Failed to modify message {message_id}: {str(error)}")