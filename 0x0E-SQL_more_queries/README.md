# SQL - More queries
Project done during **Full Stack Software Engineering studies** at **Holberton School**. It aims to learn about how to create a new user, manage privileges for a user, `PRIMARY KEY`, `FOREIGN KEY`, constraints, subqueries, `JOIN` and `UNION` with **MySQL**.

## Technologies
* `MySQL 5.7` (version 5.7.8-rc)
* Tested on Ubuntu 14.04 LTS

## Files

All the following files are scripts of MySQL:

| Filename | Description |
| -------- | ----------- |
| `0-privileges.sql` | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server. |
| `1-create_user.sql` | Creates the MySQL server user `user_0d_1` |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and the user `user_0d_2` |
| `3-force_name.sql` | Creates the table `force_name` on your MySQL server |
| `4-never_empty.sql` | Creates the table `id_not_null` on your MySQL serve |
| `5-unique_id.sql` | Creates the table `unique_id` on your MySQL server |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) |
| `7-cities.sql` | Creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) |
| `8-cities_of_california_subquery.sql` | Lists all the cities of California that can be found in the database `hbtn_0d_usa` |
| `9-cities_by_state_join.sql` | Lists all cities contained in the database `hbtn_0d_usa` |
| `10-genre_id_by_show.sql` | Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows contained in the database `hbtn_0d_tvshows` |
| `12-no_genre.sql` | Lists all shows contained in `hbtn_0d_tvshows` without a genre linked |
| `13-count_shows_by_genre.sql` | Lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each |
| `14-my_genres.sql` | Uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter` |
| `15-comedy_only.sql` | Lists all Comedy shows in the database `hbtn_0d_tvshows` |
| `16-shows_by_genre.sql` | Lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows` |
| `100-not_my_genres.sql` | Uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter` |
| `101-not_a_comedy.sql` | Lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows` |
| `102-rating_shows.sql` | Lists all shows from `hbtn_0d_tvshows_rate` by their rating |
| `103-rating_genres.sql` | Lists all genres in the database `hbtn_0d_tvshows_rate` by their rating |
