CREATE INDEX idx_name
ON users (name);


CREATE INDEX idx_name_surname
ON users (name, surname);


CREATE UNIQUE INDEX idx_name
ON users (name);


DROP INDEX idx_name;