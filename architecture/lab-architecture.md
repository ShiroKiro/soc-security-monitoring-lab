# Lab Architecture

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
```

## Description

The Kali Linux VM is used only to generate controlled test activity inside the isolated lab network.

The Ubuntu monitored host acts as the monitored endpoint. It runs Wazuh Agent for endpoint log collection and Suricata IDS for network visibility.

The Wazuh Server receives logs and alerts from the monitored endpoint and provides a centralized dashboard for investigation.