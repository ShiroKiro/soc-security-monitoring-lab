# Interview Project Explanation — Wazuh + Suricata SOC Lab

## 1. Short Project Explanation

I built a small SOC-style security monitoring lab using Wazuh and Suricata.

The goal of the project was to practice endpoint monitoring, network IDS alert collection, and basic incident investigation.

Wazuh was used as the central SIEM platform, while Suricata provided network-level visibility.

I connected a Linux endpoint to Wazuh, generated controlled security events, collected alerts, and documented investigation cases.

The project includes three main detection scenarios:

1. Failed SSH login attempts.
2. File Integrity Monitoring alert.
3. Suricata network event collection.

---

## 2. Why did you choose Wazuh?

I chose Wazuh because it is an open-source SIEM and XDR platform that is useful for learning security monitoring, log analysis, endpoint visibility, and alert investigation.

It allowed me to collect Linux endpoint logs, monitor file changes, review alerts in a centralized dashboard, and practice SOC-style investigation steps.

For this project, Wazuh worked as the central monitoring platform.

---

## 3. Why did you add Suricata?

I added Suricata to include network-level visibility in the lab.

Wazuh helped me monitor endpoint activity, while Suricata analyzed network traffic and generated IDS events.

Together, they provided a better view of both host-based and network-based activity.

This helped me understand how SOC analysts can investigate events from different log sources in one platform.

---

## 4. What did you investigate?

I documented three investigation cases.

### Case 1 — Failed SSH Login Attempts

I generated controlled failed SSH login attempts from a Kali Linux test VM against the monitored Ubuntu endpoint.

I checked Linux authentication logs and reviewed the related Wazuh alert.

The goal was to practice detecting and investigating suspicious authentication activity.

### Case 2 — File Integrity Monitoring

I configured Wazuh File Integrity Monitoring for a test directory on the Ubuntu endpoint.

Then I modified a test file and verified that Wazuh generated a file integrity alert.

The goal was to understand how file changes can be monitored and investigated.

### Case 3 — Suricata Network Event

I installed Suricata on the monitored Ubuntu host and configured it to generate events in `eve.json`.

Then I configured Wazuh Agent to collect this log file.

The goal was to practice collecting and reviewing network IDS events in Wazuh.

---

## 5. What did you learn?

During this project, I learned how to:

- deploy a basic Wazuh monitoring environment;
- connect a Linux endpoint using Wazuh Agent;
- review Linux authentication logs;
- investigate failed SSH login attempts;
- configure File Integrity Monitoring;
- install and test Suricata IDS;
- collect JSON logs from Suricata into Wazuh;
- document investigation cases using source, target, evidence, risk, and recommended actions.

The project helped me better understand the basic workflow of a SOC analyst: detect, investigate, validate, document, and recommend actions.

---

## 6. 1-Minute Interview Pitch

I built a small SOC-style monitoring lab using Wazuh and Suricata.

The lab included a Wazuh Server, an Ubuntu monitored endpoint, and a Kali Linux test VM.

I connected the Ubuntu endpoint to Wazuh using Wazuh Agent and generated controlled security events inside the lab.

The main scenarios were failed SSH login attempts, File Integrity Monitoring, and Suricata network event collection.

For each case, I reviewed logs, checked the alert details, identified the source and target, assessed the risk, and documented recommended actions.

This project helped me practice basic SOC investigation workflow, Linux log analysis, SIEM usage, and IDS event review.

---

## 7. Technical Summary

### Lab Components

| Component | Purpose |
|---|---|
| Wazuh Server | Central SIEM platform |
| Ubuntu monitored host | Endpoint with Wazuh Agent and Suricata |
| Kali Linux test VM | Controlled test traffic and security events |
| Suricata | Network IDS |
| Wazuh Agent | Endpoint log collection |

### Main Log Sources

| Log Source | Purpose |
|---|---|
| `/var/log/auth.log` | SSH authentication events |
| `/var/log/suricata/eve.json` | Suricata network events |
| Wazuh FIM alerts | File modification monitoring |

---

# Interview Questions and Answers

## 1. What is SIEM?

SIEM stands for Security Information and Event Management.

It is a platform that collects, analyzes, and correlates security logs from different systems.

In this project, Wazuh worked as the SIEM because it collected logs and alerts from the monitored Ubuntu endpoint and Suricata.

---

## 2. What is IDS?

IDS stands for Intrusion Detection System.

It monitors network or system activity and generates alerts when it detects suspicious behavior.

In this project, Suricata was used as a network IDS.

---

## 3. What is the difference between IDS and IPS?

An IDS detects suspicious activity and generates alerts.

An IPS can actively block or prevent suspicious traffic.

In simple terms:

- IDS = detects and alerts.
- IPS = detects and blocks.

In this project, I used Suricata mainly in IDS mode.

---

## 4. What is Wazuh?

Wazuh is an open-source security monitoring platform.

It can collect logs, monitor endpoints, detect suspicious activity, perform file integrity monitoring, and show alerts in a dashboard.

In my lab, Wazuh was used as the central SIEM platform.

---

## 5. What is Suricata?

Suricata is an open-source IDS/IPS and network security monitoring engine.

It analyzes network traffic and generates events or alerts.

In my project, Suricata generated network events in `eve.json`, and Wazuh collected those events.

---

## 6. What is a false positive?

A false positive is an alert that looks suspicious but is actually harmless or expected activity.

For example, in my lab, failed SSH login attempts were expected because I generated them intentionally for testing.

In a real SOC environment, I would validate the source, user, timestamp, and related events before escalating.

---

## 7. What is alert triage?

Alert triage is the first step of reviewing and prioritizing alerts.

The goal is to understand:

- what happened;
- which host was affected;
- who or what caused it;
- whether it is expected or suspicious;
- whether it needs escalation.

In my project, I practiced this by reviewing Wazuh alerts and documenting investigation cases.

---

## 8. What logs would you check after failed SSH login attempts?

I would check:

- Linux authentication logs;
- Wazuh alerts;
- source IP address;
- targeted username;
- timestamps;
- whether there was a successful login after failed attempts.

On Ubuntu, I checked authentication logs using:

```bash
sudo grep "Failed password" /var/log/auth.log
```
## 9. How would you investigate suspicious SSH activity?

First, I would check the alert details in the SIEM.

Then I would identify the source IP, target host, username, timestamp, and number of failed attempts.

After that, I would check if there was a successful login after the failed attempts.

I would also check whether the source IP is trusted, whether the account is valid, and whether similar activity happened on other hosts.

If the activity looked suspicious, I would recommend actions such as disabling password login, using SSH keys, applying rate limiting, and reviewing user permissions.

## 10. How would you reduce alert noise?

I would reduce alert noise by tuning detection rules, excluding known safe activity, adjusting thresholds, and focusing on high-confidence alerts.

For example, a few failed SSH attempts from an internal admin machine may be normal, but many failed attempts from an unknown source should be treated more seriously.

The goal is not to ignore alerts, but to make them more useful and reduce unnecessary false positives.

Final Project Explanation

This project demonstrates a basic SOC monitoring workflow.

It combines endpoint monitoring with Wazuh, network visibility with Suricata, and structured investigation documentation.

The project is useful for Junior SOC Analyst preparation because it shows practical experience with logs, alerts, SIEM, IDS, Linux endpoints, and basic incident investigation.