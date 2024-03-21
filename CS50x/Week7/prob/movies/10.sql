SELECT DISTINCT name
FROM people
where id in (
    SELECT person_id
    FROM directors
    where movie_id in (
        SELECT id
        FROM movies
        JOIN ratings ON movies.id = ratings.movie_id
        where rating >= 9
    )
);