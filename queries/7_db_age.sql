-- Database Age
SELECT
    datname,
    ltrim(to_char(age(datfrozenxid), '999,999,999,999,999'))
    age
FROM
    pg_database
WHERE
    datname NOT LIKE 'rdsadmin'
ORDER BY
    ltrim(to_char(age(datfrozenxid), '999,999,999,999,999'))
LIMIT 5;

