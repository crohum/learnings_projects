"""
La instruccion para este ejercicio es:

* Crear un juego que:
    - Tenga una nave que se desplace de un lado a otro en el fondo de la pantalla (linea recta).
    - Aparezcan 6 enemigos al mismo tiempo.
    - La nave pueda disparar varias balas.
    - Al destruir una nave enemiga, reaparezca en pantalla.
    - Cada enemigo destruido aumenta el puntaje.
    - El juego finaliza si algun enemigo llega abajo.
"""
import math
import random
import pygame
from pygame import mixer


# Iniciar el modulo pygame
pygame.init()


# Crear la pantalla donde se va a mostrar el juego
pantalla = pygame.display.set_mode((800, 600))


# Estandarizamos la velocidad del juego sin importar que tan potente sea el ordenador
fps = 60


# Personalizar el Icono y Titulo (superiores)
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
pygame.display.set_caption('Invasión Espacial')


# Musica de fondo
mixer.music.load('musica_fondo.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)


# Guardar el fondo
fondo = pygame.image.load('fondo.png')


# Puntaje
puntaje = 0
fuente = pygame.font.Font("space age.ttf", 32)
fuente_final = pygame.font.Font('space age.ttf', 50)
texto_x = 10
texto_y = 10


# parametros para la Nave Protagonista del jugador
imagen_jugador = pygame.image.load('astronave.png')
jugador_x = 368
jugador_y = 530
jugador_x_movimiento = 0


# parametros para los disparos del jugador
imagen_bala = pygame.image.load('bala.png')
balas = []
bala_x = 368
bala_y = 530
bala_y_movimiento = 10
bala_disparada = False


# parametros para los Enemigos
imagen_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_movimiento = []
enemigo_y_movimiento = []
cantidad_enemigos = 9


# Multiples enemigos en una lista
for e in range(cantidad_enemigos):
    if e == 1 or e == 3 or e == 7:
        imagen_enemigo.append(pygame.image.load('enemigo_1.png'))
    elif e == 2 or e == 4 or e == 8:
        imagen_enemigo.append(pygame.image.load('enemigo_2.png'))
    else:
        imagen_enemigo.append(pygame.image.load('enemigo_3.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 150))
    enemigo_x_movimiento.append(50)
    enemigo_y_movimiento.append(50)


# Funcion jugador (colocar y mover el jugador en pantalla)
def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))


# Funcion de la bala
def disparar_bala(x, y):
    global bala_disparada
    bala_disparada = True
    pantalla.blit(imagen_bala, (x + 16, y + 10))


# Funcion enemigo (colocar y mover el enemigo en pantalla)
def enemigo(x, y, enem):
    pantalla.blit(imagen_enemigo[enem], (x, y))


# Funcion para detectar colisiones
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    if distancia < 30:
        return True
    else:
        return False


# Funcion para mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion texto final del juego
def texto_final():
    mensaje_final = fuente_final.render(' JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mensaje_final, (80, 200))


# Loop del juego
se_ejecuta = True
jugando = True
while se_ejecuta:


    # Colocar la Imagen del fondo de pantalla
    pantalla.blit(fondo, (0, 0))


    # Chequeador de "Eventos"
    for evento in pygame.event.get():


        # Loop que la ventana no se cierre hasta hacer clic en X
        if evento.type == pygame.QUIT:
            se_ejecuta = False


    # Loop para chequear el ingreso de ordenes del jugador


        # Empezar a moverse izquierda o derecha
        if evento.type == pygame.KEYDOWN and jugando:
            if evento.key == pygame.K_LEFT:
                jugador_x_movimiento = -5
            elif evento.key == pygame.K_RIGHT:
                jugador_x_movimiento = 5


        # Disparar las balas
            elif evento.key == pygame.K_UP:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                nueva_bala = {'x': jugador_x, 'y': jugador_y, 'velocidad': -10}
                balas.append(nueva_bala)
                if not bala_disparada:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)


        # Dejar de moverse
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_movimiento = 0


    # Modificar la ubicacion del pj
    jugador_x += jugador_x_movimiento


    # Mantener la nave dentro de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    # modificar la ubicacion de la bala
    for bala in balas:
        bala['y'] += bala['velocidad']
        pantalla.blit(imagen_bala, (bala['x']+16, bala['y']+10))
        if bala['y'] < 0:
            balas.remove(bala)


    # modificar la ubicacion de los enemigos
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_movimiento[e]


    # mantener los enemigos dentro de la pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_movimiento[e] = 10
            enemigo_y[e] += enemigo_y_movimiento[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_movimiento[e] = -10
            enemigo_y[e] += enemigo_y_movimiento[e]


    # revisar si hay coliciones
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("explosion.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break


    # Ejecuta las funciones "jugador", "enemigo" y "puntaje"
        jugador(jugador_x, jugador_y)
        enemigo(enemigo_x[e], enemigo_y[e], e)
        mostrar_puntaje(texto_x, texto_y)


    # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_x[k] = 1000
            jugando = False
            texto_final()
            break


    # Actualizar lo que se muestra en la pantalla
    pygame.display.update()
