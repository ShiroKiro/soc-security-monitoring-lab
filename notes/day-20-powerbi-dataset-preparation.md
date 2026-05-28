# Day 20 — Power BI Dataset Preparation

## Goal

The goal of this day was to prepare a structured CSV dataset for a Power BI security dashboard.

## What I did

1. Extended the Python log analyzer with a Power BI CSV output.
2. Added normalized fields for dashboard creation.
3. Added basic risk classification.
4. Created a separate `security_events_for_powerbi.csv` file.
5. Added a SQL summary query.
6. Updated project documentation.

## Output

`python-log-analyzer/output/security_events_for_powerbi.csv`

## Dataset fields

- event_date
- event_time
- timestamp_raw
- host
- user
- src_ip
- src_port
- event_type
- risk_level
- event_category
- event_count

## Risk logic

- successful SSH login: Low
- failed SSH login for root/admin/administrator: High
- other failed SSH login: Medium

## Result

The project now has a structured dataset that can be imported into Power BI for security dashboard creation.

## Next step

Build a Power BI security dashboard using the prepared CSV dataset.