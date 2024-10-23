"""
La instruccion para este ejercicio es:

* Crear un programa que descomprima el archivo: "Proyecto+Dia+9.zip"
    - Esto se hizo con: "00_unzip_inst.py"

* Dentro del .zip, viene el archivo "Instrucciones.txt" con las indicaciones.
    - "...crear un Buscador de Números de Serie.
        ¿Qué es eso? Es un programa que se encargue de buscar números de serie
        que cumplan un determinado formato, dentro de un arbol de carpetas."
"""
from pathlib import Path
import os
import re
import time
import datetime
import math


inicio = time.time()

hoy = datetime.date.today()
directorio = Path('D:/Proyectos Python/Zzz_learnings_projects/python_total/day_09/Mi_Gran_Directorio')

numeros_encontrados = []
archivos_encontrados = []


def buscar_serie(archivo):
    patron = r'N\D{3}-\d{5}'
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(directorio):
        for a in archivo:
            resultado = buscar_serie(Path(carpeta, a))
            if resultado != '':
                archivos_encontrados.append(a.title())
                numeros_encontrados.append(resultado.group())


def imprimir_serie():
    contador = 0
    print('*'*30)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('-' * 12 + '\t\t' + '-' * 11)
    print('  ARCHIVO: \t\t\t NUM.SERIE:')
    print('-'*12 + '\t\t' + '-'*11)
    for a in archivos_encontrados:
        print(f'{a}\t\t{numeros_encontrados[contador]}')
        contador += 1
    print('\n')
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')


crear_listas()
imprimir_serie()
