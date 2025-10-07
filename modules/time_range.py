import subprocess
from datetime import datetime, timedelta

def get_activities(range_str):
    now = datetime.now()
    if range_str.endswith("h"):
        delta = timedelta(hours=int(range_str[:-1]))
    elif range_str.endswith("d"):
        delta = timedelta(days=int(range_str[:-1]))
    else:
        return [{"Error": "Invalid time format. Use '24h' or '7d'"}]

    cutoff = now - delta
    result = subprocess.check_output(["journalctl", "--since", cutoff.strftime("%Y-%m-%d %H:%M:%S")]).decode()
    return [{"Log": line} for line in result.splitlines()]
