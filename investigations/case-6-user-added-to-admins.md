# Case 6 — User Added to Local Administrators Group

## What happened?

A local Windows user was added to the local Administrators group.

## Source

- Source host: Windows endpoint
- Action performed by: local administrator / lab user

## Target

- Target host: Windows endpoint
- Modified group: Administrators
- Added user: soc_test_user

## Evidence

- Windows Security log recorded Event ID 4732.
- The event showed that a user was added to a security-enabled local group.
- Wazuh collected the Windows Security event and displayed it in the dashboard.

## Investigation Steps

1. Verified that the test user existed on the Windows endpoint.
2. Added the test user to the local Administrators group.
3. Reviewed Windows Security logs.
4. Filtered events by Event ID 4732.
5. Checked the added user, modified group, timestamp, and host.
6. Reviewed the related event in Wazuh Dashboard.
7. Assessed whether the group membership change was expected.

## Risk

Adding a user to the local Administrators group gives that account elevated privileges.

Unexpected administrator group membership changes may indicate privilege escalation, unauthorized access, persistence, or misuse of administrative rights.

## Recommended Actions

- Verify whether the group membership change was authorized.
- Check who performed the action.
- Review recent login events for the added user.
- Remove unauthorized users from privileged groups.
- Monitor all local administrator group changes.
- Review other endpoints for similar activity.
- Enforce least privilege access.

## Result

The lab successfully demonstrated detection and investigation of a user being added to the local Administrators group using Windows Security logs and Wazuh.

## MITRE ATT&CK Mapping

- Tactic: Persistence / Privilege Escalation
- Technique: T1098.007 — Account Manipulation: Additional Local or Domain Groups
- Reason: Adding a user to a privileged local group can grant elevated permissions and support persistence or privilege escalation.