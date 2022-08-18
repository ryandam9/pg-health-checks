-- Logging parameters
SELECT
    name,
    setting,
    short_desc
FROM
    pg_settings
WHERE
    name IN ('log_connections', 'log_disconnections', 'log_checkpoints', 'log_min_duration_statement', 'log_statement', 'log_temp_files', 'log_autovacuum_min_duration');

