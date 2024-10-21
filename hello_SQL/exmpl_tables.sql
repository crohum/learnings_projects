-- Tabla inicial USERS

CREATE TABLE users (
    'user_id' int NOT NULL AUTO_INCREMENT,
    'name' varchar(50) NOT NULL,
    'surname' varchar(50) DEFAULT NULL,
    'age' int DEFAULT NULL,
    'init_date' date DEFAULT NULL,
    'email' varchar(100) DEFAULT NULL,
    PRIMARY KEY (`user_id`)
);
