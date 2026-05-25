# SOC Security Monitoring Lab: Wazuh, Suricata, Linux and Windows

This project is a hands-on SOC-style lab built to practice security monitoring, alert investigation, endpoint visibility, IDS log collection, and basic incident documentation.

The lab includes Wazuh SIEM, Suricata IDS, Linux and Windows monitored endpoints, Sysmon, authentication log analysis, File Integrity Monitoring, and MITRE ATT&CK mapping.

---

## Key Skills Demonstrated

- SIEM deployment and alert review with Wazuh
- Linux endpoint monitoring with Wazuh Agent
- Windows event monitoring with Wazuh Agent
- Suricata IDS log collection through `eve.json`
- Linux authentication log investigation
- Windows Security Event ID analysis
- File Integrity Monitoring
- Basic Sysmon-based investigation
- SOC-style alert triage and documentation
- MITRE ATT&CK mapping for detection scenarios

---

## Project Goal

The goal of this project is to build a small SOC-style security monitoring lab using Wazuh and Suricata.

The lab demonstrates endpoint monitoring, Linux authentication log analysis, File Integrity Monitoring, Suricata IDS event collection, and basic incident investigation workflow.

This project was created as a portfolio project for Junior SOC Analyst / Cyber Security Analyst roles.

---

## Lab Architecture

The lab was built in a local virtualized environment using isolated virtual machines.

### Main Components

| Component | Role |
|---|---|
| Wazuh Server | Central SIEM platform for collecting and analyzing alerts |
| Ubuntu monitored host | Linux endpoint monitored by Wazuh Agent |
| Suricata IDS | Network IDS installed on the monitored Ubuntu host |
| Kali Linux / Test VM | Controlled test traffic and security event generation |

### Lab Network

Example lab IP plan:

| Machine | Example IP | Purpose |
|---|---:|---|
| Wazuh Server | 192.168.62.10 | SIEM server |
| Ubuntu monitored host | 192.168.62.20 | Endpoint + Wazuh Agent + Suricata |
| Kali Linux / Test VM | 192.168.62.30 | Test traffic source |

All events were generated only inside the isolated local lab environment.

---

## Tools Used

- Wazuh
- Suricata
- Ubuntu Server
- Kali Linux
- VMware Workstation Pro
- Linux authentication logs
- File Integrity Monitoring
- JSON log collection
- Basic SOC investigation workflow

---

## Lab Environment

The lab consists of three main virtual machines:

1. **Wazuh Server**

   Used as the central SIEM platform.  
   It collects, processes, and visualizes security events from monitored endpoints.

2. **Ubuntu monitored host**

   Used as the Linux endpoint.  
   It runs Wazuh Agent and Suricata IDS.

3. **Kali Linux / Test VM**

   Used only for controlled test activity inside the lab network.

---

## MITRE ATT&CK Mapping

The completed investigation cases were mapped to relevant MITRE ATT&CK tactics and techniques where applicable.

The mapping is used for learning and documentation purposes.  
The lab events were controlled and intentionally generated inside an isolated environment.

Full mapping:

[MITRE ATT&CK Mapping](docs/mitre-attack-mapping.md)

---

## Detection Scenarios

| Case | Scenario | Data Source | Detection Focus |
|---|---|---|---|
| 1 | Failed SSH login attempts | Linux auth logs, Wazuh | Brute-force / suspicious authentication |
| 2 | File Integrity Monitoring | Wazuh FIM | Unauthorized file modification |
| 3 | Suricata network event | Suricata `eve.json`, Wazuh | Network IDS event review |
| 4 | Windows failed login attempts | Windows Security logs | Event ID 4625 |
| 5 | New local user created | Windows Security logs | Event ID 4720 |
| 6 | User added to Administrators group | Windows Security logs | Event ID 4732 |
| 7 | Suspicious PowerShell activity | Sysmon, PowerShell logs, Wazuh | Process and command-line visibility |

---

## Investigation Workflow

For each alert, the following investigation workflow was used:

1. Identify the alert type.
2. Check the affected host.
3. Review source and destination information.
4. Review related endpoint or network logs.
5. Assess whether the activity is expected or suspicious.
6. Document the potential risk.
7. Suggest remediation or monitoring actions.

---

## Screenshots

| Screenshot | Description |
|---|---|
| `01-wazuh-dashboard.png` | Wazuh Dashboard access |
| `02-wazuh-server-status.png` | Wazuh services status |
| `03-agent-connected.png` | Ubuntu agent connected to Wazuh |
| `04-agent-details.png` | Wazuh agent details |
| `05-linux-auth-log-failed-ssh.png` | Failed SSH login evidence in Linux logs |
| `06-wazuh-failed-ssh-alert.png` | Wazuh alert for failed SSH login attempts |
| `07-fim-test-directory.png` | Test directory for File Integrity Monitoring |
| `08-wazuh-file-integrity-alert.png` | Wazuh FIM alert |
| `09-suricata-installed.png` | Suricata installation and service check |
| `10-suricata-eve-json.png` | Suricata `eve.json` events |
| `11-wazuh-suricata-events.png` | Suricata events visible in Wazuh |
| `12-suricata-alert-details-in-wazuh.png` | Suricata event details in Wazuh |

---

## What This Project Demonstrates

This project demonstrates that I can:

- deploy a basic SIEM lab environment;
- connect Linux and Windows endpoints to Wazuh;
- collect and review endpoint and IDS events;
- investigate authentication, file integrity, and Windows account management alerts;
- document alerts using a structured SOC workflow;
- explain evidence, affected hosts, risk, and recommended actions;
- map selected detections to MITRE ATT&CK.

---

## Results

The lab successfully demonstrated:

- deployment of Wazuh Server as a central SIEM platform;
- connection of an Ubuntu endpoint using Wazuh Agent;
- collection and review of Linux authentication logs;
- detection of failed SSH login attempts;
- File Integrity Monitoring alert generation;
- Suricata IDS installation and event generation;
- collection of Suricata `eve.json` events in Wazuh;
- basic SOC-style investigation documentation.

## Limitations

This project was completed in a local virtualized lab environment.

The generated events were controlled and intentionally created for learning purposes.

The lab does not represent a full production SOC environment, but it demonstrates core monitoring and investigation concepts relevant to entry-level SOC work.

---

## Extension 1 — Windows Endpoint Monitoring

A Windows endpoint was added to the lab to extend monitoring beyond Linux systems.

The Windows VM was connected to the same isolated lab network and Wazuh Agent was installed on it.

This allows Wazuh to collect Windows endpoint events and prepares the lab for Sysmon-based detection scenarios.

Planned Windows scenarios:

- Windows failed login attempts
- New local user creation
- Suspicious PowerShell activity
- Sysmon process creation events

### Case 4 — Windows Failed Login Attempts

A Windows endpoint was added to the lab and monitored using Wazuh Agent.

Controlled failed login attempts were generated against a test local Windows user.  
Windows recorded these attempts as Security Event ID 4625, and Wazuh collected the related events.

This scenario demonstrates basic investigation of Windows authentication failures.

Investigation file:

`investigations/case-4-windows-failed-login.md`

### Case 5 — New Local User Created

A new local user account was created on the Windows endpoint as a controlled lab activity.

Windows recorded this action as Security Event ID 4720, and Wazuh collected the related event.

This scenario demonstrates investigation of Windows account management activity, which can be important for detecting unauthorized account creation or persistence attempts.

Investigation file:

`investigations/case-5-new-local-user-created.md`

### Case 6 — User Added to Local Administrators Group

A test local Windows user was added to the local Administrators group as controlled lab activity.

Windows recorded this action as Security Event ID 4732, and Wazuh collected the related event.

This scenario demonstrates investigation of privileged group membership changes, which can be important for detecting privilege escalation or unauthorized administrative access.

Investigation file:

`investigations/case-6-user-added-to-admins.md`

### Case 7 — Suspicious PowerShell Activity

PowerShell activity was generated on the Windows endpoint as controlled lab activity.

PowerShell logging and Sysmon were used to collect evidence about PowerShell execution.  
Wazuh collected the related Windows and Sysmon events and displayed them in the dashboard.

This scenario demonstrates basic investigation of PowerShell activity using process execution logs, command line visibility, Windows Event Logs, Sysmon, and Wazuh.

Investigation file:

`investigations/case-7-suspicious-powershell-activity.md`

--- 

## Future Improvements

Planned improvements:

- Add more custom Wazuh detection rules.
- Expand Sysmon-based detection scenarios.
- Add Windows process creation analysis with Event ID 4688 and Sysmon Event ID 1.
- Add basic threat hunting queries.
- Add more MITRE ATT&CK mappings for each case.
- Create a small Python log parser for selected Wazuh or Suricata events.
- Build a simple dashboard or report for security event summaries.

---
