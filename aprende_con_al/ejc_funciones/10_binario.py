"""
La instruccion para este ejercicio es:

* Escribir una función que convierta un número decimal en binario
    y otra que convierta un número binario en decimal.
"""


def a_binario():
    numero = ''
    binario = []
    while not numero.isdigit():
        numero = input('Ingresa el numero entero positivo'
                       '\nque quieres convertir en binario: ')
    numero2 = int(numero)
    while numero2 > 0:
        if numero2 % 2 == 0:
            binario.append(0)
        else:
            binario.append(1)
        numero2 = round(numero2 / 2)
    binario = binario[::-1]
    binario = ''.join(map(str, binario))
    print(f'\n{numero} en binario es:'
          f'\n"{binario}"')


a_binario()


def a_decimal():
    numero = input('Ingresa el numero en binario (0´s y 1´s)'
                   '\nque deseas convertir: ')
    numero = list(numero)
    numero = numero[::-1]
    contador = 0
    suma = 0
    mostrar = True
    for n in numero:
        if n != '0' and n != '1':
            print('El numero ingresado solo puede contener 1´s y 0´s')
            mostrar = False
            break
        else:
            suma += int(n)*(2**contador)
            contador += 1
    if mostrar:
        print(suma)


a_decimal()
