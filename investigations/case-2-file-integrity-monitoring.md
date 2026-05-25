# Case 2 — File Integrity Monitoring Alert

## What happened?

A monitored file was modified on the Ubuntu endpoint.

## File Path

/opt/test-monitoring/test.txt

## Evidence

- The file was changed manually in the lab.
- Wazuh generated a File Integrity Monitoring alert.

## Investigation Steps

1. Checked the monitored file path.
2. Reviewed the timestamp of the file change.
3. Verified that the change was expected in the lab.
4. Reviewed Wazuh alert details.
5. Assessed whether the monitored path could be sensitive in a real environment.

## Risk

Unauthorized changes to critical files may indicate compromise, misconfiguration, or insider activity.

## Recommended Actions

- Verify whether the change was authorized.
- Restrict permissions on sensitive directories.
- Monitor critical system paths.
- Review recent user activity.
- Create alert rules for sensitive file changes.

## Result

The lab successfully demonstrated file change detection using Wazuh File Integrity Monitoring.

## MITRE ATT&CK Mapping

- Tactic: Context-dependent
- Technique: Not directly mapped
- Reason: A file modification alone is not enough to map the activity to a specific ATT&CK technique. The mapping depends on which file was changed and the surrounding activity.