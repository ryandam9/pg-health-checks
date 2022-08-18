-- Top 10 biggest tables
SELECT
    schemaname AS table_schema,
    relname AS table_name,
    pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
    pg_size_pretty(pg_relation_size(relid)) AS data_size,
    pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) AS external_size
FROM
    pg_catalog.pg_statio_user_tables
WHERE
    schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY
    pg_total_relation_size(relid) DESC,
    pg_relation_size(relid) DESC
LIMIT 10;

