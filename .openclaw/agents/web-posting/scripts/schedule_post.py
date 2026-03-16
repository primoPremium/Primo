#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def schedule_social_post(platform, content, schedule_time):
    """
    Schedule a social media post
    
    Args:
        platform (str): Social platform (instagram|facebook|twitter)
        content (str): Post content
        schedule_time (str): Scheduled time (YYYY-MM-DD HH:MM)
    """
    # Create memory entry for scheduled post
    post_data = {
        "platform": platform,
        "content": content,
        "schedule_time": schedule_time,
        "status": "scheduled"
    }
    
    print(json.dumps(post_data))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: schedule_post.py <platform> <content> <schedule_time>")
        sys.exit(1)
        
    schedule_social_post(sys.argv[1], sys.argv[2], sys.argv[3])