SELECT
    s.user,
    s.src_ip,
    COUNT(f.id) AS failed_attempts_before_success,
    s.timestamp AS success_timestamp,
    s.line_number AS success_line_number
FROM auth_events s
JOIN auth_events f
    ON s.user = f.user
    AND s.src_ip = f.src_ip
    AND f.line_number < s.line_number
WHERE s.event_type = 'successful_ssh_login'
  AND f.event_type = 'failed_ssh_login'
GROUP BY
    s.user,
    s.src_ip,
    s.timestamp,
    s.line_number
ORDER BY failed_attempts_before_success DESC;