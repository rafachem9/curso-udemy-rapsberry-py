import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

#5 se define el PWM para modificar la potencia del led
#500 es la frecuencia
pwm= GPIO.PWM(2, 500)
pwm.start(0)

continuar = True
while continuar:
    dato= input("Intorducir valor nuevo DC entre 0-100:")
    if dato == "z":
        continuar =False
    else:
        pwm.ChangeDutyCycle(int(dato))

pwm.stop()
GPIO.cleanup()
print("Fin de programa")
    

