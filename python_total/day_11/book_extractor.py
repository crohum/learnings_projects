"""
La instruccion para este ejercicio es:

* Crear un programa que extraiga los libros con 4 o 5 estrellas de una pagina.
"""
import bs4
from bs4 import BeautifulSoup
import requests


# Pagina a explorar
direccion_web = 'https://books.toscrape.com/catalogue/page-{}.html'
# Los {} sirven para crear una url sin numero de pagina


# LISTA DE TITULOS CON 4 o 5 ESTRELLAS
titulos_rating_alto = []


# Iterar paginas
print('\n' + ('*' * 20))
for pagina in range(1, 51):

    # Crear sopa en cada pagina
    direccion_pagina = direccion_web.format(pagina)
    resultado = requests.get(direccion_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    print(f'page {pagina} scanned')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:

        # Checar si tienen 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # Guardar titulo en una variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar el titulo a la lista
            titulos_rating_alto.append(titulo_libro)
print(('*' * 20) + '\n')


# Ver libros 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
