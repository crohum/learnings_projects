"""
La instruccion para este ejercicio es:

* Crear un programa que permita gestionar el consumo en un restaurant.
* Debe permitir ingresar cuantos platillos se pidieron de cada cosa
* Dar un subtotal por cada categoria
    - Platillos
    - Bebidas
    - Postres
* Debe calcular el total, con y sin impuestos.
* Finalmente tiene que imprimir el ticket de consumo
* Adicional, debe tener una calculadora funcional
"""

import random
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime


# variable que almacena y da vida al visor de la calculadora
operador = ''


# hace funcional la calculadora
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# hace funcional el boton borrar de la calculadora
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


# hace funcionar el total
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


# revisa la palomita para permitir o no escribir cantidades
def revisar_check():
    indice = 0
    for c in cuadros_comida:
        if variables_comida[indice].get() == 1:
            cuadros_comida[indice].config(state=NORMAL)
            if cuadros_comida[indice].get() == '0':
                cuadros_comida[indice].delete(0, END)
            cuadros_comida[indice].focus()
        else:
            cuadros_comida[indice].config(state=DISABLED)
            texto_comida[indice].set('0')
        indice += 1

    indice = 0
    for c in cuadros_bebida:
        if variables_bebida[indice].get() == 1:
            cuadros_bebida[indice].config(state=NORMAL)
            if cuadros_bebida[indice].get() == '0':
                cuadros_bebida[indice].delete(0, END)
            cuadros_bebida[indice].focus()
        else:
            cuadros_bebida[indice].config(state=DISABLED)
            texto_bebida[indice].set('0')
        indice += 1

    indice = 0
    for c in cuadros_postre:
        if variables_postre[indice].get() == 1:
            cuadros_postre[indice].config(state=NORMAL)
            if cuadros_postre[indice].get() == '0':
                cuadros_postre[indice].delete(0, END)
            cuadros_postre[indice].focus()
        else:
            cuadros_postre[indice].config(state=DISABLED)
            texto_postre[indice].set('0')
        indice += 1


# saca la suma de todos los items consumidos mas impuestos
def total():
    subtotal_comida = 0
    subtotal_bebida = 0
    subtotal_postre = 0

    indice_comida = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + float(cantidad.get()) * precios_comidas[indice_comida]
        indice_comida += 1

    indice_bebida = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + float(cantidad.get()) * precios_bebidas[indice_bebida]
        indice_bebida += 1

    indice_postre = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + float(cantidad.get()) * precios_postres[indice_postre]
        indice_postre += 1

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = subtotal * 0.15
    total_cuenta = subtotal + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total_cuenta, 2)}')


# crea el recibo o ticket
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'Ticket:#{random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'   {fecha_recibo}\t\t\t     {num_recibo}'
                             f'\n' + ('*' * 63) + ''
                             f'\n\t      RESTAURANT PYTHON'
                             f'\n     Calle del Programador #42, Ciudad, Pais'
                             f'\n' + ('*' * 63) + ''
                             f'\n     Items:\t\tCant.\t\tCosto:'
                             f'\n     -' + ('-'*63) + '')
    contador_comida = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'\n     {lista_comidas[contador_comida]}\t'
                                     f'\t    {comida.get()}\t'
                                     f'\t${round(int(comida.get()) * precios_comidas[contador_comida], 2)}')
        contador_comida += 1

    contador_bebida = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'\n     {lista_bebidas[contador_bebida]}\t'
                                     f'\t    {bebida.get()}\t'
                                     f'\t${round(int(bebida.get()) * precios_bebidas[contador_bebida], 2)}')
        contador_bebida += 1

    contador_postre = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'\n     {lista_postres[contador_postre]}\t'
                                     f'\t    {postre.get()}\t'
                                     f'\t${round(int(postre.get()) * precios_postres[contador_postre], 2)}')
        contador_postre += 1

    texto_recibo.insert(END, f'\n     -' + ('-'*63) + ''
                             f'\n     Costo Comidas:\t\t\t{var_costo_comida.get()}'
                             f'\n     Costo Bebidas:\t\t\t{var_costo_bebida.get()}'
                             f'\n     Costo Postres:\t\t\t{var_costo_postre.get()}'
                             f'\n     -' + ('-' * 63) + ''
                             f'\n     Subtotal:\t\t\t{var_subtotal.get()}'
                             f'\n     Impuestos:\t\t\t{var_impuestos.get()}\n'
                             f'\n     TOTAL:\t\t\t{var_total.get()}'
                             f'\n' + ('*' * 63) + ''
                             f'\n\t     ¡ MUCHAS GRACIAS !\n\t    Los esperamos pronto.')


# guarda el ticket para imprimir o enviar por correo
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


# borra la consola para poder recibir un nuevo cliente
def reiniciar():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for v in variables_comida:
        v.set(0)
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    var_costo_comida.set('')

    for texto in texto_bebida:
        texto.set('0')
    for v in variables_bebida:
        v.set(0)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    var_costo_bebida.set('')

    for texto in texto_postre:
        texto.set('0')
    for v in variables_postre:
        v.set(0)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
    var_costo_postre.set('')

    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter (aplicacion es variable, el nombre de la ventana [podria llamarse facturacion])
aplicacion = Tk()


# tamaño de la ventana
aplicacion.geometry('1145x560+100+100')


# evitar maximizar
aplicacion.resizable(0, 0)


# titulo
aplicacion.title('Mi Restaurante - Sistema de Facturacion')


# icono para la ventana
icono = tkinter.PhotoImage(file='restaurante.png')
aplicacion.iconphoto(True, icono)


# color de fondo de la ventana
aplicacion.config(bg='burlywood')


# panel superior
panel_superior = Frame(aplicacion,
                       bd=1,
                       relief=RAISED)
panel_superior.pack(side=TOP)


# etiqueta del titulo
etiqueta_titulo = Label(panel_superior,
                        text='Sistema de Facturacion',
                        fg='azure4',
                        font=('Dosis', 58),
                        bg='burlywood',
                        width=27)
etiqueta_titulo.grid(row=0, column=0)


# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        relief=SUNKEN)
panel_izquierdo.pack(side=LEFT)


# panel costos
panel_costos = Frame(panel_izquierdo,
                     bd=1,
                     relief=FLAT,
                     bg='azure4',
                     padx=50)
panel_costos.pack(side=BOTTOM)


# panel comidas
panel_comidas = LabelFrame(panel_izquierdo,
                           text='Comidas',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=GROOVE,
                           fg='azure4')
panel_comidas.pack(side=LEFT)


# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                           text='Bebidas',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=GROOVE,
                           fg='azure4')
panel_bebidas.pack(side=LEFT)


# panel postres
panel_postres = LabelFrame(panel_izquierdo,
                           text='Postres',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=GROOVE,
                           fg='azure4')
panel_postres.pack(side=LEFT)


# panel derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      relief=SUNKEN)
panel_derecho.pack(side=RIGHT)


# panel calculadora
panel_calculadora = Frame(panel_derecho,
                          bd=1,
                          relief=RIDGE,
                          bg='burlywood')
panel_calculadora.pack()


# panel recibo
panel_recibo = Frame(panel_derecho,
                     bd=1,
                     relief=RIDGE,
                     bg='burlywood')
panel_recibo.pack()


# panel botones
panel_botones = Frame(panel_derecho,
                      bd=1,
                      relief=RIDGE,
                      bg='burlywood')
panel_botones.pack()


# lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Kebab', 'Pozole', 'Pizza', 'Tacos']
lista_bebidas = ['Agua', 'Coca', 'Jugo', 'Soda', 'Vino', 'Cerveza', 'Malteada', 'Cafe']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Pastel', 'Pay', 'Galletas']

# lista de precios
precios_comidas = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebidas = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# generar items de comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)


    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# generar items de bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)


    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1


# generar items de postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)


    # crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1


# variables del panel de costos
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comidas:',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)


etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebidas:',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)


etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postres:',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)


etiqueta_subtotal = Label(panel_costos,
                          text='Sub-Total:',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)


etiqueta_impuestos = Label(panel_costos,
                           text='Impuestos:',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)


etiqueta_total = Label(panel_costos,
                       text='Total:',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# botones
botones = ['Total', 'Recibo', 'Guardar', 'Reiniciar']
boton_creado = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    boton.grid(row=0, column=columnas)
    boton_creado.append(boton)
    columnas += 1

boton_creado[0].config(command=total)
boton_creado[1].config(command=recibo)
boton_creado[2].config(command=guardar)
boton_creado[3].config(command=reiniciar)


# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=12)
texto_recibo.grid(row=0, column=0)


# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=38,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '−',
                       '1', '2', '3', 'x',
                       'Borrar', '0', '=', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1, width=8)
    boton.grid(row=fila, column=columna)
    botones_guardados.append(boton)

    if columna == 3:
        fila += 1

    columna += 1
    if columna == 4:
        columna = 0


# asignar funcionabilidad a los botones
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=borrar)
botones_guardados[13].config(command=lambda: click_boton('0'))
botones_guardados[14].config(command=obtener_resultado)
botones_guardados[15].config(command=lambda: click_boton('/'))


# evitar que la pantalla se cierre
aplicacion.mainloop()
