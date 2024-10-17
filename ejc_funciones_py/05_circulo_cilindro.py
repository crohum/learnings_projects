"""
La instruccion para este ejercicio es:

* Escribir una función que calcule el área de un círculo
* y otra que calcule el volumen de un cilindro usando la primera función.
"""
import math


def circulo(r):
    a_circulo = math.pi * r**2
    return a_circulo


def cilindro(a_circulo, h):
    a_cilindro = round((2 * math.pi * h) + (2 * a_circulo), 2)
    return a_cilindro


r = int(input('Ingresa el Radio de la base del cilindro en cm: '))
h = int(input('Ingresa la altura del cilindro en cm: '))

base = circulo(r)
print(f'{cilindro(base, h)} cm^2')
