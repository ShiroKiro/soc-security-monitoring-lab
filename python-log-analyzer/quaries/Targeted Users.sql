SELECT
    user,
    COUNT(*) AS failed_attempts
FROM auth_events
WHERE event_type = 'failed_ssh_login'
GROUP BY user
ORDER BY failed_attempts DESC;