import psutil
import RPi.GPIO as GPIO
import time

# Configura los pines de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  #  verde
GPIO.setup(18, GPIO.OUT)  #  amarillo
GPIO.setup(19, GPIO.OUT)  #  rojo

#  encender un LED y apagar los demás
def encender_led(color):
    if color == 'verde':
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
    elif color == 'amarillo':
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
    elif color == 'rojo':
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.HIGH)

try:
    while True:
        # Obtener el uso de CPU
        cpu_usage = psutil.cpu_percent(interval=1)

        # Determina el color del LED en base al uso de la CPU
        if cpu_usage < 10:
            encender_led('verde')
        elif 10 <= cpu_usage < 20:
            encender_led('amarillo')
        else:
            # Hace parpadear el LED rojo
            for _ in range(5):
                encender_led('rojo')
                time.sleep(0.5)
                encender_led('')
                time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
