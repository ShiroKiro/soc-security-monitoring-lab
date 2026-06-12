# Case 1 — Failed SSH Login Attempts

## 1. Case Summary

This investigation focuses on repeated failed SSH authentication attempts detected in Linux authentication logs.  
The activity may indicate brute-force behavior, password guessing, or unauthorized access attempts against the monitored host.

## 2. Data Source

- Source system: Ubuntu Server
- Log source: `/var/log/auth.log`
- Detection tool: Python log analyzer / Wazuh
- Related technology: SSH
- Event type: Failed authentication

## 3. Detection Focus

The main detection focus is identifying repeated SSH login failures from the same source IP address or against the same user account.

Suspicious indicators include:

- multiple failed SSH login attempts;
- login attempts for invalid users;
- repeated attempts from the same source IP;
- attempts against privileged accounts such as `root`;
- successful login after multiple failed attempts.

## 4. Example Log Evidence

```text
May 21 15:32:40 monitoredhost sshd-session[120402]: Failed password for invalid user wronguser from 192.168.62.129 port 52620 ssh2
May 21 15:33:01 monitoredhost sshd-session[120403]: Failed password for root from 192.168.62.129 port 52621 ssh2
May 21 15:33:15 monitoredhost sshd-session[120404]: Failed password for root from 192.168.62.129 port 52622 ssh2
May 21 15:33:28 monitoredhost sshd-session[120405]: Failed password for root from 192.168.62.129 port 52623 ssh2
May 21 15:33:42 monitoredhost sshd-session[120406]: Failed password for root from 192.168.62.129 port 52624 ssh2
May 21 15:34:05 monitoredhost sshd-session[120407]: Failed password for root from 192.168.62.129 port 52625 ssh2
```

## 5. Investigation Steps

Reviewed Linux authentication logs.
Filtered SSH authentication events.
Identified failed login attempts.
Grouped failed attempts by source IP address.
Checked whether the attempts targeted valid or invalid users.
Reviewed whether a successful login occurred after repeated failures.
Assigned severity based on the number and pattern of failed attempts.

## 6. Detection Logic

The activity is considered suspicious when one source IP address generates multiple failed SSH login attempts within a short period of time.

### Detection rule:

If one source IP has 5 or more failed SSH login attempts,
mark the activity as potential brute-force behavior.

### Additional high-risk condition:

If a successful login occurs after multiple failed attempts from the same source IP,
mark the event as high severity.

## 7. Findings

Field	Value
Source IP	192.168.62.129
Target host	monitoredhost
Targeted users	wronguser, root
Event type	Failed SSH login
Failed attempts	6
Invalid user attempt	Yes
Privileged account targeted	Yes, root
Severity	High

## 8. Analysis

The source IP address 192.168.62.129 generated multiple failed SSH login attempts against the monitored host.
The activity included an invalid username and repeated attempts against the root account.

This behavior is consistent with SSH brute-force activity or password guessing.
Attempts against the root account increase the severity because successful compromise of this account could provide full administrative access to the system.

## 9. MITRE ATT&CK Mapping

Tactic	Technique	Description
Credential Access	T1110 — Brute Force	Repeated attempts to guess valid credentials
Initial Access	T1078 — Valid Accounts	Possible use of valid credentials after successful login

## 10. Impact

Potential impact includes:

unauthorized access to the server;
compromise of privileged accounts;
lateral movement inside the network;
further deployment of malicious tools;
data exposure or system manipulation.

## 11. Recommended Response Actions

Block or investigate the source IP address.
Review whether any successful login occurred from the same source IP.
Disable direct SSH login for the root account.
Enforce strong passwords or SSH key-based authentication.
Enable account lockout or rate limiting.
Review other hosts for similar authentication attempts.
Continue monitoring SSH authentication events in Wazuh.

## 12. Recommended Preventive Measures

Disable password-based SSH authentication where possible.
Use SSH keys instead of passwords.
Restrict SSH access by firewall rules.
Disable root login via SSH.
Enable MFA where supported.
Use Fail2Ban or similar protection.
Regularly review authentication logs.

## 13. SOC Analyst Conclusion

The observed activity should be treated as a high-severity authentication security event.
Multiple failed SSH login attempts from the same source IP, especially against the root account, indicate possible brute-force behavior.

The recommended action is to investigate the source IP, verify whether any successful authentication occurred, and apply SSH hardening measures.