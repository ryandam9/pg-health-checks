-- Top 5 Databases Size
SELECT
    "DB_Name",
    "Pretty_DB_size"
FROM (
    SELECT
        pg_database.datname AS "DB_Name",
        pg_database_size(pg_database.datname) AS "DB_Size",
        pg_size_pretty(pg_database_size(pg_database.datname)) AS "Pretty_DB_size"
    FROM
        pg_database
    ORDER BY
        2 DESC
    LIMIT 5) AS a;

