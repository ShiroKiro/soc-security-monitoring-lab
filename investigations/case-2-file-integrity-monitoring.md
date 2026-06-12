# Case 2 — File Integrity Monitoring

## What happened?

A monitored file was modified on the Ubuntu endpoint.  
Wazuh File Integrity Monitoring detected the change and generated an alert.

This case demonstrates how unauthorized or unexpected file changes can be detected and reviewed during a SOC investigation.

## Source

- Source host: Ubuntu monitored host
- Monitoring tool: Wazuh
- Detection module: File Integrity Monitoring
- Log source: Wazuh alerts
- Event type: File modification

## Target

- Target host: Ubuntu monitored host
- Monitored file: `/var/www/html/index.html`
- File type: Web server file
- Related service: Apache web server

## Evidence

- Wazuh generated a File Integrity Monitoring alert.
- The monitored file was modified on the Ubuntu endpoint.
- The alert included information about the file path, action, timestamp, and affected host.

### Example monitored file:

```text
/var/www/html/index.html
```

### Example change:

The content of the web server index page was modified.

## Severity

Medium

Severity can be increased to High if the modified file is critical, for example:

/etc/passwd
/etc/shadow
/etc/ssh/sshd_config

## Detection Logic

The activity was considered suspicious because a monitored file was changed on the Ubuntu endpoint.

### Detection condition:

If a monitored system or application file is created, modified, or deleted,
Wazuh File Integrity Monitoring should generate an alert.

### High-risk condition:

If the modified file is related to authentication, user accounts, SSH configuration, or web content,
the event should be reviewed as a possible unauthorized change.

## Investigation Steps

1. Reviewed the Wazuh File Integrity Monitoring alert.
2. Identified the affected host.
3. Checked the modified file path.
4. Reviewed the action type: created, modified, or deleted.
5. Checked the timestamp of the change.
6. Verified whether the change was expected or authorized.
7. Reviewed related system activity around the same time.
8. Assessed the potential impact of the file modification.
9. Documented recommended response actions.

## Indicators
Indicator	Value
Host	Ubuntu monitored host
File path	/var/www/html/index.html
Event type	File modification
Detection tool	Wazuh
Module	File Integrity Monitoring
Severity	Medium
Related service	Apache web server

## Analysis

The monitored file /var/www/html/index.html was modified on the Ubuntu endpoint.
Because this file belongs to the web server directory, unauthorized modification could indicate website defacement, unauthorized access, or post-compromise activity.

File Integrity Monitoring is important because attackers may modify files after gaining access to a system. This can include changing web content, adding backdoors, modifying configuration files, or altering authentication-related files.

In this lab case, the modification was controlled and performed for testing purposes. However, in a real SOC environment, similar activity should be investigated to confirm whether the change was authorized.

## MITRE ATT&CK Mapping

Tactic	Technique	Description
Defense Evasion	T1565.001 — Stored Data Manipulation	Modification of stored files or application data
Persistence	T1505.003 — Web Shell	Possible risk if web server files are modified to maintain access

## Risk

Unexpected file modification may indicate:

unauthorized system access;
website defacement;
malicious file upload;
web shell deployment;
configuration tampering;
persistence activity;
attempt to hide or alter evidence.

The risk depends on the modified file.
Changes to web files are usually Medium to High severity.
Changes to authentication or SSH configuration files should be treated as High severity.

## Recommended Actions

Verify whether the file modification was authorized.
Review the user account that performed the change.
Check command history and related system logs.
Review Wazuh alerts around the same timestamp.
Restore the file from a trusted backup if the change was unauthorized.
Check the web directory for suspicious scripts or unknown files.
Review file permissions.
Restrict write access to sensitive directories.
Continue monitoring critical files with Wazuh FIM.

## Recommended Preventive Measures
Enable File Integrity Monitoring for critical paths.
Monitor /etc/passwd, /etc/shadow, /etc/ssh/sshd_config, and web directories.
Restrict administrative access.
Use least privilege for service accounts.
Maintain backups of important configuration files.
Review Wazuh FIM alerts regularly.
Separate administrative users from normal users.

## Result

The lab successfully demonstrated detection and investigation of file modification activity using Wazuh File Integrity Monitoring.

The event was classified as a suspicious file integrity event because a monitored file was changed on the Ubuntu endpoint. The investigation confirmed that Wazuh can detect modifications to important files and provide useful evidence for SOC analysis.

## SOC Analyst Conclusion

The observed file modification should be reviewed as a potential security event.

In this lab, the change was controlled and expected. In a real environment, an unexpected modification of a web server file could indicate website defacement, unauthorized access, or post-compromise activity.

The recommended action is to verify whether the change was authorized, review related system activity, and ensure that critical files are continuously monitored through Wazuh File Integrity Monitoring.