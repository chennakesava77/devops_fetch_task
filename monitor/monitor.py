import time
from monitor.logger import log_info
from modules import ports, docker_info, nginx_info, users

def run():
    while True:
        log_info("Monitoring ports", ports.get_ports("all"))
        log_info("Monitoring docker", docker_info.get_docker("all"))
        log_info("Monitoring nginx", nginx_info.get_nginx("all"))
        log_info("Monitoring users", users.get_users("all"))
        time.sleep(300)  # every 5 minutes
