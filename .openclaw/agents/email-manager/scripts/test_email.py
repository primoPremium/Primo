#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from gmail_handler import send_email

def main():
    print("Testing email-manager...")
    
    # Send test email with SOUL.md attachment
    soul_md_path = '/home/ubuntu/.openclaw/workspace/SOUL.md'
    result = send_email(
        'bweldy82@gmail.com',
        'Premium Meds - SOUL.md Configuration File',
        'Hello,\n\nPlease find attached the current SOUL.md configuration file that defines my role as Marketing and Advertising Director and outlines our agent relationships and delegation protocols.\n\nBest regards,\nPrimo\nMarketing & Advertising Director\nPremium Meds',
        soul_md_path
    )
    
    print(f"\nResult: {result}")

if __name__ == "__main__":
    # Verify environment variables
    required_vars = ['WP_CRED_USER', 'WP_CRED_PASS']
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)
    
    main()