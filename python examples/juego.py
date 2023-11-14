'''
vamos a hacer un juego donde tenemos dos led, uno para el jugador 1 y otro para el jugador 2
el juego dura 30 segundos, y en estos 3 segundos el led de cada uno de los jugadores se encendera
aleartoriamente

mientras el led esta encendido cada uno de los jugaodres tiene que oprimir su boton lo mas rapido posible
y cuando el led no esta parpadeando no debe de oprimir el boton, (hacer esta accion le baja muchos puntos)

¿como se programaria este juego? 

consideraciones:    
el led dura entre 2 y 8 segundos alearatoriamente encendido
los tiempos de descanso duran entre 4 y 8 segundos 
cada click en tiempo de descanso resta 5 puntos (5 clicks)
al final del juego, se muestran los resultados de ambos jugadores

pip install gpiozero
'''
from gpiozero import LED, Button
import time 
import random

# Configurar pines
led1_pin = 14  # Pin del LED para el jugador 1
led2_pin = 15 # Pin del LED para el jugador 2
button1_pin = 23  
button2_pin = 24  # Pin del botón para el jugador 2

# Configurar tiempo de juego
#tiempo de juego
tiempoDjuego = 30

#inicializar los pines

GPIO.setmode(GPIO.BCM)
Gpio.setup(led1_pin, GPIO.OUT)  
gpio.setup(led2_pin, GPIO.OUT)
gpio.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#puntos de cada jugador
score1 = 0
score2 = 0

#encender leds
def encender_led(led_pin):
    GPIO.output(led_pin, GPIO.HIGH)

#apagar leds
def apagar_led(led_pin):
    GPIO.output(led_pin, GPIO.LOW)

#verificar botones
def verificar_botones():
    global score1, score2
    if GPIO.input(button1_pin) == GPIO.LOW:
        score1 += 1
    if GPIO.input(button2_pin) == GPIO.LOW:
        score2 += 1

        
#definir el juego
def juego():
    #variable global de inicializacion de variables de puntos
    global score1, score2
    inicio_tiempo = time.time()



    while (time.time() - inicio_tiempo) < tiempoDjuego:
        # Encender LED1 aleatoriamente
        led1_tiempo = random.uniform(2, 8)
         #encender LED2 aleatoriamente  
        led2_tiempo = random.uniform(2, 8)

        encender_led(led1_pin)
        encender_led(led2_pin)

        time.sleep(led1_tiempo)
        apagar_led(led1_pin)

        time.sleep(led2_tiempo)
        apagar_led(led2_pin)

        # Verificar botones mientras el LED está encendido
        verificar_botones()

       #tiempo random de entre 4 y 8 segundos
        tiempo_descanso = random.uniform(4, 8)
        time.sleep(tiempo_descanso)

    #resta de puntos por penzalizacion al precionar el boton el LED apagado
       #boton 1
        score1 -= 5 if GPIO.input(button1_pin) == GPIO.LOW else 0
        #boton 2
        score2 -= 5 if GPIO.input(button2_pin) == GPIO.LOW else 0

  #imprimir las puntuaciones
    print(f"Puntuaciones: Jugador 1 - {score1}, Jugador 2 - {score2}")

# Configurar GPIO
try:
    juego()

    #limpiar la puntuacion
finally:
    GPIO.cleanup()
