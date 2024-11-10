"""
La instruccion para este ejercicio es:

* Crear un programa que pida dos entradas de dato al usuario, una es su nombre y la otra una cantidad.
* El programa debe de calcular el 13% de la cantidad ingresada, redondeado a 2 decimas.
* Mostrarlo en pantalla, usando una frase similar a "Felicidades "NOMBRE", tus comisiones de este mes
  son: $CANTIDAD CALCULADA".

Para esta mejora de ejercicio, he decidido colocar un boton para generar el calculo una vez se llenen
los dos campos solicitados, agregando un contron de errores en caso de omitirlos.
El texto se mostrara en una caja de texto, respetando las instrucciones; y este a su vez se puede
limpiar con un boton especifico."""


import tkinter
from tkinter import *
import datetime


def imprimir(ventas, nombre):
    comision = round((ventas * 13) / 100, 2)
    texto_final.delete(1.0, END)
    fecha = datetime.datetime.now()
    fecha_acomodada = f'{fecha.day}/{fecha.month}/{fecha.year}'
    texto_final.insert(END, f'\t      {fecha_acomodada}\n\n'
                       + ('*' * 24)
                       + f'\n¡Felicidades {nombre}!'
                         f'\n\nTu comision calculada al'
                         f'dia de hoy, es de:'
                         f'\n\n${comision} M.N.\n\n'
                       + ('*' * 24))


def calcular(nombre):
    global var_ventas
    try:
        ventas = float(var_ventas.get())
        if ventas < 0:
            texto_final.delete(1.0, END)
            texto_final.insert(END, f'\n\n{"*" * 24}'
                                    f'\nEl valor de ventas'
                                    f'\nno puede ser negativo.'
                                    f'\nPor favor intentalo de'
                                    f'\nnuevo.'
                                    f'\n\n{"*" * 24}')
        else:
            imprimir(ventas, nombre)
    except ValueError:
        texto_final.delete(1.0, END)
        texto_final.insert(END, f'\n\n{"*" * 24}'
                                f'\n\nEl valor de ventas solo puede llevar numeros.'
                                f'\nPor favor intentalo de'
                                f'\nnuevo.'
                                f'\n\n{"*" * 24}')


def verificar_nombre():
    global var_nombre
    try:
        lista_nombre = var_nombre.get().split()
        nombre = lista_nombre[0]
        calcular(nombre)
    except IndexError:
        texto_final.delete(1.0, END)
        texto_final.insert(END, f'\n\n{"*" * 24}'
                                f'\n\n Debes de  ingresar tu'
                                f'\n nombre antes de poder'
                                f'\n continuar.'
                                f'\n\n\n{"*" * 24}')


def limpiar():
    texto_final.delete(1.0, END)
    var_nombre.set('')
    var_ventas.set('')


# iniciar tkinter
aplicacion = Tk()


# tamaño de la ventana
aplicacion.geometry('610x350')
aplicacion.resizable(0, 0)


# titulo
aplicacion.title('Calculador de Comisiones')


# icono para la ventana
icono = tkinter.PhotoImage(file='icono.png')
aplicacion.iconphoto(True, icono)


# color de fondo de la ventana
aplicacion.config(bg='royalblue')


# panel superior
panel_superior = Frame(aplicacion,
                       bd=1,
                       relief=FLAT)
panel_superior.pack(side=TOP, pady=5)


# etiqueta del titulo
etiqueta_titulo = Label(panel_superior,
                        text='Sistema de Comisiones',
                        fg='azure4',
                        font=('Lucida Console', 26, 'bold'),
                        bg='navy',
                        width=27)
etiqueta_titulo.grid(row=0, column=0)


# panel medio
panel_medio = Frame(aplicacion,
                    bd=1,
                    relief=FLAT)
panel_medio.pack(side=TOP)


# instrucciones
instrucciones = Label(panel_medio,
                      text='Excelente dia,\n'
                           'para conocer el monto obtenido por la comision\n'
                           'correspondiente a tus ventas de este mes.\n'
                           'Por favor ingresa los datos que se piden.',
                      fg='azure4',
                      font=('Lucida Console', 12,),
                      bg='navy',
                      width=59)
instrucciones.grid(row=0, column=0)


# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        bg='navy',
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT, padx=5)


# datos
var_nombre = StringVar()
var_ventas = StringVar()


# panel entradas
panel_entradas = Frame(panel_izquierdo,
                       bd=1,
                       bg='navy',
                       relief=FLAT)
panel_entradas.pack(side=TOP)


etiqueta_nombre = Label(panel_entradas,
                        text='Nombre Completo:',
                        font=('Lucida Console', 12, 'bold'),
                        fg='azure4',
                        bg='navy')
etiqueta_nombre.grid(row=0, column=0, pady=5)


texto_nombre = Entry(panel_entradas,
                     font=('Lucida Console', 12, 'bold'),
                     bd=1,
                     width=25,
                     textvariable=var_nombre)
texto_nombre.grid(row=1, column=0, padx=10, pady=10)


etiqueta_ventas = Label(panel_entradas,
                        text='Ventas durante el mes:',
                        font=('Lucida Console', 12, 'bold'),
                        fg='azure4',
                        bg='navy')
etiqueta_ventas.grid(row=2, column=0, pady=5)


texto_ventas = Entry(panel_entradas,
                     font=('Lucida Console', 12, 'bold'),
                     bd=1,
                     width=25,
                     textvariable=var_ventas)
texto_ventas.grid(row=3, column=0, padx=10, pady=10)


# panel botones
panel_botones = Frame(panel_izquierdo,
                      bd=1,
                      bg='navy',
                      relief=FLAT)
panel_botones.pack(side=BOTTOM)


# botones
botones = ['LIMPIAR', 'CALCULAR']
boton_creado = []
filas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Arial', 14, 'bold'),
                   fg='black',
                   bg='azure4',
                   bd=4,
                   width=9)
    boton.pack(side=RIGHT, padx=10, pady=10)
    boton_creado.append(boton)
    filas += 1


# acciones de los botones
boton_creado[0].config(command=limpiar)
boton_creado[1].config(command=verificar_nombre)


# panel derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      bg='navy',
                      relief=FLAT)
panel_derecho.pack(side=LEFT, padx=5)


# area de texto
texto_final = Text(panel_derecho,
                   font=('Lucida Console', 12, 'bold'),
                   bd=3,
                   width=24,
                   height=12)
texto_final.grid(row=0, column=0, padx=5, pady=5)


# evitar que la pantalla se cierre
aplicacion.mainloop()
