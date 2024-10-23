"""
Este archivo es creado para descomprimir el archivo ".zip" que continene
    las instrucciones necesarias para hacer el proyecto del dia 09.
"""
# Este codigo utiliza la libreria "ZIPFILE"
import zipfile


zip_abierto = zipfile.ZipFile('Proyecto+Dia+9.zip', 'r')

zip_abierto.extractall()

zip_abierto.close()

print('Este codigo ha descomprimido el archivo en la carpeta donde se encuentra el .zip')


""" -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- """
# Este otro codigo es utilizando la libreria "SHUTIL"
import shutil


shutil.unpack_archive('Proyecto+Dia+9.zip',
                      'Extraccion_Terminada',
                      'zip')

print('Este codigo ha descomprimido el archivo en la carpeta Extraccion_Terminada')
