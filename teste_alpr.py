from openalpr import Alpr
import cv2
import re
import os
alpr = Alpr("eu", "/etc/openalpr/openalpr.conf","/home/pi/openalpr/runtime_data")
if not alpr.is_loaded():
    print('Erro ao carregar ALPR')
    sys.exit(1)
alpr.set_top_n(200)
#alpr.set_default_region('md')
#Trabalhando com imagens
img = ('/home/pi/Pictures/celular01.jpg')
print('Started...')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False
cv2.imwrite(img, frame)
cap.release()
print("Finish")

#seleciona a imagem
results = alpr.recognize_file(img)

i=0
placa = ""
for plate in results['results']:
        i+=1
        print('Plate #%d' %i)
        print(" %12s %12s" % ("Plate","Cofidence"))

        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix= "*"
            print(" %s %12s%12f" % (prefix, candidate['plate'],candidate['confidence']))
            teste = candidate['plate']
            x = re.search('^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}',teste)
            if(x):
                placa = candidate['plate']
                break

if(placa != ""):
    print(placa)

alpr.unload()

