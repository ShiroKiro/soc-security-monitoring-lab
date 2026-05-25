# Case 3 — Suricata Network Alert

## What happened?

Suricata detected network activity inside the lab environment and generated an event.

## Source

- Source IP: 192.168.62.129
- Source host: Kali Linux test VM / Ubuntu monitored host

## Destination

- Destination IP: 192.168.62.20
- Destination host: Ubuntu monitored host

## Protocol

- Protocol: ICMP / DNS / HTTP

## Evidence

- Suricata generated an event in `/var/log/suricata/eve.json`.
- Wazuh collected the Suricata log and displayed it in the dashboard.

## Investigation Steps

1. Reviewed the Suricata event in `eve.json`.
2. Checked source and destination IP addresses.
3. Verified the protocol and event category.
4. Reviewed the same event in Wazuh Dashboard.
5. Assessed whether the activity was expected lab traffic.

## Risk

Network IDS events can indicate scanning, suspicious connections, policy violations, or possible attack attempts.

## Recommended Actions

- Verify source and destination hosts.
- Check related endpoint logs.
- Review firewall rules.
- Monitor repeated activity.
- Tune IDS rules if false positives are detected.

## Result

The lab successfully demonstrated collection and analysis of Suricata network events in Wazuh.

## MITRE ATT&CK Mapping

- Tactic: Context-dependent
- Technique: Not directly mapped
- Reason: A generic network event alone is not enough to map the activity to a specific ATT&CK technique. More context is required, such as destination reputation, payload, frequency, and related endpoint activity.