"""
La instruccion para este ejercicio es:

* Escribir una función que calcule el total de una factura tras aplicarle el IVA.
* La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
    y devolver el total de la factura.
* Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""


def factura(valor, iva):
    total = round(valor + (valor * iva), 2)
    print(total)


valor = int(input('Ingresa el valor de la factura antes de impuestos. '))

iva = input('¿Cual es el valor de IVA aplicable? ')
if not iva.isdigit():
    iva = 0.21
elif int(iva) > 1:
    iva = int(iva)/100

factura(valor, iva)
