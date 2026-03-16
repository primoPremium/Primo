from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
import os
from .auth import GmailAuth

class GmailClient:
    def __init__(self):
        self.auth = GmailAuth()
        self.service = build('gmail', 'v1', credentials=self.auth.get_credentials())
        self.user_id = 'me'
        
    def read_messages(self, limit=10, query=None):
        """Read Gmail messages."""
        try:
            messages = []
            request = self.service.users().messages().list(
                userId=self.user_id, q=query, maxResults=limit
            )
            while request is not None:
                response = request.execute()
                messages.extend(response.get('messages', []))
                request = self.service.users().messages().list_next(request, response)
                if len(messages) >= limit:
                    messages = messages[:limit]
                    break
                    
            return [self._get_message(msg['id']) for msg in messages]
        except HttpError as error:
            print(f'An error occurred: {error}')
            return []
            
    def _get_message(self, msg_id):
        """Get a specific message by ID."""
        try:
            message = self.service.users().messages().get(
                userId=self.user_id, id=msg_id, format='full'
            ).execute()
            return message
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
            
    def send_email(self, to, subject, body, attachments=None):
        """Send an email."""
        try:
            message = MIMEMultipart()
            message['to'] = to
            message['subject'] = subject
            
            msg = MIMEText(body)
            message.attach(msg)
            
            if attachments:
                for attachment in attachments:
                    self._add_attachment(message, attachment)
                    
            raw_message = base64.urlsafe_b64encode(
                message.as_bytes()
            ).decode('utf-8')
            
            self.service.users().messages().send(
                userId=self.user_id,
                body={'raw': raw_message}
            ).execute()
            
            return True
        except HttpError as error:
            print(f'An error occurred: {error}')
            return False
            
    def _add_attachment(self, message, attachment_path):
        """Add an attachment to the email."""
        try:
            content_type = 'application/octet-stream'
            main_type, sub_type = content_type.split('/', 1)
            
            filename = os.path.basename(attachment_path)
            
            with open(attachment_path, 'rb') as f:
                part = MIMEBase(main_type, sub_type)
                part.set_payload(f.read())
                
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                'attachment',
                filename=filename
            )
            message.attach(part)
        except Exception as error:
            print(f'Error adding attachment: {error}')