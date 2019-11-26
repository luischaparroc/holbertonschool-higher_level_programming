-- Script that lists genres and number of shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows -- Query to join tables
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.id ASC;
