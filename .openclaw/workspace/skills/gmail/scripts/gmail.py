#!/usr/bin/env python3

"""
Gmail Integration Core Functions
------------------------------
Simple Gmail automation via Gmail API
"""

import os
import json
import base64
import email
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from pathlib import Path

class Gmail:
    def __init__(self):
        self.service = self._get_service()
        self.templates = {}
        self._load_templates()
    
    def _get_service(self):
        """Initialize Gmail API service using OAuth2 credentials."""
        SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
        
        # Load credentials from service-account.json
        creds_path = Path(__file__).parent.parent / 'service-account.json'
        with open(creds_path) as f:
            creds_data = json.load(f)
        
        creds = Credentials.from_authorized_user_info(creds_data, SCOPES)
        return build('gmail', 'v1', credentials=creds)
    
    def _load_templates(self):
        """Load email templates."""
        template_dir = Path(__file__).parent.parent / 'templates'
        if template_dir.exists():
            for file in template_dir.glob('*.txt'):
                with open(file, 'r') as f:
                    self.templates[file.stem] = f.read()
    
    def send_email(self, to, template, vars=None):
        """Send email using template."""
        if template not in self.templates:
            raise ValueError(f"Template '{template}' not found")
        
        content = self.templates[template]
        if vars:
            for key, value in vars.items():
                content = content.replace(f"{{{key}}}", str(value))
        
        message = MIMEText(content)
        message['to'] = to
        message['from'] = 'premiummedscollective@gmail.com'
        message['subject'] = f"Premium Meds - {template.replace('_', ' ').title()}"
        
        raw = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode('utf-8')
        
        return self.service.users().messages().send(
            userId='me',
            body={'raw': raw}
        ).execute()
    
    def check_inbox(self, labels=None, query=None):
        """Check inbox for messages with specified labels and query."""
        q_parts = []
        if labels:
            q_parts.extend(f'label:{label}' for label in labels)
        if query:
            q_parts.append(query)
        
        q = ' '.join(q_parts) if q_parts else ''
        
        results = self.service.users().messages().list(
            userId='me',
            q=q
        ).execute()
        
        return results.get('messages', [])
    
    def get_message(self, message_id):
        """Get full message content by ID."""
        message = self.service.users().messages().get(
            userId='me',
            id=message_id,
            format='full'
        ).execute()
        
        # Get headers
        headers = {h['name']: h['value'] for h in message['payload']['headers']}
        
        # Get body
        if 'parts' in message['payload']:
            parts = message['payload']['parts']
            body = ''
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    body = base64.urlsafe_b64decode(
                        part['body']['data']
                    ).decode('utf-8')
                    break
        else:
            body = base64.urlsafe_b64decode(
                message['payload']['body']['data']
            ).decode('utf-8')
        
        return {
            'id': message['id'],
            'threadId': message['threadId'],
            'from': headers.get('From', ''),
            'to': headers.get('To', ''),
            'subject': headers.get('Subject', ''),
            'date': headers.get('Date', ''),
            'body': body
        }
    
    def apply_label(self, label, message_id):
        """Apply label to message."""
        # Get or create label
        results = self.service.users().labels().list(
            userId='me'
        ).execute()
        
        label_id = None
        for l in results.get('labels', []):
            if l['name'].lower() == label.lower():
                label_id = l['id']
                break
        
        if not label_id:
            # Create new label
            label_object = {
                'name': label,
                'messageListVisibility': 'show',
                'labelListVisibility': 'labelShow'
            }
            created = self.service.users().labels().create(
                userId='me',
                body=label_object
            ).execute()
            label_id = created['id']
        
        # Apply label
        return self.service.users().messages().modify(
            userId='me',
            id=message_id,
            body={'addLabelIds': [label_id]}
        ).execute()

def main():
    """CLI interface."""
    import argparse
    parser = argparse.ArgumentParser(description='Gmail automation')
    parser.add_argument('action', choices=['send', 'check', 'label', 'read'])
    parser.add_argument('--to', help='Email recipient')
    parser.add_argument('--template', help='Email template')
    parser.add_argument('--vars', help='Template variables (JSON)')
    parser.add_argument('--labels', help='Labels to check (comma-separated)')
    parser.add_argument('--query', help='Search query')
    parser.add_argument('--label', help='Label to apply')
    parser.add_argument('--message-id', help='Message ID')
    
    args = parser.parse_args()
    gmail = Gmail()
    
    if args.action == 'send':
        vars = json.loads(args.vars) if args.vars else None
        result = gmail.send_email(args.to, args.template, vars)
        print(f"Sent message ID: {result['id']}")
    
    elif args.action == 'check':
        labels = args.labels.split(',') if args.labels else None
        messages = gmail.check_inbox(labels, args.query)
        print(f"Found {len(messages)} messages")
        for msg in messages:
            print(f"- {msg['id']}")
    
    elif args.action == 'read':
        if not args.message_id:
            print("Error: --message-id required for read action")
            return
        message = gmail.get_message(args.message_id)
        print(f"\nFrom: {message['from']}")
        print(f"To: {message['to']}")
        print(f"Subject: {message['subject']}")
        print(f"Date: {message['date']}")
        print("\nBody:")
        print(message['body'])
    
    elif args.action == 'label':
        result = gmail.apply_label(args.label, args.message_id)
        print(f"Applied label '{args.label}' to message {result['id']}")

if __name__ == '__main__':
    main()