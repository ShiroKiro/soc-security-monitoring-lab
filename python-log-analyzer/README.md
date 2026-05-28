# Python Log Analyzer

## Goal

This script analyzes Linux authentication logs and extracts failed SSH login attempts.

It was created as an extension for the Wazuh + Suricata SOC lab project.

## What it does

The analyzer:

- reads a sample Linux authentication log;
- extracts failed SSH login attempts;
- identifies source IP addresses;
- identifies targeted usernames;
- counts failed login attempts;
- generates a CSV report.

## Input

`sample_auth.log`

## Output

`output/failed_ssh_report.csv`

## Usage

```bash
python3 analyze_auth_log.py
Example findings

The script can help answer questions such as:

Which IP generated the most failed SSH attempts?
Which usernames were targeted?
How many failed SSH login attempts were found?
```

## SQLite Output

The analyzer creates a SQLite database:

`output/auth_events.db`

The database contains parsed SSH authentication events in the `auth_events` table.

Main fields:

- `timestamp`
- `host`
- `user`
- `src_ip`
- `src_port`
- `event_type`
- `raw_line`

## SQL Analysis

SQL queries are stored in:

`queries/`

Available queries:

- `top_failed_ips.sql`
- `failed_by_user.sql`
- `failed_to_success.sql`

## Notes

The analyzer supports both common SSH log formats:

- `sshd[PID]`
- `sshd-session[PID]`

This was added because Ubuntu logs may use `sshd-session` depending on the system configuration.

## Power BI Dataset

The analyzer also creates a Power BI-ready CSV file:

`output/security_events_for_powerbi.csv`

This file contains cleaned and structured fields for dashboard creation:

- `event_date`
- `event_time`
- `host`
- `user`
- `src_ip`
- `src_port`
- `event_type`
- `risk_level`
- `event_category`
- `event_count`

The goal of this file is to make the data easier to import and visualize in Power BI.