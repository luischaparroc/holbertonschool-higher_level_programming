-- Script that lists genres of Dexter show
SELECT tv_shows.title -- Query to join tables
FROM tv_shows
     JOIN tv_show_genres
     	  ON tv_show_genres.show_id = tv_shows.id
     JOIN tv_genres
     	  ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
