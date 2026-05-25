# Day 15 — User Added to Local Administrators Group

## Goal

The goal of this day was to add a local Windows user to the Administrators group and investigate the related Windows Security event in Wazuh.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows endpoint
- Log source: Windows Security log
- Event ID: 4732

## What I did

1. Verified that Wazuh Agent was running on the Windows endpoint.
2. Confirmed that the test local user existed.
3. Added the test user to the local Administrators group.
4. Reviewed Event ID 4732 in Windows Security logs.
5. Reviewed the related event in Wazuh Dashboard.
6. Documented the investigation case.

## Commands used

```powershell
Get-Service WazuhSvc

net user soc_test_user
net user soc_test_user TestPassword123! /add

net localgroup Administrators soc_test_user /add
net localgroup Administrators

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4732} -MaxEvents 10

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4732} -MaxEvents 5 |
Select-Object TimeCreated, Id, ProviderName, Message

Restart-Service WazuhSvc
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 100# Day 15 — User Added to Local Administrators Group

## Goal

The goal of this day was to add a local Windows user to the Administrators group and investigate the related Windows Security event in Wazuh.

## Environment

- SIEM: Wazuh Server
- Endpoint: Windows endpoint
- Log source: Windows Security log
- Event ID: 4732

## What I did

1. Verified that Wazuh Agent was running on the Windows endpoint.
2. Confirmed that the test local user existed.
3. Added the test user to the local Administrators group.
4. Reviewed Event ID 4732 in Windows Security logs.
5. Reviewed the related event in Wazuh Dashboard.
6. Documented the investigation case.

## Commands used

```powershell
Get-Service WazuhSvc

net user soc_test_user
net user soc_test_user TestPassword123! /add

net localgroup Administrators soc_test_user /add
net localgroup Administrators

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4732} -MaxEvents 10

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4732} -MaxEvents 5 |
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

A local Windows user was added to the Administrators group, and the related event was detected by Wazuh.

## Screenshots
screenshots/21-windows-user-added-to-admins-eventviewer.png
screenshots/22-wazuh-user-added-to-admins-alert.png
## Next step

Create a case for suspicious PowerShell activity using Windows logs and Sysmon events.

After testing, the user was removed from the local Administrators group.