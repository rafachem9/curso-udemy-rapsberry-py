import socket
import RPi.GPIO as GPIO


#Crear un servidor
s=socket.socket()
#Abriendo conexion en puerto 2020
s.bind(("192.168.1.25",2020))
s.listen(10)

#Configuración de las salidas LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

while True:
    (sc, addrc) = s.accept()
    print("Cliente conectador", addrc)
    continuar= True
    while continuar:
        dato=sc.recv(64)
        if not dato:
            continuar= False
            print("Cliente desconectado")
        else:
            dato2=dato.decode()
            str(dato2)
            if dato2=="a":
                print ("Led encendido")
                GPIO.output(2, GPIO.HIGH)
            elif dato2== "b":
                print ("Led apagado")
                GPIO.output(2, GPIO.LOW)
                
s.close()
print("Fin del programa")