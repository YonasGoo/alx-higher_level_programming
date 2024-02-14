-- lists all comedy shows in the database
SELECT ts.title FROM tv_show AS ts
On ts.id = tgs.show_id
JOIN ts.id = tgs.show_id
JOIN tv_genres AS tgg
ON tgs.genre_id = tgg.id
WHERE tgg.name = 'Comedy'
GROUP BY ts.title ASC;
