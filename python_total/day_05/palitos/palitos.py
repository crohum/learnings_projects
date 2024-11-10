"""
La instruccion para este ejercicio es:

* Crear un programa/juego que mezcle 4 palitos de diferentes tamaños.
* Pedir al usuario elegir uno de ellos.
    - Si le toca el mas pequeño, debera mandarlo a lavar los platos.
    - Si le toca cualquier otro, debe decirle "te has salvado".
* En cualquier caso, debe mostrar cual palito ha sacado
"""
from random import shuffle


# Mezclar los palitos cada vez
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento a jugador
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4 ')
    return int(intento)


# Ver que palito le ha salido
def chequea_intento(lista, intento):
    if lista[intento - 1] == '_':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')
    print(f'Te ha salido {lista[intento -1]}')


# lista inicial de palitos
palitos = ['_', '__', '___', '____']

palitos_mezclados = mezclar(palitos)

seleccion = probar_suerte()

chequea_intento(palitos_mezclados, seleccion)
