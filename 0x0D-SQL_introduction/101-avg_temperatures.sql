-- average temp by city
SELECT city, AVG(value) AS avgTemp FROM temperatures
GROUP BY city ORDER BY avgTemp DESC;
