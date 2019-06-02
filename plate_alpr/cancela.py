from subprocess import call #para ler o teclado
import RPi.GPIO as GPIO
from time import sleep


class Cancela():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.PIN_GREEN  = 40
        self.PIN_YELLOW = 38
        self.PIN_RED    = 36
        GPIO.setup(self.PIN_GREEN, GPIO.OUT)
        GPIO.setup(self.PIN_YELLOW, GPIO.OUT) 
        GPIO.setup(self.PIN_RED, GPIO.OUT)
        

    def abre_cancela(self):
        GPIO.output(self.PIN_GREEN, True)
        GPIO.output(self.PIN_YELLOW, False)
        GPIO.output(self.PIN_RED, False)

    def fecha_cancela(self):
        GPIO.output(self.PIN_GREEN, False)
        GPIO.output(self.PIN_YELLOW, False)
        GPIO.output(self.PIN_RED, True)

    def mantem_aberta(self):
        GPIO.output(self.PIN_GREEN, False)
        GPIO.output(self.PIN_YELLOW, True)
        GPIO.output(self.PIN_RED, False)
        
"""
while True:
    try:
        
        cancela = Cancela()
        cancela.fecha_cancela()
        sleep(2)
        cancela.abre_cancela()
        sleep(2)
        cancela.mantem_aberta()
        sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
"""
