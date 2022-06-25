import serial
import socket

#Nos conectamos al Serial del arduino
serial=serial.Serial("/dev/ttyACM0",9600)

#Actuamos como cliente
s=socket.socket()
s.connect(("192.168.1.17", 60042))
print("Conectado al servidor")

try:
    
    continuar = True
    while continuar:
        #dato= input("Ponga una letra: ")
        #if dato == "z":
         #   continuar = False
         #   serial.close()
        #else:
            temperatura = serial.readline()
            nivelLuz = serial.readline() 
            #decode es para pasar a string
            temp = float(temperatura.decode())
            luz =  float(nivelLuz.decode())
            datos=[0,0]
            print(type(temp))
            datos[0]=int(temp)
            datos[1]=int(luz)
            
            s.send(bytes(datos))
            print(datos)
        
except:
    s.close()
    print("Fin del Programa")