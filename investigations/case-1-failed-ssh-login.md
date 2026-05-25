# Case 1 — Failed SSH Login Attempts

## What happened?

Multiple failed SSH login attempts were generated against the monitored Ubuntu endpoint.

## Source

- Source IP: 192.168.62.129
- Source host: Kali Linux test VM

## Target

- Target IP: 192.168.62.20
- Target host: Ubuntu monitored host
- Target user: shiro / wronguser

## Evidence

- Linux authentication logs showed failed SSH login attempts.
- Wazuh generated an alert based on SSH authentication activity.

## Investigation Steps

1. Checked SSH service status on the monitored Ubuntu endpoint.
2. Generated controlled failed SSH login attempts from Kali Linux.
3. Reviewed authentication logs on the Ubuntu endpoint.
4. Identified source IP, target host, and targeted username.
5. Reviewed the related Wazuh alert in the dashboard.
6. Checked whether any successful login followed the failed attempts.

## Risk

Repeated failed SSH login attempts may indicate brute-force activity or unauthorized access attempts.

## Recommended Actions

- Verify whether the source IP is trusted.
- Disable password-based SSH login where possible.
- Use SSH keys.
- Apply rate limiting.
- Monitor repeated failed attempts.
- Review user accounts and permissions.

## Result

The lab successfully demonstrated detection and investigation of failed SSH login attempts using Linux authentication logs and Wazuh.

## MITRE ATT&CK Mapping

- Tactic: Credential Access
- Technique: T1110 — Brute Force
- Reason: Repeated failed SSH login attempts may indicate password guessing or brute-force behavior.