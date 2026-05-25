# Case 5 — New Local User Created

## What happened?

A new local user account was created on the Windows endpoint.

## Source

- Source host: Windows endpoint
- Action performed by: local administrator / lab user

## Target

- Target host: Windows endpoint
- Created user: soc_test_user

## Evidence

- Windows Security log recorded Event ID 4720.
- The event showed that a new local user account was created.
- Wazuh collected the Windows Security event and displayed it in the dashboard.

## Investigation Steps

1. Created a test local user on the Windows endpoint.
2. Reviewed Windows Security logs.
3. Filtered events by Event ID 4720.
4. Checked the created username and timestamp.
5. Reviewed the related event in Wazuh Dashboard.
6. Verified whether the activity was expected in the lab.
7. Assessed the risk of unexpected local account creation.

## Risk

Unexpected local user creation may indicate unauthorized access, privilege abuse, persistence, or preparation for further malicious activity.

## Recommended Actions

- Verify whether the account creation was authorized.
- Check who created the account.
- Review group membership of the new account.
- Disable or remove unknown accounts.
- Check for related login events.
- Monitor similar account creation events across other endpoints.
- Review administrator activity.

## Result

The lab successfully demonstrated detection and investigation of new local user account creation using Windows Security logs and Wazuh.

## MITRE ATT&CK Mapping

- Tactic: Persistence
- Technique: T1136.001 — Create Account: Local Account
- Reason: Creating a local account can be used to maintain access to a system.