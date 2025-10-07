import subprocess

def get_ports(port="all"):
    """
    Get active TCP/UDP ports. If a specific port is given, filter for that port.
    Returns a list of dictionaries with Protocol and Port (and optionally PID/Process if available).
    """
    data = []

    try:
        # Get all listening TCP/UDP ports
        result = subprocess.check_output(["ss", "-tulnp"]).decode()
        lines = result.splitlines()[1:]  # skip header

        for line in lines:
            parts = line.split()
            proto = parts[0]
            local_addr = parts[4]  # local address:port
            process_info = parts[-1] if '/' in parts[-1] else "-"  # PID/Process if available

            # Extract port number from address
            port_num = local_addr.rsplit(":", 1)[-1]

            if port == "all" or str(port) == port_num:
                data.append({
                    "Protocol": proto,
                    "Port": port_num,
                    "Process": process_info
                })

        # If specific port requested but not found
        if port != "all" and not data:
            data.append({"Protocol": "-", "Port": f"{port} not in use", "Process": "-"})

    except subprocess.CalledProcessError:
        data.append({"Protocol": "-", "Port": "Error retrieving ports", "Process": "-"})

    return data
