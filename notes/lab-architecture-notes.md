# Lab Architecture Notes

This project uses a small isolated lab environment for security monitoring practice.

The Wazuh Server works as the central SIEM component. It receives logs and alerts from monitored endpoints.

The Ubuntu monitored host runs Wazuh Agent. It sends system and authentication logs to the Wazuh Server.

Suricata is installed on the monitored Ubuntu host to generate network IDS events.

The Kali Linux / test VM is used only to generate controlled and safe lab activity, such as failed SSH login attempts or simple network traffic.

All activity is performed inside the local virtualized environment.

# Day 1 Summary

## What I did

Today I created the initial structure for the Wazuh and Suricata SOC lab project.

I prepared the main project folders, created the first version of the README file, and described the planned lab architecture.

## Planned lab components

- Wazuh Server
- Ubuntu monitored host with Wazuh Agent
- Suricata IDS
- Kali Linux / Test VM

## Current status

The project structure is ready.  
The next step is to install and configure the Wazuh Server.

