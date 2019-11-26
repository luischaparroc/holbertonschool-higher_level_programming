-- Script that lists shows that don't belong to Comedy genre
SELECT tv_shows.title -- Query to get shows that are not comedies
FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title -- Query to get Comedy shows
	FROM tv_shows
     	JOIN tv_show_genres
     	     ON tv_show_genres.show_id = tv_shows.id
     	JOIN tv_genres
     	     ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.id
) comedy_shows ON comedy_shows.title = tv_shows.title
WHERE comedy_shows.title is NULL
ORDER BY tv_shows.title;
