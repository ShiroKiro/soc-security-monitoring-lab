# Case 4 — Windows Failed Login Attempts

## What happened?

Multiple failed Windows login attempts were generated against the Windows endpoint.

## Source

- Source: Local Windows logon attempt
- Source host: Windows endpoint

## Target

- Target host: Windows endpoint
- Target user: labuser

## Evidence

- Windows Security log recorded failed login events.
- Event ID 4625 was generated.
- Wazuh collected the Windows Security event and displayed it in the dashboard.

## Investigation Steps

1. Created a test local user for the lab.
2. Generated controlled failed login attempts.
3. Reviewed Windows Security logs in Event Viewer.
4. Filtered events by Event ID 4625.
5. Reviewed the related event in Wazuh Dashboard.
6. Checked the targeted username, timestamp, and affected host.
7. Assessed whether the activity was expected or suspicious.

## Risk

Repeated failed Windows login attempts may indicate password guessing, brute-force activity, unauthorized access attempts, or misuse of valid accounts.

## Recommended Actions

- Verify whether the login attempts were expected.
- Check the source workstation and targeted account.
- Review whether a successful login occurred after failed attempts.
- Enforce strong password policy.
- Enable account lockout policy.
- Monitor repeated failed login attempts.
- Investigate similar events across other endpoints.

## Result

The lab successfully demonstrated detection and investigation of Windows failed login attempts using Windows Security logs and Wazuh.

## MITRE ATT&CK Mapping

- Tactic: Credential Access
- Technique: T1110 — Brute Force
- Reason: Repeated failed Windows login attempts may indicate password guessing or brute-force behavior.