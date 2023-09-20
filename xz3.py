import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

aux = [21, 20, 26, 16, 19, 25, 23, 24]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

GPIO.output(leds,1)
time.sleep(2)

while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))
        time.sleep(0.1)  