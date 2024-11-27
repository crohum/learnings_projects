"""
La instruccion para este ejercicio es:

* Crear un programa que haga la funcion de un turnero de una farmacia.
* El programa debe preguntar el area a la cual va el usuario:
    - Perfumeria
    - Cosmeticos
    - Farmacia (Medicamentos)
    - Atencion Medica (Esta area yo la agrege adicional a las solicitdas)
* El programa debe imprimir un turno con formato: "X-00" donde la letra corresponde
    a el area a visitar, y el numero consecutivo de cada letra.

Se mejora agregando un comando "secreto": (salir), para que el admon de la farmacia
    pueda cerrar el programa al fin del dia.
"""
from gen_numeros import *
from pathlib import Path


def seleccion():
    menu = input('\n¿Que area deseas visitar?: ').lower()
    try:
        menu = int(menu)
        if menu == 1:
            return num_atn
        elif menu == 2:
            return num_med
        elif menu == 3:
            return num_prf
        elif menu == 4:
            return num_cos
        else:
            print('\nElige entre una de las opciones disponibles.\n')
            return 'No valido'
    except:
        if menu == 'salir':
            salir = True
            print('\nHas salido del programa.\n')
            return salir
        else:
            print('\nPor favor, Ingresa una opcion valida.\n')
            return 'No valido'


en_linea = False
while not en_linea:
    ruta_base = Path('D:/Proyectos Python/Zzz_learnings_projects/python_total/day_08')
    saludo = Path(ruta_base, 'turnero.txt')
    print(saludo.read_text())
    opcion = seleccion()
    # si quitamos el comparativo a True, el programa falla
    if opcion == True:
        en_linea = opcion
        break
    elif opcion == 'No valido':
        continue
    else:
        texto(opcion)
