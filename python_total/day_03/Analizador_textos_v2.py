"""

"""

import tkinter
from tkinter import *
from python_total.day_03.estilos import Color, TextColor, Fonts


# iniciar tkinter
aplicacion = Tk()


# tamaño de la ventana
aplicacion.geometry('1210x750')
aplicacion.resizable(False, False)


# titulo
aplicacion.title('- Analizador de Textos')


# icono para la ventana
icono = tkinter.PhotoImage(file='icono.png')
aplicacion.iconphoto(True, icono)


# color de fondo de la ventana
aplicacion.config(bg=Color.SECUNDARIO.value)


# panel superior
panel_superior = Frame(aplicacion,
                       bd=2,
                       relief=FLAT)
panel_superior.pack(side=TOP, pady=5)


# etiqueta del titulo
etiqueta_titulo = Label(panel_superior,
                        text='Analizador de Texto',
                        fg=TextColor.DESTACADO.value,
                        font=('Baskerville Old Face', 58),
                        bg=Color.PRIMARIO.value,
                        width=27)
etiqueta_titulo.grid(row=0, column=0)


# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=2,
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT, padx=5)

etiqueta_instrucciones = Label(panel_izquierdo,
                               text='Ingresa el texto a ser analizado en esta area.',
                               fg=TextColor.PRIMARIO.value,
                               font=(Fonts.TEXTO.value, 14),
                               bg=Color.PRIMARIO.value,
                               width=35)
etiqueta_instrucciones.grid(row=0, column=0)


# area de entrada del texto
texto_entrada = Text(panel_izquierdo,
                     font=(Fonts.TEXTBOX.value, 12, 'bold'),
                     bd=2,
                     width=40,
                     height=30)
texto_entrada.grid(row=1, column=0, pady=5)


# panel central
panel_centro = Frame(aplicacion,
                     bd=2,
                     relief=FLAT)
panel_centro.pack(side=LEFT, padx=5)


# panel letras


# panel palabra


# panel seleccion espejo/invertido









'''etiqueta_temp = Label(panel_centro,
                               text='Ingresa en esta area el texto a ser analizado.',
                               fg='white',
                               font=('Baskerville Old Face', 14),
                               bg='#69371c',
                               width=35)
etiqueta_temp.grid(row=0, column=0)


# area de entrada del texto
texto_temp = Text(panel_centro,
                     font=('Dosis', 12, 'bold'),
                     bd=2,
                     width=40,
                     height=30)
texto_temp.grid(row=1, column=0, pady=5)'''






# panel derecho
panel_derecho = Frame(aplicacion,
                      bd=2,
                      relief=FLAT)
panel_derecho.pack(side=LEFT, padx=5)


# area de salida
texto_salida = Text(panel_derecho,
                    font=(Fonts.TEXTBOX.value, 12, 'bold'),
                    bd=2,
                    width=40,
                    height=31)
texto_salida.grid(row=1, column=0, pady=10, padx=10)






























# evitar que la pantalla se cierre
aplicacion.mainloop()
