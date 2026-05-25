# Day 13 — Windows Failed Login Attempts

## Goal

The goal of this day was to generate failed Windows login attempts and investigate them using Windows Security logs and Wazuh.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows endpoint
- Log source: Windows Security log
- Event ID: 4625

## What I did

1. Verified that Wazuh Agent was running on the Windows endpoint.
2. Confirmed that Windows Security logs were available.
3. Created a test local user.
4. Generated controlled failed login attempts.
5. Reviewed Event ID 4625 in Windows Event Viewer.
6. Reviewed the related event in Wazuh Dashboard.
7. Documented the investigation case.

## Commands used

```powershell
Get-Service WazuhSvc

Get-WinEvent -LogName Security -MaxEvents 5

net user labuser CorrectPassword123! /add
net user labuser

runas /user:labuser cmd

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 10

Restart-Service WazuhSvc
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 100
```

## Wazuh Agent configuration

```xml
<localfile>
  <location>Security</location>
  <log_format>eventchannel</log_format>
</localfile>
```

## Result

Windows failed login events were generated and detected by Wazuh.

## Screenshots
screenshots/17-windows-failed-login-eventviewer.png
screenshots/18-wazuh-windows-failed-login-alert.png

## Next step

Create a Windows case for new local user creation or suspicious PowerShell activity.