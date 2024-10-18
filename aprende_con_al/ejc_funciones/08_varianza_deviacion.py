"""
La instruccion para este ejercicio es:

* Escribir una función que reciba una muestra de números en una lista
    y devuelva un diccionario con su media, varianza y desviación típica.
"""
import statistics


def operaciones(mi_lista):
    promedio = round(statistics.mean(mi_lista), 2)
    varianza = round(statistics.variance(mi_lista), 2)
    desviacion = round(statistics.stdev(mi_lista), 2)
    resultado = {'Promedio': promedio, 'Varianza': varianza, 'Desviacion': desviacion}
    return resultado


mi_lista = []
valor = '0'
while valor.isdigit():
    valor = input('Ingresa un numero o deja vacio para terminar: ')
    if valor.isdigit():
        mi_lista.append(int(valor))

print(f'\nDatos : {mi_lista}')
print(operaciones(mi_lista))
