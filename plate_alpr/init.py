#from motor_c import Motor
from cancela import Cancela
print("Cancela importada com sucesso...")
from camera import Camera
print("Camera importada com sucesso...")
from hc import Sensor
print("Sensor importado com sucesso...")
from plate_ocr import Plate
print("Plate OCR importado com sucesso...")

import RPi.GPIO as GPIO
import time
from subprocess import call
GPIO.setmode(GPIO.BOARD)
print("Importacoes terminadas com sucesso...")
print("")
print("Limpando buffer...")
#GPIO.cleanup()
print("Terminado...")
print("")
print("")
sensor = Sensor()
print("Objeto Sensor criado")
camera = Camera()
print("Objeto Camera criado")
cancela = Cancela()
print("Objeto Cancela criado")
ocr = Plate()
print("Objeto Plate-OCR criado")
print("")
print("")

while True:
    try:
        if sensor.distance() == -1:
            print("Cancela Fechada...")
            cancela.fecha_cancela()
        else:
            print(sensor.distance())
            placa = ""
            img = camera.captura_img()
            placa = ocr.plate_ocr(img)
            if placa != "":
                print(placa)
                print("Abre Cancela")
                cancela.abre_cancela()
                time.sleep(1)
                while sensor.distance() != -1:
                    print("Mantem Cancela Aberta")
                    cancela.mantem_aberta()
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

