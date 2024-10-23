SELECT users.name, dni.dni_number
FROM users
LEFT JOIN dni
ON users.user_id = dni.user_id;


SELECT users.name, dni.dni_number
FROM dni
LEFT JOIN users
ON users.user_id = dni.user_id;


-- con tablas intermedias

SELECT users.name, languages.name
FROM users
LEFT JOIN users_languages ON users_languages.user_id = users.user_id
LEFT JOIN languages ON users_languages.language_id = languages.language_id;
