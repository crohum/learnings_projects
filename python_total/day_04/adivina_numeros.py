"""
La instruccion para este ejercicio es:

* Crear un programa que pregunte el nombre del jugador.
* Le dice al jugador que ha pensado un numero y el (el jugador) debe adivinar.
* El numero debe estar entre el 1 y 100.
* El jugador tiene hasta 8 intentos para adivinar.
* EL jugador dice un numero y el programa:
    - si es > 1 o < 100, dice que es un numero no permitido
    - si es "N" < "?", dice es incorrecto, que "?" es mas grande
    - si es "N" > "?", dice es incorrecto, que "?" es mas chico
* En cualquiera de esos casos, debe pedir otro numero, hasta que adivine o se acaben los intentos
* Si el jugador adivina "?", le avisa que gano y en cuantos intentos.
"""
from random import randint


nombre = input('¿Cual es tu nombre? ')

print(f'\nExcelente dia {nombre}, hoy jugaremos a adivinar el numero.\n\n'
      'Estoy pensando en un numero entero entre el 1 y el 100, incluidos estos,\n'
      'y tendras que adivinar en  menos de 8 intentos  de que numero se  trata.\n'
      'Suena interesante verdad, vamos a ello.\n')


respuesta = 's'

while respuesta == 's':
    secreto = randint(1, 101)
    adivinado = False
    intentos = 0

    while not adivinado:
        if intentos >= 8:
            print(f'\nLo siento {nombre}, te has quedado sin intentos'
                  f'\nEl numero secreto era {secreto}')
            break

        numero = int(input('\n¿Cual crees que es el numero? '))

        if numero < 1 or numero > 100:
            print('Ese numero no es valido, debe ser entre 1 y 100, incluidos')
        elif numero < secreto:
            print(f'El numero secreto es mayor a {numero}')
            intentos += 1
        elif numero > secreto:
            print(f'El numero secreto es menor a {numero}')
            intentos += 1
        elif numero == secreto:
            adivinado = True
            print(f'Felicidades {nombre},'
                  f'\nel numero secreto era {secreto}'
                  f'\ny lo has descubierto en {intentos} intentos')

    respuesta = input('\nEl juego ha terminado, ¿lo quieres volver a intentar? S/N ').lower()
else:
    print(f'\nGracias por jugar {nombre}')
