from src.gmail_client import GmailClient
from datetime import datetime, timedelta
from base64 import urlsafe_b64decode
import email
import sys

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
    print("Starting Gmail test...")
    
    # Create client
    client = GmailClient()
    
    # Calculate 24 hours ago
    after = datetime.now() - timedelta(hours=24)
    query = f'after:{after.strftime("%Y/%m/%d")}'
    
    print(f"\nQuerying emails after {after.strftime('%Y/%m/%d')}...")
    
    # Get messages from last 24 hours
    messages = client.read_messages(query=query, limit=50)  # Limit to avoid too many results
    
    if not messages:
        print("No messages found in the last 24 hours")
        return
        
    print(f"\nFound {len(messages)} messages\n")
    print("=== Message Summary ===")
    
    for msg in messages:
        headers = msg.get('payload', {}).get('headers', [])
        
        subject = get_headers(headers, 'subject') or '(no subject)'
        date = get_headers(headers, 'date')
        from_addr = get_headers(headers, 'from')
        
        # Get body
        body = get_body(msg.get('payload', {}).get('parts', []))
        if not body:
            # Try non-multipart message
            data = msg.get('payload', {}).get('body', {}).get('data', '')
            if data:
                body = urlsafe_b64decode(data).decode()
        
        # Truncate body for summary
        body_preview = body[:100] + '...' if body and len(body) > 100 else body
        
        print(f"\nFrom: {from_addr}")
        print(f"Date: {date}")
        print(f"Subject: {subject}")
        print(f"Preview: {body_preview}")
        print("-" * 80)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)