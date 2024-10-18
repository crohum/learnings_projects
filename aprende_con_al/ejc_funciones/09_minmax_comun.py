"""
La instruccion para este ejercicio es:

* Escribir una función que calcule el máximo común divisor de dos números
    y otra que calcule el mínimo común múltiplo.
"""
import math


def con_funciones(*args):
    maximo = math.gcd(*args)
    minimo = math.lcm(*args)
    return maximo, minimo


mi_lista = []
valor = '0'
while valor.isdigit():
    valor = input('Ingresa un numero o deja vacio para terminar: ')
    if valor.isdigit():
        mi_lista.append(int(valor))

max_cmn_div, min_cmn_mul = con_funciones(*mi_lista)
print(f'\n\nDatos: {mi_lista}'
      f'\nMaximo Comun Divisor:  {max_cmn_div}'
      f'\nMinimo Comun Multiplo: {min_cmn_mul}')
