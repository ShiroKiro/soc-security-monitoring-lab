# MITRE ATT&CK Mapping

## Purpose

This document maps the lab investigation cases to relevant MITRE ATT&CK tactics and techniques.

The mapping is used for learning and documentation purposes.  
The events in this lab were controlled and intentionally generated inside an isolated environment.

---

## Mapping Summary

| Case | Scenario | ATT&CK Tactic | ATT&CK Technique | Evidence |
|---|---|---|---|---|
| Case 1 | Failed SSH Login Attempts | Credential Access | T1110 — Brute Force | Linux authentication logs, failed SSH attempts, Wazuh alert |
| Case 2 | File Integrity Monitoring Alert | Defense Evasion / Persistence context | Not directly mapped | File modification detected by Wazuh FIM |
| Case 3 | Suricata Network Event | Discovery / Command and Control context | Not directly mapped | Suricata `eve.json`, source/destination IP, protocol |
| Case 4 | Windows Failed Login Attempts | Credential Access | T1110 — Brute Force | Windows Security Event ID 4625, Wazuh alert |
| Case 5 | New Local User Created | Persistence | T1136.001 — Create Account: Local Account | Windows Security Event ID 4720, Wazuh alert |
| Case 6 | User Added to Local Administrators Group | Persistence / Privilege Escalation | T1098.007 — Account Manipulation: Additional Local or Domain Groups | Windows Security Event ID 4732, Wazuh alert |
| Case 7 | Suspicious PowerShell Activity | Execution | T1059.001 — Command and Scripting Interpreter: PowerShell | PowerShell logs, Sysmon Event ID 1, Wazuh event |

---

## Case 1 — Failed SSH Login Attempts

### Mapping

- Tactic: Credential Access
- Technique: T1110 — Brute Force

### Why this mapping fits

Repeated failed SSH login attempts may represent password guessing or brute-force behavior.

### Evidence in this lab

- Linux authentication log showed failed SSH login attempts.
- Wazuh generated related authentication alerts.
- Source IP and targeted username were reviewed.

---

## Case 2 — File Integrity Monitoring Alert

### Mapping

- Tactic: Context-dependent
- Technique: Not directly mapped in this lab

### Why this mapping is limited

A file modification alone is not enough to confidently map the activity to one specific ATT&CK technique.

In a real incident, the mapping would depend on which file was changed and why.  
For example, changes to startup files, SSH keys, scheduled tasks, or security tool configuration could indicate persistence or defense evasion.

### Evidence in this lab

- A test file was modified in `/opt/test-monitoring`.
- Wazuh File Integrity Monitoring detected the change.

---

## Case 3 — Suricata Network Event

### Mapping

- Tactic: Context-dependent
- Technique: Not directly mapped in this lab

### Why this mapping is limited

A generic network event such as DNS, HTTP, ICMP, or flow activity is not enough to assign a specific ATT&CK technique.

In a real SOC investigation, mapping would depend on the full network behavior, destination, payload, frequency, and related endpoint activity.

### Evidence in this lab

- Suricata generated events in `/var/log/suricata/eve.json`.
- Wazuh collected and displayed Suricata events.
- Source IP, destination IP, protocol, and event type were reviewed.

---

## Case 4 — Windows Failed Login Attempts

### Mapping

- Tactic: Credential Access
- Technique: T1110 — Brute Force

### Why this mapping fits

Repeated failed Windows login attempts may represent password guessing or brute-force behavior.

### Evidence in this lab

- Windows Security Event ID 4625 was generated.
- Wazuh collected the event.
- Targeted username, timestamp, and affected host were reviewed.

---

## Case 5 — New Local User Created

### Mapping

- Tactic: Persistence
- Technique: T1136.001 — Create Account: Local Account

### Why this mapping fits

Creating a local account can be used to maintain access to a system after initial access.

### Evidence in this lab

- A test local user was created.
- Windows Security Event ID 4720 was generated.
- Wazuh collected and displayed the event.

---

## Case 6 — User Added to Local Administrators Group

### Mapping

- Tactic: Persistence / Privilege Escalation
- Technique: T1098.007 — Account Manipulation: Additional Local or Domain Groups

### Why this mapping fits

Adding a user to a privileged local group can grant elevated permissions and may support persistence or privilege escalation.

### Evidence in this lab

- A test user was added to the local Administrators group.
- Windows Security Event ID 4732 was generated.
- Wazuh collected and displayed the event.

---

## Case 7 — Suspicious PowerShell Activity

### Mapping

- Tactic: Execution
- Technique: T1059.001 — Command and Scripting Interpreter: PowerShell

### Why this mapping fits

PowerShell is a legitimate administration tool, but it can also be abused to execute commands and scripts.

### Evidence in this lab

- PowerShell activity was generated in a controlled way.
- Sysmon recorded PowerShell process creation.
- Wazuh collected PowerShell/Sysmon events.

---

## Important Note

This mapping does not mean that the lab events were real attacks.

The activity was intentionally generated for learning purposes.  
MITRE ATT&CK mapping is used here to connect observed behavior with common adversary techniques and SOC investigation logic.