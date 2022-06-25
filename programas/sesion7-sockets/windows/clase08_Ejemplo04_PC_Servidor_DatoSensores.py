import socket


s=socket.socket()
s.bind(("192.168.1.17", 60042))
print("Servidor conectado")
s.listen(10)

continuar = True
while continuar:
        print("Esperando conexiones...")
        (sc,addrc) = s.accept()
        print("Cliente conectado",addrc)
        continuar = True
        while continuar:
            data = sc.recv(64)
            if not data:
                continuar = False
                print("Cliente desconectado",addrc)
            else:
                print("Temperarura","Luz")
                print(data[0],data[1])
                
print("Fin de programa")
sc.close()