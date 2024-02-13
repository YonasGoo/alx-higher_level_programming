-- states maximum temp
SELECT state, MAX(value) AS maxTemp FROM temperatures
GROUP BY state ASC;
