#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def check_rankings(keywords=None):
    """
    Check keyword rankings and positions
    
    Args:
        keywords (list): List of keywords to check, or None for default set
    """
    if keywords is None:
        keywords = [
            "cannabis delivery orange county",
            "weed delivery near me",
            "marijuana delivery service",
            "premium cannabis delivery",
            "same day cannabis delivery"
        ]
    
    check_config = {
        "keywords": keywords,
        "locations": ["Orange County, CA"],
        "devices": ["mobile", "desktop"]
    }
    
    print(json.dumps(check_config))
    
if __name__ == "__main__":
    keywords = sys.argv[1:] if len(sys.argv) > 1 else None
    check_rankings(keywords)