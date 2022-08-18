-- Total Size of all databases
SELECT
    pg_size_pretty(SUM(pg_database_size(pg_database.datname))) AS "Total_DB_size"
FROM
    pg_database;

