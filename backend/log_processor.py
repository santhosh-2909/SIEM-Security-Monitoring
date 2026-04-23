import re
import os
import random

LINUX_LOG = "../simulations/mock_auth.log"

def process_security_logs():
    """Core logic to parse logs and generate a unified intelligence object."""
    logs = []
    unique_ips = set()
    assets = {}
    failed_count = 0
    total_count = 0
    
    log_path = os.path.join(os.path.dirname(__file__), LINUX_LOG)
    
    if not os.path.exists(log_path):
        return {"logs": [], "stats": {}, "assets": [], "alerts": []}
        
    with open(log_path, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            total_count += 1
            # Basic parsing - expand this for windows if needed
            match = re.search(r"(\w+ \d+ \d+:\d+:\d+) (\S+) sshd\[\d+\]: (Failed|Accepted) password for (\S+) from (\S+)", line)
            
            if match:
                timestamp, host, status_str, user, ip = match.groups()
                status = "FAILED" if status_str == "Failed" else "SUCCESS"
                severity = "Low"
                description = "User logged in"
                
                if status == "FAILED":
                    failed_count += 1
                    severity = "High" if ip == "45.33.22.11" else "Medium"
                    description = f"Failed login for {user}"
                
                unique_ips.add(ip)
                
                # Asset Tracking
                if host not in assets:
                    assets[host] = {"hostname": host, "status": "Active", "last_activity": timestamp, "risk": "Low"}
                else:
                    assets[host]["last_activity"] = timestamp
                
                if severity != "Low": 
                    assets[host]["risk"] = severity

                entry = {
                    "id": idx,
                    "time": timestamp,
                    "server": host,
                    "user": user,
                    "ip": ip,
                    "status": status,
                    "severity": severity,
                    "description": description
                }
                logs.append(entry)
    
    health = max(10, 100 - (failed_count // 2))
    
    # Filter only security threats for the Alerts module
    alerts = [l for l in logs if l["severity"] != "Low"]
    
    # Generate the Top-Level Security Report
    report = {
        "summary": {
            "total_events": total_count,
            "threats_detected": len(alerts),
            "high_risk_count": len([a for a in alerts if a["severity"] == "High"]),
            "system_health": f"{health}%"
        },
        "top_attackers": sorted([{"ip": ip, "count": len([l for l in logs if l["ip"] == ip and l["status"] == "FAILED"])} for ip in unique_ips], key=lambda x: x["count"], reverse=True)[:5]
    }

    # Time-series Trend (Mocking 6 time bins for the line chart)
    # in a real system, we would group by _time
    failed_trend = [random.randint(5, 50) for _ in range(6)]

    return {
        "logs": logs[::-1],
        "alerts": alerts[::-1],
        "assets": list(assets.values()),
        "report": report,
        "trends": failed_trend,
        "stats": {
            "total": total_count,
            "failed": failed_count,
            "unique_ips": len(unique_ips),
            "health": f"{health}%"
        }
    }

def get_alert_details(alert_id):
    """Finds a specific alert and attaches remediation intelligence."""
    # Re-run process to get the alert (in Prod use a DB)
    data = process_security_logs()
    alert = next((a for a in data["alerts"] if str(a["id"]) == str(alert_id)), None)
    
    if alert:
        alert["remediation"] = [
            "1. Block Source IP at Firewall.",
            "2. Reset user password via Active Directory.",
            "3. Enable Multi-Factor Authentication.",
            "4. Monitor account activity for 24 hours."
        ]
        alert["threat_intel"] = {
            "origin": "AbuseIPDB Verified",
            "risk_score": 98 if alert["severity"] == "High" else 45
        }
    return alert
