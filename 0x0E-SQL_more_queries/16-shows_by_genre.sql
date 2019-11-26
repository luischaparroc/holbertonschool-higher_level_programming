-- Script that lists all shows and all genres
SELECT tv_shows.title, tv_genres.name -- Query to join tables
FROM tv_shows
     LEFT JOIN tv_show_genres
     	  ON tv_show_genres.show_id = tv_shows.id
     LEFT JOIN tv_genres
     	  ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
