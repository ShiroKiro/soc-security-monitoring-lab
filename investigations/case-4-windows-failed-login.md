 Case 4 — Windows Failed Login Attempts

## What happened?

Multiple failed login attempts were detected on the Windows endpoint.

Windows Security logs recorded authentication failure events with Event ID `4625`.  
This activity may indicate password guessing, brute-force attempts, unauthorized access attempts, or a misconfigured user/service account.

## Source

- Source system: Windows endpoint
- Log source: Windows Security logs
- Tool used: Event Viewer / Wazuh
- Event ID: 4625
- Event type: Failed logon

## Target

- Target host: Windows endpoint
- Target user: Windows user account
- Authentication type: Local or remote logon attempt
- Detection focus: Failed authentication activity

## Evidence

Windows Security logs generated failed logon events.

Important Event ID:

```text
4625 — An account failed to log on
```

## Important fields reviewed during the investigation:

Account Name
Account Domain
Failure Reason
Status
Sub Status
Logon Type
Workstation Name
Source Network Address
Source Port
Process Name
Authentication Package

## Severity

Medium

Severity should be increased to High if:

- many failed attempts are generated in a short period of time;
- the targeted account is privileged;
- the source IP is unknown or external;
- a successful login follows the failed attempts;
- the same source attempts to access multiple accounts.

## Detection Logic

The activity was considered suspicious because Windows recorded repeated failed authentication attempts.

### Detection condition:

If multiple Event ID 4625 events are generated for the same user, source IP, or workstation,
review the activity as possible brute-force behavior or unauthorized access attempts.

### High-risk condition:

If Event ID 4625 is followed by Event ID 4624 from the same source and user,
review the activity as a possible successful compromise.

## Investigation Steps

Opened Windows Event Viewer.
Navigated to Windows Logs → Security.
Filtered events by Event ID 4625.
Reviewed the failed login timestamp.
Identified the targeted account.
Checked the failure reason.
Reviewed the logon type.
Checked the source workstation or source IP address.
Verified whether the account was privileged.
Checked whether Event ID 4624 occurred after the failed attempts.
Documented the risk and recommended response actions.

## Indicators

Indicator	Value
Event ID	4625
Event name	An account failed to log on
Log source	Windows Security logs
Target system	Windows endpoint
Event type	Failed authentication
Severity	Medium
Related successful login event	4624

## Important Logon Types

Logon Type	Meaning	SOC Relevance
2	Interactive logon	User logged in locally
3	Network logon	Access over network, common for SMB/RDP-related activity
7	Unlock	Workstation unlock
10	RemoteInteractive	RDP login attempt
11	CachedInteractive	Cached domain login

For SOC investigation, Logon Type 3 and 10 are especially important because they may indicate remote access attempts.

## Analysis

Event ID 4625 indicates that an account failed to log on to the Windows endpoint.

A single failed login can happen because of a user mistake. However, repeated failed logins from the same source, against the same user, or against privileged accounts should be investigated.

If failed login attempts are followed by Event ID 4624, this may indicate that the attacker eventually guessed or obtained valid credentials.

In this lab case, the failed login activity was generated in a controlled environment for testing and investigation purposes.

## MITRE ATT&CK Mapping

Tactic	Technique	Description
Credential Access	T1110 — Brute Force	Repeated attempts to guess valid credentials
Initial Access	T1078 — Valid Accounts	Possible use of valid credentials after successful login
Risk

### Repeated Windows failed login attempts may indicate:

brute-force attack;
password guessing;
unauthorized RDP access attempts;
compromised user credentials;
misconfigured service account;
attempted access to privileged accounts.

The risk depends on the source, target account, logon type, and whether successful authentication occurred after the failures.

## Recommended Actions

Verify whether the failed login attempts were expected.
Identify the source IP or workstation.
Check whether the targeted account is privileged.
Review successful login events with Event ID 4624.
Check if the same source targeted other accounts.
Lock or reset the account if compromise is suspected.
Enable account lockout policy.
Enforce strong passwords.
Enable MFA where possible.
Restrict RDP access.
Continue monitoring Windows authentication logs.

## Recommended Preventive Measures

Enable account lockout after repeated failed attempts.
Use MFA for remote access.
Restrict RDP access by firewall or VPN.
Disable unused accounts.
Review privileged accounts regularly.
Monitor Event IDs 4625 and 4624.
Forward Windows Security logs to Wazuh or SIEM.
Create correlation rules for failed login bursts.

## Result

The lab successfully demonstrated investigation of Windows failed login attempts using Windows Security logs.

Event ID 4625 provided useful information for identifying failed authentication activity, including the targeted account, failure reason, logon type, and possible source system.

## SOC Analyst Conclusion

The observed Windows failed login activity should be reviewed as a suspicious authentication event.

In this lab, the activity was controlled and used for testing. In a real environment, repeated Event ID 4625 events may indicate brute-force behavior, password guessing, or unauthorized remote access attempts.

The recommended action is to identify the source, check whether the targeted account is privileged, review successful login events after the failures, and apply account protection measures.