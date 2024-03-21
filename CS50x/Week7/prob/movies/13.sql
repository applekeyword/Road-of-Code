SELECT DISTINCT name
FROM people
JOIN stars ON people.id = stars.person_id
where movie_id IN (
    SELECT movie_id
    FROM stars
    JOIN people ON stars.person_id = people.id
    where name = 'Kevin Bacon'
    AND birth = 1958
)
AND name != 'Kevin Bacon';