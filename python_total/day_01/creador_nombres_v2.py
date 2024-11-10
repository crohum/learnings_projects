"""
La instruccion para este ejercicio es:

* Crear un programa que pida dos o mas entradas de dato al usuario.
* Combinar esas palabras para formar un "nombre".
* Mostrarlo en pantalla en dos renglones, anteponiendo la frase "El nombre de tu producto es:"
  y continuando con el "nombre" generado por las entradas entre comillas.

Para esta mejora de ejercicio, he decidido remover las entradas libres del usuario, y en su lugar
hacerlo presionar una serie de 3 botones, los cuales, obtendran las partes del nombre de listas
predeterminadas.
En caso de no haber presionado todos los botones, el programa lo indicara.
El texto se mostrara en una caja de texto, respetando las instrucciones; y este a su vez se puede
limpiar con un boton especifico."""


import random
import tkinter
from tkinter import *


# listas de nombres
nombre_1 = ['Speedy', 'Great', 'Magic', 'Hungry', 'Fire', 'Scary', 'Incredible',
            'Fierce', 'Super', 'Mighty', 'Giant', 'Fast', 'Angry', 'Cold', 'Strong']
nombre_2 = ['Dragon', 'Chimera', 'Fairy', 'Monster', 'Goblin', 'Pegasus', 'Vampire',
            'Werewolf', 'Zombie', 'Gorgon', 'Demon', 'Hidra', 'Kraken', 'Troll', 'Ogre']
nombre_3 = ['Claw', 'Wing', 'Sword', 'Heart', 'Horn', 'Storm', 'Breath', 'Hurricane',
            'Tail', 'Bow', 'Shield', 'Crush', 'Spear', 'Wrath', 'Calamity']
poder = ''
criatura = ''
objeto = ''


# genera un nombre aleatorio
def nombre_power():
    global poder
    num = random.randint(0, 14)
    poder = nombre_1[num]
    var_power_text.set('Iniciando nombre')


def nombre_creature():
    global criatura
    num = random.randint(0, 14)
    criatura = nombre_2[num]
    var_creature_text.set('Combinando')


def nombre_item():
    global objeto
    num = random.randint(0, 14)
    objeto = nombre_3[num]
    var_item_text.set('Completando')


def generar_nombre():
    global poder, criatura, objeto
    texto_final.delete(1.0, END)
    if poder == '' or criatura == '' or objeto == '':
        texto_final.insert(END, '\n\n\n\nNecesitas presionar los tres botones'
                                '\npara obtener un nombre genial.')
    else:
        texto_final.insert(END, f'\n\n\n         El nombre para tu producto es:'
                                f'\n\n\t"{poder} {criatura} {objeto}"')


def limpiar():
    global poder, criatura, objeto
    texto_final.delete(1.0, END)
    poder = ''
    var_power_text.set('')
    criatura = ''
    var_creature_text.set('')
    objeto = ''
    var_item_text.set('')


# iniciar la ventana de la aplicacion
aplicacion = Tk()


# tamaño de la ventana
aplicacion.geometry('712x350')


# evitar maximizar
aplicacion.resizable(0, 0)


# titulo
aplicacion.title('Creador de Nombres')


# icono para la ventana
icono = tkinter.PhotoImage(file='icono.png')
aplicacion.iconphoto(True, icono)


# color de fondo de la ventana
aplicacion.config(bg='#2d572c')


# panel superior
panel_superior = Frame(aplicacion,
                       bd=3,
                       relief=FLAT)
panel_superior.pack(side=TOP)


# titulo del panel superior
etiqueta_titulo = Label(panel_superior,
                        text='Generador Fantastico de Nombres',
                        fg='white',
                        font=('Old London', 40),
                        bg='#274227',
                        width=25)
etiqueta_titulo.grid(row=0, column=0)


# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        bg='#2d572c',
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT)


# panel interior con indicaciones
panel_instrucciones = Frame(panel_izquierdo,
                            bd=1,
                            relief=FLAT)
panel_instrucciones.pack(side=TOP)


# indicaciones
indicaciones = Label(panel_instrucciones,
                     text='Presiona cada uno de los botones,\npara obtener un nombre genial.',
                     fg='gray',
                     font=('Baskerville Old Face', 16),
                     bg='#274227',
                     width=30)
indicaciones.grid(row=0, column=0)


# panel interior con botones
panel_botones = Frame(panel_izquierdo,
                      bd=1,
                      bg='#2d572c',
                      relief=FLAT)
panel_botones.pack(side=TOP)


# botones
botones = ['Power', 'Creature', 'Item']
boton_creado = []
filas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Book Antiqua', 14, 'bold'),
                   fg='black',
                   bg='azure4',
                   bd=4,
                   width=9)
    boton.grid(row=filas, column=0, padx=6, pady=5)
    boton_creado.append(boton)
    filas += 1


# botones inferiores
botones_abajo = ['LIMPIAR', 'GENERAR']
filas = 0
for boton in botones_abajo:
    boton = Button(panel_izquierdo,
                   text=boton.title(),
                   font=('Book Antiqua', 14, 'bold'),
                   fg='black',
                   bg='azure4',
                   bd=4,
                   width=9)
    boton.pack(side=RIGHT, padx=10)
    boton_creado.append(boton)
    filas += 1


# acciones de los botones
boton_creado[0].config(command=nombre_power)
boton_creado[1].config(command=nombre_creature)
boton_creado[2].config(command=nombre_item)
boton_creado[3].config(command=limpiar)
boton_creado[4].config(command=generar_nombre)


# cajas de texto
var_power_text = StringVar()
var_creature_text = StringVar()
var_item_text = StringVar()

power_text_box = Entry(panel_botones,
                       font=('Book Antiqua', 16, 'bold'),
                       bd=3,
                       bg='#c2c2c2',
                       width=19,
                       state='readonly',
                       textvariable=var_power_text)
power_text_box.grid(row=0, column=1, padx=8)

creature_text_box = Entry(panel_botones,
                          font=('Book Antiqua', 16, 'bold'),
                          bd=3,
                          bg='#c2c2c2',
                          width=19,
                          state='readonly',
                          textvariable=var_creature_text)
creature_text_box.grid(row=1, column=1, padx=8)

item_text_box = Entry(panel_botones,
                      font=('Book Antiqua', 16, 'bold'),
                      bd=3,
                      bg='#c2c2c2',
                      width=19,
                      state='readonly',
                      textvariable=var_item_text)
item_text_box.grid(row=2, column=1, padx=8)


# panel derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      bg='#2d572c',
                      relief=FLAT)
panel_derecho.pack(side=TOP)


# area de texto
texto_final = Text(panel_derecho,
                   font=('Dosis', 12, 'bold'),
                   bd=3,
                   width=35,
                   height=13)
texto_final.grid(row=0, column=0, padx=5, pady=5)


# evitar que la pantalla se cierre
aplicacion.mainloop()
