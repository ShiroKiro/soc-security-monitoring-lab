SELECT
    src_ip,
    COUNT(*) AS failed_attempts
FROM auth_events
WHERE event_type = 'failed_ssh_login'
GROUP BY src_ip
ORDER BY failed_attempts DESC;