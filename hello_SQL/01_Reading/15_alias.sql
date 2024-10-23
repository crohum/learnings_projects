SELECT name, init_date AS 'Fecha de inicio en programación'
FROM users
WHERE age BETWEEN 20 AND 40;


SELECT CONCAT(name, ' ', surname) AS 'Nombre Completo'
FROM users;


SELECT CONCAT(name, ' ', surname) AS 'Nombre Completo'
FROM users
WHERE surname IS NOT NULL;
