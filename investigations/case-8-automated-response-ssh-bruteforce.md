# Case 8 — Automated Response to SSH Brute Force (Active Response)

## What happened?

Repeated failed SSH login attempts were generated against the Ubuntu monitored host from a Kali Linux test VM using invalid credentials.

Wazuh already detected this pattern as a brute-force attempt (Case 1). This case extends that detection with **Wazuh Active Response**, so that instead of only generating an alert, the platform automatically blocks the attacking IP address on the monitored host's firewall — turning passive detection into an automated containment action.

## Source

- Source system: Kali Linux / Test VM
- Attack type: Repeated SSH authentication attempts with invalid credentials and a non-existent user
- Log source: Linux authentication logs (`sshd`, PAM), Wazuh
- Rule triggered: `5712` — sshd: brute force trying to get access to the system. Non existent user.
- Rule level: 10

## Target

- Target host: Ubuntu monitored host (Wazuh agent `001`)
- Target service: SSH (`sshd`)
- Detection focus: Authentication brute-force behavior
- Response focus: Automated IP containment via Active Response

## Evidence

Wazuh aggregated multiple authentication failure events into a single brute-force detection:

```text
5710 — sshd: Attempt to login using a non-existent user
5503 — PAM: User login failed
5712 — sshd: brute force trying to get access to the system. Non existent user. (level 10)
```

Active Response log (`active-responses.log`) on the Wazuh Manager confirmed execution of the containment action:

```text
active-response/bin/firewall-drop: Starting
command: "add"
agent: {"id":"001","name":"monitoredhost","ip":"192.168.62.20"}
rule: {"level":10,"description":"sshd: brute force trying to get access to the system. Non existent user.","id":"5712"}
srcip: "192.168.62.129"
```

The block was confirmed directly on the monitored host's firewall:

```text
$ sudo iptables -L -n | grep 192.168.62.129
DROP  all  --  192.168.62.129  0.0.0.0/0
DROP  all  --  192.168.62.129  0.0.0.0/0
```

## Configuration

Active Response was configured on the Wazuh Manager to trigger the `firewall-drop` command on the specific monitored agent (not the manager itself) whenever rule `5712` fires:

```xml
<command>
  <name>firewall-drop</name>
  <executable>firewall-drop</executable>
  <timeout_allowed>yes</timeout_allowed>
</command>

<active-response>
  <disabled>no</disabled>
  <command>firewall-drop</command>
  <location>defined-agent</location>
  <agent_id>001</agent_id>
  <rules_id>5712</rules_id>
  <timeout>600</timeout>
</active-response>
```

`location: defined-agent` was used instead of `local` so the block is applied on the actual attacked endpoint rather than on the Wazuh Manager itself. The block automatically expires after the configured `timeout` (600 seconds) if no further brute-force attempts are detected, keeping the response temporary rather than permanent.

## Severity

High (level 10 — matches existing Wazuh brute-force rule severity)

### Severity should be increased further if:

- the brute force succeeds and results in a valid authenticated session;
- the targeted account has elevated privileges;
- the attack originates from multiple distributed source IPs (credential stuffing / distributed brute force), which a single-IP firewall block would not fully mitigate;
- the same source IP repeatedly bypasses the block after timeout expiry, indicating a persistent threat actor.

## Detection Logic

The activity was considered a brute-force attempt because Wazuh aggregated multiple authentication failures (Event 5710 / 5503) from the same source IP within a short time window into rule 5712.

### Detection condition:

If rule `5712` fires (sshd brute force, non-existent user),
automatically trigger Active Response `firewall-drop` on the affected agent.

### Response condition:

If the source IP repeats the same behavior before the block expires,
Active Response extends the block duration (`continue` action) rather than issuing a duplicate block.

## Related events:

5503 — PAM: User login failed
5710 — sshd: Attempt to login using a non-existent user
5712 — sshd: brute force trying to get access to the system. Non existent user.

## Investigation Steps

1. Reviewed Case 1 (SSH brute-force detection) as the baseline detection rule.
2. Configured Active Response on the Wazuh Manager with `firewall-drop`, scoped to the specific monitored agent via `defined-agent` and `agent_id`.
3. Verified the Active Response script existed and had correct permissions on the manager (`/var/ossec/active-response/bin/firewall-drop`).
4. Validated the XML configuration and restarted the Wazuh Manager.
5. Generated repeated failed SSH login attempts from the Kali VM against the monitored host using `sshpass`.
6. Reviewed the triggered alert (rule 5712) in the Wazuh Dashboard.
7. Reviewed `active-responses.log` on the Wazuh Manager to confirm the `add` command was executed against the correct agent and source IP.
8. Verified the resulting firewall rule directly on the monitored host using `iptables -L -n`.
9. Documented the full detect → respond → block cycle.

## Indicators

| Indicator | Value |
|---|---|
| Rule ID | 5712 |
| Rule description | sshd: brute force trying to get access to the system. Non existent user. |
| Rule level | 10 |
| Log source | Linux authentication logs, Wazuh |
| Target agent | 001 (monitoredhost) |
| Response action | firewall-drop (Active Response) |
| Response scope | defined-agent |
| Block duration | 600 seconds (auto-expiring) |
| Related events | 5503, 5710 |

### Why Active Response Matters

| Aspect | Why It Matters |
|---|---|
| Automated containment | Reduces time-to-response compared to manual alert triage |
| `defined-agent` scoping | Ensures the block applies to the actual attacked host, not the SIEM server |
| Auto-expiring block | Avoids permanent firewall bloat from transient/opportunistic scanning |
| Verifiable at multiple layers | Confirmed in SIEM alert, Active Response log, and host firewall independently |

## Analysis

This case demonstrates the difference between detection and response in a SOC workflow. Case 1 already showed that Wazuh can detect an SSH brute-force pattern; this case adds an automated containment step so the attacking IP is blocked without requiring manual analyst intervention.

Scoping the response to the specific monitored agent (`defined-agent` + `agent_id`) was an important configuration detail — an initial `local` scope would have applied the firewall block on the Wazuh Manager rather than on the actual attacked endpoint, which would not have stopped the attack against the real target.

In this lab, the activity was generated in a controlled environment for testing and investigation purposes.

## MITRE ATT&CK Mapping

| Tactic | Technique | Description |
|---|---|---|
| Credential Access | T1110 — Brute Force | Repeated authentication attempts against SSH |
| (Response) | Active Response / automated containment | Automated blocking of the source IP following detection |

## Risk

Unmitigated SSH brute-force activity may indicate:

- credential guessing against valid or default accounts;
- reconnaissance ahead of a targeted attack;
- botnet-driven opportunistic scanning;
- a precursor to successful unauthorized access if left unaddressed.

Automated containment reduces the window during which a brute-force attempt can succeed, but does not replace monitoring — a persistent or distributed attacker can still probe from other source IPs.

## Recommended Actions

Confirm the blocked IP in `active-responses.log` and on the host firewall.
Review whether the same source IP appears in other logs (Suricata, other hosts).
Confirm the targeted account(s) were not compromised prior to the block.
Extend monitoring for repeat attempts from related IP ranges.
Consider permanent blocklisting if the source IP is confirmed malicious rather than opportunistic.

## Recommended Preventive Measures

Disable password-based SSH authentication in favor of key-based authentication.
Restrict SSH access by source IP / VPN where feasible.
Enable rate limiting (e.g., fail2ban) as a defense-in-depth layer alongside Wazuh Active Response.
Monitor Active Response logs regularly to confirm the automation is functioning as expected.
Periodically review and adjust the Active Response timeout based on observed attack patterns.

## Result

The lab successfully demonstrated a complete detect-to-response cycle: Wazuh detected the SSH brute-force pattern (rule 5712), automatically triggered Active Response to block the source IP on the correct monitored endpoint, and the block was independently verified in the Active Response log and on the host's firewall.

## SOC Analyst Conclusion

This case shows the value of moving from passive alerting to automated containment for well-understood, high-confidence detections such as SSH brute force. Scoping the response correctly to the affected endpoint (rather than the SIEM server) was essential for the containment action to have real effect. In a production environment, this type of automated response reduces analyst workload for high-volume, low-ambiguity threats while preserving an audit trail across the SIEM alert, the response log, and the endpoint firewall state.