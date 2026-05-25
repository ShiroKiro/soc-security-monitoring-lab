# Day 4 — Failed SSH Login Attempts

## Goal

The goal of this day was to generate controlled failed SSH login attempts and investigate them using Linux logs and Wazuh alerts.

## Environment

- Source: Kali Linux test VM
- Target: Ubuntu monitored host
- SIEM: Wazuh Server

## What I did

1. Installed and enabled OpenSSH Server on the Ubuntu monitored host.
2. Verified network connectivity between Kali and Ubuntu.
3. Generated failed SSH login attempts from Kali.
4. Checked authentication logs on the Ubuntu endpoint.
5. Reviewed related alerts in Wazuh Dashboard.
6. Documented the investigation case.

## Commands used

```bash
sudo apt update
sudo apt install -y openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh
sudo ss -tulpn | grep :22

sudo tail -f /var/log/auth.log
sudo grep "Failed password" /var/log/auth.log
sudo journalctl -u ssh --since "10 minutes ago"

From Kali:
ssh wronguser@192.168.62.20
ssh shiro@192.168.62.20
```
