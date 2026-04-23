# Project Report: Brute-Force Attack Simulation & Detection

**Analyst:** [Your Name]  
**Date:** April 23, 2024  
**SIEM Platform:** Splunk Enterprise  

## 1. Executive Summary
This project demonstrates the deployment of a real-time threat detection system designed to monitor and alert on unauthorized access attempts. During the simulation, a high-severity brute-force attack was detected and successfully blocked by the logic.

## 2. Detection Methodology
- **Log Source:** SSH Authentication (`/var/log/auth.log`) and Windows Event ID 4625.
- **Threshold:** 5 failed logins within 300 seconds (5 minutes).
- **Enrichment:** IPs were cross-referenced against a global threat intelligence feed (Mock AbuseIPDB).

## 3. Incident Details
- **Timestamp:** 2024-04-23 12:41:16  
- **Source IP:** 45.33.22.11  
- **Country of Origin:** China (Matched via Threat Intel)  
- **Targeted Account:** `root`  
- **Total Attempts:** 7  

## 4. Visual Evidence
- **Dashboard:** Shown in `dashboards/soc_overview.xml`.
- **Alert Status:** Triggered.

## 5. Analyst Recommendation
- Immediately block the Source IP `45.33.22.11` at the edge firewall.
- Enable Multi-Factor Authentication (MFA) for the `root` account.
- Review recent successful logins from this IP range.
