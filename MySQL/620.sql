select id, movie, description, rating
FROM cinema
Where id % 2 = 1 and description <>"boring"
order by rating DESC;