import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)

#El servo gira de 0 a 180 grados
# T= 20 ms
# Control se hace con Ton= 0.5 ms ==> 0 grados
#Ton= 0.5 ms ==> 0 grados

pwm= GPIO.PWM(2,50)
pwm.start(2.5)

continuar = True
while continuar:
    dato= input("Intorducir valor nuevo DC entre 0-12.5:")
    if dato == "z":
        continuar =False
    else:
        #Se ha tenido en cuenta que 12.5 equivale 180º y 2.5 equivale 0º
        dato=float(dato)*0.0556+2.5
        pwm.ChangeDutyCycle(float(dato))

pwm.stop()
GPIO.cleanup()
print("Fin de programa")
    