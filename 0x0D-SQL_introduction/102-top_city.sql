-- top 3 cities temp
SELECT city, AVG(value) AS avgTemp FROM
(SELECT city, month, value FROM temperatures
WHERE month=7 OR month=8) AS A
GROUP BY city ORDER BY avgTemp DESC LIMIT 3;
