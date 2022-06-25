import socket
import random
import time

#Se conecta a la ip del raspberry
s=socket.socket()
s.connect(("192.168.1.25", 2020))
print("Conectado")

#Generación de los datos
data= [0,0,0]
for i in range(20):
    data[0]= random.randint(10,30)
    data[1]= random.randint(15,45)
    data[2]= random.randint(10,30)
    #Enviar los datos en forma de byte
    s.send(bytes(data))
    #Esto retrasa el envío de datos, y se ve como va llegando cada dato
    #time.sleep(1)
    
    
s.close()
print("Data enviada")
print("Fin del programa")