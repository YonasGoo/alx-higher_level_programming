-- lists all genres by their rating
SELECT tg.name, SUM(tr.rate) AS rating FROM tv_shows_genres tgs
JOIN tv_genres tg
ON tg.id = tgs.genre_id
JOIN tv_shows_rating tr
On tr.shows_id = tgs.show_id
GROUP BY tg.name DESC ORDER BY RATING DESC;
