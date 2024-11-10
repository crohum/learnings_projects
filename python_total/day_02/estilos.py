from enum import Enum


# Colores de fondo
class Color(Enum):
    DESTACADO = 'navy'
    PRIMARIO = 'royalblue'
    BOTONES = 'azure4'


# Colores de letras
class TextColor(Enum):
    DESTACADO = 'white'
    PRIMARIO = 'azure4'
    SECUNDARIO = 'black'


# Tipos de letras
class Fonts(Enum):
    TITULOS = 'Lucida Console'
    TEXTO = 'Lucida Console'
    TEXTBOX = 'Lucida Console'
    BOTONES = 'Arial'
