SELECT users.user_id AS u_user_id, dni.user_id AS d_user_id
FROM users
LEFT JOIN dni
ON users.user_id = dni.user_id
UNION
SELECT users.user_id AS u_user_id, dni.user_id AS d_user_id
FROM users
RIGHT JOIN dni
ON users.user_id = dni.user_id;



SELECT users.name, dni.dni_number
FROM users
LEFT JOIN dni
ON users.user_id = dni.user_id
UNION
SELECT users.name, dni.dni_number
FROM users
RIGHT JOIN dni
ON users.user_id = dni.user_id;