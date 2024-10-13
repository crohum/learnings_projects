"""
La instruccion para este ejercicio es:

* Crear un programa que solicite al usuario ingresar un texto cualquiera.
* Debe pedir 3 letras a su eleccion.
* El programa tiene que analizar el texto y devolver en pantalla:
    - Cuantas veces aparece cada letra.
    - Cuantas palabras hay en el texto.
    - Informar cual es la primera y ultima letra del texto, asi como en que palabras aparecen.
    - Mostrar el texto de forma invertida.
    - Decir si la palabra "Python" aparece en el texto.
"""


# El usuario ingresa un texto cualquiera
print('Por favor ingresa un texto para analizar y presiona "enter" al final: ')
texto = input().lower()


# Cuantas palabras hay en total en el texto
caracteres = len(texto)

primer_c = texto[0]
ultimo_c = texto[-1]

todas_palabras = list(texto.split(' '))
palabras = len(todas_palabras)

primer_p = todas_palabras[0]
ultima_p = todas_palabras[-1]

print(f'\nEn este texto hay {palabras} palabras, '
      f'en un total de {caracteres} caracteres, contando espacios;')

print(f'Siendo la letra "{primer_c}" la primera, que aparece en "{primer_p}" '
      f'\ny "{ultimo_c}" la ultima en aparecer, y lo hace en la palabra"{ultima_p}"')


# Se solicitan 3 letras
print('\nAhora contaremos cuantas letras hay de 3 de ellas que nos indiques ^_^!')

print('¿Cual letra quieres que contemos en primer lugar?')

letra1 = input().lower()
print('¿Cual sera la segunda letra que quieres que contemos?')

letra2 = input().lower()
print('¿Y la tercer letra que contaremos?')

letra3 = input().lower()


# Cuantas veces aparece cada una de las letras indicadas
num_letra1 = texto.count(letra1)
num_letra2 = texto.count(letra2)
num_letra3 = texto.count(letra3)

print(f'\nHemos encontrado que hay:'
      f'\n {num_letra1} letras "{letra1}"'
      f'\n {num_letra2} letras "{letra2}"'
      f'\n {num_letra3} letras "{letra3}"')


# Indica si aparece la palabra python
aparicion = {'True': '\nLa palabra Python aparece al menos una vez en el escrito',
             'False': 'La palabra Python no aparece en el texto.'}

clave = str(bool('python' in texto))

print(aparicion[clave])
print(input('\npresiona "enter" para ver tu texto invertido y en modo espejo.\n'))


# Texto ordenado al reves
todas_palabras.reverse()
print('INVERTIDO')
print(' '.join(todas_palabras))


# Muestra el texto en orden inverso
print('\nESPEJO')
print(texto[::-1])
