import re
import json
from collections import defaultdict

def analyze_logs(filepath, threshold=3):
    failed_attempts = defaultdict(int)
    alerts = []

    pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - USER: (\w+) - STATUS: (.*)")

    with open(filepath, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                timestamp, user, status = match.groups()
                if "FAILED_LOGIN" in status:
                    failed_attempts[user] += 1
                    if failed_attempts[user] >= threshold:
                        alerts.append({
                            "timestamp": timestamp,
                            "threat": "Brute-Force Detected",
                            "user": user,
                            "count": failed_attempts[user]
                        })

    return alerts

if __name__ == "__main__":
    results = analyze_logs("sample_logs.log")
    print(json.dumps(results, indent=4))
