#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def broadcast_event(event_type, data, target_agents=None):
    """
    Broadcast events to relevant agents
    
    Args:
        event_type (str): Type of event (alert|update|request)
        data (dict): Event data
        target_agents (list): List of target agents, or None for auto-routing
    """
    event = {
        "type": event_type,
        "timestamp": datetime.now().isoformat(),
        "data": data,
        "source": "cross_agent_coordinator",
        "targets": target_agents
    }
    
    # Add to event stream
    print(json.dumps(event))
    
def route_task(task_type, task_data):
    """
    Route tasks to appropriate agents based on type
    
    Args:
        task_type (str): Type of task
        task_data (dict): Task details
    """
    routing = {
        "market_research": ["research", "seo"],
        "content_update": ["web-posting", "seo"],
        "security_check": ["security", "integration"],
        "performance_analysis": ["analytics", "research"],
        "communication": ["email-manager"],
        "system_maintenance": ["integration", "security"]
    }
    
    task = {
        "type": task_type,
        "data": task_data,
        "assigned_to": routing.get(task_type, ["main"]),
        "timestamp": datetime.now().isoformat()
    }
    
    print(json.dumps(task))

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else None
    if command == "broadcast":
        event_type = sys.argv[2]
        data = json.loads(sys.argv[3])
        targets = sys.argv[4].split(',') if len(sys.argv) > 4 else None
        broadcast_event(event_type, data, targets)
    elif command == "route":
        task_type = sys.argv[2]
        task_data = json.loads(sys.argv[3])
        route_task(task_type, task_data)