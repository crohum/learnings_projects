import mysql.connector

config = {
    "host": "127.0.0.1",
    "port": "3306",
    "database": "hello_mysql",
    "user": "root",
    "password": "root*125"
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

query = "SELECT * FROM users"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

#cursor.close()
#connection.close()


# Utilizando una funcion para mantener la base de datos mas segura.
def print_user(usuario):
    query = "SELECT * FROM users WHERE name=%s;"
    print(query)

    cursor.execute(query, (usuario,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


print_user('Alex')
