# Here we are just dumping the and logging the data in the .json format 
import json 
from datetime import datetime
import os 

LOG_FILE = "mood_log.json"


def log_entry(text , ai_response):
    entry = {
        "timestamp" : datetime.now().isoformat(),
         "input" : text, 
         "response" : ai_response
    }

    # Ensure existing log is valid JSON
    if not os.path.exists(LOG_FILE):
        data = []
    else:
        with open(LOG_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  # Corrupted or empty

    # Append and save
    data.append(entry)
    with open(LOG_FILE, 'w') as f:
        json.dump(data, f, indent=2)
