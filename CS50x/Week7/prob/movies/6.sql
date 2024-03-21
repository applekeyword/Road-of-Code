SELECT AVG(rating)
FROM ratings
where movie_id in (
    SELECT id
    FROM movies
    where year = 2012
);