import re

def get_nginx(domain):
    with open("/etc/nginx/sites-enabled/default") as f:
        config = f.read()
    blocks = re.findall(r"server \{.*?\}", config, re.DOTALL)
    data = []
    for block in blocks:
        server_name = re.search(r"server_name\s+(.*);", block)
        listen = re.search(r"listen\s+(\d+);", block)
        if server_name and listen:
            data.append({"Domain": server_name.group(1), "Port": listen.group(1)})
    if domain == "all":
        return data
    return [entry for entry in data if domain in entry["Domain"]]
