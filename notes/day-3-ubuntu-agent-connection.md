# Day 3 — Ubuntu Agent Connection

## Goal

The goal of this day was to connect an Ubuntu monitored host to the Wazuh Server using Wazuh Agent.

## Environment

- Wazuh Server IP: 192.168.62.10
- Ubuntu Agent IP: 192.168.62.20
- Agent OS: Ubuntu Server 24.04 LTS
- VM platform: VMware Workstation Pro

## What I did

1. Created a separate Ubuntu Server VM as a monitored endpoint.
2. Configured the network connection between Ubuntu Agent and Wazuh Server.
3. Verified connectivity using ping.
4. Installed Wazuh Agent on the Ubuntu endpoint.
5. Configured the agent to communicate with Wazuh Manager.
6. Started and enabled the Wazuh Agent service.
7. Verified that the agent appeared in Wazuh Dashboard.

## Commands used

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl wget gnupg apt-transport-https net-tools netcat-openbsd

ping -c 4 192.168.62.10
nc -zv 192.168.62.10 1514
nc -zv 192.168.62.10 1515

curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import
sudo chmod 644 /usr/share/keyrings/wazuh.gpg

echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list

sudo apt-get update
sudo WAZUH_MANAGER="192.168.62.10" apt-get install -y wazuh-agent

sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
sudo systemctl status wazuh-agent