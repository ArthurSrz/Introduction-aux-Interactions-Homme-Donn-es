-- SQLite
SELECT airports.name, cities.city, cities.country
    FROM airports
    JOIN cities ON airports.city_id = cities.id
    WHERE cities.city='London' AND cities.country='United Kingdom';


