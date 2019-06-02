from openalpr import Alpr
import re
import os
class Plate:
        
    def __init__(self):
        self.alpr = Alpr("eu","/etc/openalpr/conf", "/usr/share/openalpr/runtime_data")
        if not self.alpr.is_loaded():
            print("Erro ao carregar o ALPR..")
            sys.exit(1)
        self.alpr.set_top_n(10)
        self.alpr.set_default_region("")

    def plate_ocr(self, placa):
        results = self.alpr.recognize_file(placa)

        i = 0
        plate = ""
        for plate in results['results']:
            i += 1
            for candidate in plate['candidates']:
                if candidate ['matches_template']:
                    prefix = "*"
                teste = candidate['plate']
                x = re.search('^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}', teste)
                if (x):
                    plate = candidate['plate']
                    #return plate
                    break
        self.alpr.unload()
        if(plate != ""):
            print(plate)
        return plate


#placa = Plate()
#placa01 = placa.plate_ocr('/home/pi/Pictures/Mercosul/img01.jpeg')
#print(placa01)
