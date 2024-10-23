"""
Genera los numeros de cada categoria del turnero: "menu_principal.py".
"""
import os


def atn_medica():
    x = 0
    while True:
        x += 1
        yield f'A-{str(x).zfill(3)}'


def medicamento():
    x = 0
    while True:
        x += 1
        yield f'M-{str(x).zfill(3)}'


def perfumeria():
    x = 0
    while True:
        x += 1
        yield f'P-{str(x).zfill(3)}'


def cosmeticos():
    x = 0
    while True:
        x += 1
        yield f'C-{str(x).zfill(3)}'


def texto(categoria):
    print('\n' + '*'*15 + '\nTURNO:')
    print(next(categoria))
    print('Aguarde y será atendido en breve\n' + '*'*15)
    input('\n\nPresiona enter para regresar al menu.')
    os.system('cls')


num_atn = atn_medica()
num_med = medicamento()
num_prf = perfumeria()
num_cos = cosmeticos()
