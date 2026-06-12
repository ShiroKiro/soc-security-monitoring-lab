# Case 7 — Suspicious PowerShell Activity

## What happened?

A PowerShell process was executed on the Windows endpoint.

Windows Security logs recorded Event ID `4688`, which indicates that a new process was created.  
PowerShell is a legitimate administrative tool, but suspicious PowerShell usage may indicate attacker activity, script execution, post-exploitation behavior, or defense evasion.

## Source

- Source system: Windows endpoint
- Log source: Windows Security logs
- Tool used: Event Viewer / Wazuh
- Event ID: 4688
- Event type: Process creation
- Process of interest: `powershell.exe`

## Target

- Target host: Windows endpoint
- Target process: `powershell.exe`
- Detection focus: Suspicious command-line execution
- Security relevance: Possible script execution, reconnaissance, or post-exploitation activity

## Evidence

Windows Security logs generated a process creation event.

Important Event ID:

```text
4688 — A new process has been created
```

## Important fields reviewed during the investigation:

New Process Name
Process Command Line
Creator Process Name
Subject Account Name
Subject Domain
Process ID
Parent Process ID
Token Elevation Type
Timestamp

### Example process of interest:

powershell.exe

### Example suspicious indicators:

PowerShell executed with unusual command-line arguments
PowerShell launched from an unusual parent process
PowerShell executed by an unexpected user
PowerShell activity occurred outside normal administrative work

## Severity

Medium

### Severity should be increased to High if:

- PowerShell was executed with obfuscated or encoded commands;
- PowerShell downloaded or executed remote content;
- PowerShell was launched by an unusual parent process;
- PowerShell was executed by a non-administrative user unexpectedly;
- the activity happened after a suspicious login;
- the command modified security settings or user accounts;
- the activity was followed by persistence or privilege escalation events.

## Detection Logic

The activity was considered suspicious because PowerShell was executed on the Windows endpoint and required review.

### Detection condition:

If Event ID 4688 shows powershell.exe execution,
review the command line, parent process, user account, and timestamp.

### High-risk condition:

If powershell.exe is executed with suspicious command-line parameters,
unusual parent process, or after suspicious authentication activity,
treat the event as possible attacker activity.

## Related events:

4624 — An account successfully logged on
4625 — An account failed to log on
4688 — A new process has been created
4720 — A user account was created
4732 — A member was added to a security-enabled local group

## Investigation Steps

1. Opened Windows Event Viewer.
2. Navigated to Windows Logs → Security.
3. Filtered events by Event ID 4688.
4. Searched for powershell.exe process creation.
5. Reviewed the PowerShell command line.
6. Identified the user account that executed the process.
7. Checked the parent process.
8. Reviewed the timestamp of execution.
9. Checked whether the activity was expected administrative work.
10. Reviewed related login events such as 4624 and 4625.
11. Reviewed related account and privilege events such as 4720 and 4732.
12. Documented the risk and recommended response actions.

## Indicators

Indicator	Value
Event ID	4688
Event name	A new process has been created
Log source	Windows Security logs
Target process	powershell.exe
Target system	Windows endpoint
Event type	Process creation
Severity	Medium
Related login events	4624, 4625
Related account events	4720, 4732

### Suspicious PowerShell Indicators

Indicator	Why It Matters
Encoded or obfuscated command line	May hide the real command
Remote content execution	May indicate download or execution of external script
Unusual parent process	May indicate exploitation or abuse of another application
Execution by unexpected user	May indicate compromised account
Execution after failed logins	May indicate post-compromise activity
Security setting changes	May indicate defense evasion
Account or group changes after execution	May indicate persistence or privilege escalation

## Analysis

Event ID 4688 indicates that a new process was created on the Windows endpoint.

PowerShell is commonly used by administrators for automation and system management. However, it is also frequently abused by attackers because it is built into Windows and can execute commands, scripts, and system changes.

A PowerShell event should not automatically be treated as malicious. The command line, parent process, user account, timestamp, and related events must be reviewed.

In this lab case, the activity was generated in a controlled environment for testing and investigation purposes.

## MITRE ATT&CK Mapping
Tactic	Technique	Description
Execution	T1059.001 — PowerShell	Use of PowerShell to execute commands or scripts
Defense Evasion	T1027 — Obfuscated Files or Information	Relevant if commands are encoded or obfuscated
Discovery	T1082 — System Information Discovery	Relevant if PowerShell is used to collect system information
Risk

## Suspicious PowerShell activity may indicate:

script execution;
post-exploitation activity;
system reconnaissance;
credential access attempts;
defense evasion;
persistence setup;
privilege escalation preparation;
misuse of administrative tools.

The risk depends on the command line, user account, parent process, and related events.

## Recommended Actions

Verify whether the PowerShell execution was authorized.
Review the full command line.
Identify the user account that executed the process.
Check the parent process.
Review related login events.
Check whether the command changed system settings.
Check whether the activity created users or changed group membership.
Isolate the endpoint if malicious activity is suspected.
Collect additional logs for timeline analysis.
Continue monitoring PowerShell activity.

## Recommended Preventive Measures

Enable process command-line logging.
Enable PowerShell Script Block Logging where appropriate.
Forward Windows logs to Wazuh or SIEM.
Monitor Event ID 4688.
Restrict PowerShell usage for non-administrative users where possible.
Use least privilege.
Review administrative activity regularly.
Monitor suspicious parent-child process relationships.
Use endpoint protection or EDR where available.

## Result

The lab successfully demonstrated investigation of suspicious PowerShell activity using Windows Security logs.

Event ID 4688 provided useful evidence for identifying process execution, the user account, command line, and parent process.

## SOC Analyst Conclusion

The observed PowerShell execution should be reviewed as a potentially suspicious process creation event.

In this lab, the activity was controlled and used for testing. In a real environment, suspicious PowerShell activity may indicate script execution, post-exploitation behavior, or misuse of administrative tools.

The recommended action is to review the command line, identify the executing user, check the parent process, and correlate the event with authentication, account creation, and privilege change events.