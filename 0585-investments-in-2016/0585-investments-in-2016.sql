SELECT 
   ROUND(SUM(tiv_2016),2)as tiv_2016
FROM Insurance
WHERE
tiv_2015 in (
   SELECT tiv_2015
   FROM Insurance
   GROUP BY tiv_2015 HAVING COUNT(*)>1
)
AND(lat,lon)in(
SELECT lat,lon 
    FROM Insurance
    GROUP BY lat,lon having COUNT(*)=1


);
