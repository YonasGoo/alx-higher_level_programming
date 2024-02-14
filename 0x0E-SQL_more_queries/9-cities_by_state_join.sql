-- lists all cities in the database
SELECT c.id, c.name, s.name FROM cities c, states s
WHERE c.states_id = s.id
GROUP BY c.id ASC;
