SELECT
    host,
    user,
    src_ip,
    event_type,
    COUNT(*) AS event_count
FROM auth_events
GROUP BY
    host,
    user,
    src_ip,
    event_type
ORDER BY event_count DESC;