-- Relacion de tablas R[1 : 1]

create table dni(
    dni_id int AUTO_INCREMENT PRIMARY KEY,
    dni_number int NOT NULL,
    user_id int,
    UNIQUE(user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- Relacion de tablas R[1 : N]

CREATE TABLE companies(
    company_id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

ALTER TABLE users
ADD company_id varchar(100);

ALTER TABLE users
ADD CONSTRAINT fk_companies
FOREIGN KEY (company_id) REFERENCES companies(company_id);


-- Relacion de tablas R[N : M]

CREATE TABLE languages(
    language_id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE users_languages(
    users_languages_id int AUTO_INCREMENT PRIMARY KEY,
    user_id int,
    language_id int,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (language_id) REFERENCES languages(language_id),
    UNIQUE (user_id, language_id)
);
