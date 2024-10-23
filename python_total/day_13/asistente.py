"""
La instruccion para este ejercicio es:

* Crear un programa que funcione como asistente virtual por voz
* Debe de poder:
    - Dar fecha y/o hora
    - abrir youtube y el navegador web
    - buscar en wikipedia o internet
    - dar valor actual de acciones en bolsa
    - reproducir un video
    - contar chistes
"""
import pyttsx3
import speech_recognition as speech
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia


# opciones de voz/ idioma

# ESPAÑOL
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'

# ENGLISH
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
id3 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'

'''# Para ver las voces instaladas en el ordenador (no debe quedar este codigo al final)
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)'''


# Escuchar el micro y convertirlo a texto
def transformar_audio_texto():

    # almacenar en una variable
    r = speech.Recognizer()

    # configurar el microfono
    with speech.Microphone() as origen:

        # colocar un tiempo de espera
        r.pause_threshold = 0.8

        # informar que empezo a grabar
        print('ya puedes hablar')

        # guardar en una variable lo dicho
        audio = r.listen(origen)

        try:
            # busca en google
            pedido = r.recognize_google(audio, language='es-mx')

            # prueba de que pudo ingresar correctamente
            print('Dijiste: ' + pedido)

            #devolver a pedido
            return pedido

        # en caso de que no pueda entender el audio
        except speech.UnknownValueError:

            hablar('Disculpa, no entendi, ¿me lo puedes repetir?')

            # devolver error
            return 'sigo esperando'

        # en caso de no resolver el pedido
        except speech.RequestError:

            hablar('Parece que no hay servicio, intentalo de nuevo')

            # devolver error
            return 'sigo esperando'

        # otros casos
        except:

            hablar('Ups, al parecer algo ha salido mal')

            # devolver error
            return 'sigo esperando'


# Que el asistente se escuche por el altavoz
def hablar(mensaje):

    # encender el motor pyttsx3
    engine = pyttsx3.init()

    # asignar la voz que queremos oir
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)
    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombre dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]} {dia.day} de {dia.month}')


# informar la hora del dia
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    print(hora)
    hora = f'En este momento son las {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos.'
    print(hora)

    # decir la hora
    hablar(hora)


# saludar al inicio
def saludo_inicial():

    # crear variable del saludo
    hora = datetime.datetime.now()

    if 6 <= hora.hour < 12:
        momento = 'Buenos dias'
    elif 12 <= hora.hour < 21:
        momento = 'Buenas tardes'
    else:
        momento = 'Buenas noches'

    # decir un saludo
    hablar(f'{momento}, Soy Sabina, tu asistente personal. por favor, dime en que te puedo ayudar.')


# CENTRO DE COMANDOS
def pedir_cosas():
    # activar saludo inicial
    saludo_inicial()

    # loop de uso
    salir = False
    while not salir:

        # activar micro y guardar
        pedido = transformar_audio_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
        elif 'buscar en wikipedia' in pedido:
            hablar('buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:' + resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ya estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip
            cartera = {'apple':'APPL', 'amazon':'AMZN', 'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón, pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break
