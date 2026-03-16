#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def check_priority_inbox():
    """
    Check priority inbox for important messages
    """
    check_config = {
        "accounts": [
            "premiummedscollective@gmail.com",
            "bweldy82@gmail.com"
        ],
        "priorities": [
            "customer_service",
            "orders",
            "support",
            "urgent"
        ]
    }
    
    print(json.dumps(check_config))
    
if __name__ == "__main__":
    check_priority_inbox()