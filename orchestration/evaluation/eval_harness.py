import time
from metrics.grounding_accuracy import compute_grounding_accuracy
from metrics.latency_tracker import track_latency

def evaluate_agent_response(agent_output, gold_standard):
    accuracy = compute_grounding_accuracy(agent_output, gold_standard)
    latency = track_latency(agent_output)
    return {
        "grounding_accuracy": accuracy,
        "latency_ms": latency
    }
