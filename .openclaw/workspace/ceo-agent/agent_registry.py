class AgentRegistry:
    def __init__(self):
        self.agents = {}
        self.capability_index = {}
        
    def register(self, agent_config):
        agent_id = agent_config['id']
        if agent_id in self.agents:
            return False
            
        self.agents[agent_id] = {
            'config': agent_config,
            'status': 'idle',
            'last_heartbeat': None,
            'tasks_completed': 0
        }
        
        # Build capability index
        for capability in agent_config['capabilities']:
            if capability not in self.capability_index:
                self.capability_index[capability] = []
            self.capability_index[capability].append(agent_id)
            
        return True
    
    def get_available_agents(self):
        return [agent_id for agent_id, data in self.agents.items() 
                if data['status'] == 'idle']
    
    def get_agents_by_capability(self, capability):
        return self.capability_index.get(capability, [])
    
    def update_agent_status(self, agent_id, status):
        if agent_id in self.agents:
            self.agents[agent_id]['status'] = status
            self.agents[agent_id]['last_heartbeat'] = time.time()
            return True
        return False
    
    def save_to_file(self, filename="agent_states.json"):
        with open(filename, "w") as f:
            json.dump(self.agents, f)
    
    def load_from_file(self, filename="agent_states.json"):
        with open(filename, "r") as f:
            self.agents = json.load(f)