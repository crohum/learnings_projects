delimiter //
CREATE PROCEDURE p_all_users()
BEGIN
	SELECT *
	FROM users;
END //


CALL p_all_users();


DROP PROCEDURE p_all_users;


delimiter //
CREATE PROCEDURE p_age_users(IN age_search int)
BEGIN
	SELECT *
	FROM users WHERE age = age_search;
END //


CALL p_age_users(20);
