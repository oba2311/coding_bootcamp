## Week 1:

**ER Diagrams:**
Entities are represented by squares,
Relationships are drawn between entities and processes are represented by a diamond shape.

Cardinality rules:
The number 1 and usually the letters n or m are used to describe one to many, one to one,many to one or many to many relationships.

**Temporary tables:** faster than regular tables, and simplify complicated queries.

CREATE TEMPORARY TABLE name AS (
  SELECT field names FORM original_table
  WHERE desired condition
  )


## Week 2:
Refresher for aggregate funcs:
AVG, MIN, MAX, COUNT, SUM. Remember to use DISTINCT especially when using COUNT.

After GROUP BY we use HAVING instead of WHERE, since WHERE applies before
the data is grouped.

For wildcards, use * or % and LIKE (there are some more).

Subqueries:
Allow better running time.
