-- Key PostgreSQL Parameters
SELECT
    name,
    setting,
    source,
    short_desc
FROM
    pg_settings
WHERE
    name IN ('max_connections', 'shared_buffers', 'checkpoint_timeout', 'max_wal_size', 'default_statistics_target', 'work_mem', 'maintenance_work_mem', 'random_page_cost', 'rds.logical_replication', 'wal_keep_segments', 'hot_standby_feedback');

