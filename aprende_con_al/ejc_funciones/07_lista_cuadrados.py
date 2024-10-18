"""
La instruccion para este ejercicio es:

* Escribir una función que reciba una muestra de números en una lista
    y devuelva otra lista con sus cuadrados.
"""


def cuadrados(mi_lista):
    lista_cuadra2 = []
    for l in mi_lista:
        lista_cuadra2.append(l**2)
    return lista_cuadra2


mi_lista = []
valor = '0'
while valor.isdigit():
    valor = input('Ingresa un numero o deja vacio para terminar: ')
    if valor.isdigit():
        mi_lista.append(int(valor))


print(cuadrados(mi_lista))
