#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def generate_email_report(start_date=None, end_date=None):
    """
    Generate comprehensive email activity report
    
    Args:
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)
    """
    report_config = {
        "date_range": {
            "start": start_date,
            "end": end_date
        },
        "metrics": [
            "message_volume",
            "response_times",
            "category_distribution",
            "priority_levels",
            "resolution_rates"
        ],
        "format": "markdown"
    }
    
    print(json.dumps(report_config))
    
if __name__ == "__main__":
    start = sys.argv[1] if len(sys.argv) > 1 else None
    end = sys.argv[2] if len(sys.argv) > 2 else None
    generate_email_report(start, end)