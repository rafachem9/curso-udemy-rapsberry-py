import socket

#Crear un servidor

s=socket.socket()
#Abriendo conexion en puerto 2020
s.bind(("192.168.1.25",2020))
s.listen(10)
print("Esperando conexion...")
(sc, addrc) = s.accept()
#Imprime la dirección del cliente
print("Cliente conectado:", addrc)

continuar = True
while continuar:
    #Bytes que puede enviar el cliente
    dato = sc.recv(64)
    if not dato:
        continuar= False
        print("Cliente se ha desconectado")
    else:
        print (dato)

sc.close()
s.close()
print("Fin de programa")