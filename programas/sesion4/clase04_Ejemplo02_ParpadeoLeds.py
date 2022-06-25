import RPi.GPIO as GPIO
import time

#Programa para producir el parpadeo de un led


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

try:
    while True:
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.4)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.2)
except:
    print("fin de programa")
    GPIO.cleanup()