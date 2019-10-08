Database ua_dillards;

-- Exercise 1. How many distinct dates are there in the saledate column of the transaction
-- table for each month/year combination in the database?
SELECT
EXTRACT(MONTH FROM saledate) AS m,
EXTRACT (YEAR FROM saledate) AS y,
COUNT (DISTINCT EXTRACT (DAY FROM saledate))
FROM trnsact
GROUP BY y, m
ORDER BY y ASC, m ASC;

-- Exercise 2. Use a CASE statement within an aggregate function to determine which sku
-- had the greatest total sales during the combined summer months of June, July, and August.

SELECT DISTINCT sku,
SUM(CASE WHEN EXTRACT(MONTH from saledate)=06 AND stype='p' THEN amt END) as June,
SUM(CASE WHEN EXTRACT(MONTH from saledate)=07 AND stype='p' THEN amt END) as July,
SUM(CASE WHEN EXTRACT(MONTH from saledate)=08 AND stype='p' THEN amt END) as August,
ZEROIFNULL(June)+
ZEROIFNULL(July)+
ZEROIFNULL(August) as total
from trnsact
group by sku
order by total desc
