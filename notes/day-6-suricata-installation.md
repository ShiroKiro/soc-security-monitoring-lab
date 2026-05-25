# Day 6 — Suricata Installation

## Goal

The goal of this day was to install Suricata IDS on the Ubuntu monitored host and verify that it generates events.

## Environment

- Endpoint: Ubuntu monitored host
- IDS: Suricata
- Log file: /var/log/suricata/eve.json
- Test traffic source: Kali Linux / Ubuntu endpoint

## What I did

1. Installed Suricata on the Ubuntu monitored host.
2. Checked the Suricata version.
3. Identified the network interface used by the Ubuntu endpoint.
4. Configured Suricata to listen on the correct interface.
5. Started and enabled the Suricata service.
6. Verified that Suricata generated the `eve.json` log file.
7. Generated safe test traffic inside the lab.
8. Confirmed that network events were written to `eve.json`.

## Commands used

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y software-properties-common curl wget jq net-tools
sudo apt install -y suricata

suricata --build-info
ip -br a

sudo nano /etc/default/suricata
sudo nano /etc/suricata/suricata.yaml

sudo suricata -T -c /etc/suricata/suricata.yaml -v

sudo systemctl enable suricata
sudo systemctl restart suricata
sudo systemctl status suricata

sudo ls -lah /var/log/suricata/
sudo tail -n 20 /var/log/suricata/eve.json
sudo tail -n 10 /var/log/suricata/eve.json | jq '.event_type'