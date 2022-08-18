-- Performance Parameters
SELECT
    name,
    setting
FROM
    pg_settings
WHERE
    name IN ('shared_buffers', 'effective_cache_size', 'log_temp_files', 'work_mem', 'shared_preload_libraries', 'maintenance_work_mem', 'default_statistics_target', 'random_page_cost', 'rds.logical_replication', 'wal_keep_segments');

