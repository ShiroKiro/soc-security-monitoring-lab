# Day 11 — Windows Endpoint and Wazuh Agent

## Goal

The goal of this day was to add a Windows endpoint to the Wazuh monitoring lab.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows 10/11 VM
- Wazuh Server IP: 192.168.62.10
- Windows endpoint IP: 192.168.62.40

## What I did

1. Created a Windows endpoint VM.
2. Connected it to the same lab network as the Wazuh Server.
3. Verified network connectivity with ping and Test-NetConnection.
4. Installed Wazuh Agent on Windows.
5. Started the Wazuh Agent service.
6. Verified that the Windows endpoint appeared in Wazuh Dashboard.

## Commands used

```powershell
ipconfig
ping 192.168.62.10

Test-NetConnection 192.168.62.10 -Port 1514
Test-NetConnection 192.168.62.10 -Port 1515

.\wazuh-agent-4.14.5-1.msi /q WAZUH_MANAGER="192.168.62.10"

NET START WazuhSvc
Get-Service WazuhSvc
```
## Result

The Windows endpoint was successfully connected to Wazuh.

## Screenshots
screenshots/13-windows-agent-installed.png
screenshots/14-windows-agent-active-in-wazuh.png
## Next step

Install Sysmon on the Windows endpoint and configure Wazuh to collect Sysmon events.