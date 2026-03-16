import sys
sys.path.append('/home/ubuntu/.openclaw/agents/email-manager/src')

from gmail_handler import send_email

result = send_email(
    'bweldy82@gmail.com',
    'Test Email from OpenClaw',
    'This is a test email sent via the Gmail API and OpenClaw automation.'
)

print(result)