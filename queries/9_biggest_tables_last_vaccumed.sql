-- Top 10 biggest tables last vacuumed
SELECT
    schemaname,
    relname,
    cast(last_vacuum AS date),
    cast(last_autovacuum AS date),
    cast(last_analyze AS date),
    cast(last_autoanalyze AS date),
    pg_size_pretty(pg_total_relation_size(relid)) AS table_total_size
FROM
    pg_stat_user_tables
ORDER BY
    pg_total_relation_size(relid) DESC
LIMIT 10;

