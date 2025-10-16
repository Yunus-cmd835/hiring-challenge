# solutions/Yunus Evangeline/logger.py

import json
from datetime import datetime

def log_step(step, success, message):
    log = {
        "step": step,
        "success": success,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }
    print(json.dumps(log))
    with open("execution_logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")
