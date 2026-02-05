import json
from datetime import datetime

LOG_FILE = "logs/audit_log.json"

def log_event(data):
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
