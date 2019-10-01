# SQL Basics:

### Queries:
`SELECT fields FROM db_name
WHERE
GROUP BY
HAVING
LIMIT ;`

### CREATE Tables:
`CREATE TABLE table_name (
  field_1  type for field_1 constraints_for_field1,
  field_2  type for field_2 constraints_for_field2
  );`

### INSERTion:
`INSERT INTO table_name(
  'col1', 'col2'
  ) VALUES (
    'val for col1',
    'val for col2'
    );`

### DELETion:
`DELETE FROM `table_name` [WHERE condition];`

### UPDATE:
```
UPDATE `table_name` SET `column_name` = `new_value` [WHERE condition];
```

### JOINs:  

![/joinsVenn.png](/joinsVenn.png)



##Gotchas:
- When using `COUNT`, `DISTINCT` will go inside the `COUNT` rather than the other way around.
- There is a way to look for a column within all tables in a DB:
```
SELECT DISTINCT TABLE_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE COLUMN_NAME IN ('desired_column_here')
        AND TABLE_SCHEMA='the_DBs_name';
```

- Aliases can be used once are set, for example they can be called in ORDER BY,
and this way if the alias stands for a compound attribute (i.e. `(COUNT(fieldname)`)) then the alias would capture the whole thing.


# Teradata:
- `Database db_name;` instead of `use db_name`.
- `EXTRACT(MONTH FROM saledate)` of day / year to extract days.
- 
