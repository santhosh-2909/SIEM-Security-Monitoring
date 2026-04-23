# 🛡️ SIEM Threat Detection & Alerting System

This repository contains a complete, implementation-ready SOC project designed for recruiters and technical interviews. It simulates a Splunk-based SIEM environment focused on authentication security.

## 🚀 Overview
- **Objective:** Detect Brute-Force attacks and Unusual Login patterns.
- **SIEM Platform:** Splunk (Logic can be ported to ELK/KQL).
- **Log Sources:** Windows Security Event Logs (4625/4624) and Linux `/var/log/auth.log`.
- **Advanced Features:** Threat Intel Enrichment, After-Hours detection, and Severity Scoring.

---

## 📂 Project Structure
- `backend/`: Core API and Log Processing logic (`main.py`, `log_processor.py`).
- `frontend/`: UI templates and static assets.
- `splunk_configs/`: Ingestion settings (`inputs.conf`, `props.conf`, lookup CSV).
- `detections/`: Production-ready SPL queries.
- `dashboards/`: XML code for visual monitoring.
- `simulations/`: Python script to generate sample logs and `cleanup_demo.sh` to reset.
- `docs/`: SOC Playbooks, Alert Templates, and Recruiter Reports.

---

## 🛠️ Step-by-Step Setup Guide

### 1. Ingesting Data
To simulate this in a local Splunk instance:
1. Copy `splunk_configs/suspicious_ips.csv` to `$SPLUNK_HOME/etc/apps/search/lookups/`.
2. Configure the lookup in Splunk Web (Settings > Lookups).
3. Install the **Splunk Add-on for Windows/Unix** to correctly parse these sourcetypes.

### 2. Running the Localhost SIEM Dashboard
1. Ensure Flask is installed: `pip install flask`
2. Start the backend:
```bash
cd backend
python3 main.py
```
3. View the UI at: **http://localhost:5000**

### 3. Setting Up Detections
Navigate to **Search & Reporting** in Splunk and paste the queries found in `detections/detection_queries.spl`. 
- **Saved Search:** Save the Brute Force query as an "Alert".
- **Trigger Conditions:** `Number of Results > 0`.
- **Action:** Add to "Triggered Alerts" or send an email.

### 4. Visualizing the SOC Dashboard
1. Go to **Dashboards** > **Create New Dashboard**.
2. Switch to the **Source** tab.
3. Paste the XML content from `dashboards/soc_overview.xml`.

---

## 📊 Key Detection Logic
| Use Case | Threshold | Severity |
| :--- | :--- | :--- |
| **Brute Force** | >= 5 fails / 5 mins | 🔥 High |
| **After-Hours** | 6 PM - 9 AM | ⚠️ Medium |
| **Threat Intel Match** | List of known malicious IPs | ☢️ Critical |

---

## 👔 Recruiter Demo Package
If presenting this for a job:
1. **Show the Dashboard:** Demonstrate the "Failed Login Trend" and "Active Alerts" panels.
2. **Explain the SPL:** Focus on how you used `eval` and `where` to filter noise.
3. **Simulate an Attack:** Run the script live and watch the dashboard update (near real-time).
4. **Report Sample:** Check `docs/demo_report.md` for a pre-written project summary.
