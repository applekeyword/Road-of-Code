SELECT DISTINCT name
FROM people
where id in (
    SELECT person_id
    FROM stars
    where movie_id in (
        SELECT id
        FROM movies
        where year = 2004
    )
)
ORDER BY birth;