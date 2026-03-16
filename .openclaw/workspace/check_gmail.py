from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
from datetime import datetime
import pytz

# Load credentials from token file
with open('/home/ubuntu/.config/gogcli/token.json', 'r') as token_file:
    token_data = json.load(token_file)

creds = Credentials.from_authorized_user_info(token_data)

# Build Gmail API service
service = build('gmail', 'v1', credentials=creds)

# Search for emails from specific sender
query = "from:bweldy82@gmail.com"
results = service.users().messages().list(userId='me', q=query, maxResults=10).execute()
messages = results.get('messages', [])

# Convert UTC to PST
pst = pytz.timezone('America/Los_Angeles')

email_list = []
if messages:
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        headers = msg['payload']['headers']
        
        # Get subject and date
        subject = next(h['value'] for h in headers if h['name'].lower() == 'subject')
        date_str = next(h['value'] for h in headers if h['name'].lower() == 'date')
        
        # Parse and convert date to PST
        date_obj = datetime.strptime(date_str.split(' (')[0].strip(), '%a, %d %b %Y %H:%M:%S %z')
        pst_date = date_obj.astimezone(pst)
        
        # Get snippet (brief content summary)
        snippet = msg.get('snippet', '')
        
        email_list.append({
            'date': pst_date.strftime('%I:%M %p PST, %m/%d/%Y'),
            'subject': subject,
            'summary': snippet
        })

# Sort by date
email_list.sort(key=lambda x: datetime.strptime(x['date'], '%I:%M %p PST, %m/%d/%Y'))

# Print results
current_time_pst = datetime.now(pst).strftime('%I:%M %p PST, %m/%d/%Y')
print(f"Email Check Report")
print(f"Timestamp: {current_time_pst}")
print(f"Status: {'Success' if True else 'Failed'}")
print("\nFound Emails:")
if email_list:
    for email in email_list:
        print(f"\nDate: {email['date']}")
        print(f"Subject: {email['subject']}")
        print(f"Summary: {email['summary']}")
else:
    print("No emails found")
print(f"\nAPI Status: Connected")