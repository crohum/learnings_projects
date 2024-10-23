CREATE TRIGGER nombre
BEFORE/AFTER INSERT/UPDATE/DELETE
ON tabla
FOR EACH ROW
condiciones;


delimiter//
CREATE TRIGGER tg_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		INSERT INTO email_history (user_id, email)
        VALUES (user_id, OLD.email);
	END IF;
END//


DROP TRIGGER tg_email;
