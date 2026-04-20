"""
Decision Tracing Engine
-----------------------
Captures every agent decision, tool call, and state transition.
"""

class DecisionTrace:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.events = []

    def log(self, event_type, payload):
        self.events.append({
            "type": event_type,
            "payload": payload
        })

    def export(self):
        return self.events
