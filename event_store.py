"""
Event Store
-----------
Persists observability events for replay and audits.
"""
import json

class EventStore:
    def __init__(self, path="events.jsonl"):
        self.path = path

    def write(self, event):
        with open(self.path, "a") as f:
            f.write(json.dumps(event) + "
")
