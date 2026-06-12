# Analyst Summary

## Project Overview

This SOC Security Monitoring Lab was created as a hands-on portfolio project for Junior SOC Analyst / Cyber Security Analyst roles.

The project demonstrates practical experience with security monitoring, endpoint log collection, network IDS alerts, Windows event analysis, Linux authentication log parsing, SQLite-based investigation, Power BI reporting, and SOC-style documentation.

The lab combines several tools and data sources:

* Wazuh SIEM
* Wazuh Agent for Linux and Windows endpoints
* Suricata IDS
* Sysmon
* Windows Security logs
* Linux authentication logs
* Python log analyzer
* SQLite database
* SQL queries
* Power BI dashboard
* MITRE ATT&CK mapping

All activities were performed in an isolated virtual lab environment. Events were generated intentionally for learning and investigation purposes.

---

## What I Built

I built a local SOC-style monitoring lab with both Linux and Windows endpoints connected to Wazuh.

The Linux side of the lab includes SSH authentication monitoring, File Integrity Monitoring, and Suricata IDS visibility. The Windows side includes Windows Security Event Log monitoring, Sysmon telemetry, account activity investigation, group membership changes, and suspicious PowerShell activity review.

I also created a Python-based log analyzer that parses Linux authentication logs, extracts SSH events, stores them in CSV and SQLite formats, and prepares structured data for Power BI visualization.

The project includes seven documented SOC investigation cases and a Power BI dashboard for authentication event analysis.

---

## Detection and Investigation Cases

The project includes the following investigation cases:

| Case   | Scenario                                | Main Focus                                  |
| ------ | --------------------------------------- | ------------------------------------------- |
| Case 1 | SSH brute-force / failed login attempts | Linux authentication monitoring             |
| Case 2 | File Integrity Monitoring               | Unauthorized file modification detection    |
| Case 3 | Suricata network event                  | Network IDS alert review                    |
| Case 4 | Windows failed login attempts           | Event ID 4625 investigation                 |
| Case 5 | New local user created                  | Event ID 4720 account creation monitoring   |
| Case 6 | User added to Administrators group      | Event ID 4732 privileged group change       |
| Case 7 | Suspicious PowerShell activity          | Event ID 4688 and Sysmon process visibility |

Each case follows a basic SOC investigation workflow:

1. Identify the event or alert.
2. Review the affected host.
3. Check source, target, user and timestamp information.
4. Review related logs.
5. Assess the risk.
6. Map the activity to MITRE ATT&CK where applicable.
7. Document recommended actions.

---

## Data Sources Used

The lab uses multiple log and telemetry sources:

| Data Source           | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| Linux auth.log        | SSH authentication analysis                       |
| Wazuh alerts          | SIEM alert review                                 |
| Wazuh FIM             | File modification detection                       |
| Suricata eve.json     | Network IDS visibility                            |
| Windows Security logs | Authentication and account activity investigation |
| Sysmon logs           | Endpoint process visibility                       |
| SQLite database       | Structured log analysis                           |
| Power BI dataset      | Security dashboard and reporting                  |

---

## SOC Skills Demonstrated

This project demonstrates the following SOC-related skills:

* Reviewing SIEM alerts in Wazuh
* Investigating Linux authentication events
* Investigating Windows Security Event IDs
* Understanding failed and successful authentication patterns
* Reviewing account creation and privilege changes
* Monitoring file integrity changes
* Reviewing Suricata IDS alerts
* Using Sysmon for endpoint visibility
* Mapping events to MITRE ATT&CK
* Writing structured investigation reports
* Parsing logs with Python
* Storing security events in SQLite
* Running SQL queries for security analysis
* Creating a Power BI dashboard for security reporting

---

## Python and Data Analysis Part

The Python log analyzer processes Linux SSH authentication logs and extracts useful fields such as:

* timestamp
* hostname
* username
* source IP
* source port
* event type
* raw log line

The analyzer generates CSV files and a SQLite database. These outputs are used for SQL-based analysis and Power BI visualization.

This part of the project demonstrates how scripting and data analysis can support SOC work by making raw logs easier to search, filter, summarize and visualize.

---

## Power BI Dashboard

The Power BI dashboard visualizes authentication-related security events.

The dashboard includes:

* total authentication events
* failed SSH login attempts
* successful SSH logins
* unique source IP addresses
* failed logins by source IP
* failed logins by username
* events by risk level
* event type breakdown
* detailed event table

The goal of the dashboard is to provide a simple security reporting view for authentication monitoring and investigation.

---

## MITRE ATT&CK Coverage

The investigation cases were mapped to relevant MITRE ATT&CK techniques, including:

| Technique                         | Description                                         |
| --------------------------------- | --------------------------------------------------- |
| T1110 — Brute Force               | Repeated password guessing or failed login attempts |
| T1078 — Valid Accounts            | Possible use of valid credentials                   |
| T1136 — Create Account            | New account creation for persistence                |
| T1098 — Account Manipulation      | Group membership or permission changes              |
| T1059.001 — PowerShell            | PowerShell command execution                        |
| T1046 — Network Service Discovery | Network service discovery and scanning              |
| T1595 — Active Scanning           | Active reconnaissance or probing                    |

The mapping was used for learning and documentation purposes.

---

## What I Learned

During this project, I practiced how to collect, review and document security events from different sources.

The main lessons learned were:

* Wazuh can be used as a central SIEM for Linux and Windows endpoint monitoring.
* Suricata provides useful network-level visibility through IDS alerts.
* Windows Security Event IDs are important for authentication and account activity investigations.
* Sysmon improves endpoint visibility, especially for process creation events.
* Python and SQLite can help transform raw logs into structured investigation data.
* Power BI can be used to create simple security dashboards.
* SOC investigation is not only about detecting alerts, but also about reviewing context, documenting evidence and recommending actions.

---

## Production Improvements

In a real production environment, this lab could be improved by adding:

* custom Wazuh detection rules;
* centralized log retention policies;
* more advanced Sysmon configuration;
* additional Windows process creation detections;
* alert correlation between Wazuh, Sysmon and Suricata;
* automated alert enrichment;
* ticketing system integration;
* more detailed incident response playbooks;
* vulnerability management workflow;
* production-ready network segmentation;
* role-based access control for SIEM users.

---

## Analyst Conclusion

This project demonstrates practical entry-level SOC skills across endpoint monitoring, network detection, authentication analysis, log parsing, SQL-based investigation, dashboarding and documentation.

The lab is not a full production SOC environment, but it shows the ability to build a working monitoring setup, generate test events, investigate alerts, document findings, and explain security activity using a structured SOC workflow.
