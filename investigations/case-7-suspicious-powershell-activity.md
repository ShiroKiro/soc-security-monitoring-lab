# Case 7 — Suspicious PowerShell Activity

## What happened?

PowerShell activity was generated on the Windows endpoint and detected through Windows logs, Sysmon, and Wazuh.

## Source

- Source host: Windows endpoint
- Process: powershell.exe
- User: lab user / local administrator

## Target

- Target host: Windows endpoint

## Evidence

- PowerShell events were recorded in Windows Event Logs.
- Sysmon recorded PowerShell process creation.
- Wazuh collected and displayed the related events in the dashboard.

## Investigation Steps

1. Verified that Wazuh Agent and Sysmon were running on the Windows endpoint.
2. Enabled PowerShell Script Block Logging.
3. Generated controlled PowerShell activity using safe administrative commands.
4. Reviewed PowerShell events in Windows Event Viewer.
5. Reviewed Sysmon process creation events related to powershell.exe.
6. Checked the same events in Wazuh Dashboard.
7. Reviewed the process name, command line, user, timestamp, and host.
8. Assessed whether the PowerShell activity was expected or suspicious.

## Risk

PowerShell is a legitimate administration tool, but it is also commonly used in suspicious activity because it can execute commands, access system information, and automate actions.

Unexpected PowerShell activity may indicate misuse of administrative tools, unauthorized script execution, reconnaissance, or post-compromise activity.

## Recommended Actions

- Verify whether the PowerShell activity was authorized.
- Review the command line and executed commands.
- Check the user account that executed PowerShell.
- Review parent process information.
- Check for repeated or unusual PowerShell execution.
- Monitor PowerShell Script Block Logging events.
- Investigate related Sysmon process creation events.

## Result

The lab successfully demonstrated detection and investigation of PowerShell activity using Windows Event Logs, Sysmon, and Wazuh.

## MITRE ATT&CK Mapping

- Tactic: Execution
- Technique: T1059.001 — Command and Scripting Interpreter: PowerShell
- Reason: PowerShell can be used to execute commands and scripts on Windows systems.