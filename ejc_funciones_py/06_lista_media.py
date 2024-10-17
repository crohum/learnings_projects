"""
La instruccion para este ejercicio es:

* Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""


def media(lista):
    contador = 0
    suma = 0
    for l in lista:
        suma += l
        contador += 1

    resultado = round(suma/contador, 2)
    return resultado


mi_lista = []
print('Ingresa una serie de numeros, de uno en uno,'
      'para obtener su promedio')

valor = '0'
while valor.isdigit():
    valor = input('Ingresa un numero o deja vacio para terminar: ')
    if valor.isdigit():
        mi_lista.append(int(valor))

print(media(mi_lista))
