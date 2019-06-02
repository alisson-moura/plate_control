import RPi.GPIO as GPIO
from time import sleep

class Motor():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    pwm = GPIO.PWM(13, 50)
    def __init__(self):
        self.pwm.start(0)
        
 
        
       
    def SetAngle(self, angle):
        
        duty = angle / 18 + 2
        GPIO.output(13, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(13, False)
        self.pwm.ChangeDutyCycle(0)
        #self.pwm.stop()

