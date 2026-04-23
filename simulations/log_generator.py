import time
import random
from datetime import datetime, timedelta

# Configuration
USERS = ["admin", "root", "santhosh", "hr_manager", "dev_user", "guest"]
IPS = ["192.168.1.10", "192.168.1.50", "45.33.22.11", "185.122.3.4", "10.0.0.5"]
SERVERS = ["prod-web-01", "dev-db-01", "internal-app-01"]

def generate_linux_log(ip, user, server, status="Failed"):
    """Generates a mock /var/log/auth.log entry"""
    # Use current time occasionally, but also scatter some logs back in time
    current_time = datetime.now() - timedelta(minutes=random.randint(0, 60))
    timestamp = current_time.strftime("%b %d %H:%M:%S")
    
    if status == "Failed":
        return f"{timestamp} {server} sshd[1234]: Failed password for {user} from {ip} port {random.randint(1024, 65535)} ssh2\n"
    else:
        return f"{timestamp} {server} sshd[1234]: Accepted password for {user} from {ip} port {random.randint(1024, 65535)} ssh2\n"

def generate_windows_log(ip, user, status="Failed"):
    """Generates a mock Windows Security Event ID 4625/4624 simulation"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event_id = "4625" if status == "Failed" else "4624"
    return f"{timestamp} | EventCode={event_id} | User={user} | SourceIP={ip} | Message=An account {'failed' if status=='Failed' else 'succeeded'} to log on.\n"

def simulate_brute_force(ip, target_user, server):
    print(f"[*] Simulating Brute Force from {ip} on user {target_user} at {server}...")
    logs = []
    for _ in range(random.randint(10, 20)):
        logs.append(generate_linux_log(ip, target_user, server, "Failed"))
        time.sleep(0.1)
    return logs

if __name__ == "__main__":
    linux_log_path = "simulations/mock_auth.log"
    windows_log_path = "simulations/mock_windows_security.log"

    print("[+] Starting Advanced SOC Log Simulation...")
    
    # Clear old logs for a fresh demo if needed, but here we append to show history
    with open(linux_log_path, "a") as f_lin, open(windows_log_path, "a") as f_win:
        # 1. Random Background Noise (Successful logins)
        for _ in range(20):
            user = random.choice(USERS)
            ip = random.choice(IPS)
            server = random.choice(SERVERS)
            if ip in ["45.33.22.11", "185.122.3.4"]: continue # Attackers don't get in easily
            f_lin.write(generate_linux_log(ip, user, server, "Accepted"))
            f_win.write(generate_windows_log(ip, user, "Success"))

        # 2. Targeted Attack (The Brute Force)
        attacker_ip = "45.33.22.11"
        target = "root"
        target_server = "prod-web-01"
        bf_logs = simulate_brute_force(attacker_ip, target, target_server)
        for log in bf_logs:
            f_lin.write(log)
            
        # 3. Unusual Time Login (Manual Entry)
        # We simulate this by simply adding an entry that looks like it's from 3 AM
        timestamp_3am = (datetime.now().replace(hour=3, minute=15)).strftime("%b %d %H:%M:%S")
        f_lin.write(f"{timestamp_3am} prod-web-01 sshd[1234]: Accepted password for admin from 10.0.0.5 port 22 ssh2\n")

    print(f"[!] Simulation complete. Extra logs generated.")
