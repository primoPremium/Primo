import time
import random
from collections import deque
from queue import PriorityQueue

class TaskDistributor:
    def __init__(self):
        self.task_queue = deque()
        self.priority_queue = PriorityQueue()
        self.agent_load_balancer = {}
        self.distribution_strategy = "round_robin"
        
    def assign(self, task):
        # Find best agent based on capability
        capable_agents = self._find_capable_agents(task)
        
        if not capable_agents:
            return None
            
        # Select agent based on strategy
        selected_agent = self._select_agent(capable_agents)
        
        # Update agent status
        self._update_agent_load(selected_agent)
        
        return selected_agent
    
    def add_task(self, task, priority=1):
        self.priority_queue.put((priority, task))
    
    def get_next_task(self):
        return self.priority_queue.get()[1]
    
    def _find_capable_agents(self, task):
        # Simulate capability matching
        if task.get('required_capabilities'):
            return [f"agent_{i}" for i in range(1, 4)]  # Mock capable agents
        return []
    
    def _select_agent(self, agents):
        if self.distribution_strategy == "round_robin":
            return agents[0]  # Simplified round robin
        elif self.distribution_strategy == "least_loaded":
            return min(agents, key=lambda x: self.agent_load_balancer.get(x, 0))
        elif self.distribution_strategy == "random":
            return random.choice(agents)
    
    def _update_agent_load(self, agent_id):
        if agent_id not in self.agent_load_balancer:
            self.agent_load_balancer[agent_id] = 0
        self.agent_load_balancer[agent_id] += 1
    
    def complete_task(self, agent_id):
        if agent_id in self.agent_load_balancer:
            self.agent_load_balancer[agent_id] = max(0, self.agent_load_balancer[agent_id] - 1)