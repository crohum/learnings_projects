from enum import Enum


# Color de fondos
class Color(Enum):
    DESTACADO = '#274227'
    PRIMARIO = '#2d572c'
    SECUNDARIO = '#c2c2c2'
    BOTONES = 'azure4'


# Color de letras
class TextColor(Enum):
    DESTACADO = 'white'
    PRIMARIO = 'gray'
    SECUNDARIO = 'black'


# Tipos de letras
class Fonts(Enum):
    TITULO = 'Old London'
    TEXTO = 'Baskerville Old Face'
    BOTONES = 'Book Antiqua'
    RESPUESTA = 'Dosis'
