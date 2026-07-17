# SOC Security Monitoring Lab — Wazuh, Suricata, Sysmon, Python, SQLite and Power BI

## Project Summary

This project is a hands-on SOC-style security monitoring lab created to practice endpoint monitoring, network IDS visibility, alert investigation, log analysis, and security reporting.

The lab combines **Wazuh SIEM**, **Suricata IDS**, **Linux and Windows monitored endpoints**, **Sysmon**, **MITRE ATT&CK mapping**, a **Python log analyzer**, **SQLite-based analysis**, and a **Power BI security dashboard**.

The project was built as a portfolio project for **Junior SOC Analyst / Cyber Security Analyst** roles.

---

## Key Skills Demonstrated

- SIEM deployment and alert review with Wazuh
- Linux endpoint monitoring with Wazuh Agent
- Windows endpoint monitoring with Wazuh Agent
- Suricata IDS log collection through `eve.json`
- Windows Security Event ID analysis
- Sysmon-based endpoint visibility
- Linux authentication log parsing with Python
- SQLite storage and SQL-based investigation
- Power BI dashboard creation
- File Integrity Monitoring
- SOC-style alert triage and investigation documentation
- MITRE ATT&CK mapping for selected detection scenarios
- Wazuh Active Response configuration (automated containment)

---

## Lab Architecture

The lab was built in a local virtualized environment using isolated virtual machines.

```text
Kali Linux / Test VM
        |
        | controlled test traffic
        v
Ubuntu monitored host
- Wazuh Agent
- Suricata IDS
- SSH service
        |
        | endpoint logs + Suricata eve.json
        v
Wazuh Server
- Wazuh Manager
- Wazuh Indexer
- Wazuh Dashboard

Windows endpoint
- Wazuh Agent
- Sysmon
- Windows Security logs
        |
        | Windows events + Sysmon telemetry
        v
Wazuh Server
```

All events were generated intentionally and only inside the isolated lab environment.

---

## Main Components

| Component | Purpose |
|---|---|
| Wazuh Server | Central SIEM platform for collecting, processing and reviewing alerts |
| Ubuntu monitored host | Linux endpoint monitored by Wazuh Agent |
| Suricata IDS | Network IDS installed on the Ubuntu monitored host |
| Kali Linux / Test VM | Controlled test traffic and authentication event generation |
| Windows endpoint | Windows system monitored by Wazuh Agent |
| Sysmon | Detailed Windows endpoint telemetry |
| Python Log Analyzer | Linux authentication log parsing and report generation |
| SQLite | Structured event storage and SQL-based analysis |
| Power BI | Security event dashboard and reporting |

---

## Example Lab Network

| Machine | Example IP | Purpose |
|---|---:|---|
| Wazuh Server | `192.168.62.10` | SIEM server |
| Ubuntu monitored host | `192.168.62.20` | Linux endpoint, Wazuh Agent, Suricata |
| Kali Linux / Test VM | DHCP-assigned, for example `192.168.62.129` | Controlled test traffic |
| Windows endpoint | `192.168.62.40` | Windows logs, Sysmon, Wazuh Agent |

---

## Tools Used

- Wazuh
- Suricata
- Sysmon
- Ubuntu Server
- Kali Linux
- Windows
- VMware Workstation Pro
- Python
- SQLite
- SQL
- Power BI
- MITRE ATT&CK
- iptables

---

## Investigation Cases

| Case | Scenario | Main Data Source | Detection Focus |
|---|---|---|---|
| Case 1 | SSH brute-force / failed login attempts | Linux authentication logs, Wazuh | Suspicious authentication / brute-force behavior |
| Case 2 | File Integrity Monitoring | Wazuh FIM, Ubuntu endpoint | Unauthorized file modification detection |
| Case 3 | Suricata network event | Suricata `eve.json`, Wazuh | Network IDS event review |
| Case 4 | Windows failed login attempts | Windows Security logs, Wazuh | Event ID 4625 / authentication failure investigation |
| Case 5 | New local user created | Windows Security logs, Wazuh | Event ID 4720 / account creation monitoring |
| Case 6 | User added to Administrators group | Windows Security logs, Wazuh | Event ID 4732 / privileged group change |
| Case 7 | Suspicious PowerShell activity | Windows Security logs, Sysmon, Wazuh | Event ID 4688 / process creation investigation |
| Case 8 | SSH brute-force with automated containment | Wazuh Active Response, iptables | Automated IP blocking (T1110 Brute Force) |

Investigation files are stored in:

```text
investigations/
```

---

## Investigation Workflow

For each case, the following workflow was used:

1. Identify the alert or event type.
2. Check the affected host.
3. Review source, target, user and timestamp information.
4. Review related endpoint, network or Windows logs.
5. Assess whether the activity is expected or suspicious.
6. Document the risk.
7. Suggest recommended actions.
8. Map the case to MITRE ATT&CK where applicable.

---

## MITRE ATT&CK Mapping

The completed investigation cases were mapped to relevant MITRE ATT&CK tactics and techniques where applicable.

The mapping is used for learning and documentation purposes. The lab events were controlled and intentionally generated inside an isolated environment.

Full mapping:

```text
docs/mitre-attack-mapping.md
```

---

## Data Analysis Pipeline

The project also includes a small security data analysis pipeline.

```text
Linux auth.log
    ↓
Python Log Analyzer
    ↓
CSV + SQLite database
    ↓
SQL analysis
    ↓
Power BI dashboard
```

The Python analyzer extracts SSH authentication events, stores them in CSV and SQLite formats, detects failed-to-success login patterns, and prepares a structured dataset for Power BI.

---

## Python Log Analyzer

The Python log analyzer processes Linux authentication logs and extracts SSH authentication events.

Analyzer folder:

```text
python-log-analyzer/
```

Main outputs:

```text
python-log-analyzer/output/ssh_auth_events.csv
python-log-analyzer/output/security_events_for_powerbi.csv
python-log-analyzer/output/auth_events.db
```

The analyzer supports common SSH log formats such as:

```text
sshd[PID]
sshd-session[PID]
```

It extracts:

- timestamp
- host
- username
- source IP
- source port
- event type
- raw log line

It also creates a Power BI-ready CSV dataset with normalized fields such as:

- event date
- event time
- host
- user
- source IP
- event type
- risk level
- event count

---

## SQLite and SQL Analysis

Parsed SSH authentication events are stored in a SQLite database:

```text
python-log-analyzer/output/auth_events.db
```

SQL queries are stored in:

```text
python-log-analyzer/queries/
```

Implemented query examples:

- top failed source IPs
- failed attempts by username
- failed-to-success login patterns
- Power BI summary query

This part demonstrates how Python and SQL can support SOC-style log analysis.

---

## Power BI Security Dashboard

A Power BI dashboard was created using the structured CSV dataset generated by the Python log analyzer.

Dashboard file:

```text
powerbi-dashboard/security-authentication-dashboard.pbix
```

Dataset:

```text
python-log-analyzer/output/security_events_for_powerbi.csv
```

The dashboard visualizes:

- total authentication events
- failed SSH login attempts
- successful SSH logins
- unique source IP addresses
- failed logins by source IP
- failed logins by targeted user
- events by risk level
- event type breakdown
- detailed authentication event table

---

## Screenshots

Screenshots are stored in:

```text
screenshots/
```

Main screenshot groups:

| Screenshot Range | Description |
|---|---|
| `01`–`04` | Wazuh Server and Linux agent setup |
| `05`–`08` | Failed SSH login and File Integrity Monitoring cases |
| `09`–`12` | Suricata installation and Wazuh integration |
| `13`–`16` | Windows Agent and Sysmon monitoring |
| `17`–`24` | Windows investigation cases |
| `25`–`28` | Python analyzer, SQLite and Power BI dataset preparation |
| `29`–`30` | Power BI security dashboard |
| `31`–`36` | Active Response config, brute-force alert, active-response log, iptables block |

---

## What This Project Demonstrates

This project demonstrates the ability to:

- deploy a basic SIEM lab environment;
- connect Linux and Windows endpoints to Wazuh;
- collect and review endpoint and IDS events;
- investigate Linux and Windows authentication events;
- configure File Integrity Monitoring;
- integrate Suricata IDS logs with Wazuh;
- collect Windows Security and Sysmon events;
- investigate Windows account management events;
- review PowerShell activity using Windows logs and Sysmon;
- document alerts using a structured SOC workflow;
- map selected detections to MITRE ATT&CK;
- automate Linux log parsing with Python;
- store parsed events in SQLite;
- run SQL-based security analysis;
- build a Power BI dashboard for security event reporting.
- configure automated containment (Active Response) for high-confidence detections;

---

## Results

The lab successfully demonstrated:

- Wazuh Server deployment as a central SIEM platform;
- Linux endpoint monitoring with Wazuh Agent;
- Windows endpoint monitoring with Wazuh Agent;
- failed SSH login detection;
- File Integrity Monitoring alert generation;
- Suricata IDS installation and event generation;
- Suricata `eve.json` collection in Wazuh;
- Windows failed login detection;
- new local user creation detection;
- local Administrators group membership change detection;
- PowerShell activity monitoring with Sysmon and Wazuh;
- MITRE ATT&CK mapping for investigation cases;
- Python-based authentication log parsing;
- CSV and SQLite output generation;
- SQL-based authentication event analysis;
- Power BI security dashboard creation.
- automated SSH brute-force containment via Wazuh Active Response, verified end-to-end (alert → response log → firewall rule);

---

## Limitations

This project was completed in a local virtualized lab environment.

All events were generated intentionally and safely for learning purposes.

The lab does not represent a full production SOC environment. However, it demonstrates practical concepts relevant to entry-level SOC work, including log collection, alert review, investigation documentation, event analysis, and basic security reporting.

---

## Future Improvements

Possible future improvements:

- Add custom Wazuh detection rules.
- Expand Sysmon-based detection scenarios.
- Expand Windows process creation analysis with additional Sysmon Event ID 1 examples.
- Add additional threat hunting queries.
- Add more Suricata detection scenarios.
- Add more Power BI pages for Windows and Suricata events.
- Improve timestamp parsing by adding full year and normalized datetime fields.
- Add automated export from Wazuh alerts to the analysis pipeline.

---

## Repository Structure

```text
.
├── investigations/              # SOC-style investigation reports
├── docs/                         # MITRE ATT&CK mapping and supporting documentation
├── python-log-analyzer/          # Python parser, SQLite database and SQL queries
│   ├── output/                   # Generated CSV and SQLite outputs
│   └── queries/                  # SQL investigation queries
├── powerbi-dashboard/            # Power BI dashboard file
├── screenshots/                  # Lab screenshots and evidence
└── README.md
```

---

## Project Status

The main version of this portfolio project is complete.

Completed parts:

- Wazuh SIEM lab
- Linux endpoint monitoring
- Suricata IDS integration
- Windows endpoint monitoring
- Sysmon monitoring
- eight documented investigation cases
- MITRE ATT&CK mapping
- Python log analyzer
- SQLite and SQL analysis
- Power BI security dashboard

---

## How to Use This Project

1. Review the lab architecture and tools used.
2. Open the `investigations/` folder to read SOC-style case reports.
3. Review the Python log analyzer in `python-log-analyzer/`.
4. Check generated CSV and SQLite outputs in `python-log-analyzer/output/`.
5. Open the Power BI dashboard to review authentication event visualizations.
6. Use screenshots as supporting evidence for the completed lab scenarios.
