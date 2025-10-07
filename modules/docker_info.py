import subprocess
import json

def get_docker(target="all"):
    data = []

    if target == "all":
        # Get Docker images
        images = subprocess.check_output(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"]
        ).decode().splitlines()
        for img in images:
            data.append({"Type": "Image", "Name": img, "Status": "", "Ports": ""})

        # Get Docker containers
        containers = subprocess.check_output(
            ["docker", "ps", "-a", "--format", "{{.Names}}|{{.Status}}|{{.Ports}}"]
        ).decode().splitlines()
        for c in containers:
            name, status, ports = c.split("|")
            data.append({"Type": "Container", "Name": name, "Status": status, "Ports": ports})

    else:
        # Inspect a specific container/image
        try:
            result = subprocess.check_output(["docker", "inspect", target]).decode()
            data = json.loads(result)
        except subprocess.CalledProcessError:
            data = [{"Type": "-", "Name": target, "Status": "Not found", "Ports": ""}]

    # Remove duplicates
    seen = set()
    unique_data = []
    for entry in data:
        key = (entry.get("Type"), entry.get("Name"))
        if key not in seen:
            seen.add(key)
            unique_data.append(entry)

    return unique_data
