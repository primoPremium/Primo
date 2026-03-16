"""Helper module for OpenClaw tool access"""

class ToolWrapper:
    """Wrapper for OpenClaw tools that provides a more Pythonic interface"""
    def __init__(self, name):
        self.name = name
        self.args = {}
    
    def __setattr__(self, name, value):
        if name in ('name', 'args'):
            super().__setattr__(name, value)
        else:
            self.args[name] = value
    
    def invoke(self):
        # Import here to avoid circular imports
        from openclaw import agent
        return agent.invoke_tool(self.name, self.args)

# Tool instances
browser = ToolWrapper('browser')