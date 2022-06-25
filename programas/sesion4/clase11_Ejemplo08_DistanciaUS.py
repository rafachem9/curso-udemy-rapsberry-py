import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.IN)

GPIO.output(2, GPIO.LOW)

try:
    while True:
        GPIO.output(2, GPIO.HIGH)
        #Tada 10 us en enviar la onda
        time.sleep(0.00001)
        GPIO.output(2, GPIO.LOW)
        #Tiempo en llegar la onda al Echo
        t1 = time.time()
        while GPIO.input(20) == GPIO.LOW:
            t1 = time.time()
        while GPIO.input(20) == GPIO.HIGH:
            t2 = time.time()
        
        t= t2-t1
        
        distancia= 1700*t
        print("Distancia: ", round(distancia, 1), " cm")
        time.sleep(0.2)
except:
    GPIO.cleanup()
    print("Fin del programa")
    
            




