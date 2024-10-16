SELECT * 
FROM users 
WHERE NOT email = 'sara@correo.com';


SELECT *
FROM users 
WHERE NOT email = 'sara@correo.com' AND age= 15;


SELECT * 
FROM users 
WHERE NOT email = 'sara@correo.com' OR age= 15;
