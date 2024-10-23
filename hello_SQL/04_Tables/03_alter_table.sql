-- Modificar ADD

ALTER TABLE personas8
ADD surname varchar(150);


-- Modificar RENAME COLUMN

ALTER TABLE personas8
RENAME column surname to descripcion;


-- Modificar MODIFY COLUMN

ALTER TABLE personas8
MODIFY column descripcion varchar(250);


-- Modificar DROP

ALTER TABLE personas8
DROP column descripcion;
