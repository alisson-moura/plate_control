import RPi.GPIO as GPIO
import time
class Sensor():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.GPIO_TRIGGER = 7
        self.GPIO_ECHO = 11
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = round((TimeElapsed * 34300) / 2, 2)
        if distance < 9 or distance > 14:
            distance = -1
        #GPIO.cleanup()
        return distance



sensor = Sensor()

while True:
    print(sensor.distance())

