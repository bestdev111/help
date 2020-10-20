## Postgres

`psql -U postgres`

### Display server version

```
postgres=# SHOW SERVER_VERSION;
 server_version
----------------
 9.3.25
(1 row)
```

### Display current database

`SELECT current_database();`

### List databases

`\l`

### Connect to a database called mydb

`\c mydb;`

### List tables in database

`\d`

### List schemas in database

`\dn`

### List all tables in a schema (e.g. 'demo')

`\dt demo.`

### Create a new database

`CREATE DATABASE dbname;`

...or can use the postgres cli:

`createdb dbname`

### Switch to or connect to a different database

`\c dbname`