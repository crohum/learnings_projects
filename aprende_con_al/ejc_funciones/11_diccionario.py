"""
La instruccion para este ejercicio es:

* Escribir un programa que reciba una cadena de caracteres
    y devuelva un diccionario con cada palabra que contiene y su frecuencia.
* Escribir otra función que reciba el diccionario generado con la función anterior
    y devuelva una tupla con la palabra más repetida y su frecuencia.
"""


def conteo_palabras(texto):
    # Se separan las palabras en una lista y se ordenan
    todas_palabras = list(texto.split(' '))
    todas_palabras.sort()

    # Conteo de palabras totales
    palabras = len(todas_palabras)

    # Mapeo y zippeo de la lista
    mapeo = map(lambda p: todas_palabras.count(p), todas_palabras)
    zipeo = zip(todas_palabras, mapeo)

    # creacion del diccionario
    mi_diccionario = dict(zipeo)
    return mi_diccionario


def mas_repetida(mi_dic):
    mayor = max(mi_dic.items())
    print(mayor)


# El usuario ingresa un texto cualquiera
print('Por favor ingresa un texto para analizar y presiona "enter" al final: ')
texto = input().lower()


mi_dic = conteo_palabras(texto)

mas_repetida(mi_dic)
