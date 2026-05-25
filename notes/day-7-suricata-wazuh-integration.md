# Day 7 — Suricata Integration with Wazuh

## Goal

The goal of this day was to configure Wazuh Agent to collect Suricata `eve.json` logs and display Suricata events in Wazuh Dashboard.

## Environment

- SIEM: Wazuh Server
- Endpoint: Ubuntu monitored host
- IDS: Suricata
- Log source: /var/log/suricata/eve.json

## What I did

1. Verified that Suricata was running.
2. Confirmed that `/var/log/suricata/eve.json` existed and contained events.
3. Configured Wazuh Agent to collect Suricata JSON logs.
4. Restarted Wazuh Agent.
5. Generated controlled test network traffic.
6. Verified Suricata events in Wazuh Dashboard.
7. Documented the investigation case.

## Wazuh Agent configuration

```xml
<localfile>
  <log_format>json</log_format>
  <location>/var/log/suricata/eve.json</location>
</localfile>
```

## Commands used
``` bash
sudo systemctl is-active suricata
sudo ls -lah /var/log/suricata/
sudo tail -n 5 /var/log/suricata/eve.json | jq

sudo nano /var/ossec/etc/ossec.conf

sudo chmod 644 /var/log/suricata/eve.json
sudo systemctl restart wazuh-agent
sudo systemctl status wazuh-agent

curl http://example.com
nslookup example.com
sudo tail -n 20 /var/log/suricata/eve.json | jq '.event_type'
```
## Result

Wazuh successfully collected Suricata events from the eve.json log file.

## Screenshots
screenshots/11-wazuh-suricata-events.png
screenshots/12-suricata-alert-details-in-wazuh.png