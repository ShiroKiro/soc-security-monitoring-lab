# Day 12 — Sysmon and Wazuh Integration

## Goal

The goal of this day was to install Sysmon on the Windows endpoint and configure Wazuh Agent to collect Sysmon events.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows endpoint
- Tool: Microsoft Sysmon
- Event channel: Microsoft-Windows-Sysmon/Operational

## What I did

1. Downloaded and extracted Sysmon.
2. Installed Sysmon on the Windows endpoint.
3. Verified that Sysmon service was running.
4. Checked Sysmon events in Windows Event Log.
5. Configured Wazuh Agent to collect Sysmon event channel logs.
6. Restarted Wazuh Agent.
7. Verified Sysmon events in Wazuh Dashboard.

## Commands used

```powershell
New-Item -ItemType Directory -Path C:\Sysmon -Force
Set-Location C:\Sysmon

Invoke-WebRequest -Uri "https://download.sysinternals.com/files/Sysmon.zip" -OutFile "C:\Sysmon\Sysmon.zip"
Expand-Archive -Path "C:\Sysmon\Sysmon.zip" -DestinationPath "C:\Sysmon" -Force

C:\Sysmon\Sysmon64.exe -accepteula -i

Get-Service Sysmon64
C:\Sysmon\Sysmon64.exe -c

Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 10

Restart-Service WazuhSvc
Get-Service WazuhSvc
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 50
```

## Wazuh Agent configuration
```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

## Result

Sysmon was successfully installed on the Windows endpoint.

Wazuh Agent was configured to collect Sysmon events from the Windows Event Channel.

## Screenshots

screenshots/15-sysmon-installed-windows.png
screenshots/16-sysmon-events-in-wazuh.png

## Next step

Create a detection case based on Windows failed login attempts or suspicious PowerShell activity.