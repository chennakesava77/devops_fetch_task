import argparse
from modules import ports, docker_info, nginx_info, users, time_range, formatter
from monitor import monitor

def main():
    parser = argparse.ArgumentParser(description="DevOps system info tool")

    # Optional arguments
    parser.add_argument("-p", "--port", nargs="?", const="all", help="Show active ports or details of a specific port")
    parser.add_argument("-d", "--docker", nargs="?", const="all", help="Show Docker images/containers or specific container info")
    parser.add_argument("-n", "--nginx", nargs="?", const="all", help="Show Nginx domains and ports or specific domain info")
    parser.add_argument("-u", "--users", nargs="?", const="all", help="Show user logins or specific user info")
    parser.add_argument("-t", "--time", help="Show activities within a time range (e.g., '24h', '7d')")
    parser.add_argument("--monitor", action="store_true", help="Run in continuous monitoring mode")

    # Parse arguments
    args = parser.parse_args()

    # Handle each mode
    if args.monitor:
        monitor.run()
    elif args.port:
        data = ports.get_ports(args.port)
        formatter.print_table(data)
    elif args.docker:
        data = docker_info.get_docker(args.docker)
        formatter.print_table(data)
    elif args.nginx:
        data = nginx_info.get_nginx(args.nginx)
        formatter.print_table(data)
    elif args.users:
        data = users.get_users(args.users)
        formatter.print_table(data)
    elif args.time:
        data = time_range.get_activities(args.time)
        formatter.print_table(data)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
