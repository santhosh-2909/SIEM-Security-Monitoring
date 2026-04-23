# 📧 SIEM Alert Notification Templates

Use these templates to configure your SIEM's automated alerting (Email, Slack, or Teams).

---

## 🔴 HIGH: Brute Force Attack Detected
**Trigger:** 5+ Failed logins in 5 mins.

**Subject:** [SIEM ALERT - HIGH] Brute Force Detected from IP: $src_ip$

**Message Body:**
The SOC detection engine has triggered a high-severity alert.

**Summary Details:**
- **Source IP:** $src_ip$
- **Targeted Account(s):** $attempted_users$
- **Total Attempts:** $failure_count$
- **Time Window:** 5 Minutes
- **Host Affected:** $host$

**Action Required:**
Please refer to **SOC-PB-001 (Brute-Force Playbook)** for immediate containment steps. Verify if any successful logins occurred from this IP before blocking.

---

## 🟡 MEDIUM: After-Hours Login Detected
**Trigger:** Successful login between 6 PM and 9 AM.

**Subject:** [SIEM ALERT - MEDIUM] After-Hours Activity by User: $user$

**Message Body:**
A successful login was detected outside of standard business hours (09:00 - 18:00).

**Details:**
- **User:** $user$
- **Login Time:** $hour$
- **Source IP:** $src_ip$
- **Host:** $host$

**Action Required:**
Verify if this activity was pre-approved via Change Request or if it's an authorized employee working overtime. If suspicious, contact the user via secondary channel.

---

## 🔵 LOW: First Time Login from New IP
**Trigger:** Successful login from an IP not seen for this user in 30 days.

**Subject:** [SIEM ALERT - INFO] New Login Location for $user$

**Message Body:**
A login was detected from a new source IP address for this user.

**Details:**
- **User:** $user$
- **New IP:** $src_ip$
- **Previous Known IPs:** See User History Dashboard

**Action Required:**
Informational only. Ensure the user is not traveling or using a new VPN without authorization.
