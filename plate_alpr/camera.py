import cv2
from time import strftime

class Camera():
    def __init__(self):
        pass
        
    def captura_img(self):
        self.img = ('/home/pi/gpios/plate_alpr/imgs/'+strftime('%H %M %S %d %m %Y')+'.jpg')
        print("Started...")
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
        if cap.isOpened():
            ret, frame = cap.read()
        else:
             ret = False
        cv2.imwrite(self.img, frame)
        cap.release()  
        print("Finish")
        return self.img

#cmera = Camera()
#print(cmera.captura_img())
#print(cmera.img)
