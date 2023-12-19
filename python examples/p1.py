
import gpiozero as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)  
GPIO.setup(19, GPIO.OUT)  

def encender_led_verde():
    GPIO.output(18, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(3, GPIO.LOW)   