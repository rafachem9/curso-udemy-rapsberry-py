import socket

s=socket.socket()
s.connect(("192.168.1.17", 60042))
print("Conectado al servidor")

continuar = True

while continuar:
    dato = input("Escribe un mensaje al Servidor: ")
    if dato == "z":
        continuar=False
    else:
        s.send(dato.encode())    
s.close()
print("Fin del programa")

