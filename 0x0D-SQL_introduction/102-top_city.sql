-- Script that displays the average temperature
-- Query to display the average temperature by city ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
