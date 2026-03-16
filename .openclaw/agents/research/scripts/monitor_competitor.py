#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def monitor_competitor(url, output_dir):
    """
    Monitor a competitor's website and save snapshot data
    
    Args:
        url (str): Competitor website URL
        output_dir (str): Output directory for snapshots
    """
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Format for the OpenClaw browser tool
    browser_config = {
        "action": "snapshot",
        "profile": "openclaw",
        "targetUrl": url,
        "refs": "aria"
    }
    
    print(json.dumps(browser_config))
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: monitor_competitor.py <url> <output_dir>")
        sys.exit(1)
        
    monitor_competitor(sys.argv[1], sys.argv[2])