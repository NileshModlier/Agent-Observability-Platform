"""
Hallucination Detection
----------------------
Flags outputs unsupported by context or tools.
"""

def detect_hallucination(response, context):
    unsupported = [token for token in response.split() if token not in context]
    score = len(unsupported) / max(len(response.split()), 1)
    return score > 0.3
