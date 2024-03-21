SELECT title
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
where id in (
    SELECT movie_id
    FROM stars
    where person_id = (
        SELECT id
        FROM people
        where name = 'Chadwick Boseman'
    )
)
ORDER BY rating DESC LIMIT 5;