# 📓 SOC Playbook: Brute-Force Attack Response

**Playbook ID:** SOC-PB-001  
**Category:** Access Management / Authentication  
**Severity:** Medium to High  

## 1. Identification
*   **Alert Triggered:** `Brute Force Attack Detected`
*   **Threshold:** >5 failed login attempts from a single source IP within 5 minutes.
*   **Data Sources:** Linux `/var/log/auth.log`, Windows Event ID 4625.

## 2. Triage & Validation
1.  **Verify Source IP:** Check if the IP is internal (Local LAN/VPN) or external (Internet).
2.  **Enrich Data:** Perform a WHOIS lookup and check Threat Intel (e.g., AbuseIPDB, Virustotal).
3.  **Check Success:** Did any login from this IP succeed after the failures? 
    *   *Search:* `index=security_logs src_ip="[Attacker_IP]" (EventCode=4624 OR "Accepted password")`
4.  **Scope Impact:** Are other users being targeted by the same IP? Is the same user being targeted from other IPs?

## 3. Containment
1.  **Block IP:** If the IP is external and malicious, add it to the firewall's blocklist (Shun/Drop).
2.  **Disable Account:** If the brute-force was successful or targeting a critical account (e.g., `root`, `admin`), temporarily disable the account in Active Directory or `/etc/passwd`.
3.  **Reset Password:** Force a password reset for the targeted user.

## 4. Eradication
1.  **Rotate Keys:** If using SSH keys, rotate them for the compromised account.
2.  **Apply MFA:** Ensure Multi-Factor Authentication is enforced for the user.
3.  **Patching:** Ensure the target system has the latest security patches for SSH/RDP.

## 5. Recovery
1.  **Monitor Activity:** Keep a close watch on the user's activity for the next 24-48 hours.
2.  **Restore Access:** Once the threat is neutralized and the password is reset, restore account access.

## 6. Lessons Learned
1.  **Threshold Adjustment:** Was the alert too sensitive or not sensitive enough?
2.  **Attack Vector:** How did the attacker find the target? (e.g., Open port 22/3389).
3.  **Recommendation:** Recommend moving SSH to a non-standard port or using a VPN.
