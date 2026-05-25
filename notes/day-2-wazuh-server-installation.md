# Day 2 — Wazuh Server Installation

## Goal

The goal of this day was to install Wazuh Server and access the Wazuh Dashboard.

## Environment

- OS: Ubuntu Server 24.04 LTS
- VM platform: VMware Workstation Pro
- RAM: 8 GB
- CPU: 4 cores
- Disk: 100 GB

## What I did

1. Created a dedicated Ubuntu Server VM for Wazuh.
2. Updated the system packages.
3. Installed required utilities.
4. Installed Wazuh using the assisted installation method.
5. Checked Wazuh services.
6. Accessed the Wazuh Dashboard from the browser.

## Commands used

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl wget gnupg apt-transport-https unzip net-tools

curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh
sudo bash ./wazuh-install.sh -a

sudo systemctl is-active wazuh-manager
sudo systemctl is-active wazuh-indexer
sudo systemctl is-active wazuh-dashboard