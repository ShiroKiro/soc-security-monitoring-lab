# Day 16 — Suspicious PowerShell Activity

## Goal

The goal of this day was to generate controlled PowerShell activity and investigate it using Windows logs, Sysmon, and Wazuh.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows endpoint
- Log sources:
  - Microsoft-Windows-PowerShell/Operational
  - Microsoft-Windows-Sysmon/Operational
- Main events:
  - PowerShell Script Block Logging
  - Sysmon Process Create

## What I did

1. Verified that Wazuh Agent was running.
2. Verified that Sysmon was running.
3. Enabled PowerShell Script Block Logging.
4. Configured Wazuh Agent to collect PowerShell event channel logs.
5. Generated controlled PowerShell activity.
6. Reviewed PowerShell and Sysmon events locally.
7. Reviewed related events in Wazuh Dashboard.
8. Documented the investigation case.

## Commands used

```powershell
Get-Service WazuhSvc
Get-Service Sysmon64

New-Item -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Force

New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" `
-Name EnableScriptBlockLogging `
-Value 1 `
-PropertyType DWord `
-Force

Get-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"

whoami
hostname
Get-Date
Get-Process
Get-Service
Get-LocalUser
Get-LocalGroup

Start-Process powershell -ArgumentList "-NoProfile -Command Get-Process"

Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -MaxEvents 10

Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 20 |
Where-Object {$_.Message -like "*powershell.exe*"} |
Select-Object TimeCreated, Id, ProviderName, Message

Restart-Service WazuhSvc
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 100
```
## Wazuh Agent configuration
```xml
<localfile>
  <location>Microsoft-Windows-PowerShell/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>

<localfile>
  <location>Windows PowerShell</location>
  <log_format>eventchannel</log_format>
</localfile>

<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

## Result

Controlled PowerShell activity was generated and detected through Windows logs, Sysmon, and Wazuh.

## Screenshots
screenshots/23-powershell-events-eventviewer.png
screenshots/24-wazuh-powershell-activity.png
## Next step

Add MITRE ATT&CK mapping for all completed investigation cases.