from prometheus_client import Gauge

definitions = {
    "x-rate-limit-limit": "Nature API Rate Limit",
    "x-rate-limit-reset": "Nature API Rate Reset",
    "x-rate-limit-remaining": "Nature API Rate Limit Remaining",
}

metrics = {}
for label, desc in definitions.items():
    metrics[label] = Gauge(label.replace("-", "_"), desc)
