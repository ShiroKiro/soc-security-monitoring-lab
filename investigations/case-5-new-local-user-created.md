# Case 5 — New Local User Created

## What happened?

A new local user account was created on the Windows endpoint.

Windows Security logs recorded Event ID `4720`, which indicates that a user account was created.  
This activity may be legitimate administrative activity, but it can also indicate persistence after unauthorized access.

## Source

- Source system: Windows endpoint
- Log source: Windows Security logs
- Tool used: Event Viewer / Wazuh
- Event ID: 4720
- Event type: User account creation

## Target

- Target host: Windows endpoint
- Target object: Local user account
- Detection focus: New account creation
- Security relevance: Possible persistence or unauthorized account creation

## Evidence

Windows Security logs generated a user account creation event.

Important Event ID:

```text
4720 — A user account was created
```

### Important fields reviewed during the investigation:

Subject Account Name
Subject Domain
Subject Logon ID
New Account Name
New Account Domain
Security ID
Account Enabled
Password Last Set
User Principal Name
Timestamp

## Severity

Medium

Severity should be increased to High if:

- the new account was created outside working hours;
- the account was created by an unknown or unexpected user;
- the account was later added to the Administrators group;
- the account name looks suspicious;
- the activity happened after failed login attempts;
- the account was used for remote login shortly after creation.

## Detection Logic

The activity was considered suspicious because a new local user account appeared on the Windows endpoint.

### Detection condition:

If Event ID 4720 is generated on a Windows endpoint,
review the event to confirm whether the new account creation was authorized.

### High-risk condition:

If Event ID 4720 is followed by Event ID 4732,
review the activity as possible privilege escalation or persistence.

### Related event:

4732 — A member was added to a security-enabled local group

## Investigation Steps

Opened Windows Event Viewer.
Navigated to Windows Logs → Security.
Filtered events by Event ID 4720.
Identified the newly created account.
Identified the account that created the new user.
Checked the timestamp of the event.
Verified whether the account creation was expected.
Checked whether the new account was later added to a privileged group.
Reviewed related events such as 4732, 4624, and 4625.
Documented the risk and recommended response actions.

## Indicators

Indicator	Value
Event ID	4720
Event name	A user account was created
Log source	Windows Security logs
Target system	Windows endpoint
Event type	Account creation
Severity	Medium
Related privilege event	4732
Related login events	4624, 4625

### Related Windows Event IDs

Event ID	Meaning	SOC Relevance
4720	A user account was created	New account creation
4732	User added to local group	Possible privilege escalation
4624	Successful logon	Check whether the new account was used
4625	Failed logon	Check suspicious login attempts
4726	User account deleted	Possible cleanup activity

## Analysis

Event ID 4720 indicates that a new user account was created on the Windows endpoint.

Account creation is not always malicious. It can be part of normal administrative work. However, in a SOC investigation, unexpected account creation should always be reviewed because attackers may create new accounts to maintain access to a compromised system.

The event becomes more suspicious if the new account is later added to a privileged group, used for remote login, or created after failed authentication attempts.

In this lab case, the activity was generated in a controlled environment for testing and investigation purposes.

## MITRE ATT&CK Mapping
Tactic	Technique	Description
Persistence	T1136 — Create Account	Creation of a new account to maintain access
Privilege Escalation	T1068 / related privilege activity	Risk increases if the account receives elevated privileges
Defense Evasion	T1070 — Indicator Removal	Possible cleanup if account is later deleted
Risk

### Unexpected local user creation may indicate:

unauthorized access;
persistence attempt;
attacker-created backdoor account;
preparation for privilege escalation;
misuse of administrative rights;
compromised administrator account.

The risk depends on who created the account, when it was created, and whether it was later used or added to privileged groups.

## Recommended Actions

Verify whether the account creation was authorized.
Identify who created the account.
Check whether the new account was used for login.
Review Event ID 4624 for successful logins by the new account.
Review Event ID 4732 to check if the account was added to Administrators.
Disable the account if it is unauthorized.
Reset passwords for involved accounts if compromise is suspected.
Review recent failed login attempts.
Check other endpoints for similar account creation events.
Continue monitoring Windows Security logs.

## Recommended Preventive Measures

Limit local administrator rights.
Monitor all account creation events.
Use centralized identity management where possible.
Enable alerting for Event ID 4720.
Enable alerting when account creation is followed by group membership changes.
Review local users regularly.
Remove unused or unauthorized accounts.
Enforce least privilege.

## Result

The lab successfully demonstrated investigation of a new local user account creation event using Windows Security logs.

Event ID 4720 provided useful evidence for identifying when a new account was created and which account performed the action.

## SOC Analyst Conclusion

The observed user creation event should be reviewed as a potential persistence-related activity.

In this lab, the account creation was controlled and used for testing. In a real environment, unexpected creation of a local user account may indicate unauthorized access or an attempt to maintain persistence.

The recommended action is to verify whether the account was authorized, check whether it was added to privileged groups, and review related login activity.