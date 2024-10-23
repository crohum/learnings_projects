SELECT * FROM users
INNER JOIN dni
ON users.user_id = dni.user_id;


-- Se puede usar solo con JOIN

SELECT * FROM users
JOIN dni
ON users.user_id = dni.user_id;


-- Mezclando con otros comandos

SELECT name, age, dni_number FROM users
JOIN dni
ON users.user_id = dni.user_id
ORDER BY age ASC;


-- Con tablas intermedias 1:N

SELECT users.name, languages.name
FROM users
JOIN users_languages ON users_languages.user_id = users.user_id
JOIN languages ON users_languages.language_id = languages.language_id;