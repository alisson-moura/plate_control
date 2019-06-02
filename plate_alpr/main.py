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
print("Importacoes terminadas com sucesso...")
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
        if sensor.distance() != -1 :
            print("Captura Imagem...")
            placa = ocr.plate_ocr(camera.captura_img())
            if placa != "":
                print("Abre Cancela")
                cancela.abre_cancela()
                time.sleep(1)
            else:
                print("Mantem cancela Fechada...")
                cancela.fecha_cancela()
                continue
            while sensor.distance() != -1:
                print("Mantem Cancela aberta...")
                cancela.mantem_aberta()
            else:
                print("Fecha Cancela...")
                cancela.fecha_cancela()
                continue
        else:
            print("Mantenha Cancela Fechada...")
            cancela.fecha_cancela()
    except Exception:
        GPIO.cleanup()
        break

