import subprocess

def get_users(user):
    result = subprocess.check_output(["last"]).decode().splitlines()
    data = [{"User": line.split()[0], "Login Time": " ".join(line.split()[3:6])} for line in result if line]
    if user == "all":
        return data
    return [entry for entry in data if entry["User"] == user]
