CREATE TABLE personas (
	id int,
    name varchar(100),
    age int,
    email varchar(50),
    created date
);


-- Resticcion NOT NULL

CREATE TABLE personas2 (
	id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar(50),
    created date
);


-- Restriccion UNIQUE

CREATE TABLE personas3 (
	id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar(50),
    created datetime,
    UNIQUE (id)
);


-- Restriccion PRIMARY KEY

CREATE TABLE personas4 (
	id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar(50),
    created datetime,
    PRIMARY KEY (id),
    UNIQUE (id)
);


-- Restriccion CHECK

CREATE TABLE personas5 (
	id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar(50),
    created datetime,
    PRIMARY KEY (id),
    UNIQUE (id),
    CHECK (age >= 18)
);


-- Restriccion DEFAULT

CREATE TABLE personas6 (
	id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar(50) DEFAULT 'correo@server.com',
    created datetime DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (id),
    UNIQUE (id),
    CHECK (age >= 18)
);


-- Restriccion INCREMENT

CREATE TABLE personas7 (
	id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    age int,
    email varchar(50),
    created datetime DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (id),
    UNIQUE (id),
    CHECK (age >= 18)
);
