from subprocess import call #capturar sinal do teclado
import time
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
    GPIO.output(PIN_TRIGGER, True) #set TRIGGER to HIGH
    time.sleep(0.00001) #set TRIGGER after 0.01ms to LOW

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(PIN_ECHO) == 0: #save start_time
        start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1: #save stop_time
        stop_time = time.time()

    time_elapsed = stop_time - start_time #time difference between start and stop

    #multiply with the sonic speed 34300 cm/s and divide by 2, because there and back
    distance = round((time_elapsed * 34300) / 2, 2)

    if distance < 9 or distance > 14: #define o range de captura 
        distance = -1

    return distance # retorna a distancia em cm

def abre_cancela():
    GPIO.output(PIN_GREEN, True)
    GPIO.output(PIN_YELLOW, False)
    GPIO.output(PIN_RED, False)
def fecha_cancela():
    GPIO.output(PIN_GREEN, False)
    GPIO.output(PIN_YELLOW, False)
    GPIO.output(PIN_RED, True)
def mantem_cancela():
    GPIO.output(PIN_GREEN, False)
    GPIO.output(PIN_YELLOW, True)
    GPIO.output(PIN_RED, False)







while True:
    try:
        abre_cancela()
        time.sleep(2)
        fecha_cancela()
        time.sleep(2)
        mantem_cancela()
        time.sleep(2)
        print(distance())
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

       
        
