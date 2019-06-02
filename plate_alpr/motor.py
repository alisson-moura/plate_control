import RPi.GPIO as GPIO
from time import sleep

class Motor():
    def __init__(self):
        self.servo_pin = 13
        self.deg_0_pulse = 0.5
        self.deg_180_pulse = 2.5
        self.f = 50.0
        self.period = 1000/self.f
        self.k = 100/self.period
        self.deg_0_duty = self.deg_0_pulse*self.k
        self.pulse_range = self.deg_180_pulse - self.deg_0_pulse
        self.duty_range = self.pulse_range * self.k
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT)
    
    __pwm = GPIO.PWM(13, 50.0)
    __pwm.start(0)
    def set_angle(self, angle):
        

        duty = self.deg_0_duty + (angle/180.0)*self.duty_range
        
        __pwm.ChangeDutyCycle(duty)


motor = Motor()
try:
    while True:
        angle = int(input("Enter angle 0 a 180"))
        motor.set_angle(angle)
finally:
    print("cleaning up")
    GPIO.cleanup()
