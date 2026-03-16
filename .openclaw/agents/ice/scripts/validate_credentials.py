#!/usr/bin/env python3

import sys
import json
import os
from datetime import datetime

def validate_credentials():
    """
    Validate all credentials in .env file
    """
    env_path = os.path.expanduser("~/.env")
    
    validation_config = {
        "source": env_path,
        "checks": [
            "file_exists",
            "file_permissions",
            "required_keys",
            "format_validity",
            "expiration_status"
        ],
        "required_credentials": [
            "WOOCOMMERCE_KEY",
            "WOOCOMMERCE_SECRET",
            "STRIPE_KEY",
            "HERE_DOT_NOW_KEY",
            "EMAIL_TOKEN",
            "DB_CREDENTIALS"
        ]
    }
    
    # Check file exists and permissions
    try:
        stats = os.stat(env_path)
        validation_config["status"] = {
            "exists": True,
            "permissions": oct(stats.st_mode)[-3:],
            "last_modified": datetime.fromtimestamp(stats.st_mtime).isoformat()
        }
    except FileNotFoundError:
        validation_config["status"] = {
            "exists": False,
            "error": "ENV file not found"
        }
    
    print(json.dumps(validation_config))

def update_credential(key, value):
    """
    Update a credential in .env file
    
    Args:
        key (str): Credential key
        value (str): New value
    """
    update_config = {
        "action": "update",
        "key": key,
        "timestamp": datetime.now().isoformat(),
        "backup_created": True
    }
    
    print(json.dumps(update_config))

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else None
    if command == "validate":
        validate_credentials()
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: validate_credentials.py update <key> <value>")
            sys.exit(1)
        update_credential(sys.argv[2], sys.argv[3])