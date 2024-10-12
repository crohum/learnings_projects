"""
La instruccion para este ejercicio es:

* Crear un programa que pida dos entradas de dato al usuario,
    - una es su nombre, y la otra
    - una cantidad.
* El programa debe de calcular el 13% de la cantidad ingresada, redondeado a 2 decimas.
* Mostrarlo en pantalla, usando una frase similar a "Felicidades "NOMBRE", tus comisiones de este mes
  son: $CANTIDAD CALCULADA"
"""


print('Excelente dia.'
      '\nPara conocer tu monto obtenido por la comision correspondiente a tus ventas,'
      '\nsigue los siguentes pasos:')

nombre = input('\n¿Cual es tu nombre? ')
cantidad = round(float(input('\n¿Cual es el monto total de tus ventas de este mes? ')) * 13/100, 2)

print(f'\n\n¡Buen trabajo {nombre}!'
      f'\nEste mes ganaste ${cantidad} MN')
