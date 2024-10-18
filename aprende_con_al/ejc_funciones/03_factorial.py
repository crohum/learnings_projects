"""
La instruccion para este ejercicio es:

* Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""


def factorial(numero):
    contador = numero
    num_factorial = numero

    while contador > 2:
        contador -= 1
        num_factorial = num_factorial * contador

    return num_factorial


resultado = factorial(int(input('Escribe un numero para obtener su factorial. ')))
print(resultado)
