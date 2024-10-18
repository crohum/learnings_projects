"""
La instruccion para este ejercicio es:

* Escribir una función a la que se le pase una cadena <nombre>
    y muestre por pantalla el saludo ¡hola <nombre>!.
"""


def saludo(nombre):
    print(f'¡Hola {nombre}!')


nombre = input('¿Cual es tu nombre?')
saludo(nombre)
