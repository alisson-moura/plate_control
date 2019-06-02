from cancelas import Cancela
from subprocess import call
from time import sleep
#from hc2 import Sensor
from hcsr04sensor import sensor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#Cancela -LEDS
PIN_GREEN = 40
PIN_YELLOW = 38
PIN_RED = 36
GPIO.setup(PIN_GREEN ,GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_RED ,GPIO.OUT)

#Sensor- HC
PIN_TRIGGER = 7
PIN_ECHO = 11
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

def distance():
    valor = sensor.Measurement(PIN_TRIGGER, PIN_ECHO, gpio_mode=GPIO.BOARD)
    raw_measurement = valor.raw_distance()
    distance = valor.distance_metric(raw_measurement)
    return distance


cancela = Cancela(PIN_GREEN, PIN_YELLOW, PIN_RED)
#sensor = Sensor(PIN_TRIGGER, PIN_ECHO)
while True:
    try:
        cancela.fecha_cancela()
        sleep(2)
        cancela.abre_cancela()
        sleep(2)
        cancela.mantem_aberta()
        sleep(2)
        print(distance())
        #sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

       
        
