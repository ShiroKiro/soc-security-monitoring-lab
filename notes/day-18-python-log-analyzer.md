# Day 18 — Python Log Analyzer

## Goal

The goal of this day was to create a Python script for analyzing Linux authentication logs.

## What I did

1. Created a separate folder for the Python log analyzer.
2. Prepared a sample Linux authentication log.
3. Wrote a Python script to extract failed SSH login attempts.
4. Parsed source IP addresses, targeted usernames, timestamps, and ports.
5. Generated a CSV report.
6. Added documentation for the analyzer.

## Script

`python-log-analyzer/analyze_auth_log.py`

## Input

`python-log-analyzer/sample_auth.log`

## Output

`python-log-analyzer/output/failed_ssh_report.csv`

## Result

The script successfully extracts failed SSH login attempts and creates a structured CSV report.

## Next step

Add SQLite output and more analysis features.