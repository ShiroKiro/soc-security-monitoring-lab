SELECT
    event_type,
    COUNT(*) AS event_count
FROM auth_events
GROUP BY event_type;