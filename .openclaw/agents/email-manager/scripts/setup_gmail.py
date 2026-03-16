#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from gmail_handler import setup_initial_token

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: setup_gmail.py <refresh_token>")
        print("Please provide the Gmail API refresh token")
        sys.exit(1)
        
    refresh_token = sys.argv[1]
    result = setup_initial_token(refresh_token)
    print(result)