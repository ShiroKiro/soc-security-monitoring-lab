# Day 5 — File Integrity Monitoring

## Goal

The goal of this day was to configure Wazuh File Integrity Monitoring and detect a file modification on the Ubuntu monitored host.

## Environment

- SIEM: Wazuh Server
- Endpoint: Ubuntu monitored host
- Monitored path: /opt/test-monitoring

## What I did

1. Created a test directory on the Ubuntu endpoint.
2. Created a test file inside the monitored directory.
3. Added the directory to the Wazuh Agent File Integrity Monitoring configuration.
4. Restarted the Wazuh Agent.
5. Modified the monitored file.
6. Reviewed the generated alert in Wazuh Dashboard.
7. Documented the investigation case.

## Commands used

```bash
sudo mkdir -p /opt/test-monitoring
echo "Initial test file" | sudo tee /opt/test-monitoring/test.txt

sudo nano /var/ossec/etc/ossec.conf

sudo systemctl restart wazuh-agent
sudo systemctl status wazuh-agent

echo "Modified content" | sudo tee -a /opt/test-monitoring/test.txt
cat /opt/test-monitoring/test.txt

sudo tail -n 50 /var/ossec/logs/ossec.log