#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def analyze_sales(date=None):
    """
    Analyze daily sales data and generate reports
    
    Args:
        date (str): Date to analyze (YYYY-MM-DD), defaults to today
    """
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
        
    # Format for data collection
    analysis_config = {
        "date": date,
        "metrics": [
            "total_sales",
            "order_count",
            "average_order",
            "top_products",
            "revenue_by_category"
        ]
    }
    
    print(json.dumps(analysis_config))
    
if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else None
    analyze_sales(date)