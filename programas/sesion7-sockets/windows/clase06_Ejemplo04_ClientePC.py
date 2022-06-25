import socket

s=socket.socket()
s.connect(("192.168.1.25", 2020))

continuar = True

while continuar:
    dato = input("Escribe un mensaje a la Rpi: ")
    if dato == "z":
        continuar=False
    else:
        s.send(dato.encode())
s.close()
print("Fin del programa")