SELECT name
FROM people
where id in (
    SELECT person_id
    FROM stars
    where movie_id = (
        SELECT id
        FROM movies
        where title = 'Toy Story'
    )
);