-- lists all comedy shows in the database
SELECT ts.title FROM tv_show AS ts
JOIN tv_show_genres AS tgs
On ts.id = tgs.show_id
JOIN tv_genres AS tgg
ON tgs.genre_id = tgg.id
WHERE tgg.name = 'Comedy'
GROUP BY ts.title ASC;
