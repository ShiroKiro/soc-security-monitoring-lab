# Day 14 — New Local User Created

## Goal

The goal of this day was to create a local Windows user and investigate the related Windows Security event in Wazuh.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows endpoint
- Log source: Windows Security log
- Event ID: 4720

## What I did

1. Verified that Wazuh Agent was running on the Windows endpoint.
2. Confirmed that Windows Security logs were available.
3. Created a test local user.
4. Reviewed Event ID 4720 in Windows Security logs.
5. Reviewed the related event in Wazuh Dashboard.
6. Documented the investigation case.

## Commands used

```powershell
Get-Service WazuhSvc

Get-WinEvent -LogName Security -MaxEvents 5

net user soc_test_user TestPassword123! /add
net user soc_test_user

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720} -MaxEvents 10

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720} -MaxEvents 5 |
Select-Object TimeCreated, Id, ProviderName, Message

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

A new local Windows user creation event was generated and detected by Wazuh.

## Screenshots

screenshots/19-windows-user-created-eventviewer.png
screenshots/20-wazuh-user-created-alert.png

## Next step

Create a case for adding a user to the local Administrators group.