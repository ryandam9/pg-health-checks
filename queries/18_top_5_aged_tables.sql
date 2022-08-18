-- Top 5 aged tables
SELECT
    c.oid::regclass AS table_name,
    ltrim(to_char(greatest (age(c.relfrozenxid), age(t.relfrozenxid)), '999,999,999,999,999')) AS age
FROM
    pg_class c
    LEFT JOIN pg_class t ON c.reltoastrelid = t.oid
WHERE
    c.relkind IN ('r', 'm')
ORDER BY
    2
LIMIT 5;

