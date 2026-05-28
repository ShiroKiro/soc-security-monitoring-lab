# Day 19 — SQLite Output for Python Log Analyzer

## Goal

The goal of this day was to extend the Python log analyzer with SQLite output and SQL-based analysis.

## What I did

1. Updated the parser to detect both failed and successful SSH logins.
2. Added SQLite database output.
3. Created the `auth_events` table.
4. Stored parsed SSH authentication events in SQLite.
5. Added SQL queries for top failed IPs and targeted users.
6. Added failed-to-success pattern detection.
7. Updated project documentation.

## Output

- `python-log-analyzer/output/ssh_auth_events.csv`
- `python-log-analyzer/output/auth_events.db`

## SQL queries

- `queries/top_failed_ips.sql`
- `queries/failed_by_user.sql`
- `queries/failed_to_success.sql`

## Result

The analyzer now supports CSV output, SQLite storage, and SQL-based investigation of authentication events.

## Next step

Prepare security event data for a Power BI dashboard.

## Additional Fix

The initial parser expected SSH log lines in the `sshd[PID]` format.

The actual Ubuntu logs used the `sshd-session[PID]` format.

The regular expression was updated to support both:

- `sshd[PID]`
- `sshd-session[PID]`

## Validation

The SQLite database was checked using a SQLite GUI on the host machine.

The `auth_events` table was created successfully and contained parsed failed SSH login events.