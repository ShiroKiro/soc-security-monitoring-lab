# Case 6 — User Added to Administrators Group

## What happened?

A user account was added to a privileged local group on the Windows endpoint.

Windows Security logs recorded Event ID `4732`, which indicates that a member was added to a security-enabled local group.  
If the target group is `Administrators`, this activity may indicate privilege escalation or unauthorized administrative access.

## Source

- Source system: Windows endpoint
- Log source: Windows Security logs
- Tool used: Event Viewer / Wazuh
- Event ID: 4732
- Event type: Group membership change

## Target

- Target host: Windows endpoint
- Target group: Local Administrators group
- Target object: User account
- Detection focus: Privileged group membership change
- Security relevance: Possible privilege escalation

## Evidence

Windows Security logs generated a group membership change event.

## Important Event ID:

```text
4732 — A member was added to a security-enabled local group
```

### Important fields reviewed during the investigation:

Subject Account Name
Subject Domain
Subject Logon ID
Member Name
Member Security ID
Group Name
Group Domain
Timestamp

## Severity

High

### This event should usually be treated as High severity when the affected group is:

Administrators
Remote Desktop Users
Backup Operators
Power Users

### Severity should be increased if:

- the change was not approved;
- the account was newly created before being added to the group;
- the action happened outside working hours;
- the account was later used for remote login;
- the action was performed by an unexpected user;
- multiple accounts were added to privileged groups.

## Detection Logic

The activity was considered suspicious because a user account was added to a privileged local group.

### Detection condition:

If Event ID 4732 is generated and the target group is Administrators,
review the event as a possible privilege escalation attempt.

### High-risk condition:

If Event ID 4720 is followed by Event ID 4732 for the same account,
review the activity as possible persistence and privilege escalation.

## Related events:

4720 — A user account was created
4624 — An account successfully logged on
4625 — An account failed to log on
4728 — A member was added to a privileged global group
4738 — A user account was changed

## Investigation Steps

Opened Windows Event Viewer.
Navigated to Windows Logs → Security.
Filtered events by Event ID 4732.
Identified the account that was added to the group.
Identified the privileged group name.
Identified the account that performed the action.
Checked the timestamp of the change.
Verified whether the group membership change was authorized.
Checked whether the user account was newly created.
Reviewed Event ID 4720 for related account creation.
Reviewed Event ID 4624 to see whether the account logged in after the change.
Documented the risk and recommended response actions.

## Indicators

Indicator	Value
Event ID	4732
Event name	A member was added to a security-enabled local group
Log source	Windows Security logs
Target system	Windows endpoint
Target group	Administrators
Event type	Privileged group membership change
Severity	High
Related account creation event	4720
Related login events	4624, 4625

## Related Windows Event IDs

Event ID	Meaning	SOC Relevance
4732	Member added to local group	Privilege escalation monitoring
4720	User account created	Possible persistence
4624	Successful logon	Check whether account was used
4625	Failed logon	Check previous access attempts
4733	Member removed from local group	Possible cleanup or admin action
4738	User account changed	Account modification after privilege change

## Analysis

Event ID 4732 indicates that a user account was added to a local security group.

This event becomes highly important when the target group is Administrators, because members of this group can make system-level changes, install software, modify security settings, access sensitive data, and create additional users.

In a SOC investigation, this event should be reviewed to determine whether the change was authorized. If the account was recently created or later used for remote login, the activity may indicate persistence and privilege escalation.

In this lab case, the activity was generated in a controlled environment for testing and investigation purposes.

## MITRE ATT&CK Mapping

Tactic	Technique	Description
Privilege Escalation	T1098 — Account Manipulation	Modification of account permissions or group membership
Persistence	T1136 — Create Account	Relevant if the account was created before being added to Administrators
Initial Access	T1078 — Valid Accounts	Relevant if the privileged account is later used for login

## Risk

### Unexpected addition of a user to the Administrators group may indicate:

privilege escalation;
unauthorized administrative access;
persistence after compromise;
misuse of administrator rights;
compromised administrator account;
preparation for lateral movement;
bypassing normal access control.

The risk is especially high if a new account is created and then immediately added to the Administrators group.

## Recommended Actions

Verify whether the group membership change was authorized.
Identify the account that performed the action.
Identify the account that was added to the group.
Check whether the added account was newly created.
Review Event ID 4720 for related account creation.
Review Event ID 4624 for successful logins by the added account.
Remove the account from the Administrators group if unauthorized.
Disable the account if compromise is suspected.
Reset passwords for involved accounts.
Review other endpoints for similar group membership changes.
Continue monitoring privileged group changes.

## Recommended Preventive Measures

Limit local administrator rights.
Use least privilege.
Monitor all changes to privileged groups.
Enable alerting for Event ID 4732.
Review local Administrators group membership regularly.
Use separate admin accounts for administrative tasks.
Apply MFA where possible.
Use centralized logging with Wazuh or SIEM.
Create correlation rules for 4720 followed by 4732.

## Result

The lab successfully demonstrated investigation of a privileged group membership change using Windows Security logs.

Event ID 4732 provided useful evidence for identifying when a user was added to a local security group and which account performed the action.

## SOC Analyst Conclusion

The observed group membership change should be treated as a high-priority security event when the target group is Administrators.

In this lab, the activity was controlled and used for testing. In a real environment, unexpected addition of a user to the Administrators group may indicate privilege escalation, persistence, or misuse of administrative privileges.

The recommended action is to verify whether the change was authorized, check related account creation and login events, and remove unauthorized privileged access immediately.