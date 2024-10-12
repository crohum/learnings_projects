"""
La instruccion para este ejercicio es:

* Crear un directorio de carpetas con las recetas.
* El programa debe dar la bienvenida al usuario.
* Informar la ruta de acceso a la directorio.
* Informar cuantas recetas hay disponibles en total.
* Desplegar un menu de opciones:
    [1] leer receta
    [2] crear receta
    [3] crear categoria
    [4] eliminar receta
    [5] eliminar categoria
    [6] finalizar programa
* El programa debe ejecutar la instruccion elegida.
* No debe cerrarse hasta que se elija la opcion finalizar.
* Debe limpiar la pantalla despues de cada interaccion completa.
"""
from os import system
from pathlib import Path


ruta_base = Path('D:/Ejercicios Python/pythonProject/curso_python_total/Recetas')

saludo = Path(ruta_base, 'saludo.txt')
print(saludo.read_text())
print(f'Te recuerdo que puedes encontrar las recetas en:\n"{ruta_base}"')

n_recetas = -1

for txt in Path(ruta_base).glob('**/*.txt'):
    n_recetas +=1
print(f'Actualmente tienes {n_recetas} recetas disponibles.')
input('Presiona enter para entrar al menu.')


# FUNCIONES
def crear_categoria():
    categ_lista = []
    categ_ruta = [c for c in ruta_base.iterdir() if c.is_dir()]
    for c in categ_ruta:
        categ_lista.append(str(c.name).lower())
    categ_nva = input('\nEscribe la nueva CATEGORIA: ').lower()
    if categ_nva in categ_lista:
        print('Esa categoria ya existe')
    else:
        categ_creada = Path(ruta_base,categ_nva)
        categ_creada.mkdir()


# def crear_contenido(receta_creada):
def crear_receta(categoria):
    receta_lista = []
    ruta_nva = Path(ruta_base, categoria)
    receta_ruta = [r for r in ruta_nva.iterdir() if r.is_file()]
    for r in receta_ruta:
        receta_lista.append(str(r.stem).lower())
    receta_nva = input('\nEscribe el nombre de la nueva RECETA: ').lower()
    if receta_nva in receta_lista:
        print('Esa receta ya existe')
    else:
        receta_creada = Path(ruta_base, categoria, receta_nva+'.txt')
        receta_creada.touch()


def elegir_categoria():
    correcto = False
    while correcto == False:
        categ_ruta = [c for c in ruta_base.iterdir() if c.is_dir()]
        print('\nElige una de las siguientes Categorias:\n**********')
        categ_lista = []
        for c in categ_ruta:
            categ_lista.append(str(c.name).lower())
            print(c.name)
        categoria = input('**********\nCategoria: ').lower()
        if categoria in categ_lista:
            correcto = True
            return categoria
        else:
            continue


def elegir_receta(categoria):
    correcto = False
    while correcto == False:
        ruta_nva = Path(ruta_base,categoria)
        receta_ruta = [r for r in ruta_nva.iterdir() if r.is_file()]
        print('\nElige una de las siguientes Recetas:\n**********')
        receta_lista = []
        for r in receta_ruta:
            receta_lista.append(str(r.stem).lower())
            print(r.stem)
        receta = input('**********\nReceta: ').lower()
        if receta in receta_lista:
            correcto = True
            return receta
        else:
            continue


def eliminar_categoria(categoria):
    ruta_nva = Path(ruta_base, categoria)
    confirmacion = input(f'Se eliminara la categoria {categoria.upper()} y todas las recetas que contenga.'
                         f'\nEsta accion no se puede deshacer, ¿deseas continuar? S/N: ').lower()
    if confirmacion == 's':
        ruta_nva.rmdir()
        print('Ha sido eliminada con exito.')


def eliminar_receta(categoria,receta):
    receta_ext = str(receta) + '.txt'
    archivo = Path(ruta_base, categoria, receta_ext)
    confirmacion = input(f'Se eliminara la receta {receta.upper()}.'
                         f'\nEsta accion no se puede deshacer, ¿deseas continuar? S/N: ').lower()
    if confirmacion == 's':
        archivo.unlink()
        print('Ha sido eliminada con exito.')


def mostrar_contenido(categoria,receta):
    receta_ext = str(receta)+'.txt'
    archivo = Path(ruta_base,categoria,receta_ext)
    print('\n----------------------------')
    print(archivo.read_text())
    input('\npresiona enter para regresar al menu')


# MENU*
en_linea = True
while en_linea == True:
    system('cls')
    menu = Path(ruta_base,'menu.txt')
    opcion = input(menu.read_text()).lower()
    if opcion == '1' or opcion == 'leer':
        categoria = elegir_categoria()
        receta = elegir_receta(categoria)
        mostrar_contenido(categoria,receta)
    elif opcion == '2' or opcion == 'crear':
        categoria = elegir_categoria()
        receta_creada = crear_receta(categoria)
        # crear_contenido(receta_creada)
    elif opcion == '3' or opcion == 'nueva':
        crear_categoria()
    elif opcion == '4' or opcion == 'borrar':
        confirmacion = input('Esta accion no se puede deshacer,'
                             '\n¿realmente quieres borrar una receta? S/N: ').lower()
        if confirmacion == 's':
            categoria = elegir_categoria()
            receta = elegir_receta(categoria)
            eliminar_receta(categoria,receta)
        else:
            break
    elif opcion == '5' or opcion == 'eliminar':
        confirmacion = input('Esta accion no se puede deshacer,'
                             '\ntodas las recetas dentro de esta categoria seran borradas'
                             '\n¿Realmente quieres eliminar la categoria? S/N: ').lower()
        if confirmacion == 's':
            categoria = elegir_categoria()
            eliminar_categoria(categoria)
        else:
            break
    elif opcion == '6' or opcion == 'salir':
        print('\nGracias por usar este programa y buen provecho.')
        en_linea = False
    else:
        break
