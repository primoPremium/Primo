from src.gmail_client import GmailClient
from base64 import urlsafe_b64decode
import email

def get_body(msg_parts):
    """Extract email body from message parts."""
    text = ""
    if not msg_parts:
        return text
        
    for part in msg_parts:
        if part.get('mimeType') == 'text/plain':
            data = part.get('body', {}).get('data', '')
            if data:
                text += urlsafe_b64decode(data).decode()
    return text

def get_headers(headers, name):
    """Get specific header value."""
    for header in headers:
        if header['name'].lower() == name.lower():
            return header['value']
    return None

def main():
    client = GmailClient()
    # Get most recent message
    messages = client.read_messages(limit=1)
    
    if not messages or not messages[0]:
        print("No messages found")
        return
        
    message = messages[0]
    headers = message.get('payload', {}).get('headers', [])
    
    subject = get_headers(headers, 'subject')
    date = get_headers(headers, 'date')
    
    body = get_body(message.get('payload', {}).get('parts', []))
    if not body:
        # Try non-multipart message
        data = message.get('payload', {}).get('body', {}).get('data', '')
        if data:
            body = urlsafe_b64decode(data).decode()
    
    print(f"Subject: {subject}")
    print(f"Date: {date}")
    print("\nBody:")
    print(body)

if __name__ == "__main__":
    main()